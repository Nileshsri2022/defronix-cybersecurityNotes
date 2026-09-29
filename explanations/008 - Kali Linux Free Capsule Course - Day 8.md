# Day 8 — Kali Linux Capsule Course: `sudo`, Sudoers aur Password Management (Hinglish Explanation)

**Source transcript:** `transcripts/008 - Kali Linux Free Capsule Course - Day 8 [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** Day 7 — users, groups, `su`, `/etc/passwd` aur `/etc/shadow` ka introduction
**Note:** Ye explanation Hindi original transcript ko samajh kar likhi gayi hai; ye line-by-line literal translation nahi hai. Auto-captions mein `sudo`, `sudoers`, `login.defs`, `chage`, `passwd`, `shadow`, `UID_MIN`, `NOPASSWD` aur locking-related options kai jagah garbled mile. Context ke basis par intended commands aur concepts restore karke simple Hinglish mein explain kiya gaya hai.

---

## 1. Day 8 ka focus

Day 7 mein humne dekha tha ki normal user aur root user ke privileges alag hote hain. Day 8 usi problem ko continue karta hai:

1. Agar normal user ke paas root password nahi hai, to admin task kaise kare?
2. `su` aur `sudo` mein kya difference hai?
3. `/etc/sudoers` mein kisi user/group ko limited command access kaise diya jata hai?
4. User password ka hash aur password-ageing data kahan store hota hai?
5. `/etc/shadow` ki fields ka kya meaning hai?
6. Password expiry, warning, inactive grace period aur next-login password change kaise configure hote hain?
7. Kisi account ko lock/disable karne ke safe methods kya hain?
8. Root password bhoolne par recovery possible kyu hoti hai, aur physical access security kyu important hai?

Trainer pehle `sudo`/sudoers ka concept samjhate hain aur phir detailed **password management** par aate hain.

---

## 2. Normal user ko admin task kyu nahi karne milta?

Day 7 ke example ko continue karo:

```bash
useradd sachin
```

Agar ye command normal user run kare aur uske paas required privilege na ho, to permission error mil sakta hai. User create karna system-level change hai, isliye normal account ko by default ye access nahi diya jata.

Pehla obvious solution hota hai:

```bash
su -
```

Lekin `su` ke liye target account, yani root, ka password chahiye hota hai. Real organization mein root password sab employees ke saath share nahi kiya jata.

### 2.1 Root password ko limited kyu rakha jata hai?

Trainer real-industry practice ka example dete hain:

- Root/superuser access sirf limited administrators ko milta hai.
- Root password ko digital vault/password-management tool mein store kiya ja sakta hai.
- Password ko fixed interval, jaise 15, 20 ya 30 days, par rotate kiya ja sakta hai.
- Password retrieve karne ke liye reason aur approval/request required ho sakta hai.
- Security reasons ki wajah se root password casually share nahi kiya jata.

Is design mein normal employee ke paas root password nahi hota, lekin kabhi-kabhi usko ek specific administrative command run karni pad sakti hai. Yahin **`sudo`** ka use aata hai.

---

## 3. `su` aur `sudo` ka core difference

### 3.1 `su`

```bash
su -
```

`su` target user ke account mein switch karne ki koshish karta hai. Isliye aam taur par target user ka password chahiye hota hai — root ke liye root password.

### 3.2 `sudo`

```bash
sudo <command>
```

`sudo` ka main benefit ye hai ki authorized user ko root password dene ki zarurat nahi hoti. Prompt aaye to aam taur par **command run karne wale current user ka apna password** use hota hai.

| Command | Password kis ka? |
|---|---|
| `su` | Target user ka password, jaise root ke liye root password |
| `sudo` | Current/authorised user ka apna password |

Lekin har user automatically sudo nahi kar sakta. Us user ya uske group ke liye `/etc/sudoers` mein appropriate entry honi chahiye.

### 3.3 Sudo user ka meaning

Jis account ko sudoers policy ke through selected commands run karne ki permission milti hai, use informal language mein **sudo user** kaha jata hai. Permission poori root power bhi ho sakti hai, lekin best practice hai ki sirf required command(s) grant kiye jayein.

### 3.4 Sudo ka audit benefit

`sudo` ke through run kiye gaye administrative commands ka audit/logging ho sakta hai. Organization ko pata lag sakta hai ki kis user ne kab privilege elevation use kiya. Ye accountability ke liye useful hai.

---

## 4. Offensive-security perspective: `sudo -l`

Authorized security assessment ya CTF mein agar normal Linux user shell milti hai, to basic questions hote hain:

- Current user kaun hai?
- Is user ke groups kya hain?
- Kya user ko sudo permission hai?
- Agar hai, to exactly kaunse commands run kar sakta hai?

Iske liye command:

```bash
sudo -l
```

`sudo -l` current user ki allowed sudo commands list karta hai. Defensive administration mein bhi ye command useful hai, kyunki isse pata chalta hai ki account ko expected se zyada privilege to nahi mil gaya.

> Day 8 ka point permission audit samajhna hai. Kisi system par privilege escalation ya access testing sirf explicit authorization ke saath karni chahiye.

---

## 5. `/etc/sudoers` file

Sudo policy ka main configuration file hai:

```text
/etc/sudoers
```

Is file mein define hota hai ki:

- kaunsa user ya group,
- kis host se,
- kis user ke roop mein,
- kaunsi command run kar sakta hai.

### 5.1 Basic sudoers format

Conceptual format:

```text
user    host = (runas_user)    commands
```

Root ki common entry ka simplified example:

```text
root    ALL = (ALL:ALL) ALL
```

Iska rough meaning: root user all hosts par all users/groups ke roop mein all commands run kar sakta hai.

### 5.2 Entry ke parts

| Part | Meaning |
|---|---|
| User | Username, ya group ke liye `%groupname` |
| Host | Hostname ya `ALL`; zarurat ho to IP/host scope |
| `(runas)` | Kis identity ke roop mein command chalegi, commonly `root` |
| Commands | `ALL` ya specific commands ke full paths |

Group ko refer karne ke liye naam se pehle percent sign lagta hai:

```text
%devops ALL = (root) /usr/sbin/useradd
```

Yahan `%devops` ka matlab devops group ke members hain, na ki literal username `%devops`.

---

## 6. Limited command ka worked example

Maan lo `defronix` user ko sirf root ke roop mein `/etc/shadow` read karne ke liye `cat` command ki permission deni hai:

```text
defronix ALL = (root) /usr/bin/cat /etc/shadow
```

Iska intended meaning:

- `defronix` user
- all applicable hosts
- root ke roop mein
- sirf `/usr/bin/cat /etc/shadow` command run kar sakta hai

Normal state mein:

```bash
cat /etc/shadow
# Permission denied aa sakta hai
```

Permission milne ke baad:

```bash
sudo /usr/bin/cat /etc/shadow
```

> Exact binary path apne system par `command -v cat` se verify karo. Sudoers mein full path use karna command ambiguity aur unintended binaries ka risk kam karta hai.

### 6.1 Full path kyu?

Sudoers entry mein sirf `cat` likhne ke badle `/usr/bin/cat` jaise full path specify kiya jata hai. Isse policy exact executable par apply hoti hai. Path, arguments aur wildcard behavior ko carefully test karna zaruri hai; galat broad pattern limited permission ko unintended full access bana sakta hai.

### 6.2 `sudo -l` se verification

```bash
sudo -l
```

User ko dikh sakta hai ki allowed command kya hai aur kis identity ke roop mein run ho sakti hai. Policy test karte waqt allowed command ke saath disallowed command bhi test karo, taaki access boundary verify ho.

---

## 7. `/etc/sudoers` edit karne ka safe tareeka — `visudo`

Sudoers file syntax-sensitive hoti hai. Syntax error se sudo access break ho sakta hai, isliye direct editor use karna risky hai.

Recommended tool:

```bash
visudo
```

`visudo` file ko edit karne se pehle/baad syntax validate karta hai. Agar syntax invalid ho, to administrator ko error report mil sakti hai instead of silently saving a broken policy.

```bash
visudo
```

Kuch systems par editor `vi` hota hai; environment ke `EDITOR`/`VISUAL` configuration ke hisaab se editor change ho sakta hai.

> `nano /etc/sudoers` se directly edit karne ke badle `visudo` use karo. Emergency mein bhi backup aur validation ka plan rakho.

---

## 8. `NOPASSWD` aur sudo password cache

Sudoers entry mein `NOPASSWD:` tag use karke listed command ke liye password prompt disable kiya ja sakta hai:

```text
defronix ALL = (root) NOPASSWD: /usr/sbin/useradd, /usr/bin/passwd
```

Iska meaning hai ki `defronix` ko in specific commands ke liye apna password enter nahi karna padega.

Agar `NOPASSWD` nahi hai, to normal sudo password prompt aa sakta hai:

```text
defronix ALL = (root) /usr/sbin/useradd
```

### 8.1 Sudo dobara password kyu nahi poochta?

Trainer batate hain ki sudo authentication success hone ke baad credential ek short time window ke liye memory/cache mein reh sakta hai. Isliye turant next sudo command par prompt repeat na ho.

Ye permanent password storage nahi hai. Timeout ke baad prompt wapas aa sakta hai. Organization apni sudo timestamp policy ke through is behavior ko configure kar sakti hai.

---

## 9. Normal user ko `ALL` dene ka risk

Aisi entry:

```text
someuser ALL = (ALL:ALL) ALL
```

practically user ko root-level capability de sakti hai. Trainer ka logical question hai:

> Agar normal user ko root ki saari commands, saari identities aur saara access de diya, to root aur normal user mein difference kya bacha?

Real organization mein blanket `ALL` dene ke badle least privilege follow karo:

- specific user/group
- specific host scope
- specific run-as identity
- specific command paths
- required arguments only

Sudoers policy security boundary hai, convenience shortcut nahi.

---

## 10. `sudo` group ka shortcut

Day 7 mein groups samjhe the. Debian/Kali-type systems par kisi user ko `sudo` group mein add karna usko broad sudo permission de sakta hai:

```bash
usermod -aG sudo username
```

Exact privileged group distribution ke hisaab se change ho sakta hai, isliye `/etc/sudoers` aur included configuration check karo.

Is shortcut ki wajah se hardening/audit ke waqt sirf `/etc/sudoers` dekhna enough nahi hai. Ye bhi check karo:

```bash
id username
groups username
grep -R "^[^#].*sudo" /etc/sudoers /etc/sudoers.d 2>/dev/null
```

`/etc/sudoers.d` ke included files ko bhi review karna chahiye. Group membership grant karna effectively us group ke policy-defined members ko admin capability de sakta hai.

---

## 11. Class practice: group ko limited sudo permission dena

Trainer ek practical scenario dete hain: maan lo teen ya chaar users ko kuch selected administrative binaries chalani hain. Har user ke liye alag sudoers line likhne ke bajay group use karo.

### Step 1 — Group create karo

```bash
groupadd admin-tools
```

### Step 2 — Users ko secondary group mein add karo

```bash
usermod -aG admin-tools user1
usermod -aG admin-tools user2
usermod -aG admin-tools user3
```

New login/session ke baad membership active dikh sakti hai. Verify:

```bash
groups user1
id user1
```

### Step 3 — Group ko sudoers entry do

```text
%admin-tools ALL = (root) /usr/sbin/useradd, /usr/bin/passwd
```

Isse group members ko sirf listed commands ka root-level access dene ka intent hai.

### Step 4 — Positive aur negative test

Allowed commands test karo:

```bash
sudo /usr/sbin/useradd labuser
sudo /usr/bin/passwd labuser
```

Disallowed command ka test bhi karo, jaise `fdisk` ya koi aur admin command jo policy mein listed nahi hai:

```bash
sudo /sbin/fdisk -l
```

Expected result policy ke hisaab se denial hona chahiye. Exact path aur command availability apne system par verify karo.

> Lab practice ke liye disposable VM use karo. Real system mein user/group/sudoers changes se pehle backup aur rollback plan rakho.

---

## 12. `passwd` command

Apna password change karna:

```bash
passwd
```

Kisi doosre user ka password change karna aam taur par administrative privilege maangta hai:

```bash
sudo passwd username
```

Root/admin directly kisi user ka password reset kar sakta hai:

```bash
passwd username
```

Command new password aur confirmation prompt karegi. Password screen par type karte waqt characters echo na hona normal behavior hai.

### 12.1 Password bhool jao to?

Agar normal user apna password bhool gaya aur uske paas root/sudo authority nahi hai, to wo khud arbitrary reset nahi kar sakta. Organization mein:

1. Admin authority/helpdesk ko request raise karo.
2. Reason aur identity verification provide karo.
3. Authorized administrator reset ya temporary credential issue kare.

Is boundary ka purpose ye hai ki koi bhi user doosre account ka password casually change na kar sake.

---

## 13. `/etc/shadow` — password hashes aur ageing

Login ke time system entered password ko stored credential ke against verify karta hai. Linux systems mein password hash aur password-ageing metadata commonly yahan hota hai:

```text
/etc/shadow
```

```bash
cat /etc/shadow
```

Normal user ko is file ka read access aam taur par nahi diya jata. Root ya specifically authorized privileged process hi ise access kar sakta hai.

> `/etc/shadow` mein normally plaintext passwords nahi hote; password hashes aur related fields hote hain. Phir bhi hash database sensitive credential material hai — ise expose ya copy nahi karna chahiye.

### 13.1 `/etc/shadow` ke eight fields

Colon-separated conceptual example:

```text
defronix:$6$salt$hash:19536:0:99999:7:2:
```

Fields:

| # | Field | Meaning |
|---|---|---|
| 1 | Username | Account name |
| 2 | Password hash | Hashing algorithm marker, salt aur resulting hash |
| 3 | Last change | 1 January 1970 se count kiye gaye days mein last password change |
| 4 | Minimum days | Itne days se pehle password dobara change nahi kar sakte |
| 5 | Maximum days | Itne days ke baad password change required/expire ho sakta hai |
| 6 | Warning days | Expiry se kitne days pehle warning start hogi |
| 7 | Inactive days | Password expiry ke baad grace period |
| 8 | Expiry date | Account expiry ki absolute date, system format mein |

Exact empty values aur special markers ka behavior distribution/documentation par depend kar sakta hai, lekin Day 8 mein trainer in eight logical fields ko explain karte hain.

### 13.2 Field 2: algorithm, salt aur hash

Transcript mein SHA-512 style example dikhaya gaya hai:

```text
$6$salt$hash
```

Conceptually:

- `$6$` — algorithm identifier; traditional Linux convention mein SHA-512 se associated.
- `salt` — random salt, jisse identical passwords ke hashes same na rahen.
- `hash` — password plus salt se derived one-way value.

Modern distributions doosre algorithms, jaise yescrypt, bhi use kar sakti hain. Isliye `$6$` ko har current Linux machine ka universal format na samjho; local system ki configuration aur `crypt(5)` documentation verify karo.

---

## 14. Password ageing ko example se samjho

Trainer ek example dete hain:

- Minimum days = `0`
- Maximum days = `10`
- Warning days = `2`
- Inactive days = `2`

### 14.1 Timeline

| Time | Behavior |
|---|---|
| Day 0 | Password change hua |
| Day 0–10 | Password normal use ho sakta hai; `min=0` se kabhi bhi change allowed |
| Day 8 | Expiry se 2 days pehle warning start |
| Day 10 | Maximum age complete; password change required/expired state |
| Day 10–12 | Inactive grace; old password se login ke baad naya password set karna force ho sakta hai |
| Day 12 ke baad | Grace cross; account/password recovery ke liye admin help chahiye |

### 14.2 Inactive grace period kyu?

Real life mein user password expiry warning dekh kar soch sakta hai, “kal change kar lunga.” Agle din time na mile, machine on na ho, ya koi urgent task aa jaye — aur user bhool jaye.

Inactive period ek limited recovery buffer deta hai:

- old password se login allow ho sakta hai,
- lekin login ke waqt new password set karna force hota hai,
- grace period cross hone par admin intervention required ho sakta hai.

### 14.3 Expired/inactive account recovery

Agar grace period cross ho gaya, to user ko system administrator se contact karna hoga. Admin broadly do methods use kar sakta hai:

1. Password manually reset karna.
2. Last-change/ageing state adjust karna, taaki user valid range mein aakar khud password change kar sake.

Exact recovery command environment aur policy par depend karegi; production system par documented admin procedure follow karo.

---

## 15. `/etc/login.defs` — default password policy

Password ageing data `/etc/shadow` mein per-user stored hota hai, lekin new user accounts ke defaults ek policy file se aa sakte hain:

```bash
cat /etc/login.defs
```

Trainer is file ko new-user defaults aur password policy ke context mein explain karte hain. Common settings:

| Setting | Role |
|---|---|
| `UID_MIN` / `UID_MAX` | Normal user UID range |
| `SYS_UID_MIN` / `SYS_UID_MAX` | System/service account UID range |
| `GID_MIN` / `GID_MAX` | Group ID ranges |
| `ENCRYPT_METHOD` | Password hash method ka default setting, if supported |
| `SHA_CRYPT_MAX_ROUNDS` | SHA-based hashing rounds, if applicable |
| `PASS_MAX_DAYS` | New users ke password maximum age ka default |
| `PASS_MIN_DAYS` | Minimum age ka default |
| `PASS_WARN_AGE` | Warning period ka default |

Transcript demonstration mein `UID_MIN` ko `1000` ke context mein dikhaya gaya hai. Exact value distribution/version ke hisaab se check karo; system account ranges universal nahi hoti.

### 15.1 Future users par policy ka effect

Agar organization chahti hai ki naye accounts ke passwords, example ke liye, 10 days ke baad change hon aur warning period ho, to default policy configure ki ja sakti hai. Isse future account creation ke defaults affect honge.

Important distinction:

- `/etc/login.defs` defaults/future account policy deta hai.
- Existing user ki current ageing values `/etc/shadow` mein already stored ho sakti hain.
- Existing users ko update karne ke liye `chage` ya documented account-management process use karna pad sakta hai.

Production mein `login.defs` edit karne se pehle current values backup aur impact review karo.

---

## 16. `chage` — readable password-ageing management

`/etc/shadow` mein dates days-since-1970 form mein hoti hain, jo manually read karna inconvenient hai. User-friendly listing ke liye:

```bash
chage -l kali
```

Isse last password change, expiry, inactive period, minimum/maximum days aur warning information readable form mein mil sakti hai.

### 16.1 Important `chage` options

| Option | Meaning |
|---|---|
| `-l` | Current ageing information list |
| `-m` | Minimum days between password changes |
| `-M` | Maximum password age |
| `-W` | Warning days before expiry |
| `-I` | Inactive grace days after expiry |
| `-d` | Last password-change date/value set karna |

### 16.2 Full example

```bash
chage -m 0 -M 15 -W 7 -I 2 kali
```

Iska conceptual meaning:

- Password kabhi bhi change ho sakta hai (`-m 0`).
- 15 days ke baad password change required/expire policy (`-M 15`).
- Expiry se 7 days pehle warning (`-W 7`).
- Expiry ke baad 2 days inactive grace (`-I 2`).

Verify:

```bash
chage -l kali
```

Aisi policy ko lab user par test karo, main/root account par casually nahi.

### 16.3 `chage -d 0` — next login par change force karna

```bash
chage -d 0 kali
```

Iska common use case hai temporary password issue karna aur user ko next login par immediately naya password set karne ke liye force karna.

Workflow:

1. Admin temporary password set karta hai.
2. `chage -d 0 username` set karta hai.
3. User next login par password update prompt dekhta hai.
4. New password set hone ke baad normal login continue hota hai.

---

## 17. Password policy ke three important locations

Day 8 ke end mein trainer user/password information ke locations ko connect karte hain:

| File | Main role |
|---|---|
| `/etc/passwd` | Account record: username, UID, GID, comment, home, shell |
| `/etc/shadow` | Password hash aur password ageing fields |
| `/etc/login.defs` | New users/password policy ke defaults |

Group information ka related location:

```text
/etc/group
```

Password ko manually plaintext file mein store nahi karna chahiye. Configuration files ko permissions ke saath protect karna aur least privilege maintain karna zaruri hai.

---

## 18. User account lock/disable karna

Kabhi user ko permanently delete nahi karna hota, lekin login temporarily stop karna hota hai. Is case mein account lock/disable options useful hote hain.

### 18.1 Direct `/etc/shadow` editing — risky method

Trainer demonstration mein password hash ke aage special marker add karke password lock dikhate hain. Example conceptually:

```text
!!$6$salt$hash
```

Ya existing hash ke start mein `!` prefix.

Lekin direct shadow editing risky hai:

- Typo se entry malformed ho sakti hai.
- Wrong delimiter/field change se authentication break ho sakta hai.
- Sensitive file accidentally expose ho sakti hai.

> Manual editing ko learning demonstration samjho. Normal administration mein dedicated commands use karo.

### 18.2 Recommended: `usermod -L` / `usermod -U`

Account password lock:

```bash
usermod -L defronix
```

Unlock:

```bash
usermod -U defronix
```

`-L` aam taur par password hash ke aage lock marker add karta hai. `-U` unlock karne ki koshish karta hai. Command run karne ke baad state verify karo aur apne distro ke `man usermod` ko check karo.

### 18.3 `passwd -l` / `passwd -u`

Password lock/unlock ke liye doosra command family:

```bash
passwd -l defronix
passwd -u defronix
```

Ye password authentication ko lock/unlock karta hai. Account ke doosre login paths, jaise SSH keys, service behavior ya shell restrictions, alag policy ho sakte hain; sirf password lock ko complete account disable samajhna safe nahi hai.

### 18.4 Login shell ko `nologin` karna

Account ke `/etc/passwd` record ke shell field ko restricted shell, jaise `/usr/sbin/nologin` ya distribution ke available path, par set kiya ja sakta hai. Isse interactive login deny ho sakta hai.

Exact path check karo:

```bash
command -v nologin
```

Shell change ko carefully test karo, kyunki service accounts ko valid non-interactive shell ki zarurat ho sakti hai.

### 18.5 Lock ka effect

Password sahi hone ke baad bhi locked account authentication failure dikha sakta hai:

```bash
su - defronix
# Authentication failure ho sakta hai
```

Reason wrong password nahi, account lock/password-authentication policy bhi ho sakti hai.

### 18.6 Lock markers ka rough idea

| Shadow state | General meaning |
|---|---|
| `!!` | Password disabled/never initialized ya manually marked, context-dependent |
| Hash ke start mein `!` | Password authentication locked |
| Normal hash | Password hash active state, other policy checks ke subject to |

Exact semantics distro/PAM implementation ke hisaab se verify karo. Account unlock karne se pehle incident/security reason samjho; blindly unlock mat karo.

---

## 19. Root password bhoolne par recovery

Doubt session mein trainer discuss karte hain ki root password bhoolne par Linux machine ko boot-time recovery ya live media se access kiya ja sakta hai.

Broad possibilities:

- Boot ke time advanced boot selection se recovery environment choose karna.
- Live ISO/image se system filesystem access karke authorized reset process follow karna.

Windows mein live CD/media ka similar concept ho sakta hai, lekin exact steps OS/version par depend karte hain.

### 19.1 Physical access ka security impact

Agar koi attacker machine tak physical access paakar:

1. live image boot kar sake,
2. disk/filesystem access kar sake,
3. root password reset kar sake,

to login password alone sufficient protection nahi rahega.

Isliye real environment mein additional controls use hote hain:

- bootloader par password/protection,
- firmware/UEFI settings protection,
- external media boot restrictions,
- full-disk encryption,
- server-room/physical access controls,
- monitoring aur asset security.

> Authorized recovery aur unauthorized password reset alag cheezein hain. Apni lab/owned machine par documented recovery procedure practice karo; kisi aur machine par physical access ka use bina permission illegal hai.

---

## 20. Day 8 command summary

```bash
# Sudo inspection and safe policy editing
sudo <command>
sudo -l
visudo

