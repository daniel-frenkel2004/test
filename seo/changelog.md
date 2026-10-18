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

## 2026-10-11: weekly run

### New article draft (`articleCreate`, `isPublished: false`)
- **Old value:** none (new article; nothing existed before). Handle `what-are-compression-packing-cubes` was checked and is free.
- **New:** "קוביות דחיסה: מה זה, איך משתמשים, ושווה או לא", in blog `news` (`gid://shopify/Blog/103550681328`), content plan #2.
  - Body: 719 words, 2 store images (`6859f567…png` double zipper, `hf_20260920_101257_…png` red set); featured image `hf_20260920_102323_8108d6fd…png` (light-blue set).
  - Links: `/products/compression-cubes-6`, `/collections/travel-essentials`, `/products/luggage-scale`, pillar `/blogs/news/how-to-pack-carry-on-for-a-week`.
  - Metafields `global.title_tag` and `global.description_tag` set on create.
- **To undo:** the owner deletes the draft in Shopify admin (the agent never deletes articles).

### Fixes

#### Pillow filled with clothes: `כרית-צוואר-שממלאים-בבגדים-חוסכת-מקום-בתיק` `gid://shopify/Product/10347021435120` (`productUpdate`)
Went live 2026-10-08 16:45Z via Shopify Claude Connector (not by this agent).
- **SEO title:** old (empty) → new `כרית צוואר שממלאים בבגדים · חוסכת מקום · Higanu`
- **SEO description:** old (empty) → new `כרית צוואר שממלאים בבגדים דרך רוכסן בקצה, והיא מקבלת צורת U רכה. ריקה היא מתקפלת לכף יד, וכך נשאר מקום בטרולי לבגדים.`
- **Category:** old (none) → new Health & Beauty > Personal Care > Sleeping Aids > Travel Pillows (`gid://shopify/TaxonomyCategory/hb-3-15-3`, same as neck-pillow)
- **descriptionHtml** (rewrite 1 of 5): the old text kept word for word, with one closing paragraph with 2 links added.
  - Old value:
```html
<p><strong>הסוודר שלא נכנס לתיק הופך לכרית לטיסה.</strong></p><p>הכרית מגיעה ריקה. ממלאים אותה דרך רוכסן בקצה בחולצות, בסוודר או בצעיף, והיא מקבלת צורת U רכה שמחזיקה את הצוואר. ככה יש כרית בטיסה, ויש מקום בטרולי לבגדים.</p><ul>
<li>בד קטיפתי רך, שחור</li>
<li>רוכסן מילוי בקצה</li>
<li>אבזם קדמי שמחזיק את הכרית סגורה</li>
<li>רצועה מתכווננת לתלייה על התיק או על הטרולי</li>
<li>ריקה היא מתקפלת לגודל של כף יד</li>
</ul>
```
  - Added at the end:
```html
<p>את הבגדים שלא נכנסו לכרית מסדרים ב<a href="/products/compression-cubes-6">קוביות הדחיסה של Higanu</a>. את שאר האביזרים לטיסה רואים ב<a href="/collections/travel-essentials">לדרך</a>.</p>
```
- **To undo:** `productUpdate` with `seo: {title: "", description: ""}`, `category: null`, and `descriptionHtml` = the old value above.

#### Hood pillow: `כרית-צוואר-עם-ברדס-נרדמים-גם-כשהאור-דולק` `gid://shopify/Product/10347021730032` (`productUpdate`)
Went live 2026-10-08 16:45Z via Shopify Claude Connector (not by this agent).
- **SEO title:** old (empty) → new `כרית צוואר עם ברדס · חוסמת אור בטיסה · Higanu`
- **SEO description:** old (empty) → new `כרית צוואר עם ברדס שנמשך על העיניים וחוסם את האור במטוס. צורת U באורך 73 ס״מ, ג׳רסי כותנה רך. מתקפלת לשקית עם רצועה שנתלית על הטרולי.`
- **Category:** old (none) → new Health & Beauty > Personal Care > Sleeping Aids > Travel Pillows (`gid://shopify/TaxonomyCategory/hb-3-15-3`)
- **descriptionHtml** (rewrite 2 of 5): the old text kept word for word, with one closing paragraph with 2 links added.
  - Old value:
```html
<p><strong>מושכים את הברדס על העיניים, והאור של המטוס נעלם.</strong></p><p>כרית צוואר בצורת U עם ברדס רך מחובר. הכרית מחזיקה את הראש כשנרדמים בישיבה, והברדס חוסם את האור ואת התנועה מסביב. בסוף הטיסה מקפלים אותה לשקית קטנה עם רצועה שנתלית על ידית הטרולי.</p><ul>
<li>בד ג׳רסי כותנה רך, אפור</li>
<li>ברדס מחובר שנמשך על העיניים</li>
<li>אבזם קדמי מתכוונן</li>
<li>שקית אחסון עם רצועת כתף</li>
<li>73 ס״מ לאורך הכרית</li>
</ul>
```
  - Added at the end:
