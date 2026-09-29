# Day 9 — Kali Linux Capsule Course: File Security, Permissions aur `umask` (Hinglish Explanation)

**Source transcript:** `transcripts/009 - Kali Linux Free Capsule Course - Day 9 [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** Day 7–8 — users, groups, `sudo`, password management aur privileges
**Note:** Ye explanation Hindi original transcript ko samajh kar likhi gayi hai; ye line-by-line literal translation nahi hai. Auto-captions mein `inode`, `file type`, `permission`, `chown`, `chgrp`, `chmod`, `umask`, `mkdir -m` aur octal values kai jagah garbled mile. Context ke basis par intended Linux concepts aur commands restore karke simple Hinglish mein explain kiya gaya hai.

---

## 1. Day 9 ka focus

Day 7 mein users/groups aur Day 8 mein sudo/password management samjha gaya. Ab next layer hai **file security** — kaun file ko read, modify ya execute kar sakta hai?

Trainer file security ko do broad parts mein divide karte hain:

1. **Basic file permissions** — Day 9 ka main topic.
2. **Advanced file permissions** — next class mein special permissions aur advanced security discuss honge.

Aaj ke major topics:

- Virtual machine snapshots
- `ls -l` ka output read karna
- Inode number aur file type
- Owner, group aur others
- File vs directory permissions
- `chown`, `chgrp` aur `chmod`
- Numeric aur symbolic permissions
- `umask`
- New file/directory ki effective permissions
- `mkdir -m`
- Group members ke liye file ko read/modify karne ka practice task

---

## 2. Virtual machine snapshot — practical safety habit

Class ke start mein trainer ek practical habit remind karte hain: Kali ya kisi bhi Linux lab VM mein successful configuration ke baad snapshot lo.

### 2.1 Suggested workflow

1. Kali VM install karo.
2. Clean, working installation ka snapshot lo.
3. Tool install ya configuration change karo.
4. Tool ko test karo — kya machine aur tool dono properly work kar rahe hain?
5. Working state ka naya snapshot lo.
6. Purana unnecessary snapshot cleanup karo, agar storage policy allow kare.

VirtualBox mein generally VM select karke **Snapshots** section se current machine state save ki ja sakti hai. Exact UI version ke hisaab se change ho sakta hai.

### 2.2 Snapshot kyu useful hai?

Security tools aur internet se downloaded scripts/configurations ke saath risk ho sakta hai:

- Tool mein malware ya unwanted behavior ho sakta hai.
- YouTube/Google se follow ki gayi configuration se system settings break ho sakti hain.
- Kisi command se network, package, shell ya permission configuration change ho sakti hai.
- Problem ka exact cause baad mein yaad na rahe.

Snapshot hone par VM ko known-good state par revert karna easy hota hai. Isse:

- pura OS dobara install karne ka time bachta hai,
- tools ko baar-baar download karne ki zarurat nahi padti,
- experiments isolated rehte hain,
- learning lab recoverable rehti hai.

> Snapshot backup ka complete replacement nahi hai. Important notes/data ka separate backup rakho, kyunki snapshot files corrupt ho sakti hain ya disk space consume kar sakti hain.

---

## 3. File security ki zarurat

Agar Linux machine mein file security na ho, to koi bhi process ya user kisi bhi file ko modify/delete/read/run kar sakta hai. File permissions ka purpose ye decide karna hai ki:

- owner kya kar sakta hai,
- group members kya kar sakte hain,
- baaki users, yani others, kya kar sakte hain.

File security ka simple goal:

> **Required user ko required access do, aur baaki sabka unnecessary access restrict karo.**

Isse accidental changes aur malicious activity dono ka impact reduce hota hai. Permissions perfect protection nahi hain — root, vulnerable services aur advanced controls alag topics hain — lekin Linux access-control ka basic layer yahi hai.

---

## 4. `ls -l` output ko read karna

```bash
ls -l
```

Conceptual output:

```text
-rw-r--r-- 1 root root 4096 Sep 28 15:58 file.txt
```

Is line mein multiple pieces of information hoti hain:

```text
-rw-r--r--  1  root  root  4096  Sep 28 15:58  file.txt
    |        |   |     |      |          |            |
    |        |   |     |      |          |            +-- name
    |        |   |     |      |          +-- modification time
    |        |   |     |      +-- size
    |        |   |     +-- group owner
    |        |   +-- user/owner
    |        +-- hard-link count
    +-- file type + permissions
