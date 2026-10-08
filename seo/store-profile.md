# Store profile: Higanu (הגענו)

Settings the owner can change:
- `auto_publish_articles: false`: when `true`, the agent publishes its weekly article instead of leaving a draft.
- `report_day: Sunday 09:00 Asia/Jerusalem`

## Basics
- Domain: https://higanu.co.il. Shopify plan "Shopify". Currency ILS. Language Hebrew only (`he`). Country Israel.
- Contact: hello@higanu.co.il, 053-236-5776, Sunday–Thursday 9:00–18:00.
- Shop description (also the homepage meta description): "קוביות דחיסה עם רוכסן כפול, קובייה לכל סוג בגד. אותם בגדים, חצי מהמקום במזוודה. 30 יום החזר כספי, 12 חודשי אחריות על הרוכסן, משלוח חינם מעל 139 ₪."

## Facts the agent may use (from the store's own policies and product data)
- 30-day money-back guarantee from delivery. The customer pays return shipping unless the item arrived damaged or wrong.
- Israeli consumer-law cancellation: 14 days.
- 12-month warranty on the compression zipper.
- Free shipping over 139 ₪. Ships within 1–2 business days; arrives within up to 14 business days in total. Tracking number by email.
- Prices include VAT.

## Live products (status ACTIVE, on the Online Store)
| Handle | Product GID | Price | Key facts |
|---|---|---|---|
| compression-cubes-6 | gid://shopify/Product/10247981498608 | 239 | 5 cubes plus a laundry bag, double compression zipper, water-resistant polyester, mesh window. Sizes: XL 40×40×9 (coats and sweaters), L 30×40×9 (pants), M 25×35×9 (shirts), S 20×30×9 (underwear), XS 35×10×9 (socks); laundry bag 47×35. 5 colors (black, red, light blue, green, grey). Up to 60% more space (store claim). Template `higanu-dr`. |
| toiletry-bag | gid://shopify/Product/10247982743792 | 99 | Water-resistant Oxford fabric, opens fully and hangs on the door, 19×10×24 cm, 150 g. |
| luggage-scale | gid://shopify/Product/10247982842096 | 69 | Up to 50 kg, LCD, 110 g, battery included. |
| neck-pillow | gid://shopify/Product/10247982973168 | 59 | Inflates in 3 breaths, folds to palm size. |
| cable-organizer | gid://shopify/Product/10247983137008 | 99 | 3 layers, elastic loops, mesh pockets. |
| family-passport-wallet | gid://shopify/Product/10247983268080 | 59 | Up to 6 passports, boarding passes and credit cards, RFID-blocking coating. |
| medicine-bag | gid://shopify/Product/10311535526128 | 69 | Opens like a book, elastic loops for bottles and pill trays, mesh pockets, 22×15×6 cm. |

- Every live product has image alt text.
- No variant has a barcode (GTIN).
- No product is published to the "Google & YouTube" channel yet.

## Collections
| Handle | GID | Status |
|---|---|---|
| travel-essentials (לדרך) | gid://shopify/Collection/490279108848 | live, main menu v1 |
| small-addons (תוספות קטנות) | gid://shopify/Collection/490279174384 | live |
| all-products (כל המוצרים) | gid://shopify/Collection/491267588336 | live, main menu v2 |
| kits (ערכות) | gid://shopify/Collection/490279141616 | empty, hidden from Google |
| KNEORA collections ×4, dog-car | see `seo/changelog.md` | old brands, hidden from Google |

## Old brands on the same store
The store previously sold KNEORA (knee sleeves, home gym) and PetIL (dog products).
- Their products are DRAFT, so they are not on the site.
- Their collections, pages and blogs were hidden from Google on 2026-10-08 with `seo.hidden = 1`. The pages stay live, so ads that point to them keep working.
- Never surface old-brand content.

## IDs
- Publications:
  - Online Store `gid://shopify/Publication/187224162544`
  - Google & YouTube `gid://shopify/Publication/190092345584`
  - Facebook & Instagram `gid://shopify/Publication/187695202544`
- Blog for articles: "News", handle `news`, `gid://shopify/Blog/103550681328`. It sits in the main menu as "בלוג". Its title is still "News" (renaming it needs the owner's OK).
- Live theme: "הגענו | 5.10 Claude: החורף טסים עד 31.10", `gid://shopify/OnlineStoreTheme/167088947440`. This changes often, so re-check `themes(roles: [MAIN])`.

## Brand voice (copy what is already in the store)
- Short, concrete sentences. Real numbers (sizes, grams, days).
- No hype words, no exclamation marks, no emojis.
- Uses "·" as a separator in titles.
- Speaks to the traveler in plural/neutral present tense ("שוקלים בבית", "פותחים את המזוודה").
- Product SEO title format: `<what it is + main keyword> · Higanu`, 25–65 characters.