```html
<p>הכרית בשקית שלה נתלית על הטרולי, והבגדים מסודרים בפנים ב<a href="/products/compression-cubes-6">קוביות הדחיסה של Higanu</a>. את שאר האביזרים לטיסה רואים ב<a href="/collections/travel-essentials">לדרך</a>.</p>
```
- **To undo:** `productUpdate` with `seo: {title: "", description: ""}`, `category: null`, and `descriptionHtml` = the old value above.

### New article draft: result
- **Created:** `gid://shopify/Article/599295721712`, handle `what-are-compression-packing-cubes`, `isPublished: false` (checked after create). This belongs to "New article draft" above, not to "Fixes".

#### Collection intros (`collectionUpdate` → `descriptionHtml`)
To undo any of these, run `collectionUpdate` with `descriptionHtml` = the old value.

- **small-addons** `gid://shopify/Collection/490279174384`: the old intro listed 5 items and missed the medicine bag. The new one lists all 6, links the cubes set and adds free shipping (54 words).
  - Old value:
```html
<p>הפריטים הקטנים שמשלימים את המזוודה: תיק טואלטיקה, משקל, כרית, ארגונית כבלים וארנק דרכונים.</p>
```
  - New value:
```html
<p>הפריטים הקטנים שמשלימים את המזוודה ואת <a href="/products/compression-cubes-6">סט קוביות הדחיסה</a>. תיק טואלטיקה תלוי שנפתח ונתלה על הדלת. משקל מזוודה דיגיטלי עד 50 ק״ג. כרית צוואר מתנפחת שמתקפלת לגודל כף יד. ארגונית כבלים בשלוש שכבות. ארנק דרכונים משפחתי עם חסימת RFID, עד 6 דרכונים. תיק תרופות לדרך שנפתח כמו ספר. משלוח חינם מעל 139 ₪.</p>
```

- **all-products** `gid://shopify/Collection/491267588336`: the owner's first sentence was kept word for word. Added: the 5-cube set with the laundry bag, the accessories for the flight and for families, and the guarantees (64 words). The two new pillows are not named, because they are not in this collection.
  - Old value:
```html
<p>הסט המלא בראש, ואחריו כל מה שמשלים אותו: תיקים לנסיעה, ארגון ונוחות בטיסה.</p>
```
  - New value:
```html
<p>הסט המלא בראש, ואחריו כל מה שמשלים אותו: תיקים לנסיעה, ארגון ונוחות בטיסה.</p><p>הסט הוא <a href="/products/compression-cubes-6">חמש קוביות דחיסה ושק כביסה</a>, עם רוכסן כפול וקובייה לכל סוג בגד. לטיסה יש תיק טואלטיקה תלוי, משקל מזוודה, כרית צוואר מתנפחת וארגונית כבלים. למשפחות יש ארנק דרכונים לעד 6 דרכונים ותיק תרופות לדרך.</p><p>30 יום החזר כספי, 12 חודשי אחריות על הרוכסן, משלוח חינם מעל 139 ₪.</p>
```

- **travel-essentials** `gid://shopify/Collection/490279108848`: removed the sentence "טרולי מיני (3 קוביות) למי שנוסע קל.", because `compression-cubes-3` (`gid://shopify/Product/10248484684016`) is DRAFT and can't be bought. The owner's other two sentences were kept word for word. Added the accessories, including the two new neck pillows (49 words).
  - Old value:
```html
<p>הסט המלא הוא הבסיס: חמש קוביות דחיסה ושק כביסה, וכל בגד יודע לאן. טרולי מיני (3 קוביות) למי שנוסע קל. את השאר מוסיפים לפי הצורך.</p>
```
  - New value:
```html
<p>הסט המלא הוא הבסיס: חמש קוביות דחיסה ושק כביסה, וכל בגד יודע לאן. את השאר מוסיפים לפי הצורך.</p><p>לטיסה יש שלוש כריות צוואר: מתנפחת שמתקפלת לכף יד, כרית שממלאים בבגדים, וכרית עם ברדס שחוסם את האור. וגם: תיק טואלטיקה תלוי, משקל מזוודה, ארגונית כבלים, ארנק דרכונים משפחתי ותיק תרופות.</p>
```

#### Weekly caps used by these fixes
- SEO title/description edits: 4 of 50 (2 titles, 2 descriptions).
- Description rewrites: 2 of 5 for products (the two pillows). The 3 collection intros were also rewritten, so 5 of 5 if collection intros count against the same cap.
- Categories set: 2 (no cap).

