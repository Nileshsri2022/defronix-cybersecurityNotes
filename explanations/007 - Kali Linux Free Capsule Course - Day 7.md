# Day 7 — Kali Linux Capsule Course: User Management + Group Management (Hinglish Explanation)

**Source transcript:** `transcripts/007 - Kali Linux Free Capsule Course - Day 7 [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** Day 6 — `cut`, `awk`, compression aur `tar`
**Note:** Ye explanation Hindi original transcript ko samajh kar likha gaya hai; ye line-by-line literal translation nahi hai. Auto-captions mein `whoami`, `su`, `UID/GID`, `useradd`, `usermod`, `groupadd`, `/etc/passwd`, `/etc/shadow`, `/etc/default/useradd` aur `/etc/skel` jaise technical words kai jagah garbled mile. Context ke basis par unka intended command/concept restore karke simple Hinglish mein explain kiya gaya hai.

---

## 1. Day 7 ka focus

Pichhli classes mein commands ke through text processing aur files ke saath kaam hua. Day 7 se course **system administration** ki taraf move karta hai. Aaj ke major topics hain:

1. **User management** — users ko identify, create, modify aur delete karna.
2. **Root/superuser** — root ke paas itni power kyu hoti hai aur root ke roop mein permanently kaam karna risky kyu hai.
3. **`su` command** — ek user account se doosre account mein switch karna; normal switch aur login shell ka difference.
4. **User database files** — `/etc/passwd`, `/etc/shadow`, `/etc/default/useradd` aur `/etc/skel`.
5. **Group management** — primary/secondary groups, group create/modify/delete karna aur user ko group mein add karna.

Trainer ka emphasis hai ki sirf commands ratna goal nahi hai. User, UID, GID, home directory, shell aur group membership aapas mein kaise connected hain, ye samajhna Linux administration aur penetration-testing dono ke liye fundamental hai.

---

## 2. User management ki zarurat kyu padti hai?

### 2.1 Har department ko har file ki access nahi chahiye

Ek organization mein development, accounts, finance, production aur security jaise alag departments ho sakte hain. Har department ka kaam aur required data alag hota hai.

- Developer ko apne project ki files par kaam karne ki permission chahiye.
- Accounts team ko technical department ki saari files dene ka koi reason nahi hai.
- Finance user ko poore server ya poori machine ka access de dena unnecessary hai.

Is principle ko simple words mein samjho:

> **Jis user ko jitni access ki zarurat hai, usko utni hi access do — extra permission mat do.**

Isko security mein **least privilege** approach kaha jata hai. Extra permission convenient lag sakti hai, lekin agar account compromise ho gaya to attacker ko wahi extra power mil jayegi.

### 2.2 Normal user se kaam karna safer kyu hai?

Trainer explain karte hain ki system administrator ko normally **privileged/root account se permanently logged in nahi rehna chahiye**. Better workflow hota hai:

1. Normal user ke roop mein login karo.
2. Jab administrative kaam ho tab temporary privilege elevation ya user switch use karo.
3. Kaam ke baad wapas normal account par aa jao.

Reason ko blast radius se samjho:

| Situation | Vulnerability exploit hone par risk |
|---|---|
| Normal user logged in | Mostly us user ki permissions tak impact limit ho sakta hai |
| Root logged in | Attacker ko poore system par control mil sakta hai |

Agar system mein vulnerability ho aur humne har jagah root/admin access de rakha ho, to ek chhoti mistake se **poori machine compromise** ho sakti hai. Isliye “root se kaam karna possible hai” aur “root se har waqt kaam karna safe hai” — ye dono alag baatein hain.

---

## 3. Root user aur UID 0

Linux mein ek special privileged account hota hai:

- Iska naam aam taur par **`root`** hota hai.
- Root ko **superuser** ya administrator bhi kaha jata hai.
- Root ki **UID hamesha `0`** hoti hai.
- Root normal users ki permissions ko override kar sakta hai.
- Root system files ko modify/remove kar sakta hai aur users/groups manage kar sakta hai.

UID ka matlab **User ID** hai. Linux username ko sirf text ke roop mein nahi, balki internally numeric UID ke saath identify karta hai. Root ke case mein woh reserved identity `0` hai.

### Security impact

Agar kisi attacker ko root account mil gaya, to problem sirf ek file ya ek user tak limited nahi rahegi. Wo system configuration, accounts, services aur sensitive data tak pahunch sakta hai. Isliye root compromise ko full-system compromise maana jata hai.

### Pen-testing/CTF context

Trainer offensive-security angle bhi batate hain: enumeration aur scanning ke baad kisi target par normal shell mil jana aksar final goal nahi hota. Normal user ki permissions limited hoti hain, isliye authorized lab/CTF mein next task privilege escalation karke root-level access samajhna hota hai.

> Real systems par ye sab sirf written authorization aur controlled lab ke andar practice karna chahiye.

---

## 4. Current user aur logged-in users check karna

### 4.1 `whoami` — main kaun hoon?

```bash
whoami
```

Ye current shell mein active username batata hai. Agar output `root` aaye to current shell root identity ke under chal raha hai; agar `kali` aaye to current user `kali` hai.

### 4.2 `who` — kaun-kaun logged in hai?

```bash
who
```

Isse logged-in users, unka terminal/session aur login time jaise details mil sakti hain. Transcript mein trainer output se dikhate hain ki `kali` kis terminal, jaise `tty7`, par logged in hai.

### 4.3 `w` — kaun kya kar raha hai?

```bash
w
```

`w` aam taur par `who` se zyada information deta hai: login time, idle time aur current activity/command ka snapshot. Admin ko live system par active sessions samajhne mein ye useful hota hai.

### 4.4 `id` — UID, GID aur groups

```bash
id
id manish
```

- `id` bina username ke current user ki information dikhata hai.
- `id manish` kisi specific user ki identity information dikhata hai.
- Output mein UID, primary GID aur group memberships dikh sakti hain.

Typical output ka structure kuch is tarah samjho:

```text
uid=1000(kali) gid=1000(kali) groups=1000(kali),4(adm),27(sudo)
```

Exact UID/GID aur groups machine ke hisaab se different honge. Important point hai ki username ke saath numeric identity aur memberships bhi hoti hain.

---

## 5. Red Hat systems mein security context ka note

Trainer batate hain ki Red Hat/CentOS family system par `id` output mein ek additional **security context** bhi dikh sakta hai. Ye **SELinux** se related hota hai.

SELinux operating system ke upar ek additional mandatory access-control layer provide karta hai. Basic idea:

- Agar policy allow karti hai, action allow ho sakta hai.
- Agar policy deny karti hai, sirf root hone se bhi action automatically allow nahi ho jata.

Is tarah system ko isolate karke permissions ko aur strict banaya ja sakta hai. Trainer isi layered-security model ke context mein Red Hat ki industry usage aur firewall, antivirus, IDS/IPS jaise additional layers ka mention karte hain.

> Ye Day 7 ka introductory context hai; SELinux policy writing ya troubleshooting is class ka main topic nahi hai.

---

## 6. `su` — user account switch karna

`su` ka use ek user account se doosre account mein switch karne ke liye hota hai.

```bash
su <username>
```

Agar username specify na kiya jaye, to Linux systems par `su` aam taur par root account ko target karta hai:

```bash
su
```

Password prompt aane par target account ka password required ho sakta hai.

Lekin yahan ek important distinction hai: **user identity switch hona** aur **target user ka complete login environment load hona** exactly same cheez nahi hai.

---

## 7. Login shell, non-login shell aur environment

### 7.1 Environment kya hota hai?

Har user ke saath kuch environment variables aur configuration associated hoti hai. Examples:

- `HOME` — home directory
- `PATH` — commands search karne ki locations
- `SHELL` — default shell
- prompt aur shell startup configuration

Jab user machine par username/password ke saath normal login karta hai, system us user ka login environment prepare karta hai.

### 7.2 `su user` — identity switch, purana environment

```bash
su root
# ya, root ke liye username omit karke:
su
```

Transcript ke demonstration mein `su` ke baad prompt/current directory `/home/kali` hi dikhti hai, `/root` nahi. Iska reason ye samjhaya gaya hai:

- Shell target user, yani root, ki identity ke saath command run kar sakta hai.
- Lekin current shell ka environment aur working directory pehle wale user se inherited reh sakta hai.
- Isliye trainer ise target user ki tarah **acting** karna kehte hain, complete fresh login nahi.

`su` ke baad identity verify karne ke liye:

```bash
whoami
pwd
```

### 7.3 `su - user` — target user ka login environment

```bash
su - root
# ya root ke liye:
su -
```

Dash `-` ka meaning hai target user ka login-style environment load karna. Isse `HOME`, working directory aur startup configuration target user ke context mein set ho sakte hain.

```bash
su - root
whoami     # root
pwd        # aam taur par /root, system/configuration par depend karta hai
```

Memory rule:

> **`su user` = user switch with existing environment ka idea**
> **`su - user` = target user ka login environment load karne ka idea**

Exact behavior shell aur distribution ke configuration par depend kar sakta hai, lekin Day 7 ka conceptual difference yahi hai.

### 7.4 Shell nesting aur `$SHLVL`

Transcript mein nested shell samjhane ke liye shell level check kiya jata hai:

```bash
echo $SHLVL
```

Agar ek shell ke andar doosra shell open karte ho, to nesting level badh sakta hai — jaise `1` se `2`. Ye user identity nahi batata; ye shell nesting depth batata hai.

Nested session se bahar aane ke liye:

```bash
exit
```

---

## 8. `/etc/passwd` — user record samajhna

Trainer ke according user management samajhne ke liye `/etc/passwd` ki entry ko samajhna bahut important hai.

```bash
cat /etc/passwd
```

Har line colon `:` se separated fields ka record hoti hai. Conceptual example:

```text
manish:x:1001:1001:Manish:/home/manish:/bin/bash
```

Is line ke seven fields:

| Field | Meaning |
|---|---|
| 1 | Username/account name |
| 2 | Password field marker, commonly `x` |
| 3 | UID — User ID |
| 4 | GID — primary Group ID |
| 5 | Comment/GECOS field — descriptive information |
| 6 | User ki home directory |
| 7 | Login shell |

### 8.1 Password field mein `x` kyu hota hai?

Historically password information `/etc/passwd` mein rakhi ja sakti thi. Security improve karne ke liye password hash ko alag protected file, **`/etc/shadow`**, mein move kiya gaya. Isliye `/etc/passwd` ki second field mein aksar actual hash ke badle `x` marker dikhta hai.

```bash
ls -l /etc/passwd /etc/shadow
```

`/etc/shadow` ko casually edit ya expose nahi karna chahiye. Is file mein password hashes aur password-aging information hoti hai.

### 8.2 UID aur GID

- UID user ki numeric identity hai.
- GID user ke primary group ki numeric identity hai.
- Root ki UID `0` hoti hai.
- Normal/system users ke IDs distribution aur configuration ke hisaab se assign hote hain.

Username badal sakta hai, lekin file ownership internally numeric UID se associate hoti hai. Isi wajah se deleted user ke UID reuse hone par orphaned files ka security issue aa sakta hai; is topic ko neeche detail mein dekhenge.

### 8.3 Home directory aur shell

Example mein `/home/manish` batata hai ki user ka home directory path kya hai. Last field `/bin/bash` batata hai ki login par us user ke liye default shell kaunsa hoga.

---

## 9. `useradd` se naya user banana

### 9.1 Basic user creation

```bash
useradd user1
```

Isse user record create hota hai aur system defaults ke basis par baaki values choose ki ja sakti hain. Verify karne ke liye trainer last entries dekhne ka method use karte hain:

```bash
tail -2 /etc/passwd
```

> `useradd` account record create karta hai; password set karna alag user/password-management task hai. Day 7 ke end mein trainer password management ko next class ke liye defer karte hain.

### 9.2 Important values explicitly specify karna

Trainer advise karte hain ki user create karte waqt sirf username par depend na karo. Home directory, comment, shell aur zarurat ho to UID explicitly define karna clearer hota hai:

```bash
useradd \
  -d /home/user2 \
  -c "Finance team member" \
  -s /bin/bash \
  user2
