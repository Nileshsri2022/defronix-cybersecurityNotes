# Day 1 — Kali Linux Capsule Course: Linux ki History + Data Storage Planning (Hinglish Explanation)

**Source transcript:** `transcripts/001 - Kali Linux Free Capsule Course - Day 1 [ Hindi ].hi-orig.srt`  
**Note:** Ye explanation current English notes se nahi, balki Hindi original transcript ko samajh kar banaya gaya hai. Auto-caption mein `नक्`/`लिनेक्स` jaise words garbled mile; unka intended meaning **Linux/Kali Linux** liya gaya hai.

---

## 1. Class ka intro aur Day 1 ke 2 main topics

Trainer sabse pehle batate hain ki Kali Linux install ka separate recorded video channel par already available hai. Isliye is class mein installation repeat nahi ki ja rahi; Day 1 ka focus do conceptual topics par hai:

1. **History of Linux** — Linux aaya kahan se, UNIX se uska relation kya hai, aur log isko use kyu karte hain.
2. **Data Storage Planning of Linux** — Linux mein file/folder **kahan create karne chahiye**, kaunsi jagah private hoti hai, kaunsi public hoti hai, aur beginner ko “file banayi par chal nahi rahi / permission nahi mil rahi” jaisi problem kyu aati hai.

Trainer ka point simple hai: kisi bhi cheez ko padhne se pehle uski thodi history pata honi chahiye. Agar background nahi pata, to hum sirf command yaad karte hain, concept nahi samajhte. Dusra point: Linux admin ho ya cyber-security engineer ho, storage planning sabke liye important hai. Agar aap blindly kahin bhi file create karoge, to ya to permission issue aayega, ya system folders mein unnecessary data bharta jayega.

---

## 2. UNIX ki history — Linux samajhne ka base

Transcript mein trainer whiteboard par UNIX se start karte hain:

- **1964:** Bell Laboratories, New Jersey mein ek project start hota hai jiska goal tha **multi-user operating system** banana — matlab ek hi machine par multiple users kaam kar sakein.
- **1969:** Bell Labs us project se withdraw kar leti hai. Isi ke baad do log — **Dennis Ritchie** aur **Ken Thompson** — satisfied nahi hote aur khud kaam continue karte hain.
- In dono ne milkar ek OS banaya jiska naam initially **UNICS** tha. Full form transcript mein di gayi: **Uniplexed Information and Computing Service**. Baad mein ye popularly **UNIX** kehlaya.
- Ye OS **free** tha aur **open source** tha. Open source ka matlab: OS ka source code available hai; koi bhi review kar sakta hai aur apni need ke hisaab se modify kar sakta hai.
- **1975:** **UNIX Version 6 (v6)** release hota hai aur kaafi popular ho jata hai.
- 1975 ke aas-paas se kai companies market mein aati hain aur UNIX ke source ko lekar apne **commercial flavours/versions** banane lagti hain.

Class mein named UNIX flavours: **IBM AIX**, **Sun Solaris**, **Mac OS**, aur **HP-UX**.

Easy matlab: UNIX ek early powerful OS tha jiska design multi-user, permission-based aur source-available tha. Baad mein companies ne usi concept ke paid/commercial versions banaye.

---

## 3. Linux ka birth — UNIX copy nahi, UNIX-like design

Ab trainer Linux ki story par aate hain:

- **1991:** **Linus Torvalds**, ek university student, ko apne project ke liye OS chahiye tha.
- Uss time UNIX kaafi old ho chuka tha aur commercial UNIX versions bahut **expensive** the — hazaron dollars, jo uss time bahut bada amount tha.
- Linus ka thought tha: jab companies UNIX-like OS bana sakti hain, to main kyu nahi bana sakta?
- Important difference trainer zor dete hain: commercial companies ne existing UNIX source ko **modify** kiya tha. Linus ne Linux ka code **scratch se** likha. UNIX ko usne sirf behaviour samajhne ke liye reference ki tarah use kiya, code base ki tarah nahi.
- Linus ke sabse bade study reference mein se ek tha **MINIX** — ek teaching operating system jo **Professor Andrew Tanenbaum** ne apne students ko OS concepts padhane ke liye banaya tha. Linux conceptually MINIX/UNIX ideas se inspired hua, but code original tha.
- Naam **Linux** = **Linus + UNIX** se bana.

