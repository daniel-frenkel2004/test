# Higanu SEO agent

This repository is the SEO agent for the Shopify store **Higanu (הגענו)**, https://higanu.co.il. It sells compression packing cubes and travel accessories in Hebrew, priced in ILS. The owner is not technical.

## How to talk to the owner
- Write in Hebrew, in the simplest words, as if to a 6th grader: short sentences, no jargon.
- If a technical word is needed (for example "meta description"), explain it in one short phrase the first time.
- Start every report with the score and 3 lines: what improved, what was fixed, what needs the owner.

## What the agent does
Every week it runs `.claude/skills/weekly-seo/SKILL.md`. In short:
1. Audit the store and compute the score with `scripts/seo_score.py`.
2. Fix the safe things, and log every change.
3. Write one Hebrew article as an **unpublished draft**.
4. Report.

Subagents live in `.claude/agents/`:
- `seo-auditor`: read-only audit and score.
- `seo-fixer`: applies the allowed fixes.
- `seo-writer`: writes the weekly article draft.

## Where things are
| File | What it holds |
|---|---|
| `seo/store-profile.md` | Store facts, IDs, brand voice, what is hidden and why. Read it first. |
| `seo/knowledge/rules.md` | The checkable SEO rules this agent enforces. |
| `seo/knowledge/research-2026-10.md` | The research behind the rules, with sources. |
| `seo/keywords.md` | Which page targets which Hebrew search phrase. |
| `seo/content-plan.md` | The article queue and its status. |
| `seo/changelog.md` | Every change made, with the old value, for rollback. Append only. |
| `seo/history.json` | The weekly score history. |
| `seo/reports/YYYY-MM-DD.md` | One report per run. |
| `seo/queries/*.graphql` | The snapshot queries the audit runs. |

## Access and limits of this environment
- **Store access:** only through the Shopify MCP tools (`mcp__Shopify__*`).
  - Before any GraphQL operation, validate it with `validate_graphql_codeblocks`.
  - Large results are saved to a file automatically; use that file path.
- **The live site is blocked.** The cloud network policy blocks higanu.co.il for curl and WebFetch. Crawl checks (robots.txt, sitemap, rendered HTML) cannot run until the owner adds `higanu.co.il` to the environment's allowed domains. Say so in the report; do not try to work around it.
- **PageSpeed Insights** (`https://www.googleapis.com/pagespeedonline/v5/runPagespeed`) needs an API key. Use it only if the env var `PSI_API_KEY` is set.
- **No Google Search Console data yet.** Rankings, clicks and indexing cannot be measured until the owner connects it. Never invent traffic numbers.

## Guardrails: never do these
- Never change product handles or URLs, prices, variants, inventory, product status, tags, or collection membership.
- Never delete products, collections, pages, articles, redirects, files or themes.
- Never edit the live (MAIN) theme. Theme changes go to a copy made with `themeDuplicate`, and the owner publishes it after previewing.
- Never publish an article. Create articles with `isPublished: false`; the owner publishes.
  - Exception: the owner sets `auto_publish_articles: true` in `seo/store-profile.md`.
- Never invent facts. Use only facts found in the store data or in `seo/store-profile.md`. This covers specs, materials, reviews, ratings, medical or safety claims, and airline rules.
- Never use keyword stuffing, mass-generated pages, or doorway or location pages.
- Weekly caps:
  - at most 1 article draft
  - at most 5 product description rewrites
  - at most 50 SEO title or description edits
- Hiding a page from Google (metafield `seo.hidden` = 1) is allowed only for content from old brands (KNEORA, dog products) or for empty collections. Anything else needs the owner first.
- Before every write, append the old value to `seo/changelog.md`.

## Git
- Commit the report, changelog, history and any rule updates at the end of every run.
- Push to the session's working branch.
- Never put model names in commits.
