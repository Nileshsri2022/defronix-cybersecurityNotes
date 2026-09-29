# Day 10 — Kali Linux Capsule Course: Advanced File Permissions aur `find` (Hinglish Explanation)

**Source transcript:** `transcripts/010 - Kali Linux Free Capsule Course - Day 10 [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** Day 9 — standard permissions, ownership, `chmod` aur `umask`
**Note:** Ye explanation Hindi original transcript ko samajh kar likhi gayi hai; ye line-by-line literal translation nahi hai. Auto-captions mein `sticky bit`, `SGID`, `SUID`, `find`, `-perm`, `-exec`, `-iname` aur octal values kai jagah garbled mile. Context ke basis par intended Linux concepts aur commands restore karke simple Hinglish mein explain kiya gaya hai.

---

## 1. Day 10 ka focus

Day 9 mein standard permissions — `r`, `w`, `x` for owner, group aur others — samjhi gayi thi. Day 10 un permissions ke upar lagne wale **advanced permission bits** cover karta hai:

1. **Sticky bit** — shared directory mein doosre user ki file ko delete/rename karne se protection.
2. **SGID, yani Set Group ID** — directory ke andar banne wali files ko directory ka group inherit karwana.
3. **SUID, yani Set User ID** — executable ko file owner ki identity ke privileges ke saath run karna.
4. **`find` command** — name, type, owner, permission, size aur other conditions ke basis par files/directories search karna.
5. **`find -exec`** — search result par automatically koi further command run karna.

Trainer ka security angle clear hai: SUID/SGID bits ko samajhna privilege auditing aur authorized Linux security assessment ke liye important hai. Ye bits administration ka obscure detail nahi, system access-control ka part hain.

---

## 2. Advanced permission bits ka overview

| Bit | Octal digit | Usually applies to | Main effect |
|---|---:|---|---|
| Sticky bit | `1` | Directories | File owner/directory owner/root ke alawa doosre users files delete/rename nahi kar sakte |
| SGID | `2` | Directories; executables ka separate behavior bhi hota hai | Directory ke andar new files group owner inherit karti hain |
| SUID | `4` | Executable files | Program file owner ki effective identity ke saath run ho sakta hai |

Special permission digit ko normal three-digit mode ke aage likha jata hai:

```text
special | owner | group | others
   1    |   7   |   7   |   7       -> sticky + rwx/rwx/rwx
   2    |   7   |   7   |   5       -> SGID + rwx/rwx/r-x
   4    |   7   |   5   |   5       -> SUID + rwx/r-x/r-x
