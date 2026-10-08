# SEO rules the agent enforces

Each rule is checkable. The numbers in `scripts/seo_score.py` must match this file. Tags:
- **[G]** comes from Google's own documentation.
- **[conv.]** is an industry convention, so its threshold can be adjusted.

Sources are in `research-2026-10.md`.

## 1. Product pages
1. **SEO title.**
   - 25–65 characters, about 580 px on desktop.
   - Main Hebrew keyword first, then a benefit or spec, then `· Higanu`.
   - Unique across the site. [conv.]
2. **Meta description.**
   - 70–160 characters, with the key message in the first 120 characters (the mobile cutoff).
   - Unique, and only true facts. [conv.]
3. **One H1** that matches the product title. The theme block `blocks/product_title.liquid` does this. [G]
4. **Description.**
   - At least 60 words. The goal is 150+ for the main product. [conv.]
   - Original text, never supplier copy. [G: the March 2026 core update hit manufacturer copy.]
   - Order: a short benefit summary, then a "מה מקבלים" list of specs, then use cases, then 1–2 internal links.
5. **Image alt text** on every image.
   - Hebrew, up to 125 characters, names the item plus a visible detail.
   - Never a list of keywords. Israel's accessibility law requires alt text anyway (IS 5568).
6. **Category set** (Shopify taxonomy, not "Uncategorized"). This feeds Google Shopping.
7. **In at least one collection**, so the product has internal links.
8. **Handle.**
   - Lowercase ASCII words separated by hyphens.
   - Never change the handle of a live product (the agent never changes handles at all).

## 2. Collection pages
1. SEO title and description follow the same lengths as products. Plural keywords ("אביזרי טיסה") belong on collections, singular ones on products. [conv.]
2. Intro text of at least 15 words now; the goal is 50–150 words. [conv.]
3. A collection with no active products must not be visible to Google. Hide it with `seo.hidden` = 1, or fill it.

## 3. A clean index (what Google can see)
1. No page, collection or blog from an old brand (KNEORA, PetIL) may be visible to Google.
2. No empty blogs, and no non-Hebrew articles, visible to Google.
3. `seo.hidden` = 1 (type `number_integer`) adds noindex and also removes the URL from the sitemap. Shopify supports it on products, collections, pages, blogs and articles. [G/Shopify]
4. Redirects only fire for URLs that return 404. Never chain more than one hop.
5. An out-of-stock product stays live, marked OutOfStock. A discontinued product gets a 301 to its closest replacement, never in bulk to the homepage (Google treats that as a soft 404). [G]

## 4. Blog and content
1. One article a week, as an **unpublished draft** for the owner to approve.
2. Each article targets one search phrase from `seo/keywords.md`.
   - 500–1,200 words in plain Hebrew.
   - H2 for each step or section.
   - A short FAQ at the end.
   - 2–4 links to products or collections.
3. **First-hand value.** Use real product facts (sizes, what goes in which cube). Ask the owner for a photo or a personal tip. Google's rater guidelines rate AI-generated content with no added value as Lowest. [G]
4. **Never invent:** no fake reviews, numbers or airline rules. Write "בודקים באתר חברת התעופה" instead.
5. **SEO title and description for articles.** Set them with the metafields `global.title_tag` and `global.description_tag` (`single_line_text_field`). Articles and pages have no `seo` input. [Shopify]
6. **Clusters.** One pillar guide per main topic plus 6–8 supporting posts. Each supporting post links to the pillar and to the collection. [conv.]

## 5. Technical
These checks need the owner. They are not automatic yet.
1. `<html lang="he" dir="rtl">`. The current theme outputs `lang` but puts `dir` only on `<body data-rtl>`.
2. JSON-LD:
   - Exactly one Product block per page, with Offer, `price` as a number and `priceCurrency` "ILS".
   - Add `itemCondition`.
   - Add Organization-level `hasMerchantReturnPolicy` (country IL, 30 days, return by mail, customer pays return shipping). [G, Nov 2025]
3. The current theme's Organization `sameAs` outputs empty strings for social links that are not set. Fix it in a theme copy.
4. Core Web Vitals at p75 on mobile: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1. [G]
5. Keep third-party app scripts low. After uninstalling an app, check `theme.liquid` and `snippets/` for leftover code.
6. robots.txt: keep Shopify's defaults. Allow OAI-SearchBot, PerplexityBot, Bingbot and Googlebot. `llms.txt` has no effect on Google. [G, June 2026]

## 6. AI search (Google AI Overviews, ChatGPT)
1. Put product facts in plain text in the HTML: dimensions, weight, contents, warranty, delivery days, return terms.
2. Buying guides and comparison pages get cited far more often than product pages. Prioritize guides in the content plan.
3. Free Google Shopping listings: publish products to the Google & YouTube channel and keep feed, page and schema prices identical. This is the owner's decision; it is not done yet.