Isliye correct line ye hai: **Linux UNIX-derived nahi hai; Linux UNIX-like hai.** Matlab design philosophy aur interface similar feel hota hai, but Linux mein UNIX ka code nahi hai.

---

## 4. GNU aur Free Software Movement

Trainer batate hain ki 1991–1995 ke period mein **Free Software Movement** chal raha tha. Reason: uss era mein zyada tar software paid the, jo developers aur companies dono ke liye blocker tha.

- **GNU project** ne bahut saara software freely release kiya.
- Technically, **Linux akela sirf kernel hai**. Kernel hardware se baat karne wala core part hota hai.
- Ek usable OS banane ke liye kernel ke saath tools chahiye — shell, compilers, utilities, libraries, etc. Isliye pura system aksar **GNU/Linux** kaha jata hai: **GNU tools + Linux kernel**.

Common confusion clear: daily life mein hum “Linux” bolte hain, but technically Linux sirf kernel ka naam hai. Jaise Kali Linux ek complete distribution hai, jisme Linux kernel + GNU tools + security packages + desktop environment sab included hote hain.

---

## 5. Linux ke flavours/distributions

Class mein Linux ke flavours base ke hisaab se bataye gaye:

| Base family | Examples |
|---|---|
| Fedora / Red Hat based | RHEL (Red Hat Enterprise Linux), CentOS |
| Debian based | **Kali Linux**, Parrot OS, Ubuntu |
| Other | Arch Linux, Linux Mint |

Security field mein sabse zyada sunne ko milte hain **Kali Linux** aur **Parrot OS**. Is capsule course mein **Kali Linux** use hoga, kyunki wo pentesters aur security professionals ke beech bahut popular hai.

---

## 6. Operating System actual mein kya hota hai?

Trainer definition dete hain: **OS user aur hardware ke beech ka interface hota hai.**

Agar OS na ho, to chhoti si cheez jaise mouse move karna, file copy-paste karna, ya screen par output dikhana bhi low-level code likhkar manually karwana padta. OS ye complexity hide kar deta hai.

OS ko access karne ke 2 common ways:

| Mode | Full form | Example | Feel |
|---|---|---|---|
| **CLI** | Command Line Interface | Windows ka `cmd`, Linux terminal | Text commands se kaam; fast aur powerful |
| **GUI** | Graphical User Interface | Windows 10/11 desktop, Kali desktop | Click, icons, windows; beginner-friendly |

Windows mostly GUI ke through use hota hai, but Windows mein bhi CMD/PowerShell jaisa CLI hota hai. Linux GUI bhi deta hai, but course deliberately **CLI/terminal** par focus karega kyunki real admin/pentest work mein CLI faster aur controllable hota hai.

---

## 7. Linux ke features — companies Linux kyu use karti hain

Transcript mein features roughly is order mein aaye:

1. **Open source** — Linux ka source code available hai. Yaad rakho: “open source” ka matlab source available hona hai; ye automatically har case mein “free of cost” guarantee nahi karta. Microsoft Windows ka source share nahi karta; Linux mein organisations code review/modify kar sakti hain.
2. **Cost / licensing** — Windows ke liye paid license chahiye. Company mein pirated Windows risky hai kyunki genuine/pirated activation track ho sakta hai aur legal/compliance issue aa sakta hai. Linux generally cost pressure kam karta hai.
3. **Secure** — Linux mein malware impact comparatively kam hota hai. Reason diya gaya: Linux hardening + permission/domain model. Ek service apne required domain/files tak limited rehti hai; root permission ke bina poori machine takeover karna Windows comparison mein zyada difficult hota hai.
4. **Easy to update** — Linux update karna comparatively simple hota hai.
5. **Lightweight** — OS footprint aur RAM usage kam hota hai. Trainer example dete hain: Kali ~1 GB RAM mein acceptable chal sakta hai, jabki Windows 4 GB par bhi sluggish feel ho sakta hai aur practically 8 GB chahta hai.
6. **Android bhi Linux-based hai** — isliye Linux kernel already duniya mein bahut widely deployed hai.

### Terminology map