```

Examples:

```bash
chmod 1777 shared-dir   # sticky bit
chmod 2775 project-dir  # SGID
chmod 4755 program      # SUID
```

Advanced bits permission string mein `x` ki position par `s` ya `t` ke roop mein dikh sakte hain. Lowercase aur uppercase ka difference neeche detail mein aayega.

---

## 3. Sticky bit

### 3.1 Shared directory ka problem

Trainer ek project-directory scenario dete hain:

- Ek project par 20–30 log kaam kar rahe hain.
- Sab members ek common directory mein files create karte hain.
- Manager wahi directory dekhkar reports/status review karta hai.
- Ek user doosre user ki file read karke jealous ya malicious behavior mein us file ko delete kar deta hai.
- Victim next day login karta hai aur uski file missing hoti hai.

Shared directory mein sabko kaam karne ki permission ho sakti hai, lekin requirement ye hai:

> **User apni file par kaam kare, par doosre user ki file ko delete/rename na kar sake.**

### 3.2 Sticky bit kya karta hai?

Directory par sticky bit set hone par us directory ke entries ko delete/rename karne ki permission restricted hoti hai. Normally remove/rename karne wala user in mein se hona chahiye:

- file ka owner,
- directory ka owner,
- root/appropriate privileged administrator.

Isliye “directory writable hai” ka matlab ye nahi ki har user doosre user ki files delete kar sakega — sticky bit is behavior ko control karta hai.

### 3.3 `/tmp` se connection

Linux ka `/tmp` directory commonly world-writable hota hai, lekin us par sticky bit laga hota hai. Is wajah se multiple users temporary files create kar sakte hain, par ek normal user doosre user ki temporary file ko casually remove nahi kar sakta.

```bash
ls -ld /tmp
```

Typical output mein last permission position par `t` dikh sakta hai:

```text
drwxrwxrwt ... /tmp
```

Exact permissions/distribution configuration check karna chahiye.

---

## 4. Sticky bit ka practical demonstration

### 4.1 Lab setup

Disposable VM mein shared directory banao:

```bash
mkdir -p /tmp/common-lab
chmod 777 /tmp/common-lab
```

Do authorized test users use karo, jaise `user1` aur `user2`. User 1 file create kare:

```bash
su - user1
touch /tmp/common-lab/user1.txt
exit
```

Sticky bit ke bina, agar directory writable hai, to user2 file delete karne ki koshish kar sakta hai:

```bash
su - user2
rm /tmp/common-lab/user1.txt
```

Ye test sirf disposable lab file par karo.

### 4.2 Sticky bit apply karna

```bash
chmod +t /tmp/common-lab
ls -ld /tmp/common-lab
```

Output kuch is type ka ho sakta hai:

```text
drwxrwxrwt ... /tmp/common-lab
```

Ab `user2` ko `user1.txt` delete/rename karne ki permission deny honi chahiye, jab tak user2 directory owner/root na ho.

### 4.3 Symbolic aur numeric method

```bash
chmod +t /tmp/common-lab
chmod -t /tmp/common-lab
```

- `+t` sticky bit add karta hai.
- `-t` sticky bit remove karta hai.

Numeric method:

```bash
chmod 1777 /tmp/common-lab   # sticky bit + rwx for all
chmod 0777 /tmp/common-lab   # special bit remove, ordinary 777
```

Leading `1` sticky bit represent karta hai. Numeric command run karne ke baad `ls -ld` se actual result verify karo.

---

## 5. Sticky bit mein `t` aur `T`

Sticky bit others ke execute position par display hota hai:

| Display | Meaning |
|---|---|
| Lowercase `t` | Sticky bit set aur others execute bit bhi present |
| Uppercase `T` | Sticky bit set, lekin others execute bit absent |

Example conceptually:

```text
drwxrwxrwt   -> sticky + others x
 drwxrwxrwT  -> sticky, but others x absent
