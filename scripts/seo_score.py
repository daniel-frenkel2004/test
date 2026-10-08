#!/usr/bin/env python3
"""Higanu SEO health score.

Reads the raw JSON responses of seo/queries/products.graphql (one file per page)
and seo/queries/site.graphql, checks every page Google can see, and prints a
0-100 score plus the list of problems found.

Usage:
  python3 scripts/seo_score.py --products snapshot/products-*.json --site snapshot/site.json
  python3 scripts/seo_score.py ... --json   # machine-readable output
"""
import argparse
import datetime as dt
import glob
import json
import re
import sys

# Rules come from seo/knowledge/rules.md. Keep the two in sync.
TITLE_MIN, TITLE_MAX = 25, 65
DESC_MIN, DESC_MAX = 70, 160
PRODUCT_MIN_WORDS = 60
COLLECTION_MIN_WORDS = 15
TARGET_ARTICLES = 8          # published guides we want on the blog
FRESH_DAYS = 30              # at least one new article in this many days
STOREFRONT_TEXT = re.compile(r"[֐-׿]")  # Hebrew letters

# Share of the final score that each area is worth (sums to 100).
WEIGHTS = {
    "product_meta": 20,
    "product_content": 15,
    "image_alt": 10,
    "product_category": 5,
    "collection_seo": 15,
    "clean_index": 15,
    "blog": 20,
}

LABELS_HE = {
    "product_meta": "כותרת ותיאור לגוגל במוצרים",
    "product_content": "תיאור מוצר מספיק ארוך",
    "image_alt": "טקסט חלופי לתמונות",
    "product_category": "קטגוריה למוצר (לגוגל שופינג)",
    "collection_seo": "קטגוריות באתר עם כותרת, תיאור ומוצרים",
    "clean_index": "בלי דפים ישנים או ריקים בגוגל",
    "blog": "מאמרים בבלוג",
}


def load(paths):
    out = []
    for pattern in paths:
        for path in sorted(glob.glob(pattern)):
            with open(path, encoding="utf-8") as f:
                out.append(json.load(f))
    return out


def words(text):
    return len((text or "").split())


def is_hidden(node):
    return bool(node.get("hidden")) and str(node["hidden"].get("value")) == "1"


def check_len(value, lo, hi):
    n = len((value or "").strip())
    return lo <= n <= hi, n


