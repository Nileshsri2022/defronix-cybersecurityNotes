# OSINT Day 9 — Facebook/Meta OSINT: Company, Public Profiles aur User IDs (Hinglish Explanation)

**Source transcript:** `transcripts/024 - Day-9 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** Days 6–8 — Twitter/X, LinkedIn, manual correlation aur technical search
**Continues:** Day 10 mein Facebook URL manipulation, remaining IDs aur tools
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likhi gayi hai. Mark Zuckerberg/Meta examples public-profile demonstration hain, permission to investigate private individuals nahi. Login, browser tools, IDs aur plugins sirf authorized/public scope mein use karo; credentials/tokens collect ya misuse mat karo.

---

## 1. Facebook OSINT kyu different hai?

Trainer Facebook ko long-term social-life archive ke roop mein explain karte hain. Users years tak:

- likes,
- comments,
- tags,
- friendships,
- photos/videos,
- feelings/interests,
- life events,
- locations aur profile details
share kar sakte hain.

Twitter/X par short public conversations mil sakti hain; Facebook profile/timeline mein longer social context aur old footprint ho sakta hai. “Forgotten” posts search/index mein visible reh sakte hain.

### 1.1 Setup rules

- Desktop browser se research easier ho sakti hai.
- Platform ke current terms/privacy controls follow karo.
- Authorized assessment ke liye approved research account use karo.
- Personal account se accidental like/comment/friend request avoid.
- Google Docs/notes mein source URL aur timestamp record karo.

Logged-out view limited ho sakta hai, but login karna authorization nahi banata. Private/profile access controls bypass nahi karne.

---

## 2. Traditional method: company page

Transcript mein **Meta** company page demonstration hai. Manual checklist:

| Surface | Kya note karna hai |
|---|---|
| About/search | Official site, founders, public history |
| Pages | Business, Engineering, Media, Social Impact, Developers, Education jaise related pages |
| Main page | Tagline, website, followers, photos, public reactions/comments |
| Page Transparency | Page ID, creation date, admin-country summary if publicly shown |

Transcript Meta page ke liye February 2004/Cambridge origin context aur multiple pages discuss karta hai. Historical company facts current official sources se verify karo.

### 2.1 Page Transparency

Page Transparency public admin-country summary jaise signals de sakti hai. Ye individual admin names/passwords nahi deti; location count ko office location ya person identity proof mat samjho.

Defensive use:

- official vs impersonator page compare,
- page age/renames review,
- suspicious admin-country mismatch note,
- platform report route use.

---

## 3. Traditional method: public individual profile

Transcript Mark Zuckerberg public profile ko demo ke liye inspect karta hai. Public fields potentially include:

- founder/role,
- education,
- public residence/from fields,
- relationships,
- languages,
- photos/cover photos,
- friends/followers if visible,
- videos/reels,
- life events,
- public contact/basic info.

Transcript mein May 14, 1984 birthday, English/Mandarin aur public profile timeline details discuss hoti hain. Ye details report mein repeat karna zaruri nahi; current profile/source date ke bina old content stale ho sakta hai.

### 3.1 Photos aur reactions

Profile/cover photo open karne par public reactions, comments aur posting date visible ho sakte hain. Check:

- image event/date,
- comments ka source/context,
- public tags,
- repeated location/organization.

Reaction list ko friend/endorsement proof mat samjho. Public interaction only a lead hai.

### 3.2 In-profile search

Agar profile ke andar search available ho:

```text
profile search: meta
```

Isse general Facebook result ke badle that profile ke public content mein keyword locate karne ka intent hai. Platform UI availability badal sakti hai.

### 3.3 Video speech

Trainer spontaneous videos ko scripted posts se different information source batate hain. Defensive review mein video se accidental office screen, location, schedule, personal detail leak identify karo. Audio/video download/share se pehle privacy/copyright check karo.

---

## 4. Account age estimate

Facebook account creation ka exact public date hamesha available nahi. Transcript do indirect methods discuss karta hai:

1. **Life Events:** earliest visible update se approximate lower bound.
2. **Marketplace:** public listing par “joined Facebook in…” type signal mil sakta hai.

Technical correction:

- Earliest visible post ≠ account creation date.
- Old content delete/private ho sakta hai.
- Marketplace UI/availability location/account par vary.
- Estimate ko confidence/limitation ke saath report karo.

---

## 5. Facebook search tricks

### 5.1 Wildcard/name patterns

Conceptually:

```text
Mark *
* Zuckerberg
```

Same-name profiles/family-name candidates surface ho sakte hain, but relationship proof nahi. Current Facebook search wildcard behavior change ho sakta hai; UI result ko manually verify karo.

### 5.2 Related-search suggestions

Facebook ke related queries search shape expand kar sakte hain. Every suggestion useful nahi; irrelevant/public-person collision possible. Search log mein query and result source note karo.

### 5.3 Media keywords

```text
name photos
name pictures
name videos
```

Different keywords different result sets de sakte hain. Reposted images ko independent source na samjho.

### 5.4 `AND` / `OR`

```text
name AND keyword
name OR keyword
```

Transcript “AND” ko both ways—full/short spelling—try karne ki baat karta hai, kyunki platform parser output vary kar sakta hai. Query results ka textual overlap relationship/proof nahi.

### 5.5 Location combinations

```text
name Palo Alto
company location
```

Location keyword post/profile context narrow kar sakta hai. It does not prove current residence or real-time presence.

### 5.6 Tags/comments/likes

- Tags: friends/family/event context ka clue.
- Comments: acquaintances/interests/participants ka clue.
- Likes: content exposure, not necessarily agreement.

Transcript ke “hacker mindset” ko defensive lens se apply karo: organization ko public relationship/oversharing risk dikhana, people ko manipulate nahi.

---

## 6. User name vs numeric User ID

Facebook technical tools often two artifacts maangte hain:

1. **Username/vanity URL** — profile URL ka readable part.
2. **UID/user ID** — numeric identifier.

### 6.1 `profile.php?id=`

Agar URL:

```text
https://www.facebook.com/profile.php?id=123456789
```

ho, to `id` value numeric UID ho sakti hai. Iska matlab username set nahi bhi ho sakta hai.

### 6.2 Page source method

Public/authorized profile par:

```text
Right click -> View Page Source -> Ctrl+F -> userVanity / userID
```

Page source field names platform changes ke saath vary kar sakte hain. Browser DevTools/source ko only publicly accessible, authorized page par inspect karo; private API/internal endpoint access attempt mat karo.

### 6.3 `lookup-id.com`

Transcript third-party lookup service ka demo karta hai:

```text
profile URL -> numeric ID
```

External service ko profile URLs/data bhejne se pehle privacy policy, terms, rate limits aur legal basis check karo. Tool fail/flaky ho sakta hai; manual public-source verification preferred.

---

## 7. Tool suite ka correct interpretation

Trainer ka important clarification: many “Facebook OSINT tools” khud Facebook database crawl nahi karte. Ye generally:

- query assemble,
- filters/IDs add,
- Facebook search URL open
karte hain.

Login required ho sakta hai. Login-gated result ko public evidence mat bolo.

Transcript tools/categories:

| Tool/category | Intended function |
|---|---|
| `lookup-id.com` | Profile URL se UID lookup |
| OSINTCombine Facebook tools | Date/month/interval, location ID, posts-by-UID style queries |
| `intelx.io` | Advanced post search interface; Facebook login may be required |
| Graph-scanner-style builder | Keyword + UID + location + date clauses |
| Tabbed filter tools | Posts, people, photos, pages, places, videos, events |
| Related-search workflow | Redirect ke baad Facebook suggestions continue karna |

Current platform/API changes se old tools break ho sakte hain. Result reproduce nahi ho to tool bug, login state, index restriction ya platform change document karo.

### 7.1 Credentials/tokens safety

Kisi tool ko Facebook password, session cookie, access token ya private friend data dena high-risk hai. Only approved test tenant/research account, official OAuth flow aur written authorization use karo. Token dump, friend-graph extraction, mass actions ya bot activity execute mat karo.

---

## 8. Other IDs: location, group, event, page

Day 9 ka closing point hai ki user ID ke alawa Facebook objects ke IDs bhi useful ho sakte hain:

- page ID,
- location ID,
- group ID,
- event ID.

In IDs ko public page source/official URL context se identify karna next session mein continue hota hai. Object ID milna access permission nahi deta.

---

## 9. Defensive Facebook exposure report

```markdown
Object: official page / public profile / public post
URL and access timestamp:
Observed public field:
Source type: About / post / photo / transparency / search
Freshness:
Verification source:
Privacy impact:
Recommended action:
```

Recommended remediation:

- unnecessary public birthdays/addresses hide,
- business/personal contact separate,
- old posts/audience review,
- tag review enabled,
- MFA and login alerts,
- page admin least privilege,
- official impersonation monitoring,
- public employee/family information minimize.

---

## 10. Common mistakes aur safety points

1. Public page ko official verify kiye bina trust karna.
2. Page Transparency admin-country ko individual location proof samajhna.
3. Earliest life event ko exact account-creation date bolna.
4. Like/tag/comment ko friendship or employment proof banana.
5. Display username aur numeric UID confuse karna.
6. Page source se ID milne ko permission samajhna.
7. Old third-party tool ko current platform par guaranteed samajhna.
8. Login-gated result ko public evidence report karna.
9. Password, session cookie ya access token share karna.
10. Private profile/friend list bypass karna.
11. Mark Zuckerberg demo ko private-person investigation model banana.
12. Unnecessary personal data notes/report mein copy karna.
13. Reposted photo ko independent corroboration samajhna.
14. Current role/location without date verify karna.
15. Facebook OSINT ko phishing/social engineering mein convert karna.

---

## 11. Day 9 self-check questions

1. Facebook OSINT Twitter/X se different kyu ho sakta hai?
2. Meta company page ke kaunse surfaces manually review karoge?
3. Page Transparency ka defensive use kya hai?
4. Public profile data ko current fact samajhne se pehle kya checks karoge?
5. Life Events aur Marketplace se account-age estimate ki limitations kya hain?
6. Tags, comments aur likes ko evidence strength ke hisaab se kaise interpret karoge?
7. Username/vanity URL aur UID mein difference kya hai?
8. `profile.php?id=` URL se kya clue mil sakta hai?
9. Page source mein UID/vanity field search karte waqt ethical boundary kya hai?
10. Third-party Facebook tools generally kya karte hain?
11. Login-required result ko public evidence kyu nahi bolna chahiye?
12. Location ID, page ID, group ID aur event ID ka role kya hai?
13. Password/token/session cookie tool ko dena risky kyu hai?
14. Defensive Facebook exposure report mein kaunsi privacy remediation likhoge?
15. Public OSINT aur unauthorized private-profile access ka difference explain karo.

---

## 12. Continuity

Days 6–8 ne social-media OSINT ke manual/technical foundations aur LinkedIn cover kiya. Aaj Facebook page/profile/UID fundamentals complete hue. Day 10 mein page/event/group IDs, manual Facebook URL construction, filter encoding aur additional tools discuss honge — with the same rule: public/authorized scope only.