```

Specific UID ki zarurat ho to:

```bash
useradd -u 1500 -d /home/user2 -c "Finance team member" -s /bin/bash user2
```

| Option | Meaning |
|---|---|
| `-d` | Home directory set karna |
| `-c` | Comment/GECOS information set karna |
| `-s` | Login shell set karna |
| `-u` | Specific UID assign karna |

Command options use karne se pehle `useradd --help` ya apne system ka manual check karna useful hai, kyunki defaults distribution ke hisaab se different ho sakte hain.

### 9.3 Defaults kahan se aate hain?

```bash
cat /etc/default/useradd
```

Is file mein new users ke defaults mil sakte hain:

| Setting | General role |
|---|---|
| `SHELL` | Default login shell |
| `HOME` | Home directories ka base path, aam taur par `/home` |
| `GROUP` | Default group-related setting |
| `INACTIVE` | Password expiry ke baad account disable behavior |
| `EXPIRE` | Account expiry date ka default |
| `SKEL` | Skeleton directory ka path |

Trainer `INACTIVE=-1` ko aise explain karte hain ki password expiry ke baad inactive period ke context mein account disable nahi hoga. Exact password-aging behavior ko real system par `man useradd`, `man shadow` aur `chage` documentation se verify karna chahiye.

UID ranges bhi system policy se related hoti hain. System/service accounts aur normal human users ke liye alag ranges use ki ja sakti hain; exact threshold har distribution par same nahi hota.

---

## 10. User modify karna — `usermod`

Existing user ke attributes change karne ke liye `usermod` use hota hai:

```bash
usermod -c "Updated description" -s /bin/bash user2
```

Home directory, shell, comment, UID aur group membership jaise options ke liye `usermod --help` dekho. Modify karne ke baad record verify karna chahiye:

```bash
tail /etc/passwd
id user2
```

Production system par UID, home directory ya primary group change karne se pehle files, running processes aur ownership impact check karna zaruri hai.

---

## 11. User delete karna — `userdel`

### 11.1 Basic delete aur `-r` ka difference

```bash
userdel user1
```

Basic `userdel` account entry remove kar sakta hai, lekin home directory aur uske andar ka data reh sakta hai.

```bash
userdel -r user1
```

`-r` user ke saath associated home directory aur mail spool jaise data ko remove karne ki koshish karta hai. Isliye ise bina check kiye run karna destructive ho sakta hai.

### 11.2 Delete karne se pehle safe workflow

1. User ke processes aur active sessions check karo.
2. Home directory mein important ya sensitive data hai ya nahi dekho.
3. Required data ko authorized owner/location par transfer karo.
4. Backup ya approval confirm karo.
5. Tabhi `userdel` ya `userdel -r` choose karo.

> Kisi real server par blindly `userdel -r` run mat karo. Ye demonstration command hai; pehle target user aur data verify karo.

### 11.3 UID reuse se sensitive data leakage ka risk

Transcript ka important security scenario ye hai:

1. User delete kiya gaya, lekin home directory delete nahi hui.
2. Purane user ki files disk par reh gayi.
3. Purane user ka UID free ho gaya.
4. Baad mein naya user create hua aur system ne wahi available UID assign kar di.
5. Files ownership numeric UID par based hone ke karan purane user ki files naye user ko owned dikh sakti hain.
6. Naya user sensitive information read kar sakta hai.

Yahan problem sirf username ki nahi hai. Linux file ownership ko UID number se resolve karta hai. Isliye stale home directories aur UID reuse ko carefully handle karna chahiye.

### 11.4 Orphaned files dhoondhna

Aise files jinka owner/group system mein resolve nahi ho raha ho, unhe locate karne ke liye `find` ka use kiya ja sakta hai:

```bash
find / -nouser -o -nogroup 2>/dev/null
```

- `-nouser` — jis numeric UID ka matching username nahi mil raha.
- `-nogroup` — jis numeric GID ka matching group nahi mil raha.
- `2>/dev/null` — inaccessible directories ke errors ko display se hata sakta hai.

Root filesystem par ye command expensive ho sakti hai. Authorized lab ya maintenance window mein, aur zarurat ho to specific path se, run karna better hai.

### 11.5 Remediation ke do broad options

Situation ke hisaab se:

1. Required data ko authorized location par copy/transfer karke orphaned home directory remove karo.
2. Data retain karna ho to ownership manually kisi valid user/group ko assign karo, permissions review karo, aur old account ki files ko document karo.

Example ownership review ke liye:

```bash
ls -lan /home/old-user
```

`-n` numeric UID/GID dikhata hai, jisse unresolved ownership identify karna easy hota hai.

---

## 12. `/etc/skel` — naye user ka basic framework

Jab naya user account create hota hai, to user ke home environment ke liye ek starting template use kiya ja sakta hai. Is template directory ko **skeleton directory** kaha jata hai:

```bash
ls -la /etc/skel
```

Aam taur par yahan ye files mil sakti hain:

```text
.bash_logout
.bashrc
.profile
```

### 12.1 Iska purpose

`/etc/skel` ke contents se har naye user ko common starting configuration mil sakti hai:

- Shell startup configuration
- Default environment behavior
- Organization ke login instructions ya notice
- Har user ke home mein required common files

Lecture mein trainer naya user create karke uske home directory mein template files dikhate hain. Exact files distribution, package aur administrator customization par depend kar sakti hain.

### 12.2 Important caution

`/etc/skel` mein secret keys, passwords ya private data nahi rakhna chahiye, kyunki iska content multiple new accounts ke home directories mein copy ho sakta hai. Sirf safe, common configuration rakho.

---

## 13. Group management ki zarurat

### 13.1 Individual permissions scale nahi hoti

Trainer ek organization ka example dete hain:

- Company mein bahut saare employees hain.
- Ek project par 50 log kaam karte hain.
- Project ki 30–40 files par in sabko similar access chahiye.

Agar har user ko har file par individually permission doge, to:

- Configuration bahut time-consuming hogi.
- Monitor karna mushkil hoga ki kaun kis file ko access kar raha hai.
- Employee add/remove hone par dozens of permissions manually update karni padengi.

### 13.2 Group-based solution

Better design:

1. Project members ka ek group banao.
2. Required files/directories ka group ownership us project group ko do.
3. Group permissions ek baar configure karo.
4. New employee ko group mein add karo.
5. Employee leave kare to group se remove karo.

Is approach mein file-by-file individual permission edits ki zarurat kam ho jati hai. Group membership hi access management ka central point ban jati hai.

> Groups ka purpose permissions ko centrally manage karna hai — ye monitoring, review aur access revocation ko simpler banata hai.

---

## 14. Primary group aur secondary group

Linux user ke context mein do important group types samjho:

### 14.1 Primary group

- User ka ek primary group hota hai.
- New user create karte waqt distribution/configuration ke hisaab se user ke naam ka group create ho sakta hai.
- `/etc/passwd` ke GID field mein primary group ka numeric ID stored hota hai.
- User ke create kiye files par default group ownership primary group se related ho sakti hai.

### 14.2 Secondary groups

- User ko additional groups mein member banaya ja sakta hai.
- Ek user multiple secondary groups ka member ho sakta hai.
- Project, device, administration ya service access ke liye secondary groups use kiye ja sakte hain.
- Membership details `/etc/group` mein dikh sakti hain.

Simple comparison:

| | Primary group | Secondary group |
|---|---|---|
| Count | Usually ek | Multiple ho sakte hain |
| Main record | `/etc/passwd` ka GID field | `/etc/group` membership list |
| Use | Default group context | Additional project/access membership |

### 14.3 Group files dekhna

```bash
cat /etc/group
grep '^kali:' /etc/group
groups
groups kali
```

- `groups` current user ki group membership dikhata hai.
- `groups kali` specific user ki groups dikhata hai.
- `/etc/group` mein group name, numeric GID aur member list ka format hota hai.

---

## 15. Group commands

### 15.1 Group create karna — `groupadd`

```bash
groupadd UNIX
```

Verify karne ke liye:

```bash
tail -2 /etc/group
```

Naya group create ho sakta hai, lekin usmein members automatically nahi honge. User ko separately add karna padta hai.

### 15.2 User ko secondary group mein add karna — `usermod -aG`

```bash
usermod -aG UNIX sachin2
```

Yahan:

- `-a` ka matlab existing supplementary groups ko preserve karke append karna.
- `-G` supplementary/secondary groups specify karta hai.
- `UNIX` target group hai.
- `sachin2` target user hai.

Verify:

```bash
groups sachin2
id sachin2
```

### 15.3 `-a` bhoolne ka risk

```bash
usermod -G UNIX sachin2
```

Is form mein `-a` nahi hai. Common Linux behavior mein `-G` existing supplementary group list ko replace kar sakta hai. Matlab user ko `UNIX` group mil jayega, lekin uski purani secondary memberships remove ho sakti hain.

Isliye user ko existing groups ke saath nayi secondary group membership deni ho to normal safe pattern hai:

```bash
usermod -aG newgroup username
```

> Capital `G` aur lowercase `g` ko confuse mat karo; `-a` miss karna destructive access change ban sakta hai.

### 15.4 Primary group change karna — lowercase `-g`

```bash
usermod -g UNIX sachin2
```

Yahan lowercase `-g` user ka **primary group** change karta hai.

| Option | Meaning |
|---|---|
| `-aG group user` | Existing memberships preserve karke secondary group add |
| `-G group user` | Supplementary groups ki list replace kar sakta hai |
| `-g group user` | Primary group change |

Primary group change karne se pehle existing files, default group behavior aur application impact check karo.

### 15.5 Group rename karna — `groupmod -n`

```bash
groupmod -n unix UNIX
```

Isse old group name `UNIX` ko new name `unix` diya ja sakta hai. Verify:

```bash
grep -E '^(UNIX|unix):' /etc/group
```

Command syntax system ke manual se verify karo; case-sensitive names ko exact type karna zaruri hai.

### 15.6 Group delete karna — `groupdel`

```bash
groupdel unix
```

Agar group kisi user ka **primary group** hai, to system group delete karne se refuse kar sakta hai. Pehle affected user ka primary group kisi valid group par change karo:

```bash
usermod -g anothergroup username
groupdel unix
```

Delete karne se pehle ye check karo ki group ka use files, services, scripts ya applications mein to nahi ho raha. Group delete karna sirf command-success ka matter nahi; ownership aur access impact bhi review karna chahiye.

---

## 16. Day 7 command summary

```bash
# Current identity and sessions
whoami
who
w
id
id <user>