## 2026-10-12: owner approved publishing article #2 in chat ("תפרסם את המאמר השני")
- Article `gid://shopify/Article/599295721712` (what-are-compression-packing-cubes), via `articleUpdate`: `isPublished` changed from false to true. Nothing else changed.
- **To undo:** `articleUpdate` with `isPublished: false`.

## 2026-10-18: weekly run

### New article draft (`articleCreate`, `isPublished: false`)
- **Old value:** none (new article; nothing existed before). Handle `flight-carry-on-packing-list` was checked and is free.
- **New:** "רשימת ציוד לטיסה: מה לקחת בתיק היד", in blog `news` (`gid://shopify/Blog/103550681328`), content plan #3.
  - Body: 647 words, 3 store images (`hg-wallet-g3.jpg` passport wallet open, `hg-cables-g3.jpg` cable organizer in a backpack, `hg-pillow-inflatable-g4.jpg` neck pillow on the plane); featured image `hg-wallet-g4.jpg` (passport at the airport gate).
  - Links: `/products/family-passport-wallet`, `/products/cable-organizer`, `/products/neck-pillow`, `/collections/travel-essentials`, pillar `/blogs/news/how-to-pack-carry-on-for-a-week`.
  - Metafields `global.title_tag` and `global.description_tag` set on create.
- **To undo:** the owner deletes the draft in Shopify admin (the agent never deletes articles).

### Fixes

#### Collection intros: the two new pillows (`collectionUpdate` → `descriptionHtml`)
The owner added the two new neck pillows (`gid://shopify/Product/10347021435120`, `gid://shopify/Product/10347021730032`) to these collections around 2026-10-17. The intros named only the inflatable pillow. Minimal edit: one short fact per new pillow, all other text and links kept word for word.

- **small-addons** `gid://shopify/Collection/490279174384`, field `descriptionHtml` (54 → 63 words).
  - Old value:
```html
<p>הפריטים הקטנים שמשלימים את המזוודה ואת <a href="/products/compression-cubes-6">סט קוביות הדחיסה</a>. תיק טואלטיקה תלוי שנפתח ונתלה על הדלת. משקל מזוודה דיגיטלי עד 50 ק״ג. כרית צוואר מתנפחת שמתקפלת לגודל כף יד. ארגונית כבלים בשלוש שכבות. ארנק דרכונים משפחתי עם חסימת RFID, עד 6 דרכונים. תיק תרופות לדרך שנפתח כמו ספר. משלוח חינם מעל 139 ₪.</p>
```
  - New value:
```html
<p>הפריטים הקטנים שמשלימים את המזוודה ואת <a href="/products/compression-cubes-6">סט קוביות הדחיסה</a>. תיק טואלטיקה תלוי שנפתח ונתלה על הדלת. משקל מזוודה דיגיטלי עד 50 ק״ג. כרית צוואר מתנפחת שמתקפלת לגודל כף יד, כרית שממלאים בבגדים, וכרית עם ברדס שחוסם את האור. ארגונית כבלים בשלוש שכבות. ארנק דרכונים משפחתי עם חסימת RFID, עד 6 דרכונים. תיק תרופות לדרך שנפתח כמו ספר. משלוח חינם מעל 139 ₪.</p>
```

- **all-products** `gid://shopify/Collection/491267588336`, field `descriptionHtml` (64 → 74 words).
  - Old value:
```html
<p>הסט המלא בראש, ואחריו כל מה שמשלים אותו: תיקים לנסיעה, ארגון ונוחות בטיסה.</p><p>הסט הוא <a href="/products/compression-cubes-6">חמש קוביות דחיסה ושק כביסה</a>, עם רוכסן כפול וקובייה לכל סוג בגד. לטיסה יש תיק טואלטיקה תלוי, משקל מזוודה, כרית צוואר מתנפחת וארגונית כבלים. למשפחות יש ארנק דרכונים לעד 6 דרכונים ותיק תרופות לדרך.</p><p>30 יום החזר כספי, 12 חודשי אחריות על הרוכסן, משלוח חינם מעל 139 ₪.</p>
```
  - New value:
```html
<p>הסט המלא בראש, ואחריו כל מה שמשלים אותו: תיקים לנסיעה, ארגון ונוחות בטיסה.</p><p>הסט הוא <a href="/products/compression-cubes-6">חמש קוביות דחיסה ושק כביסה</a>, עם רוכסן כפול וקובייה לכל סוג בגד. לטיסה יש תיק טואלטיקה תלוי, משקל מזוודה, ארגונית כבלים ושלוש כריות צוואר: מתנפחת, כזו שממלאים בבגדים, וכזו עם ברדס שחוסם את האור. למשפחות יש ארנק דרכונים לעד 6 דרכונים ותיק תרופות לדרך.</p><p>30 יום החזר כספי, 12 חודשי אחריות על הרוכסן, משלוח חינם מעל 139 ₪.</p>
```
- **To undo:** `collectionUpdate` with the old value.