```

### 4.1 File owner aur group owner

Example mein:

- `root` pehla owner field hai.
- Doosra `root` group owner hai.

Permissions ke decision mein Linux pehle check karta hai ki current process file ka owner hai ya group member. Jo category match hoti hai, us category ki permissions apply hoti hain.

### 4.2 Link count

`ls -l` ka numeric field hard links ki count show karta hai. Regular file aur directory ke liye is number ka meaning different details rakhta hai; Day 9 ka main focus permissions hai, lekin field ko ignore nahi karna chahiye.

### 4.3 Size aur timestamp

- File size bytes mein dikh sakta hai.
- Timestamp last modification time ko represent karta hai.
- Directory ke case mein displayed size uske directory-entry structure ka size ho sakta hai, andar ke total files ka sum nahi.

---

## 5. Inode number aur inode table

Har file aur directory ke saath filesystem ek **inode** maintain karta hai. Inode file ki metadata aur data blocks ke references se related hota hai.

Inode ke through filesystem ko file ke baare mein information mil sakti hai, jaise:

- ownership
- permissions
- timestamps
- size
- link information
- data blocks kahan stored hain

Inode number dekhne ke liye:

```bash
ls -i
```

Example:

```text
1234567 -rw-r--r-- 1 kali kali 42 file.txt
```

### 5.1 Inode table limited hoti hai

Filesystem create karte waqt inode availability/structure define hoti hai. Isliye disk par free space hone ke baad bhi agar inodes exhaust ho jayein, to naye files create karne mein problem aa sakti hai.

Inode count disk capacity aur filesystem configuration se related hota hai; ye hamesha simple “disk double = inode double” rule nahi hota. Day 4 ke inode table/file-description discussion se iska connection hai.

### 5.2 Inode aur filename

Filename directory entry mein inode se associate hota hai. Isi wajah se hard links same inode ko refer kar sakte hain. Day 9 mein hard-link internals detail mein nahi ja rahe; abhi important point hai ki file identity sirf displayed filename nahi hoti.

---

## 6. First character: file type

`ls -l` output ka first character file type batata hai:

| Character | Meaning |
|---|---|
| `-` | Regular file |
| `d` | Directory |
| `l` | Symbolic link |
| `b` | Block device file, jaise disk/device interface |
| `c` | Character device file |
| `s` | Socket |

Example:

```text
-rw-r--r--  regular file
 drwxr-xr-x  directory
 lrwxrwxrwx  symbolic link
```

Actual output mein directory ke first character ke baad permissions start hoti hain; table ko samajhne ke liye spaces sirf visual alignment hain.

---

## 7. Permission string: owner, group aur others

File type ke baad next **nine characters** permissions hoti hain:

```text
-rw-r--r--
 ||| ||| |||
 u   g   o