```

Uppercase/lowercase rule ko SUID aur SGID par bhi apply kiya ja sakta hai:

- Lowercase special letter = special bit + underlying execute bit.
- Uppercase special letter = special bit set, underlying execute bit absent.

Directory sticky bit ko check karte waqt sirf `t` dekhna enough nahi; directory ka actual `w`/`x` context bhi samjho.

---

## 6. SGID — Set Group ID on a directory

### 6.1 SGID ka main directory behavior

Directory par SGID set karne se us directory ke andar create hone wali new files/directories ko parent directory ka **group owner** inherit karne ka behavior milta hai.

```bash
chmod g+s project-dir
```

Iska use shared project directories mein hota hai. Team members ka primary group different ho sakta hai, lekin project directory ke andar banne wali files ko common project group mil jata hai.

### 6.2 SGID ke bina problem

Suppose:

- Project directory ka group `project` hai.
- User1 ka primary group `user1` hai.
- User2 ka primary group `user2` hai.

Agar SGID nahi laga, to new file ka group creator ke default/primary group se aa sakta hai. Har file ke baad administrator ko `chgrp project file` karna padega.

20–30 members ke project mein ye repetitive aur error-prone workflow hai.

### 6.3 SGID ke saath solution

```bash
mkdir -p /tmp/project-lab
chmod 770 /tmp/project-lab
chgrp project /tmp/project-lab
chmod g+s /tmp/project-lab
ls -ld /tmp/project-lab
```

Typical permission display:

```text
drwxrws--- ... /tmp/project-lab
```

Ab authorized project members ke liye newly created files ka group `project` inherit ho sakta hai.

> Group members ko actual read/write access ke liye directory/file permissions bhi correct honi chahiye. SGID ownership inheritance karta hai; ye apne aap group ko permission grant nahi karta.

### 6.4 SGID display: `s` aur `S`

SGID group ke execute position par display hota hai:

| Display | Meaning |
|---|---|
| Lowercase `s` | SGID set + group execute present |
| Uppercase `S` | SGID set, group execute absent |

Symbolic methods:

```bash
chmod g+s project-dir
chmod g-s project-dir
```

Numeric methods:

```bash
chmod 2775 project-dir   # leading 2 = SGID
chmod 0775 project-dir   # special bit removed
```

### 6.5 SGID aur file inheritance verify karna

```bash
su - project-user
touch /tmp/project-lab/report.txt
exit
ls -l /tmp/project-lab/report.txt
```

File ka group project group ke according check karo. Exact behavior filesystem, mount options aur distribution par depend kar sakta hai, lekin Linux project-directory ka standard use-case yahi hai.

---

## 7. SUID — Set User ID on an executable

### 7.1 Password-change puzzle

Day 8 mein samjha tha ki `/etc/shadow` protected file hai. Normal user ko us file ko directly write karne ki permission nahi hoti.

Phir normal user apna password kaise change karta hai?

```bash
passwd
```

Password change karne ke process ko password hash update karna padta hai. Isliye trainer `/usr/bin/passwd` ke permission output ko example banate hain:

```bash
ls -l /usr/bin/passwd
```

Typical output mein user/owner permission block mein `s` dikh sakta hai:

```text
-rwsr-xr-x 1 root root ... /usr/bin/passwd
```

### 7.2 SUID ka meaning

Executable par SUID bit set ho to program run karte waqt effective user identity file owner ki identity ban sakti hai. Agar executable root-owned SUID hai, to us particular program ke controlled operation ko root privileges mil sakte hain.

Simple explanation:

> **SUID program ko launch karne wale user ke badle file owner ke effective privileges ke saath run karne ka behavior deta hai.**

`passwd` trusted program ke roop mein required protected update perform karta hai. Isi wajah se SUID root binary security-sensitive hoti hai.

Kuch systems par `sudo` bhi setuid-root binary ke roop mein installed hota hai, lekin actual system par output verify karo:

```bash
ls -l "$(command -v sudo)"
```

### 7.3 SUID display: `s` aur `S`

SUID user/owner ke execute position par display hota hai:

| Display | Meaning |
|---|---|
| Lowercase `s` | SUID set + owner execute present |
| Uppercase `S` | SUID set, owner execute absent |

Symbolic methods:

```bash
chmod u+s program
chmod u-s program
```

Numeric methods:

```bash
chmod 4755 program   # leading 4 = SUID
chmod 0755 program   # SUID removed
```

### 7.4 SUID security risk

SUID root binary powerful hoti hai. Agar:

- binary vulnerable ho,
- unsafe command execution kare,
- attacker-controlled input ko insecurely process kare,
- environment/path ko trust kare,
- ya known misconfiguration ho,

to normal user privilege boundary cross kar sakta hai.

Isliye authorized Linux security assessment mein SUID binaries enumerate karke unka owner, version, permissions aur behavior review kiya jata hai.

> SUID bit khud vulnerability nahi hoti. Trusted program ko limited privileged operation ke liye SUID ki zarurat ho sakti hai. Risk depends on program design, version, configuration aur exploitability.

---

## 8. SUID, SGID aur sticky bit — one-table revision

| Bit | Octal | Symbolic | Permission string position | Main use |
|---|---:|---|---|---|
| SUID | `4` | `u+s` | Owner `x` position | Executable file owner ki effective identity use kar sakta hai |
| SGID | `2` | `g+s` | Group `x` position | Directory files ko parent group inherit karwa sakti hai |
| Sticky | `1` | `+t` | Others `x` position | Shared directory mein delete/rename restriction |

Examples:

```bash
chmod 4755 program    # SUID
chmod 2775 directory  # SGID
chmod 1777 directory  # sticky
chmod 7777 object     # all three special bits + 777
```

Lowercase/uppercase recap:

```text
s  = special bit + corresponding execute bit
S  = special bit without corresponding execute bit
t  = sticky bit + others execute bit
T  = sticky bit without others execute bit
```

Special-bit display ko `ls -l` se verify karo:

```bash
ls -l program
ls -ld directory
```

---

## 9. SUID/SGID enumerate karna

Authorized audit ya lab enumeration ke liye:

```bash
find / -perm -4000 -type f 2>/dev/null
```

Ye root filesystem ke neeche SUID bit wale regular files dhoondhne ka common pattern hai.

SGID files dhoondhna:

```bash
find / -perm -2000 -type f 2>/dev/null
```

Directories ko bhi review karna ho to `-type f` remove ya appropriate type condition use karo.

### 9.1 Enumeration result ko blindly trust mat karo

Har SUID file exploitable nahi hoti. Review points:

1. File ka full path.
2. Owner/group.
3. Package aur version.
4. Kya SUID bit expected hai?
5. Program input aur subprocess behavior.
6. File writable to nahi?
7. Recent unauthorized addition to nahi?
8. Known vendor security advisory/patch status.

Unfamiliar SUID binary ko delete ya execute karne ke badle pehle evidence preserve aur owner/admin se verify karo.

---

## 10. `find` command ka introduction

Trainer `find` ko very important command batate hain, kyunki filesystem mein naam, type, permissions, owner, group, size aur other conditions ke basis par search ki ja sakti hai.

Basic form:

```bash
find <starting-path> <conditions> <actions>
```

### 10.1 Current directory ke andar sab kuch

```bash
find .
```

`.` current working directory ko represent karta hai. Iske andar ki files aur directories recursive way mein list ho sakti hain.

### 10.2 Name ke basis par search

```bash
find . -name "test.txt"
find / -name "testfile.txt" 2>/dev/null
```

Wildcard:

```bash
find . -name "*.txt"
find . -name "test*"
```

Shell wildcard ko quote karna important hai, taaki `*` shell expand karne ke badle `find` ko mile.

### 10.3 `-type` se object restrict karna

```bash
find . -type f -name "test.txt"
find . -type d -name "tmp"
find . -type l -name "link*"
```

| Value | Match |
|---|---|
| `f` | Regular file |
| `d` | Directory |
| `l` | Symbolic link |

### 10.4 Case-insensitive search — `-iname`

Linux filenames case-sensitive hote hain. `-name "test*"` aur `-name "Test*"` different patterns hain.

```bash
find . -type f -iname "test*"
```

`-iname` case ko ignore karta hai, isliye `test.txt`, `Test.txt` aur `TEST.TXT` match ho sakte hain.

### 10.5 Specific directory ya full filesystem

```bash
find /tmp -type f -name "*.log"
find / -type f -name "*.conf" 2>/dev/null
```

`/` se search expensive ho sakta hai aur permission errors aa sakte hain. Required scope se start karo; full root search sirf authorized maintenance/audit context mein karo.

---

## 11. Permission ke basis par `find`

### 11.1 Exact mode — `-perm 774`

```bash
find /path -perm 774 -print
```

Ye exact permission mode `774` wale matches dhoondhne ka pattern hai.

### 11.2 At-least permission bits — `-perm -4000`

```bash
find / -perm -4000 -type f 2>/dev/null
```

Leading `-` ka meaning broadly ye hai ki specified permission bits present hon; isi pattern se SUID enumeration ki jati hai.

### 11.3 Permission test negate karna — `!`

```bash
find /path ! -perm 077 -print
```

`!` next test ko negate karta hai. Exact command ki interpretation samajhkar run karo; `-perm 077` ka meaning aur path scope verify karo.

Modern GNU `find` mein `-perm /mode` ka pattern “in bits mein se koi bhi bit” check karne ke liye bhi use hota hai:

```bash
find /path -perm /022 -type f -print
```

Is variation ko system ke `man find` se confirm karo.

---

## 12. Owner aur group ke basis par search

### 12.1 `-user`

```bash
find . -user root
find /home -user olduser -print
```

Ye specific username ke owner wali files dhoondhne mein useful hai — inventory, migration, cleanup aur authorized forensics ke liye.

### 12.2 `-group`

```bash
find /project -group project
```

Group ownership audit karne ke liye use hota hai. Day 9 ke shared project/group-permission scenario ke saath iska direct connection hai.

### 12.3 Numeric owner/group

Deleted user ke orphaned files ke cases mein username resolve nahi hota. Numeric ownership inspect karne ke liye:

```bash
ls -lan path/to/file
```

`find -nouser` aur `find -nogroup` bhi unresolved ownership dhoondhne mein useful hain:

```bash
find / -nouser -o -nogroup 2>/dev/null
```

---

## 13. Empty files aur size ke basis par search

### 13.1 Empty files

```bash
find /tmp -type f -empty
find /path -type f -empty -print
```

Full `/` scan output-heavy aur slow ho sakta hai, isliye starting path carefully choose karo.

### 13.2 Size

```bash
find /path -type f -size 50M
find /path -type f -size +100M
find /path -type f -size -10M
```

General meaning:

- `50M` — size unit ke according 50M match pattern.
- `+100M` — 100M se larger.
- `-10M` — 10M se smaller.

GNU `find` size rounding/block-unit semantics rakhta hai. Exact boundary checks ke liye `-printf` ya `stat` se actual byte size verify karo.

---

## 14. `find -exec` — result par command chalana

### 14.1 Problem

Maan lo 200 files milti hain jinki permissions change karni hain. Manual method:

1. `find` run karo.
2. Output copy/read karo.
3. Har file par alag `chmod` run karo.

Ye slow, repetitive aur error-prone hai.

### 14.2 One-step solution

`find` ke result par further command run karne ke liye `-exec` use hota hai:

```bash
find /path -type f -perm 2644 -exec chmod 2777 {} \;
```

Is command ko root filesystem par blindly run mat karo; `/path` ko lab/test directory se replace karo.

### 14.3 Syntax breakdown

| Part | Meaning |
|---|---|
| `find /path` | Search ka starting path |
| `-type f` | Sirf regular files |
| `-perm 2644` | Condition: exact permission mode |
| `-exec` | Har result par command run karo |
| `chmod 2777` | Result par run hone wali command |
| `{}` | Current found path ka placeholder |
| `\;` | `-exec` expression ka mandatory terminator |

Important:

- `{}` aur `\;` required hote hain.
- `{}` ke baad space hona chahiye.
- Shell ko semicolon pass karne ke liye `\;` likho.
- Terminator omit karne par `find: missing argument to '-exec'` jaise error aa sakta hai.

### 14.4 More examples

```bash
find . -name "*.tmp" -exec rm -- {} \;
find . -type f -perm 777 -exec chmod 644 {} \;
find . -name "*.log" -exec grep -H "ERROR" {} \;
find . -user olduser -exec chown newuser {} \;
```

Destructive commands jaise `rm`, `chmod`, `chown` ko pehle `-print` ke saath dry-run/review karo:

```bash
find . -name "*.tmp" -print
```

Result expected ho tabhi action command add karo.

### 14.5 `-exec ... {} +` variation

Multiple paths ko batch mein command ko pass karne ke liye:

```bash
find . -type f -name "*.log" -exec grep -H "ERROR" {} +
```

`\;` har result par command run kar sakta hai, jabki `+` multiple results batch kar sakta hai. Exact command behavior aur argument safety ke liye `man find` check karo.

---

## 15. Complete advanced-permission lab workflow

### 15.1 Sticky directory

```bash
mkdir -p /tmp/perm-lab/shared
chmod 777 /tmp/perm-lab/shared
chmod +t /tmp/perm-lab/shared
ls -ld /tmp/perm-lab/shared
```

### 15.2 SGID project directory

```bash
mkdir -p /tmp/perm-lab/project
chgrp project /tmp/perm-lab/project
chmod 2770 /tmp/perm-lab/project
ls -ld /tmp/perm-lab/project
```

Ensure `project` group exists and authorized test users are members before testing.

### 15.3 Inspect SUID files

```bash
find /usr/bin /usr/sbin -type f -perm -4000 -print 2>/dev/null
```

System directories scope karna full `/` search se safer/faster ho sakta hai.

### 15.4 Test `find` without changing anything

```bash
find /tmp/perm-lab -type f -print
find /tmp/perm-lab -type f -perm 644 -print
find /tmp/perm-lab -type f -empty -print
```

Expected output verify hone ke baad hi `-exec chmod` ya `-exec chown` add karo.

---

## 16. Day 10 command summary

```bash
# Inspect special permissions
ls -l /usr/bin/passwd
ls -ld /tmp
ls -ld project-dir

