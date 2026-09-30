# OSINT Day 11 — Applied Investigation Lab: Metadata, Username Pivots, GPG aur Blockchain (Hinglish Explanation)

**Source transcript:** `transcripts/026 - Day-11 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** OSINT Days 1–10 — image analysis, usernames, Twitter/X, Facebook/LinkedIn aur correlation
**Continues:** Day 12 mein lab ke remaining tasks, BSSID/geolocation aur airport clues
**Lab context:** Transcript ek beginner/intermediate TryHackMe-style public training room ko live solve karta hai.
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai; ye literal translation nahi hai. Lab artifacts ko isolated practice room ke bahar access, credential use, cryptocurrency transfer ya dark-web searching ke liye apply mat karo.

---

## 1. Theory se practical chain tak

Learners ne repeatedly practical tasks maange the. Aaj ek staged OSINT room solve hota hai jisme har question previous finding par depend karta hai.

```text
Image artifact
  -> metadata/export path
  -> username
  -> public social accounts
  -> identity/email clues
  -> GitHub/GPG metadata
  -> audit history
  -> blockchain explorer
  -> image/geolocation clues
```

Room text hints deta hai aur next question unlock karne ke liye answer submit karna hota hai. Ye safe practice target hai; real attack victim nahi.

---

## 2. Stage A — Image forensics se username

### 2.1 Lab clue

Forensic analysis mein major damage nahi mila, lekin compromised system par criminal ka छोड़ा hua image artifact mila. Hint ka meaning hai ki information **surface ke neeche** ho sakti hai.

Image ko visually dekhna enough nahi. File metadata inspect karo:

```bash
exiftool image.png
```

Possible fields:

- file type/size,
- image dimensions,
- software/exporter,
- timestamps,
- comments,
- original/export path.

Transcript mein export path home directory tak preserve hota hai, jaise:

```text
/home/<username>/Desktop/...
```

Home-directory segment username ka lead deta hai. Lab transcript mein username ka ending “Angel” jaisa clue sunai deta hai; exact answer lab ke supplied artifact/source se verify karo.

### 2.2 Technical correction

- Metadata present hona file author prove nahi karta.
- Path old machine/user/exporter ka ho sakta hai.
- Metadata edit/remove/fake ki ja sakti hai.
- Same username many people use kar sakte hain.

Report mein “metadata says” aur “independently confirmed” alag fields rakho.

---

## 3. Stage B — Username pivot aur OPSEC mistakes

Lab username ko public web search se pivot karta hai:

```text
"candidate username"
site:x.com "candidate username"
site:instagram.com "candidate username"
```

Transcript mein same/related username se Twitter/X account, article byline aur Instagram page milne ka example hai.

### 3.1 Do OPSEC mistakes

1. Image/file metadata scrub na karna.
2. Same unique username multiple platforms par reuse karna.

Unique handle cross-platform correlation ko easy banata hai. Job/community sites kabhi full name/location jaise voluntarily public fields show kar sakti hain.

### 3.2 Defensive self-audit

Apne authorized accounts ke liye:

- uploaded images ka EXIF review,
- unique username reuse inventory,
- old bios/posts cleanup,
- separate work/personal handles,
- privacy/audience settings,
- image upload pipeline metadata stripping
check karo.

Kisi real person ke cross-platform account ko harass/track karne ke liye pivot mat use karo.

---

## 4. Stage B — Twitter/X timeline analysis

Lab account ke public footprint mein followers/following, posts, travel/season clues, public Wi-Fi/password boast aur another handle mention jaise leads discuss hote hain.

Safe analysis framework:

| Signal | What it can support | What it cannot prove |
|---|---|---|
| Public follower count | Account reach/context | Identity/authenticity |
| One following relationship | Public connection lead | Friendship/role |
| Travel/cherry-blossom post | Season/location hypothesis | Current location |
| Second @handle | Cross-platform lead | Same person without verification |
| Password boast | Credential-exposure risk | Permission to retrieve/use password |

Lab question may ask real name/email. Answer supplied room data and reputable public source se verify karo; leaked credentials ko copy/use/share mat karo.

### 4.1 Search workflow

```text
1. Original account URL/hash/timestamp note
2. Every relevant public post read
3. Day 6–8 operators use: from:, date, hashtag, language
4. Images reverse-search
5. Contradictions and deleted/edited references note
6. Identity claim only after independent source
```

---

## 5. Stage C — GitHub se GPG key aur email clue

Username pivot se lab GitHub repository tak pahunchta hai. Transcript mein hello-world code, suspicious-looking worker/password file, PGP/GPG repo aur Bitcoin-related artifact discuss hote hain.

### 5.1 Public key import

Owned lab key/file par:

```bash
gpg --import public.key
gpg --list-keys
gpg --fingerprint
```

GPG import output/public key UID mein email identity metadata embedded ho sakti hai. Lab question full email pooch sakta hai.

### 5.2 Important security boundary

- Public GPG key import safe cryptographic inspection hai.
- Private key, password file ya credential ko use/decrypt/login ke liye try mat karo.
- GitHub repository public hone ka matlab every secret legitimate use ke liye available nahi.
- Repository owner ko secret exposure responsibly report karo.
- Email address report mein redact/minimize karo unless challenge explicitly requires answer.

### 5.3 Public key vs private key

| Artifact | Share? | Role |
|---|---|---|
| Public key | Public distribution possible | Encryption/signature verification |
| Private key | Never share | Secret signing/decryption |
| Key UID/comment | Metadata lead | Identity hint, not proof |

---

## 6. Stage D — GitHub history aur deleted data

Lab storyline mein attacker ko pata chalta hai ki investigation ho rahi hai aur files/posts scrub kiye gaye. Transcript revision/audit history ko important OSINT source batata hai.

Defensive Git workflow:

```bash
git log --oneline --all
 git show <commit>
 git log --stat --all
