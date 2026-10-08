---
name: weekly-seo
description: Weekly SEO run for the Higanu Shopify store. Audits the store, scores it, applies safe fixes with a rollback log, drafts one Hebrew article, and reports to the owner in very simple Hebrew. Use when the weekly routine fires, or when the owner asks for an SEO check or status ("מה מצב ה-SEO", "תריץ SEO").
---

# Weekly SEO run

Read `CLAUDE.md` and `seo/store-profile.md` first. Use today's date (Asia/Jerusalem) as `DATE` everywhere below.

## 0. Prepare
- `git pull` the working branch so the latest changelog, history and content plan are present.
- Create `snapshot/` as a scratch folder. It is git-ignored.

## 1. Audit
Delegate to the `seo-auditor` subagent. It does three things:
1. Runs `seo/queries/products.graphql` (paged) and `seo/queries/site.graphql`, and saves the raw JSON into `snapshot/`.
2. Runs `python3 scripts/seo_score.py --products "snapshot/products-*.json" --site snapshot/site.json --json`.
3. Returns the score, the area percentages and the problem list.

Also note the owner-dependent checks, which are not in the script:
- Are any live products published to Google & YouTube?
- Is `higanu.co.il` reachable from this environment (`curl -sI https://higanu.co.il`)?
- Is `PSI_API_KEY` set? If so, run PageSpeed Insights (mobile) on the home page and on `/products/compression-cubes-6`, and record LCP, INP and CLS.

Compare with the last entry in `seo/history.json`, and list what got better or worse.

## 2. Fix
Delegate to the `seo-fixer` subagent. Give it the problem list, and stay inside the guardrails in `CLAUDE.md`. Fix in this order, at most:
1. Missing or bad SEO titles and descriptions on live products and collections. Up to 50 edits.
2. Missing image alt text on live products. Use `fileUpdate` with `alt`; never use `referencesToRemove`.
3. Missing product categories.
4. Thin descriptions: up to 5 products. Keep the original text and add facts only from store data.
5. Collection intro text under 15 words: write 40–80 words from store facts.
6. Old-brand or empty pages, collections and blogs that Google can see: set `seo.hidden` = 1.
7. Anything else from `seo/knowledge/rules.md` that is safe and reversible.

Before each write, the fixer appends the old value to `seo/changelog.md` under a `## DATE` heading. Anything outside the guardrails goes into the report as a question for the owner, and is not done.

## 3. Write
If no article draft from earlier weeks is still waiting, delegate to the `seo-writer` subagent:
- Take the next `idea` row from `seo/content-plan.md`.
- Create the article in blog `news` as unpublished.
- Mark the row `draft`, with its ID.

If two or more drafts are still waiting, skip writing this week and remind the owner instead. Drafts that pile up help no one.

## 4. Re-score and save
1. Re-run the snapshot and the score after the fixes.
2. Append `{date, score, areas, live_products, published_articles, article_drafts_waiting}` to `seo/history.json`.
3. Write `seo/reports/DATE.md` using the template below.
4. Commit everything except `snapshot/` and push.

## 5. Report to the owner
1. Reply with the same report in chat.
2. Send a push notification: "SEO שבועי: ציון X/100 (±Y). N תיקונים. M דברים מחכים לך."
   - Use the PushNotification tool; load it with ToolSearch first.

### Report template (very simple Hebrew, short lines)
```
# דוח SEO שבועי – DATE

**הציון: X/100** (שבוע שעבר: Y)

## מה השתפר
- ...

## מה תיקנתי השבוע
- ... (כל תיקון בשורה, במילים פשוטות)

## מה מחכה לך (רק את יכול/ה לעשות את זה)
1. ... (הכי חשוב ראשון, עם הסבר קצר למה זה חשוב ואיך עושים)

## מה אני אעשה בשבוע הבא
- ...

<details><summary>פרטים טכניים</summary>
אזורי הציון, רשימת בעיות מלאה, מה נבדק ומה לא היה אפשר לבדוק.
</details>
```

## Monthly extras (first run of each month)
- **Duplicate titles and descriptions** across products and collections.
- **Orphan products:** live products that are in no collection.
- **Redirect chains:** query `urlRedirects` and flag any target that is itself a redirect source or a draft or deleted product.
- **Live theme review.** Read the MAIN theme's `layout/theme.liquid` and `snippets/meta-tags.liquid`, and the Product JSON-LD in `sections/main-product.liquid`. Re-check rule 5 in `rules.md`, and list the theme fixes for the owner. Never edit the live theme.