```

- Pehli 3 positions: **user/owner**
- Agli 3 positions: **group**
- Last 3 positions: **others**

Example `rw-r--r--` ko break karo:

| Subject | Permission | Meaning |
|---|---|---|
| Owner | `rw-` | read + write |
| Group | `r--` | read only |
| Others | `r--` | read only |

Agar position par `-` ho, to woh permission present nahi hai.

---

## 8. `r`, `w`, `x` ka meaning

### 8.1 Regular file par

| Letter | Value | File par meaning |
|---|---:|---|
| `r` | 4 | Contents read karna |
| `w` | 2 | Contents modify karna |
| `x` | 1 | Program/script ke roop mein execute karna |

Example:

```text
r--   file read-only
rw-   file read + modify
r-x   file read + execute, modify nahi
```

`x` ka matlab har file ko “run” karna nahi hota; script ko execute karne ke liye valid interpreter/shebang aur required access bhi matter karte hain.

### 8.2 Directory par

Directory permissions ka meaning file se different hai:

| Letter | Directory par meaning |
|---|---|
| `r` | Directory entries ke names list karna, jaise `ls` |
| `w` | Entries create/delete/rename karna, usually `x` ke saath meaningful |
| `x` | Directory traverse/search karna; `cd` aur known path access ke liye required |

### 8.3 Directory ka `x` sabse important confusion

Directory par execute ka meaning “directory ko program ki tarah run karna” nahi hai. Ye **traverse/search permission** hai.

```bash
cd directory
```

ke liye directory par `x` permission chahiye. Sirf `r` hone se names list ho sakte hain, lekin directory ke andar enter/access karna fail ho sakta hai.

Directory par `w` ke saath `x` ho to user entries create/delete/rename kar sakta hai. Isliye kisi directory ko writable dene se pehle uske delete/rename impact ko samjho.

---

## 9. Octal permission values

Linux permissions ko numeric/octal form mein likha ja sakta hai:

| Number | Binary | Permission |
|---:|---|---|
| 0 | `000` | `---` |
| 1 | `001` | `--x` |
| 2 | `010` | `-w-` |
| 3 | `011` | `-wx` |
| 4 | `100` | `r--` |
| 5 | `101` | `r-x` |
| 6 | `110` | `rw-` |
| 7 | `111` | `rwx` |

Calculation:

- `r = 4`
- `w = 2`
- `x = 1`

Isliye:

```text
rwx = 4 + 2 + 1 = 7
rw- = 4 + 2     = 6
r-x = 4     + 1 = 5
r-- = 4         = 4
```

Three digits ka order hota hai:

```text
chmod user group others
```

Example:

```text
644 = owner rw-, group r--, others r--
755 = owner rwx, group r-x, others r-x
```

---

## 10. Ownership change karna

Permissions ke alawa file ka owner/group owner bhi important hai.

### 10.1 `chown` — owner change

```bash
chown kali file.txt
```

Ye file ka user owner `kali` set karne ka intent rakhta hai. Aam user kisi file ka owner arbitrary user ko assign nahi kar sakta; root/admin privilege required ho sakti hai.

### 10.2 `chgrp` — group owner change

```bash
chgrp kali file.txt
```

Ye file ka group owner `kali` set karne ke liye hai.

General rule:

- Root kisi valid group ko assign kar sakta hai.
- File owner apne available/allowed groups mein se group choose kar sakta hai, system policy ke subject to.
- Kisi doosre user ko owner banana normally root-level operation hai.

### 10.3 `chown user:group` — dono ek saath

```bash
chown kali:kali file.txt
```

Isse user owner aur group owner dono set karne ka intent hai. Ye do separate commands ke badle concise method hai.

### 10.4 Verify

```bash
ls -l file.txt
stat file.txt
```

`stat` ownership, permissions, inode, timestamps aur detailed metadata dikhata hai.

---

## 11. `chmod` — permission change karna

`chmod` ka use file/directory ki permission bits change karne ke liye hota hai. Do main styles hain:

1. Numeric/octal
2. Symbolic

---

## 12. Numeric `chmod`

```bash
chmod 777 file
chmod 644 file
chmod 755 directory
```

### 12.1 Common examples

```text
chmod 777 file  -> rwx rwx rwx
chmod 644 file  -> rw- r-- r--
chmod 755 dir   -> rwx r-x r-x
chmod 700 dir   -> rwx --- ---
```

`chmod 777` ka matlab har category ko read/write/execute dena hai. Practice mein samajhne ke liye use kiya ja sakta hai, lekin real system par ise permanently rakhna unsafe hai.

> Broad permissions convenience ke liye nahi, exact requirement ke according set karo.

### 12.2 `chmod` se owner/group change nahi hote

`chmod` permissions change karta hai. Owner/group change karne ke liye `chown`/`chgrp` use karo.

---

## 13. Symbolic `chmod`

Symbolic mode mein pehle target category, phir operator, phir permission specify hoti hai.

### 13.1 Target categories

| Symbol | Meaning |
|---|---|
| `u` | user/owner |
| `g` | group |
| `o` | others |
| `a` | all — user, group, others |

### 13.2 Operators

| Operator | Meaning |
|---|---|
| `+` | Existing permissions mein add |
| `-` | Existing permissions se remove |
| `=` | Exact permissions set/replace |

### 13.3 Examples

```bash
chmod g-x file
```

Group se execute permission remove karta hai.

```bash
chmod u+x file
```

Owner ko execute permission add karta hai.

```bash
chmod g+x file
```

Group ko execute permission add karta hai.

```bash
chmod u=w file
```

Owner ki permissions ko exactly write-only set karta hai. Existing read/execute permissions wipe ho sakti hain.

### 13.4 `+`/`-` vs `=`

Ye Day 9 ka important distinction hai:

```bash
chmod u+x file
```

Existing owner permissions ko preserve karke `x` add karta hai.

```bash
chmod u=w file
```

Owner ke liye exactly `w` set karta hai; existing `r` ya `x` remove ho sakti hain.

### 13.5 Multiple categories ek command mein

```bash
chmod u=rw,g=r,o=r file.txt
```

Iska result:

```text
owner  = rw-
group  = r--
others = r--
```

Comma-separated clauses alag categories set karti hain.

---

## 14. `umask` kya hota hai?

Current shell ka umask dekhne ke liye:

```bash
umask
```

Common output:

```text
0022
```

`umask` new file/directory create hote waqt default permissions se kuch permission bits **withhold** karta hai.

> Umask permission grant nahi karta; ye default permission ko restrict karta hai.

### 14.1 Four digits

```text
0 2 2 2
| | | |
| | | +-- others
| | +---- group
| +------ owner
+-------- special-bit position
```

Day 9 ka basic focus last three permission digits par hai. First digit special permission bits ke context mein aata hai; special bits next/advanced file-security topic mein detail se cover honge.

### 14.2 Umask digits ka intuition

| Umask digit | Commonly withheld permission | 7 se resulting permission intuition |
|---:|---|---|
| 0 | Kuch nahi | `rwx` |
| 2 | Write bit | `r-x` |
| 7 | Read/write/execute | `---` |

Umask ko simple decimal subtraction samajhne ke badle permission-bit mask samjho. Effective result permission bits ke combination se calculate hota hai.

---

## 15. Maximum default permissions

New objects ke liye Linux ek maximum base use karta hai:

| Object | Maximum default base | Reason |
|---|---:|---|
| Regular file | `666` (`rw-rw-rw-`) | New regular file ko execute bit default se nahi milti |
| Directory | `777` (`rwxrwxrwx`) | Directory traverse karne ke liye `x` meaningful/required hai |

### 15.1 Regular file ko default `777` kyu nahi?

Agar har newly-created file automatically executable hoti, to downloaded text/config/data files accidentally run ho sakti thi. Isliye normal regular file creation ke base mein execute permission nahi hoti.

Ye execute permission ko completely impossible nahi banata. File owner baad mein explicitly `chmod +x` kar sakta hai, agar uske paas file par ownership/permission ho.

### 15.2 Directory ko `777` base kyu?

Directory par `x` traverse/search ke liye required hai. Agar new directory ko default se `x` na mile, to usmein `cd` nahi kar paoge. Umask is base ko restrict karke normal result banata hai.

---

## 16. Effective permission formula

Day 9 mein trainer simple formula use karte hain:

```text
Effective permission = maximum base permission − umask
```

Strictly speaking, ye permission-bit masking hai, normal decimal subtraction nahi. Practical octal examples ke liye formula useful hai.

### 16.1 `umask 022` ke saath file

```text
Maximum file  = 666
umask         = 022
Result        = 644
```

Permissions:

```text
644 = rw- r-- r--
```

### 16.2 `umask 022` ke saath directory

```text
Maximum dir   = 777
umask         = 022
Result        = 755
```

Permissions:

```text
755 = rwx r-x r-x
```

Test:

```bash
umask 022
touch sample-file
mkdir sample-dir
ls -l sample-file
ls -ld sample-dir
```

Exact output ACLs, shell, filesystem defaults aur distribution settings ke context mein review karo; basic lab mein above result expected hai.

### 16.3 `umask 027` ka example

```text
File:      666 − 027 = 640  -> rw- r-- ---
Directory: 777 − 027 = 750  -> rwx r-x ---
```

Yahan others ko access nahi milta aur group ko write access nahi milta. Ye shared server par `022` se stricter default ho sakta hai.

---

## 17. Umask aur malware wala security discussion

Transcript mein ek security scenario discuss hota hai:

1. Malicious program machine par aata hai.
2. Program apna umask change karne ki koshish karta hai, jaise `000`.
3. Program chahta hai ki newly-created files ko broad permissions mil jayein.
4. System ka file-creation base regular files ko default execute bit nahi deta.

Demonstration pattern:

```bash
umask 000
touch file3
ls -l file3