| Concept | Windows | Linux |
|---|---|---|
| Most powerful account | Administrator | **root** / super user |
| Installable software bundle | Software | **Package** |
| Storage layout | C:, D:, E: drives | Single tree under `/` |

Security advice: real companies mein Linux admins ko normally direct root access nahi diya jata. Wo normal user se kaam karte hain aur zarurat par `sudo` use karte hain. Apni personal machine par har waqt root banke kaam karna bad practice hai — agar attacker session compromise kar le, to use seedha root power mil jati hai. Rule: **root tabhi bano jab zarurat ho; otherwise sudo use karo.** Ye topic later detail mein aayega.

---

## 8. Data Storage Planning — Day 1 ka sabse important concept

Ab trainer main practical confusion address karte hain: log Linux ko frustrating isliye bolte hain kyunki wo file kahin bhi create kar dete hain aur phir bolte hain “run kyu nahi ho rahi” ya “permission denied kyu aa raha”. Root cause zyada tar Linux bug nahi hota; root cause hota hai — **file ko sahi location par na banana.**

### 8.1 Data ke 2 categories

| Category | Dusra naam | Meaning |
|---|---|---|
| **OS-defined data** | Default data | Wo files/folders jo OS khud create karta hai |
| **User-defined data** | Customized data | Wo data jo user baad mein banata hai |

### 8.2 OS-defined data 2 tareeke se banta hai

1. **During OS installation** — OS install hote waqt default directory tree, programs, config files, libraries, logs ke liye structure create ho jata hai.
2. **After OS installation, jab aap koi software/package install karte ho** — package apni program files, support files aur config automatically system locations mein rakh deta hai.

User-defined data wo sab hai jo installation ke baad user banata hai — documents, movies, photos, scripts, test files, etc.

### 8.3 Windows analogy

Windows mein mental model usually aisa hota hai:

- `C:` drive → OS-defined/default data.
- `D:` / `E:` drives → personal/user-defined data.

Linux mein **same idea hai, but drive letters nahi hote.** Linux mein C:, D:, E: ka concept hi nahi hai. Sab kuch ek single tree ke andar hota hai.

---

## 9. Root partition `/` — Linux ka parent folder

Linux ka top-most point hota hai:

```text
/    ← forward slash
```

Transcript mein isko 3 naam se explain kiya gaya:

- **Root partition** — course mein mostly yehi term use hogi.
- **Parent partition**
- **Parent folder**

Important baat: chahe data OS-defined ho ya user-defined, **sab kuch `/` ke neeche create hota hai.** Koi separate C/D/E drive nahi hota.

OS install hone par `/` ke andar roughly **16–19 sub-directories** banti hain. Exact number distribution ke hisaab se thoda upar-neeche ho sakta hai; fixed nahi hai. Har default directory ka role pehle se decided hota hai — kahan config files rakhenge, kahan temporary files, kahan process files, kahan library files, kahan log files. Linux ka pura system in directories ke planning par depend karta hai.

Trainer warn karte hain: ye default planning OS ki hoti hai; aap isme apni marzi se structure disturb nahi kar sakte. Aap baad mein extra directories bana sakte ho, but wo default set ka part nahi banti.

---

## 10. User actual mein kahan kaam karta hai?

Bahut natural doubt aata hai: agar 19 default directories OS ke saath banti hain, to normal user kahan se operate karega?

Trainer explain karte hain:

- Un ~19 directories mein se around **17 directories operating system operate karta hai.**
- Sirf **2 jagah humans/users ke liye hoti hain:**
  - `/root` — **root user ka home directory**
  - `/home` — saare normal users ke home directories rakhta hai (kitne bhi users ho: 1, 5, 10, 15...)

Example: agar system mein normal user `vijay` hai, to uska private area usually `/home/vijay` hoga. Root user ka alag private area `/root` hota hai.

Isolation rule: ek normal user dusre user ke home directory mein ghus kar uska data inspect nahi kar sakta. Analogy: aap apne padosi ke ghar mein ghus kar unka kaam nahi dekh sakte.

---

## 11. Private Place vs Public Place — poora lecture isi par build hota hai

Ye concept transcript ka core hai.

