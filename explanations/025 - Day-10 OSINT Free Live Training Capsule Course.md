# OSINT Day 10 — Facebook Finale: IDs, URL Filters aur Tool Evaluation (Hinglish Explanation)

**Source transcript:** `transcripts/025 - Day-10 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** Day 9 — Facebook public pages/profiles, UID, page source aur tool-based search
**Closes:** Transcript ka Facebook block; Instagram/other OSINT continuation course poll par depend karta hai
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likhi gayi hai. Facebook URL/filter examples ko only public, owned test account ya explicitly authorized assessment par use karo. Private-account bypass, friend manipulation, password/token collection aur mass actions allowed nahi.

---

## 1. Day 10 ka leftover: object IDs

Day 9 mein user ID/UID aur location ID ka concept aaya. Aaj remaining Facebook object IDs locate kiye jate hain:

- event ID,
- page ID,
- group ID.

### 1.1 Page source workflow

Authorized/public page ya owned test page par:

```text
Open page/event/group
-> Right click
-> View Page Source
-> Ctrl+F
-> search relevant ID field
```

Transcript mein event page ke source se event ID, page source se page ID aur group source se group ID find karne ka demo hai. Aap source ko text file mein save karke command-line search bhi kar sakte ho:

```bash
grep -iE 'page_id|event_id|group_id|user(id|vanity)' saved-source.html
```

Field names Facebook updates ke saath change ho sakte hain. Source mein numeric string milna object ownership/access permission nahi deta.

### 1.2 ID report format

```text
Object type: event/page/group
Public URL:
ID field/value:
Access date/time:
Source location/context:
Verification source:
Privacy/scope note:
```

Private groups, hidden events ya login-protected content ko source/endpoint bypass karke access mat karo.

---

## 2. Tool fail ho to manual method

Transcript ka strong doctrine:

> Ethical researcher kisi single tool par dependent nahi hota.

Tool fail reasons:

- Facebook UI/API update,
- login state,
- rate limit,
- old endpoint,
- browser/memory issue,
- result index unavailable.

Fallback:

1. Official/public Facebook UI.
2. Page/event/group URL.
3. View Page Source.
4. Local text copy + `grep`.
5. Manual query/URL construction.
6. Independent source verification.

Manual method “bypass” nahi; public UI/query ko reproducibly understand karna hai.

---

## 3. Facebook search URL anatomy

Transcript Facebook URL ko components mein break karta hai. Simplified example:

```text
https://www.facebook.com/search/top?q=keyword&filter=<encoded-filter>
```

| Component | Meaning |
|---|---|
| Protocol | `https://` |
| Domain | `www.facebook.com` |
| Path/category | `search/top`, `search/posts`, etc. |
| Query | `q=keyword` |
| Filter | `filter=` ke baad encoded configuration |

Possible main categories transcript mein:

- `top`
- `posts`
- `people`
- photos/media
- pages
- places
- groups/events

Platform UI aur URL schema current version mein change ho sakta hai. Old URL ko guaranteed API contract na samjho.

---

## 4. Filter JSON aur Base64 concept

Facebook UI mein applied filters URL ke `filter=` parameter mein encoded form mein aa sakte hain. Conceptually:

```text
UI filter selection
   -> JSON-like filter object
   -> compact JSON
   -> Base64 encoding
   -> filter= URL parameter
```

Educational toy example:

```json
{"category":"posts","sort":"recent"}
```

Actual Facebook schema is simple example se different ho sakta hai.

### 4.1 Decode/encode learning workflow

Authorized test URL par:

1. `filter=` value copy.
2. URL-safe/Base64 form ko decode tool se inspect.
3. JSON structure/keys note.
4. JSON validity maintain.
5. Compact form create.
6. Encode and URL-escape as required.
7. Test only on approved account/scope.

Base64 encryption nahi; encoded data readable/reversible ho sakta hai. Filter modification access-control bypass nahi hona chahiye.

### 4.2 JSON validation

Local safe example:

```bash
python -m json.tool filter.json
```

Compact/valid JSON banane ke liye Python:

```python
import json

obj = {"category": "posts", "sort": "recent"}
print(json.dumps(obj, separators=(",", ":")))
```

Encoding/decoding ke liye standard library use karo; unknown web services par sensitive URLs paste mat karo.

---

## 5. Filter pipeline

Transcript ka single-filter workflow:

```text
1. Facebook UI mein category/filter choose
2. URL se filter value observe
3. Structure ko understand/validate
4. Authorized test value adjust
5. Re-encode and test
6. Result + active facets compare
```

UI ke left-side filters active state dikhate hain. URL manipulation ka learning goal search behavior samajhna hai, private information expose karna nahi.

---

## 6. Filter-combination rules

Transcript Q&A mein three important rules emerge hote hain:

| Rule | Explanation |
|---|---|
| R1 | Same sub-category ke multiple mutually exclusive options ek saath valid nahi ho sakte |
| R2 | Same main category ke different sub-categories se one option each combine ho sakta hai |
| R3 | Different main categories (`search/top` + `search/posts`) ke filters merge karna invalid ho sakta hai |

Example conceptual combination:

```text
main category: posts
sort: recent
post source: pages
post type: photo
```

Different category ka JSON blindly merge karoge to result reset/error/empty ho sakta hai.

### 6.1 Merge mechanics—concept only

JSON objects comma-separated key/value pairs hote hain. Merge karte waqt:

- duplicate keys avoid,
- braces/commas balance,
- JSON validate,
- URL encode,
- authorized test result compare.

Facebook search bar se query dobara type karne par custom URL filters reset ho sakte hain. Screenshot/URL copy karke reproducibility maintain karo.

---

## 7. Private accounts: privacy-risk explanation

Transcript private account ko friend pivot aur social-engineering risk ke through discuss karta hai. Is section ko attack recipe nahi samjho.

A user apna profile private kare, lekin friends:

- public comments,
- tags,
- location posts,
- group/event photos,
- relationship references
se indirectly information expose kar sakte hain.

### Defensive self-test

Apne organization/team ke approved test accounts par check karo:

- profile audience settings,
- tag review,
- friend list visibility,
- third-party app permissions,
- old public comments/photos.

Kisi target ke friend ko befriend/manipulate karke private data nikalna social engineering/unauthorized collection hai. Written red-team ROE ke bina nahi.

---

## 8. Multi-account and username tools

Transcript final section mein multiple public username/photo tools discuss hote hain:

| Tool/category | Broad use | Safety note |
|---|---|---|
| Profil3r-style GitHub CLI | Public username/email/domain presence enumeration | Local lab/public usernames only; inspect code first |
| Reverse-image web apps | Same public profile image across sites | Consent/privacy; private-person tracking avoid |
| `whatsmyname.app` | Username presence across sites | Green/result is lead, not identity proof |
| `namecheckup.com` | Username availability/presence visualization | False positives/negatives; click-through verify |
| Facebook/graph-style tools | IDs/public search queries | Password/token/friend-dump tools avoid |

### 8.1 False positives

Same username common ho sakta hai. Verify with:

- official linked website,
- matching public bio/organization,
- consistent dates and avatar,
- cross-link from verified account.

Reverse-image match too strong proof nahi: reused stock/photo/avatar, repost and cropping common hain.

### 8.2 Credentials and access tokens

Transcript mein old friend-graph/token-based tools ka mention hai. Current safe rule:

- Facebook password kisi third-party tool ko mat do.
- Session cookies/access tokens copy/export mat karo.
- Friend/phone/email dumps create mat karo.
- Mass likes/posts/messages/bot actions execute mat karo.
- OAuth app ko only approved test tenant and minimum scopes do.
- Tool code, dependencies and data handling review karo.

Tool “works” kar raha ho to bhi use lawful/authorized nahi ban jata.

---

## 9. Transcript ke additional lessons

### 9.1 Manual URL skill > tool dependency

Tools convenient wrappers ho sakte hain. URL/query schema samajhne se:

- failure troubleshoot,
- filter logic explain,
- evidence reproduce,
- outdated tool replace
kar sakte ho.

### 9.2 Search result ko evidence grade do