def score(product_pages, site):
    products = []
    for page in product_pages:
        products.extend(page["data"]["products"]["nodes"])
    site = site["data"]

    checks = {k: [] for k in WEIGHTS}  # each entry: (passed: bool, message_if_failed)

    live_products = [p for p in products
                     if p["status"] == "ACTIVE" and p.get("onStore", True) and not is_hidden(p)]
    for p in live_products:
        name = p["handle"]
        ok_t, n_t = check_len(p["seo"]["title"], TITLE_MIN, TITLE_MAX)
        checks["product_meta"].append((ok_t, f"מוצר {name}: כותרת לגוגל באורך {n_t} תווים (צריך {TITLE_MIN}-{TITLE_MAX})"))
        ok_d, n_d = check_len(p["seo"]["description"], DESC_MIN, DESC_MAX)
        checks["product_meta"].append((ok_d, f"מוצר {name}: תיאור לגוגל באורך {n_d} תווים (צריך {DESC_MIN}-{DESC_MAX})"))
        w = words(p["description"])
        checks["product_content"].append((w >= PRODUCT_MIN_WORDS, f"מוצר {name}: תיאור קצר, {w} מילים (צריך {PRODUCT_MIN_WORDS}+)"))
        images = [m for m in p["media"]["nodes"] if m["mediaContentType"] == "IMAGE"]
        no_alt = [m for m in images if not (m.get("alt") or "").strip()]
        checks["image_alt"].append((not no_alt and bool(images),
                                    f"מוצר {name}: {len(no_alt)} תמונות בלי טקסט חלופי" if images else f"מוצר {name}: אין תמונות"))
        cat = (p.get("category") or {}).get("fullName") or ""
        checks["product_category"].append((bool(cat) and cat != "Uncategorized", f"מוצר {name}: אין קטגוריה"))
        if not p["collections"]["nodes"]:
            checks["product_content"].append((False, f"מוצר {name}: לא נמצא באף קטגוריה באתר (אין אליו קישורים)"))

    for c in site["collections"]["nodes"]:
        if not c.get("onStore") or is_hidden(c):
            continue
        name = c["handle"]
        active = sum(1 for n in c["activeProducts"]["nodes"] if n["status"] == "ACTIVE")
        if active == 0:
            checks["clean_index"].append((False, f"קטגוריה {name}: גלויה לגוגל אבל אין בה מוצרים פעילים"))
            continue
        ok_t, n_t = check_len(c["seo"]["title"], TITLE_MIN, TITLE_MAX)
        checks["collection_seo"].append((ok_t, f"קטגוריה {name}: כותרת לגוגל באורך {n_t} תווים"))
        ok_d, n_d = check_len(c["seo"]["description"], DESC_MIN, DESC_MAX)
        checks["collection_seo"].append((ok_d, f"קטגוריה {name}: תיאור לגוגל באורך {n_d} תווים"))
        w = words(c["description"])
        checks["collection_seo"].append((w >= COLLECTION_MIN_WORDS, f"קטגוריה {name}: טקסט פתיחה קצר, {w} מילים"))

    # Pages that Google can see must belong to the current brand. Anything that still
    # mentions an old brand is flagged; the list lives in seo/store-profile.md.
    old_brands = re.compile(r"kneora|petil|knee sleeve|wellness|ברך|כלב|כושר|במבוק", re.I)
    for pg in site["pages"]["nodes"]:
        if not pg["isPublished"] or is_hidden(pg):
            continue
        text = f'{pg["title"]} {pg.get("bodySummary") or ""}'
        checks["clean_index"].append((not old_brands.search(text),
                                      f"דף {pg['handle']}: גלוי לגוגל ושייך למותג ישן"))

    published = []
    for b in site["blogs"]["nodes"]:
        blog_hidden = is_hidden(b)
        has_live = any(a["isPublished"] for a in b["articles"]["nodes"])
        if not blog_hidden and not has_live and b["handle"] != "news":
            checks["clean_index"].append((False, f"בלוג {b['handle']}: ריק וגלוי לגוגל"))
        for a in b["articles"]["nodes"]:
            if a["isPublished"] and not blog_hidden and not is_hidden(a):
                published.append(a)
                if not STOREFRONT_TEXT.search(a["title"]):
                    checks["clean_index"].append((False, f"מאמר {a['handle']}: לא בעברית"))
    if not checks["clean_index"]:
        checks["clean_index"].append((True, ""))

    now = dt.datetime.now(dt.timezone.utc)
    recent = [a for a in published if a.get("publishedAt") and
              (now - dt.datetime.fromisoformat(a["publishedAt"].replace("Z", "+00:00"))).days <= FRESH_DAYS]
    hebrew = [a for a in published if STOREFRONT_TEXT.search(a["title"])]
    for i in range(TARGET_ARTICLES):
        checks["blog"].append((i < len(hebrew), f"בלוג: {len(hebrew)} מאמרים בעברית מתוך {TARGET_ARTICLES} שאנחנו רוצים"))
    checks["blog"].append((bool(recent), f"בלוג: אין מאמר חדש ב-{FRESH_DAYS} הימים האחרונים"))

    areas = {}
    total = 0.0
    for key, weight in WEIGHTS.items():
        items = checks[key]
        rate = (sum(1 for ok, _ in items if ok) / len(items)) if items else 1.0
        areas[key] = round(rate * 100)
        total += rate * weight
    problems = []
    for key in WEIGHTS:
        for ok, msg in checks[key]:
            if not ok and msg not in problems:
                problems.append(msg)
    return {
        "score": round(total),
        "areas": areas,
        "live_products": len(live_products),
        "published_articles": len(published),
        "problems": problems,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--products", nargs="+", required=True)
    ap.add_argument("--site", required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    product_pages = load(args.products)
    if not product_pages:
        sys.exit("no product snapshot files found")
    with open(args.site, encoding="utf-8") as f:
        site = json.load(f)
    result = score(product_pages, site)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return
    print(f"ציון SEO: {result['score']}/100")
    for key, val in result["areas"].items():
        print(f"  {LABELS_HE[key]}: {val}%")
    print(f"מוצרים פעילים: {result['live_products']}, מאמרים מפורסמים: {result['published_articles']}")
    print("בעיות:")
    for msg in result["problems"]:
        print(f"  - {msg}")


if __name__ == "__main__":
    main()