# Sticky bit
chmod +t shared-dir
chmod -t shared-dir
chmod 1777 shared-dir
chmod 0777 shared-dir

# SGID
chmod g+s project-dir
chmod g-s project-dir
chmod 2775 project-dir

# SUID
chmod u+s program
chmod u-s program
chmod 4755 program

# Enumerate special-bit files
find / -type f -perm -4000 2>/dev/null   # SUID
find / -type f -perm -2000 2>/dev/null   # SGID

# Basic find
find .
find . -name "*.txt"
find . -type f -name "test.txt"
find . -type d -name "tmp"
find . -type f -iname "test*"

# Conditions
find /path -perm 774 -print
find /path ! -perm 077 -print
find /path -user root -print
find /path -group project -print
find /path -type f -empty -print
find /path -type f -size +100M -print

# Execute an action on matches
find /path -type f -name "*.tmp" -exec rm -- {} \;
find /path -type f -perm 777 -exec chmod 644 {} \;
```

---

## 17. Common mistakes aur safety points

1. Sticky bit ko “koi bhi delete nahi kar sakta” samajhna; file owner, directory owner aur root exceptions hote hain.
2. Sticky bit ko file par apply karke same directory behavior expect karna; iska main use shared directories mein hai.
3. SGID ko group permissions samajhna; SGID inheritance control karta hai, permissions alag set karni padti hain.
4. SUID root binary ko automatically vulnerable samajhna; program behavior aur version review karna zaruri hai.
5. `s` aur `S`, `t` aur `T` ka execute-bit difference ignore karna.
6. `chmod 4755` jaise special permissions ko unknown program par blindly apply karna.
7. SUID/SGID enumeration results ko bina authorization ke exploit karna.
8. `find /` full-root search ko har baar use karna; slow output aur permission errors aa sakte hain.
9. `-name` aur `-iname` ko same samajhna.
10. `-type f`/`d`/`l` condition omit karke unwanted object types match karna.
11. `-perm 774` exact-match semantics ko `-perm -774` se confuse karna.
12. `find -exec` mein `{}` ya `\;` omit karna.
13. `find` result review kiye bina `rm`, `chmod` ya `chown` execute karna.
14. Root filesystem par broad permission changes karna.
15. Shared lab ke bajay real user files ya production directories par testing karna.

---

## 18. Self-check questions

1. Sticky bit kis problem ko solve karta hai?
2. `/tmp` jaise shared directory mein sticky bit useful kyu hai?
3. Sticky bit permission string mein kahan dikhai deta hai?
4. Lowercase `t` aur uppercase `T` ka difference kya hai?
5. Sticky directory mein file delete karne ke authorized exceptions kaunse hain?
6. Directory par SGID ka effect kya hota hai?
7. SGID shared project directory ke group-management problem ko kaise solve karta hai?
8. SGID group execute position mein `s`/`S` kyu dikhata hai?
9. Normal user `passwd` run karke apna password kaise change kar pata hai?
10. SUID ka one-sentence definition do.
11. SUID aur SGID ke octal digits kya hain?
12. SUID root binary security-sensitive kyu hoti hai?
13. SUID files enumerate karne ki safe audit command kya hai?
14. `find .`, `find . -name '*.txt'` aur `find . -type f -iname 'test*'` mein difference kya hai?
15. `-name` aur `-iname` ka difference kya hai?
16. `-perm 774` aur `-perm -4000` ka conceptual difference kya hai?
17. `find` mein `!` operator kya karta hai?
18. `-user`, `-group`, `-empty` aur `-size` conditions ka use batao.
19. `find -exec` mein `{}` ka meaning kya hai?
20. `\;` ko escape karke likhna kyu zaruri hai?
21. `-exec ... {} \;` aur `-exec ... {} +` mein broad difference kya hai?
22. Broad `find -exec rm` run karne se pehle kaunsa safety workflow follow karoge?
23. `chmod 1777`, `chmod 2775` aur `chmod 4755` kis special bit ko represent karte hain?
24. Special permission bits ko production mein change karne se pehle kaunse checks karne chahiye?

---

## 19. Final takeaway

Day 10 ka core message:

- Sticky bit shared directory mein users ko doosre users ki files delete/rename karne se restrict karta hai.
- SGID project directory ke andar new files ko common group inherit karwa kar collaboration simplify karta hai.
- SUID executable ko file owner ke effective privileges ke saath run kar sakta hai; root-owned SUID binaries carefully audit honi chahiye.
- Special bits ke octal digits `4 = SUID`, `2 = SGID`, `1 = sticky` hain.
- Lowercase `s/t` underlying execute permission ke saath special bit dikhate hain; uppercase `S/T` execute ke bina.
- `find` filesystem search, permission auditing, owner/group discovery aur cleanup workflows ke liye powerful hai.
- `find -exec` search result par further command automate karta hai, lekin destructive action se pehle dry-run/review zaruri hai.
- Advanced permissions aur `find` ko sirf authorized lab/administration context mein use karo.

Days 9–10 ke saath basic aur advanced file security ka foundation complete hota hai: permissions kaise read/change hoti hain, special bits kya karte hain, aur filesystem ko efficiently audit kaise karna hai.