# Switch user
su <user>             # target identity, existing environment ka concept
su - <user>           # target user ka login environment
su                    # commonly root target
su -                  # root login-style shell
echo $SHLVL
exit

# User records
cat /etc/passwd
cat /etc/shadow
cat /etc/default/useradd
ls -la /etc/skel

# Create and verify user
useradd user1
tail -2 /etc/passwd
useradd -u 1500 -d /home/user2 -c "Comment" -s /bin/bash user2

# Modify and inspect user
usermod -c "New comment" -s /bin/bash user2
id user2

# Delete user — first inspect/transfer data
userdel user1
userdel -r user1

# Orphaned ownership search
find / -nouser -o -nogroup 2>/dev/null

# Groups
groups
groups <user>
cat /etc/group
groupadd UNIX
usermod -aG UNIX <user>     # add secondary group, preserve existing
usermod -G UNIX <user>      # may replace secondary group list
usermod -g UNIX <user>      # change primary group
groupmod -n unix UNIX
groupdel unix
```

Commands ko production machine par copy-paste karne se pehle `man` page, target username, backup aur expected effect verify karo. `userdel -r`, `usermod -G`, primary-group changes aur `groupdel` especially carefully handle karne chahiye.

---

## 17. Common mistakes aur revision points

1. Har task ke liye root account use karna.
2. `whoami`, `who`, `w` aur `id` ke roles ko mix karna.
3. `su user` aur `su - user` ko same samajhna.
4. `/etc/passwd` ke UID/GID/home/shell fields ka order bhoolna.
5. Ye assume karna ki `useradd` automatically password set kar deta hai.
6. User delete karte waqt home directory aur sensitive data verify na karna.
7. `userdel -r` ko bina backup/approval run karna.
8. Deleted UID reuse aur stale files se hone wale ownership issue ko ignore karna.
9. New account ke default source `/etc/default/useradd` ko check na karna.
10. `/etc/skel` mein secret information rakh dena.
11. `usermod -aG` mein `-a` omit karke existing secondary groups replace kar dena.
12. `-g` aur `-G` ka difference bhoolna.
13. Kisi user ka primary group bane hue group ko `groupdel` se delete karne ki koshish karna.
14. Group/file ownership change karne ke baad existing applications aur files ka impact verify na karna.

---

## 18. Self-check questions

1. User management aur least privilege ki zarurat kyu hoti hai?
2. Normal user ke roop mein kaam karna root ke roop mein kaam karne se safer kyu hai?
3. Root ki UID kya hoti hai?
4. `whoami`, `who`, `w` aur `id` mein practical difference kya hai?
5. `su user` aur `su - user` ke environment behavior mein kya difference hai?
6. `$SHLVL` kya batata hai?
7. `/etc/passwd` ke seven fields ka order likho.
8. `/etc/passwd` mein password field mein `x` kyu dikh sakta hai?
9. `/etc/default/useradd` aur `/etc/skel` ka role kya hai?
10. `useradd` aur `usermod` mein difference kya hai?
11. `userdel user1` aur `userdel -r user1` mein kya difference hai?
12. Deleted UID reuse se sensitive data leak kaise ho sakta hai?
13. `-nouser` aur `-nogroup` ka use kis tarah ke orphaned files dhoondhne mein hota hai?
14. Groups individual file permissions ko scalable kaise banate hain?
15. Primary aur secondary group mein kya difference hai?
16. `usermod -aG`, `usermod -G` aur `usermod -g` ka effect compare karo.
17. Kisi user ka primary group bane group ko directly delete kyu nahi kiya ja sakta?
18. Group membership ya user deletion change karne se pehle kaunse safety checks karne chahiye?

---

## 19. Final takeaway

Day 7 ka core message hai:

- User ko sirf required access do; unnecessary root privilege risk badhata hai.
- UID/GID ko samjhe bina Linux ownership aur permissions properly understand nahi hoti.
- `su -` target user ka login environment load karne ke liye use hota hai; normal `su` mein existing environment carry ho sakta hai.
- `/etc/passwd`, `/etc/shadow`, `/etc/default/useradd` aur `/etc/skel` user lifecycle ke important parts hain.
- User delete karte waqt home data, UID reuse aur orphaned files ka risk check karo.
- Groups ke through project access ko centrally manage karna individual permissions se practical hai.
- `-aG`, `-G` aur `-g` ka difference yaad rakhna zaruri hai.

Trainer Day 7 ke end mein **password management aur privileges** ko next class ka topic batate hain. Isliye abhi user/group lifecycle ka base clear hona chahiye; password-aging, password files aur privilege configuration ko agle session mein continue kiya jayega.