| Term | Kaunsi paths | Kya allowed hai |
|---|---|---|
| **Private place** | Aapka home area: root ke liye `/root`, normal user ke liye `/home/<username>` | By default sab kuch — file create, delete, execute, directory banana; restriction nahi |
| **Public place** | Home directory ke alawa `/` ke andar ki baaki almost sab jagah | Sirf wahi karo jo pehle se defined permissions allow karti hain; permissions ke saath chhedchhad nahi |

Class ki key rule line:

> Har user ko apni **home directory** mein data creation ka default right hota hai.  
> Root user ko by default har jagah file/directory create karne ka right hota hai.

Lekin trainer nuance bhi dete hain: agar aap root ho, to technically aap system ke owner jaise ho; aap kahin bhi change kar sakte ho. Public/private terminology tab bhi important hai kyunki jab attacker ya normal process ki baat aati hai, to permission boundary samajhna zaroori hota hai. Normal user public place mein permissions nahi badal sakta; root chahe to badal sakta hai, isliye root se careless kaam karna risky hai.

### Society/flat analogy

Trainer best example dete hain: ek society mein 50 flats hain. Aapka apna flat aapki **private property** hai — wahan aap owner ho; dance karo, music chalao, files banao, delete karo, jo karna hai karo. Lekin padosi ke flat mein ghus kar same cheez karna trespassing hai. Public areas mein aap ja sakte ho, but wahan owner/society ke rules follow karne padenge, apne nahi.

Linux mein bhi: apne home directory mein aap owner ho; public system directories mein aapko predefined rules/permissions follow karne padte hain.

---

## 12. Machine par demo — Kali Linux overview + architecture

Phir trainer screen par Kali Linux machine dikhate hain. Points:

- Kali Linux pentesters/security professionals dwara use hone wala bahut popular OS hai.
- GUI mode mein **600+ packages/tools** by default installed milte hain — information gathering, vulnerability analysis, web application analysis, database assessment, password attacks, etc. Categories pehle se bani hoti hain.
- GUI available hai, but course mostly **terminal/CLI** se kaam karega kyunki wahi real control deta hai.

Linux architecture simple stack mein samjhaaya:

```text
Users
  ↓ ↑
Shell / Terminal   ← aap yahan command type karte ho
  ↓ ↑
Kernel             ← ye actual "Linux" core hai
  ↓ ↑
Hardware           ← CPU, memory, disk, network, etc.
```

Flow: aap terminal/shell mein command type karte ho → shell command ko kernel tak pahunchata hai → kernel hardware ko instruction deta hai → hardware se result kernel ke paas aata hai → kernel shell ko deta hai → shell aapko screen par output dikhata hai.

Demo mein trainer root partition par ja kar dikhate hain ki `/` ke andar wahi default directories hain jinke baare mein baat ho rahi thi. Wo highlight karte hain:

- `/root` = root user ka private home.
- `/home` = normal users ke home directories ka parent.
- In dono ke alawa screen par dikhne wali baaki files/directories zyada tar **public place** hain, jinki permissions pehle se defined hoti hain.

---

## 13. Final takeaway — Day 1 ke baad aapko kya yaad rakhna hai

1. Linux ki history UNIX se judi hai, but Linux UNIX code se nahi bana; wo UNIX-like design ka scratch implementation hai.
2. Linux technically kernel hai; complete usable OS GNU tools + kernel + packages se banta hai.
3. Kali Linux Debian-based security distribution hai aur is course ka main OS hai.
4. OS user aur hardware ke beech interface hai; CLI terminal command ka fast aur professional tareeqa hai.
5. Linux popular hai kyunki open source, licensing-friendly, secure permission model, easy updates aur lightweight nature deta hai.
6. Sabse important: Linux mein file **kahan** create karte ho, ye decide karta hai ki aap us file ke saath **kya** kar sakte ho.
7. Home directory private hoti hai; baaki system locations public permission-based hoti hain.
8. Root se har waqt kaam mat karo. Normal user + sudo ki habit secure aur industry-standard hai.

Trainer end mein ye bhi bolte hain: file-system hierarchy next classes mein detail se aayegi. Tab har default directory ka exact role clear ho jayega. Day 1 ka goal sirf itna tha ki aap basic storage discipline samajh lo — **kahan kaam karna hai aur kahan nahi.**