```

Public repository mein old commit/file history still visible ho sakti hai. Lekin deleted secret ko recover karke use karna authorized nahi. Correct security action:

1. Secret exposure confirm minimally.
2. Do not authenticate with it.
3. URL/commit hash/time note.
4. Owner/platform security route report.
5. Owner rotate/revoke secret.

Git history mein unrelated private data ho sakta hai; bulk clone/archive avoid karo if not needed.

---

## 7. Blockchain artifact aur block explorer

Lab ke remaining questions wallet address aur specific date—23 January 2021—par mining pool/payment trace se related hain. Trainer block explorer se transaction flow inspect karte hain.

### 7.1 Generic workflow

1. Authorized lab-provided public wallet/transaction identifier lo.
2. Correct chain explorer select karo.
3. Address/transaction hash search.
4. From/to, timestamp, amount, token/asset note.
5. Related transaction graph cautiously follow.
6. Independent explorer/source se confirm.

```text
wallet/address -> transaction hash -> from/to -> timestamp/value -> related public entity
```

One explorer identifier reject kar sakta hai; another chain-specific explorer resolve kar sakta hai. Error ko success samajhkar random chain par search mat karo.

### 7.2 Technical and legal limits

- Wallet address person identity automatically prove nahi karta.
- Exchange/mining-pool label heuristic ho sakta hai.
- Transaction timestamp timezone/confirmation context ke saath read karo.
- Cryptocurrency transaction trace ko fund transfer, seizure ya attribution authority mat samjho.
- Real wallet/credential/seed phrase ko access/transfer mat karo.

---

## 8. Homework: attacker geolocation

Trainer learners ko remaining crypto answers ke saath full Twitter/X OSINT aur attacker geolocation assignment dete hain.

Method:

- cherry-blossom/travel photos observe,
- reverse image search,
- Day 3 foreground/background/map method,
- Day 6–8 `hashtag`, date, language, geocode concepts,
- map/satellite/airport evidence,
- report with confidence and limitations.

A single seasonal post se current home location assume mat karo. Time/date, source freshness aur alternative places compare karo.

---

## 9. Technique-to-syllabus mapping

| Lab step | Technique |
|---|---|
| Image → export path | EXIF/metadata, `exiftool` |
| Username → public accounts | Search and cross-platform pivot |
| Timeline analysis | Twitter/X manual + advanced search |
| Public key → email hint | `gpg --import`, key UID metadata |
| Edited/deleted content | Git commit/revision history |
| Wallet/mining pool trace | Blockchain explorer |
| Cherry-blossom photo → place | Reverse image + geolocation |

Ye lab demonstrate karta hai ki OSINT independent tricks ka list nahi, linked evidence chain hai.

---

## 10. Common mistakes aur safety points

1. Image pixels dekhkar metadata check na karna.
2. Export path username ko confirmed real identity samajhna.
3. Same username ko same human proof bolna.
4. Leaked Wi-Fi/password text ko use/test karna.
5. GitHub password/worker file ko login credential samajhna.
6. Private GPG key ya seed phrase search/import karna.
7. Deleted GitHub secret recover karke authenticate karna.
8. Blockchain wallet ko person identity proof samajhna.
9. One explorer result ko final attribution bolna.
10. Public lab target ke bahar same workflow run karna.
11. Travel photo se real-time/current home location publish karna.
12. Source URLs, timestamps aur uncertainty document na karna.

---

## 11. Day 11 self-check questions

1. Image metadata mein export path OSINT clue kaise ban sakta hai?
2. `exiftool` se kaunse fields inspect karoge?
3. Metadata clue ko independent source se verify kyu karna chahiye?
4. Username reuse cross-platform risk kya hai?
5. Lab Twitter timeline se travel/season clue ko location proof kyu nahi maana ja sakta?
6. Public GPG key aur private key mein difference kya hai?
7. `gpg --import public.key` ka output kya hint de sakta hai?
8. Git revision history security investigation mein useful kyu hai?
9. Exposed GitHub secret milne par responsible action kya hoga?
10. Blockchain explorer mein from/to/timestamp/value kaise read karoge?
11. Wallet address aur person identity ke beech attribution limitation kya hai?
12. Image geolocation homework mein confidence/alternative candidates kyu include karoge?
13. Applied lab mein previous Days 3–10 techniques kaise chain hoti hain?
14. Leaked credentials ko access kiye bina finding kaise report karoge?

---

## 12. Continuity

Day 11 ne image metadata se start karke username, social accounts, GPG identity clue, Git history, blockchain aur geolocation ko ek investigation chain mein joda. Day 12 mein lab ke password-cache/BSSID aur airport tasks continue honge; Instagram OSINT bhi roadmap mein enter hoga.