# Sudoers format examples
# user    host = (runas)     commands
root      ALL  = (ALL:ALL)   ALL
defronix  ALL  = (root)       /usr/bin/cat /etc/shadow
%devops   ALL  = (root)       NOPASSWD: /usr/sbin/useradd, /usr/bin/passwd

# Group-based sudo access
usermod -aG sudo username
usermod -aG admin-tools username
id username
groups username

# Password changes
passwd
passwd username
sudo passwd username

# Password and policy files
cat /etc/passwd
cat /etc/shadow
cat /etc/login.defs
cat /etc/group

# Readable password ageing information
chage -l username

# Password-ageing policy
chage -m 0 -M 15 -W 7 -I 2 username
chage -d 0 username

# Lock/unlock password authentication
usermod -L username
usermod -U username
passwd -l username
passwd -u username
```

Destructive/privileged commands ko production par directly paste mat karo. Pehle `id`, `sudo -l`, target username, current policy aur rollback plan verify karo.

---

## 21. Common mistakes aur safety points

1. `su` ko use karne ke liye current user password enough samajhna; target password required ho sakta hai.
2. `sudo` ko automatic root access samajhna; sudoers policy required hoti hai.
3. Sudoers file ko direct editor se syntax validation ke bina save karna.
4. `/etc/sudoers` check karke `/etc/sudoers.d` ya privileged group membership ignore karna.
5. Normal user ko `ALL=(ALL:ALL) ALL` de dena.
6. Sudoers mein command ka wrong path likhna.
7. `NOPASSWD` ko broad command wildcard ke saath use karna.
8. `/etc/shadow` ko plaintext-password file samajhna; ye hashes aur ageing data rakhti hai, phir bhi highly sensitive hai.
9. Shadow ke days-since-1970 values ko manually galat interpret karna.
10. `min`, `max`, `warning` aur `inactive` fields ko mix karna.
11. `chage -d 0` ko expiry disable karna samajhna; iska common meaning next login par password change force karna hai.
12. Account lock ko complete access revocation samajhna; SSH keys, services aur other authentication paths bhi review karo.
13. `/etc/shadow` manually edit karke malformed entry bana dena.
14. Root password recovery ke physical-access risk ko ignore karna.
15. Password policy change karne se pehle impact aur existing users par effect check na karna.

---

## 22. Self-check questions

1. Normal user `useradd` kyu nahi chala sakta?
2. `su` aur `sudo` mein password kis account ka use hota hai?
3. Sudo ka audit benefit kya hai?
4. `sudo -l` kya dikhata hai?
5. `/etc/sudoers` entry ke four main parts kaunse hain?
6. Sudoers mein `%groupname` ka meaning kya hai?
7. Command ka full path specify karna kyu useful hai?
8. `visudo` ko direct `nano /etc/sudoers` se safer kyu maana jata hai?
9. `NOPASSWD:` ka effect kya hai?
10. `ALL=(ALL:ALL) ALL` normal user ko dene ka risk kya hai?
11. Sudo permissions audit karte waqt group membership kyu check karni chahiye?
12. `/etc/shadow` mein password plaintext hota hai ya hash?
13. `/etc/shadow` ke eight fields ka order explain karo.
14. `$6$` style hash example mein algorithm, salt aur hash ka role kya hai?
15. Minimum, maximum, warning aur inactive password days mein difference kya hai?
16. `max=10, warn=2, inactive=2` par day 8, day 10 aur day 13 ke aas-paas kya hoga?
17. `/etc/login.defs` aur `/etc/shadow` ka relationship kya hai?
18. `chage -l user` ka practical benefit kya hai?
19. `chage -m 0 -M 15 -W 7 -I 2 user` ko words mein explain karo.
20. `chage -d 0 user` ka common use case kya hai?
21. `usermod -L` aur `usermod -U` kya karte hain?
22. Direct `/etc/shadow` editing risky kyu hai?
23. Password lock aur complete account disable mein kya difference ho sakta hai?
24. Physical access hone par boot/live media recovery ko prevent karne ke liye kaunse controls use honge?

---

## 23. Final takeaway

Day 8 ke core points:

- Root password share kiye bina selected administrative work karne ke liye **`sudo`** use hota hai.
- `sudo` ka access `/etc/sudoers` aur included policy files se control hota hai.
- Sudoers mein least privilege follow karo; broad `ALL` dangerous hai.
- Policy edit karne ke liye `visudo` use karo.
- User/group ko limited binaries dene ke liye specific command paths ya group-based entries use karo.
- `/etc/shadow` password hashes aur password-ageing fields rakhti hai; is file ko protect karo.
- `chage` shadow ke difficult numeric values ko readable banata hai aur ageing parameters manage karta hai.
- `min`, `max`, `warning` aur `inactive` ko samajhna password policy ka base hai.
- Account lock ke liye `usermod -L`/`-U` ya `passwd -l`/`-u` jaise dedicated tools direct file editing se safer hain.
- Physical security, bootloader protection aur full-disk encryption ke bina root-password protection incomplete ho sakti hai.

Trainer next session mein **file security aur file permissions** ki taraf move karte hain. Day 7 ke users/groups aur Day 8 ke sudo/password concepts us agle topic ka base banenge.
