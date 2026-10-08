# Changelog: every change the agent made in the store

Append only. Every entry records the old value, so any change can be undone by re-applying it with the same mutation:
- `productUpdate` for products
- `collectionUpdate` for collections
- `metafieldsSet` (value "0"), or `metafieldsDelete`, for hidden flags

## 2026-10-08: first audit and fixes (score 35 → 77)

### Product SEO titles and descriptions (`productUpdate` → `seo`)
| Product | Old SEO title | Old SEO description |
|---|---|---|
| medicine-bag `10311535526128` | (empty) | (empty) |
| luggage-scale `10247982842096` | משקל מזוודה דיגיטלי · Higanu | שוקלים את המזוודה בבית ולא בדלפק. עד 50 ק״ג, תצוגת LCD, 110 גרם, סוללה כלולה. |
| toiletry-bag `10247982743792` | תיק טואלטיקה תלוי לטיסה · Higanu | תיק טואלטיקה עמיד למים שנפתח ונתלה על הדלת. הבקבוקים עומדים, שום דבר לא נשפך. 19×10×24 ס״מ, 150 גרם. |
| neck-pillow `10247982973168` | כרית צוואר מתקפלת לטיסה · Higanu | כרית צוואר שמתנפחת בשלוש נשיפות ומתקפלת לגודל כף יד. תמיכה בטיסה ארוכה בלי לתפוס מקום בתיק. |
| cable-organizer `10247983137008` | ארגונית כבלים ומטענים · Higanu | שלוש שכבות, לולאות אלסטיות וכיסי רשת. כל הכבלים, המטענים והאוזניות במקום אחד ולא בתחתית התיק. |
| family-passport-wallet `10247983268080` | ארנק דרכונים משפחתי RFID · Higanu | עד 6 דרכונים, כרטיסי טיסה וכרטיסי אשראי עם חסימת RFID. בבידוק עוברים עם ארנק אחד ביד. |

### Product categories (`productUpdate` → `category`)
| Product | Old | New |
|---|---|---|
| medicine-bag | Uncategorized | Luggage & Bags > Luggage Accessories > Travel Pouches (`lb-9-8`) |
| luggage-scale | Uncategorized | Luggage & Bags > Luggage Accessories (`lb-9`) |
| toiletry-bag | Uncategorized | Luggage & Bags > Cosmetic & Toiletry Bags > Toiletry Bags (`lb-3-4`) |
| cable-organizer | (none) | Luggage & Bags > Luggage Accessories > Packing Organizers (`lb-9-6`) |

### Product descriptions (`productUpdate` → `descriptionHtml`)
The original text was kept word for word as the first paragraph. Added below it:
- a "מה מקבלים / מה נכנס" list made from existing facts
- a short "למה / מתי" paragraph
- links to `/products/compression-cubes-6` and `/collections/small-addons`

To undo, set `descriptionHtml` back to the old value:
- toiletry-bag: `<p>בד אוקספורד עמיד למים, נפתח לגמרי ונתלה על הדלת. 19×10×24 ס"מ, 150 גרם. כל הבקבוקים עומדים, שום דבר לא נשפך על הבגדים.</p>`
- luggage-scale: `<p>עד 50 ק"ג, תצוגת LCD, 110 גרם. שוקלים בבית, לא בדלפק. סוללה כלולה.</p>`
- neck-pillow: `<p>מתנפחת בשלוש נשיפות, מתקפלת לגודל כף יד. תמיכה לצוואר בטיסה ארוכה, בלי לתפוס מקום בתיק.</p>`
- cable-organizer: `<p>שלוש שכבות, לולאות אלסטיות וכיסי רשת. כל הכבלים, המטענים והאוזניות במקום אחד, לא בתחתית התיק.</p>`
- family-passport-wallet: `<p>עד 6 דרכונים, כרטיסי טיסה וכרטיסי אשראי, עם ציפוי חוסם RFID. בבידוק עוברים עם ארנק אחד ביד.</p>`
- medicine-bag: `<p>חום באמצע הלילה במלון, והסירופ כבר ביד. כל תרופה, מדחום ופלסטר במקום משלו, בלי לחפור בתחתית המזוודה.</p><p>נפתח כמו ספר: לולאות גומי לבקבוקונים ולמגשי כדורים, וכיסי רשת לפלסטרים ולשאר הדברים הקטנים. 22×15×6 ס"מ, נכנס בפינה של המזוודה ליד הקוביות.</p>`

### Collection SEO (`collectionUpdate` → `seo`)
The old SEO title and description were empty for all three:
- travel-essentials `490279108848`
- small-addons `490279174384`
- all-products `491267588336`

### Hidden from Google (`metafieldsSet` seo.hidden = 1)
These were all old-brand or empty. The pages stay live for visitors and ads. To undo, set the value to "0" or delete the metafield.
- **Collections:**
  - מדריכים-דיגיטליים-e-books `485723865328`
  - ציוד-כושר-ובריאות `485723898096`
  - שינה-ונוחות `485723930864`
  - שרוולי-תמיכה-מבמבוק `485724324080`
  - dog-car `486805733616`
  - kits (empty) `490279141616`
- **Pages:**
  - wellness1 `160650494192`
  - dash-ngisot (KNEORA accessibility statement) `161909735664`
  - 9-reasons-homegym `164355047664`
  - dog-hair `164721754352`
  - my-gifts `165095178480`
- **Blogs (empty, English):**
  - how-to-choose-a-knee-sleeve `104010514672`
  - 2026-stop-waking-up-from-knee-pain-new-sleep-solution `104024310000`

### New article draft (`articleCreate`, `isPublished: false`)
- "איך לארוז לשבוע בטרולי עלייה למטוס: שיטת הקוביות", `gid://shopify/Article/599268229360`, in blog `news`.

## 2026-10-08 (later): article images and publish (owner approved in chat)
- **Article** `gid://shopify/Article/599268229360` (how-to-pack-carry-on-for-a-week), using `articleUpdate`:
  - **Old state:** `isPublished: false`, no featured image, body without images.
  - **New state:** `isPublished: true`.
  - **Featured image:** the store's own photo `hf_20260909_103219_…png` (5 cubes plus laundry bag).
  - **3 store images added to the body,** each with Hebrew alt text, width and height set, and lazy loading:
    - `2.svg`: what goes in each cube (after step 2)
    - `hf_20260909_105939_…png`: before/after comparison (after step 4)
    - `hf_20260921_074101_46fad4ab…png`: medicine bag open (after step 6)
- **To undo:** run `articleUpdate` with `isPublished: false`. The body without images is the original draft text (`content-plan.md` #1).