```text
Search result -> candidate
Official/public source -> corroboration
Independent source/date/layout -> confirmation
```

### 9.3 Practice report

Trainer learners ko detailed report/notes aur tool list maintain karne ko kehte hain. Report mein actual sensitive account data redact karo.

---

## 10. Hardware/VM advice from the session

Q&A mein hacking practice laptop ke liye roughly:

- 16 GB RAM preferred,
- i5 minimum/i7 better context,
- 4–6 GB graphics discussion,
- VMs + programming parallel run karne ke liye processing/memory important.

Technical correction:

- Exact requirement tools/VM count par depend.
- GPU bug-bounty/OSINT basics ke liye always necessary nahi.
- SSD, RAM, virtualization support aur thermal performance often more relevant.
- “Pen-drive hacking OS” shortcut secure methodology ka substitute nahi.

---

## 11. Facebook block ka recap

| Day | Main learning |
|---|---|
| Day 9 | Public Meta/company page, public profile, search tricks, UID |
| Day 10 | Page/event/group IDs, source inspection, URL/filter structure, tools |

Social-media roadmap:

- Twitter/X — Days 6–8
- LinkedIn — Day 8
- Facebook — Days 9–10
- Instagram — continuation/poll dependent in transcript
- Email/phone/website intelligence — later roadmap

---

## 12. Common mistakes aur technical corrections

1. Page source ID ko secret/access key samajhna.
2. Base64 ko encryption samajhna.
3. Invalid JSON/duplicate keys ke saath filter URL banana.
4. Different main categories ke filters merge karna.
5. UI update ke baad old URL schema guaranteed samajhna.
6. Private account ke friend pivot ko social-engineering recipe banana.
7. Same username ko same person proof bolna.
8. Reverse-image result ko identity confirmation samajhna.
9. Third-party tool ko password/session cookie/token dena.
10. Graph/friend dumps ya mass bot actions run karna.
11. Public result ki unnecessary personal data copy karna.
12. Tool output ko independent source ke bina publish karna.
13. Filtered result zero aane ko “no posts” conclude karna.
14. VM/hardware advice ko universal requirement samajhna.
15. Bug-bounty/public OSINT learning ko unauthorized real target par apply karna.

---

## 13. Day 10 self-check questions

1. Facebook page/event/group ID ka broad purpose kya hai?
2. Page source se public object ID locate karte waqt safety boundary kya hai?
3. Facebook search URL ke protocol, domain, path, query aur filter parts identify karo.
4. `filter=` parameter ka Base64/JSON relation kya hai?
5. Base64 encryption kyu nahi hai?
6. JSON filter validate/compact kaise karoge?
7. Same sub-category ke filters mutually exclusive kyu ho sakte hain?
8. Different main search categories merge karna problematic kyu?
9. Private account ke indirect public exposure risks kya hain?
10. Username-enumeration tools ke false positives kaise verify karoge?
11. Third-party social tool ko password/token dena risky kyu?
12. Reverse-image username match ko identity proof kyu nahi maana ja sakta?
13. Tool fail hone par manual fallback workflow kya hai?
14. Data minimization ka Facebook OSINT report mein kya role hai?
15. OSINT recon aur unauthorized social engineering mein difference explain karo.

---

## 14. Final takeaway

- Facebook search UI ke peeche categories, sub-categories aur filter structures ho sakte hain.
- IDs query construction mein useful hain, permission bypass nahi.
- Manual URL understanding tool failure ke against resilience deti hai.
- JSON/URL/Base64 technical concepts ko safe owned test data se practice karo.
- Private-account exposure ko privacy lesson samjho, friend manipulation method nahi.
- Username/photo tools leads dete hain; identity confirmation independent source se karo.
- Passwords, session cookies, access tokens aur friend dumps se door raho.
- Social-media OSINT ka professional product reproducible, scoped, privacy-minimized report hai.

Facebook block complete hone ke baad next course stage Instagram/email/phone/website intelligence ki taraf move kar sakta hai, lekin har stage Day 1 ki legal boundary aur Days 6–10 ki correlation discipline par build hoti hai.