mkdir test-dir
ls -ld test-dir
```

Basic expected result:

- Regular file maximum base `666` ki wajah se execute bit default nahi milti.
- Directory maximum base `777` se create ho sakti hai.

### 17.1 Important technical clarification

Transcript is point ko “attacker ko root chahiye tabhi malware executable banega” ke direction mein explain karta hai. Isko carefully samjho:

- Umask se regular file ko default execute bit nahi milti — ye correct security property hai.
- Lekin jis user ka file par ownership/control hai, wo apni file par baad mein `chmod +x file` kar sakta hai; iske liye har situation mein root required nahi.
- Isliye umask attacker ko file ko executable banane se completely nahi rokta.
- Umask sirf **creation-time default permissions** control karta hai; ye malware prevention system nahi hai.

Defensive security ke liye file ownership, writable directories, execution controls, application allowlisting, endpoint protection, monitoring aur least privilege bhi required hain.

---

## 18. Creation time par permission set karna — `mkdir -m`

Agar directory ko pehle loose default se create karke baad mein `chmod` nahi karna, to creation command mein mode specify kar sakte ho:

```bash
mkdir -m 700 private-dir
ls -ld private-dir
```

Expected permission:

```text
drwx------ private-dir
```

`-m` ka practical benefit hai ki directory creation ke time hi desired mode request hota hai. Exact interaction umask aur implementation par depend kar sakti hai, isliye output verify karo.

Private lab directory ke liye:

```bash
mkdir -m 700 ~/private-lab
```

Shared project directory ke liye required group access explicitly plan karo; blindly `777` use mat karo.

---

## 19. Class practice task

Trainer ka practice task file/group permissions apply karne par hai:

1. Ek file banao, example `am.txt`.
2. Kisi specific group ke members ko file **read aur modify** karne ki permission do.
3. Verify karo ki group member actual file modify kar sakta hai ya nahi.
4. Non-member ka access bhi test karo.

Possible lab workflow:

```bash
touch am.txt
groupadd file-editors
chgrp file-editors am.txt
chmod g+rw am.txt
ls -l am.txt
```

Test karne ke liye authorized lab user ko group mein add karo:

```bash
usermod -aG file-editors labuser
```

Naye group membership ke liye logout/login ya fresh session required ho sakta hai. Phir labuser ke roop mein:

```bash
echo "test line" >> am.txt
cat am.txt
```

Non-member test bhi karo. Path ke parent directories par traverse permission aur file ke owner/group ko verify karo; sirf file permission dekhna enough nahi hota.

> Ye commands disposable VM aur test data par run karo. Existing system files, `/etc` ya kisi real user ki file par practice mat karo.

---

## 20. Day 9 command summary

```bash
# Inspect metadata and permissions
ls -l
ls -la
ls -i
ls -ld directory
stat file

