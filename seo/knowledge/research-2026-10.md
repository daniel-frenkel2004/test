# SEO research, October 2026

**בקצרה, בשפה פשוטה:** גוגל רוצה דפים שעוזרים לאנשים באמת. כל דף צריך כותרת ברורה ותיאור אמיתי. דפים ישנים וריקים מבלבלים את גוגל. מאמרים טובים בעברית מביאים אנשים שמחפשים "איך לארוז". ובינה מלאכותית (כמו ChatGPT) אוהבת מדריכים ברורים עם מספרים אמיתיים.

Two research agents compiled this on 2026-10-08. Their direct fetches of Google and Shopify docs were blocked by the network, so these claims come from search snippets and secondary coverage. Re-check the numbers that matter against the live docs when access allows.

## Shopify and Google rules (2025–2026)
- **Titles and descriptions**
  - Title about 580 px wide (about 50–60 Latin characters). Google rewrites most titles over 70 characters.
  - Meta description: 120–155 characters, cut at about 680 px on mobile.
  - Sources: zyppy.com/title-tags/meta-title-tag-length/ and screamingfrog.co.uk/page-title-meta-description-lengths-by-pixel-width
- **Core updates**
  - December 2025 core update: heavy on ecommerce.
  - March 2026 core update (finished 8 April): hit templated pages, manufacturer copy and unedited AI pages.
  - May 2026 core update: favored brands and first-party sources.
  - Spam updates in June, August and September 2026.
  - Sources: amsive.com/insights/seo/google-march-2026-core-update/ and searchenginejournal.com/google-begins-rolling-out-may-2026-core-update/575589/
- **Helpful content**
  - The helpful content system has been part of core ranking since March 2024.
  - The scaled content abuse policy applies to AI and human writers alike.
  - The 2025 rater guidelines give AI-generated main content with no added value the Lowest rating.
  - Source: developers.google.com/search/blog/2023/02/google-search-and-ai-content
- **FAQ rich results** stopped showing for all sites on 7 May 2026. Visible FAQs still help users and AI answers.
  - Source: searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/
- **Shipping and returns markup**
  - Can be declared once at Organization level since 12 November 2025: `hasMerchantReturnPolicy`, `hasShippingService`.
  - Source: developers.google.com/search/blog/2025/11/more-ways-to-share-shipping
- **ProductGroup** is supported by Shopify's `structured_data` filter since July 2024.
  - Source: shopify.dev/changelog/liquid-structured_data-filter-supports-productgroup
- **Hiding a resource from Google:** `seo.hidden` = 1 adds noindex and removes it from the sitemap.
  - Source: shopify.com/blog/noindex-shopify-page
- **Redirects** fire only for 404 URLs; native ones are 301 only.
  - Source: help.shopify.com/en/manual/online-store/menus-and-links/url-redirect
- **Core Web Vitals**
  - Thresholds: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 (p75).
  - Shopify mobile medians: LCP 2.26 s, INP 153 ms, CLS 0.01. LCP is the usual risk.
  - Sources: web.dev/articles/defining-core-web-vitals-thresholds and sherocommerce.com/blogs/insights/shopify-speed-benchmarks

## Hebrew and Israel
- **Language and region**
  - Use `lang="he"` and `dir="rtl"`; never "iw".
  - The .co.il domain already targets Israel, so a single-language store needs no hreflang.
- **Handles**
  - Hebrew handles become long `%D7%..` strings. Use English or transliterated handles.
  - Never change a handle that already ranks without a 301 redirect.
- **Keyword research**
  - Treat prefixed forms (ו/ה/ב/ל/מ/ש/כ) as separate research rows.
  - Put the bare form in the title and H1.
  - Plural forms usually mean collection intent; singular forms mean product intent.
  - Check full and defective spelling variants.
  - Google's handling of Hebrew morphology is not documented, so verify with Search Console queries.
- **VAT** has been 18% since January 2025. Show prices with VAT, and use the same price everywhere.

## AI search
- **Google's AI optimization guide** (15 May 2026): AI Overviews and AI Mode use core ranking plus "query fan-out". They need no special schema, no llms.txt and no chunking. Unique content, Core Web Vitals and canonicals are what help.
  - Source: developers.google.com/search/docs/fundamentals/ai-optimization-guide
- **Israel:** AI Overviews have been available here since May 2025. No source confirmed that AI Mode works in Hebrew.
- **llms.txt** has no effect on Google Search.
  - Source: searchenginejournal.com/googles-llms-txt-guidance-depends-on-which-product-you-ask/575431/
- **Citation drivers.** These are vendor studies, so read them as direction rather than precise numbers.
  - Brand mentions correlate with AI Overview visibility at r=0.66, against r=0.22 for backlinks.
  - A review-platform profile lifts AI citations a lot.
  - Buying guides and comparison pages get about 10× more citations than product pages.
  - Sources: searchengineland.com/guide/ai-citations-vs-ai-mentions-data, seerinteractive.com/news/forbes-seer-research-review-profiles-in-ai-citations, 1digitalagency.com
- **Merchant Center free listings**
  - Israel is supported. Connect through the Google & YouTube app.
  - Feed price and availability must match the page.
  - Source: support.google.com/merchants/answer/13692890

## Running SEO with an agent: what works
- **What agents do well and badly**
  - Agents handle audits, bulk metadata, alt text, internal links and monitoring well.
  - They choose priorities, judge brand voice and do off-site work badly.
  - So the owner approves content and theme changes.
  - Source: vortexiq.ai/blog/what-happens-when-you-let-ai-run-your-store-for-a-week
- **Weekly checklist**
  - Metadata on new or changed items.
  - Alt text on new images.
  - 3–5 product pages improved.
  - One article draft.
  - A check of new 404s and redirects.
  - The report.
- **Monthly checklist**
  - Thin and duplicate content.
  - Cannibalization.
  - Orphan products.
  - Speed.
  - Redirect chains.
  - Old content refreshed.
  - Duplicate JSON-LD from apps.
- **Quarterly checklist**
  - Full audit.
  - Competitor gap review.
  - Theme and app speed audit.
  - Backlinks review.
- **Health score.** Ahrefs counts the share of URLs with no errors. Semrush weighs errors more than warnings. Our score (`scripts/seo_score.py`) is a weighted share of checks passed, by area.
- **Rollback:** log the old value before every write, and re-apply it with the same mutation to revert.

## Free data sources the agent can use once the owner connects them
- **Google Search Console API.** OAuth, scope `webmasters.readonly`.
  - `searchAnalytics/query` returns clicks, impressions, CTR and position.
  - `urlInspection/index:inspect` allows 2,000 inspections a day.
- **PageSpeed Insights API.** Needs a free API key, because unkeyed quota is 0 from this environment (tested 2026-10-08). The response includes CrUX field data.
- **Shopify ShopifyQL** through the `run-analytics-query` tool: organic sessions and sales by referrer.