# File ownership
chown user file
chgrp group file
chown user:group file

# Numeric permissions
chmod 644 file
chmod 755 directory
chmod 700 private-directory

# Symbolic permissions
chmod u+x file
chmod g-x file
chmod o=r file
chmod u=rw,g=r,o=r file
chmod a+r file

# Umask
umask
umask 022
umask 027

# Create with a requested mode
mkdir -m 700 private-directory

# Group collaboration lab
groupadd file-editors
chgrp file-editors am.txt
chmod g+rw am.txt
usermod -aG file-editors labuser
```

Permission output ko read karte waqt order yaad rakho:

```text
file type | owner | group | others
```

---

## 21. Common mistakes aur safety points

1. `ls -l` ke first character ko permission samajhna; wo file type hota hai.
2. Owner, group aur others ke teen permission blocks ka order bhoolna.
3. File par `x` aur directory par `x` ka meaning same samajhna.
4. Directory par `r` hone ko enough samajhna; traverse ke liye `x` bhi chahiye.
5. Directory par `w` dena aur delete/rename impact ignore karna.
6. `chmod 777` ko permanent solution samajhna.
7. `chmod` se owner/group change hone ki expectation rakhna.
8. `chown` aur `chgrp` ke difference ko mix karna.
9. `+`/`-` adjustment aur `=` replacement ka difference bhoolna.
10. Umask ko permission grant samajhna; umask permissions withhold karta hai.
11. File ka maximum default `666` aur directory ka `777` difference ignore karna.
12. Umask ko ordinary decimal subtraction samajhna; ye permission-bit mask hai.
13. Umask ko malware prevention ka complete solution samajhna.
14. `mkdir -m` ke baad actual output verify na karna.
15. Group membership add karke current shell mein immediately change expect karna.
16. Parent directory permissions check kiye bina file access troubleshoot karna.
17. VM snapshot na lena aur risky tools/configuration ko directly main machine par try karna.

---

## 22. Self-check questions

1. Tool install ke baad VM snapshot kyu lena chahiye?
2. Snapshot aur normal file backup mein kya difference ho sakta hai?
3. Inode number kya hota hai aur `ls -i` se kaise dekhoge?
4. `ls -l` output ka first character kya batata hai?
5. Regular file, directory, symbolic link, block, character aur socket ke symbols likho.
6. Owner/group/others permission blocks ka order kya hai?
7. File par `r`, `w`, `x` ka meaning kya hai?
8. Directory par `r`, `w`, `x` ka meaning kya hai?
9. Directory mein `cd` karne ke liye `x` kyu zaruri hai?
10. `rwx`, `rw-`, `r-x` aur `r--` ke octal values kya hain?
11. `chown`, `chgrp` aur `chown user:group` ka difference kya hai?
12. `chmod 644 file` aur `chmod 755 dir` ka result explain karo.
13. Symbolic `chmod` mein `u`, `g`, `o`, `a` ka meaning kya hai?
14. `+`, `-` aur `=` operators ka difference kya hai?
15. Umask kya control karta hai? Kya umask permission grant karta hai ya withhold?
16. Umask ke four digits kis cheez ko represent karte hain?
17. New regular file ka maximum default `666` aur directory ka `777` kyu hota hai?
18. `umask 022` par new file aur directory ki effective permissions kya hongi?
19. `umask 027` par new file aur directory ki effective permissions calculate karo.
20. `umask 000` ke baad bhi new regular file ko default execute bit kyu nahi milti?
21. Kya file owner baad mein `chmod +x` kar sakta hai? Umask ka is par kya effect hai?
22. `mkdir -m 700 private-dir` ka benefit kya hai?
23. Group members ko file read/modify access dene ke liye ownership aur `chmod` kaise combine karoge?
24. Group membership change ke baad test session refresh kyu karna pad sakta hai?

---

## 23. Final takeaway

Day 9 ka core message:

- Linux file security owner, group aur others ke basis par access control karti hai.
- `ls -l` se file type, permissions, links, owner, group, size aur timestamp read karo.
- File aur directory par `r/w/x` ka meaning different hota hai; directory ka `x` traverse permission hai.
- `chown` owner change karta hai, `chgrp` group owner change karta hai, aur `chmod` permission bits change karta hai.
- Numeric permissions mein `r=4`, `w=2`, `x=1` hota hai.
- Symbolic `chmod` mein `+` add, `-` remove aur `=` exact replacement karta hai.
- `umask` new objects ki default permissions ko restrict karta hai.
- Regular files ka maximum default `666` aur directories ka `777` hota hai.
- Umask execute permission ko default se rokta hai, lekin owner ko baad mein `chmod +x` karne se automatically nahi rokta.
- VM snapshots aur small lab tests security learning ko recoverable banate hain.

Next class mein **advanced file security** aayegi — special permission bits aur attack/security scenarios ke saath.
