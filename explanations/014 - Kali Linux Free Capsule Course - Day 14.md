# Day 14 — Kali Linux Capsule Course: `history`, Root Password Recovery, `sort` aur `uniq` (Hinglish Explanation)

**Source transcript:** `transcripts/014 - Kali Linux Free Capsule Course - Day 14 [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** Days 1–13 — Linux fundamentals, permissions, shell commands, packages aur variables
**Note:** Ye explanation Hindi original transcript ko samajh kar likhi gayi hai; ye line-by-line literal translation nahi hai. Auto-captions mein `history`, `HISTFILE`, `HISTSIZE`, GRUB, root-password recovery, `sort`, `uniq` aur pipe concepts kai jagah garbled mile. Context ke basis par intended commands aur safety notes restore karke simple Hinglish mein explain kiya gaya hai.

---

## 1. Day 14 ka focus

Day 14 Kali/Linux capsule course ke final content sessions mein se ek hai. Aaj ke main topics:

1. **`history` command** — previous shell commands dekhna aur repeat karna.
2. History variables, storage aur security implications.
3. Forgotten root password recovery ka authorized lab overview.
4. `sort` se lines/columns order karna.
5. `uniq` se adjacent duplicate lines remove karna.
6. Pipes se commands ko combine karna.

Trainer session ke end mein agle live course ke roop mein OSINT announce karte hain. Kali capsule course ka purpose beginner ke Linux fundamentals ko strong banana hai, na ki har advanced administration topic complete karna.

---

## 2. `history` command

Bash shell commands ko history list mein maintain kar sakti hai. Current shell history dekhne ke liye:

```bash
history
```

Output mein number aur command dikh sakti hai:

```text
  101  pwd
  102  ls -la
  103  cd /tmp
```

History se:

- previous command recall,
- repetitive typing reduce,
- troubleshooting steps review,
- shell session ka working context samajhna
possible hota hai.

### 2.1 Last N entries

```bash
history 10
```

Last 10 history entries show karne ka common pattern hai.

### 2.2 Arrow keys

Interactive terminal mein:

- Up arrow — previous command
- Down arrow — newer command

Ye `history` command run kiye bina quick recall ka easiest method hai.

### 2.3 Previous command repeat — `!!`

```bash
!!
```

Previous command ko repeat karta hai.

Example:

```bash
apt update
sudo !!
```

Agar pehle command permission denied hui, to `sudo !!` previous command ko `sudo` ke saath repeat karne ka common shortcut hai. Repeat karne se pehle command review karo, especially destructive commands ke liye.

### 2.4 Prefix se repeat — `!string`

```bash
!apt
```

History mein `apt` se start hone wali latest command repeat kar sakta hai. Agar matching command nahi hai, shell error de sakti hai.

### 2.5 Number se repeat — `!N`

```bash
!1634
```

History number `1634` wali command execute kar sakta hai. Number run karne se pehle displayed history line check karo; old command ka effect current directory/state mein different ho sakta hai.

### 2.6 Reverse interactive search — `Ctrl+R`

```text
Ctrl+R
```

Prompt par previous commands ke text se reverse search start hota hai. Search phrase type karo; matching command mil sakti hai. Again `Ctrl+R` se older matches cycle ho sakte hain, Enter se selected command run aur arrow key se edit karke run kar sakte ho.

---

## 3. History environment variables

Bash history ke behavior ko environment/shell variables control karte hain:

| Variable | Role | Common default/example |
|---|---|---|
| `HISTFILE` | History file ka name/path | `~/.bash_history` |
| `HISTSIZE` | Current shell memory mein kitni entries | `1000` common |
| `HISTFILESIZE` | Disk history file mein kitni entries retain | `1000` common |
| `HISTCONTROL` | Certain commands ko history mein save karne ka behavior | `ignorespace`/`ignoredups` possible |

Inspect:

```bash
echo "$HISTFILE"
echo "$HISTSIZE"
echo "$HISTFILESIZE"
echo "$HISTCONTROL"
```

Values distribution, shell configuration aur user profile par depend karte hain.

### 3.1 `HISTSIZE`

```bash
HISTSIZE=5000
```

Current shell ke in-memory history limit ko temporarily change kar sakta hai. Permanent setting ke liye user shell configuration, jaise `~/.bashrc`, mein export/assignment configure kar sakte ho:

```bash
export HISTSIZE=5000
export HISTFILESIZE=10000
```

Old entries limit cross hone par drop/overwrite ho sakti hain. History ko forensic-proof log samajhna galat hai.

### 3.2 `HISTFILE`

```bash
echo "$HISTFILE"
```

Aam Bash setup mein ye `~/.bash_history` ho sakta hai. Path change kiya ja sakta hai, lekin permissions aur privacy implications samjho.

---

## 4. History disk par kab likhi jati hai?

Trainer basic behavior explain karte hain ki current session ki history memory mein hoti hai aur logout/exit ke aas-paas history file mein write ho sakti hai.

Important nuance:

- Bash configuration `history -a`, `history -w`, `histappend` jaise options se write timing change kar sakti hai.
- Abrupt terminal kill ya crash se current session ki entries file mein save na ho sakti hain.
- Multiple terminals same history file ke saath work kar sakte hain.
- `~/.bash_history` complete real-time record guaranteed nahi hai.

Useful commands:

```bash
history -a   # current session ki new lines append karne ki koshish
history -w   # current history ko history file mein write
```

Forensics mein shell history useful lead hai, lekin sole source of truth nahi. Process accounting, audit logs, terminal logs, filesystem timestamps aur other telemetry bhi review karni pad sakti hai.

---

## 5. Ek command ko history se hide karna

Kuch Bash configurations mein leading space wali command history mein save nahi hoti:

```bash
 date
```

Yahan `date` se pehle ek space hai. Ye behavior tab work karta hai jab `HISTCONTROL` mein `ignorespace`/related option enabled ho:

```bash
echo "$HISTCONTROL"
```

### 5.1 Security implication

Ye convenience/privacy feature hai, security guarantee nahi. Agar koi user sensitive command ko leading space se hide karta hai, to:

- history file mein line absent ho sakti hai,
- lekin process/audit logs, shell telemetry, terminal recording ya system logs mein evidence ho sakta hai,
- command result/filesystem changes separately visible ho sakte hain.

Defensive side par `HISTCONTROL` ko audit strategy ka replacement mat samjho.

### 5.2 Duplicate commands

`HISTCONTROL=ignoredups` ya `ignoreboth` repeated commands ko suppress kar sakta hai. Exact behavior shell settings par depend karega.

---

## 6. History clear/delete karna

Current shell history clear karne ka Bash command:

```bash
history -c
```

Specific entry delete karna:

```bash
history -d 17
```

File se old history remove karni ho to shell behavior/version ke hisaab se:

```bash
history -c
history -w
```

> Ye commands current shell/history file behavior par depend karte hain. History clear karna activity ko system-wide erase nahi karta; audit logs, backups aur other evidence separately exist kar sakte hain.

Production incident mein history delete karne ke bajay evidence-preservation/IR policy follow karo. Apni disposable lab mein hi history options test karo.

---

## 7. Forgotten root password recovery — important scope warning

Trainer promised root-password recovery demonstration continue karte hain. Ye section sirf:

- apni owned machine,
- authorized lab VM,
- documented recovery process

ke liye hai.

Kisi aur computer par physical access se password reset karna unauthorized access ho sakta hai.

### 7.1 Distribution difference

Transcript Debian-based systems — Kali, Debian, Ubuntu — ke GRUB-style recovery flow ke context mein hai. Fedora/Red Hat/CentOS systems mein boot process, SELinux labels, initramfs aur recovery steps different ho sakte hain.

> Kali/Debian procedure ko Fedora/Red Hat par blindly apply mat karo. Wrong boot parameter se system boot issue ya data risk ho sakta hai.

### 7.2 High-level recovery flow

Legacy/GRUB lab setup mein broad flow:

1. Machine power on karo.
2. GRUB menu display hone par entry select karo.
3. Edit mode ke liye `e` press karo.
4. `linux`/`linuxefi` se start hone wali kernel line identify karo.
5. Existing read-only/quiet boot arguments ko carefully review karo.
6. Authorized recovery environment ke liye writable root shell parameter add/adjust karo.
7. Boot karo.
8. Root filesystem writable hai ya nahi verify karo.
9. `passwd` se authorized password reset karo.
10. Normal init/reboot ke through system ko safely restart karo.

Transcript ka example Debian/Kali-style line ko conceptual form mein dikhata hai:

```text
# before (example only)
linux /boot/vmlinuz-... root=UUID=... ro quiet splash

# recovery example discussed in class
linux /boot/vmlinuz-... root=UUID=... rw init=/bin/bash
```

Exact kernel line, bootloader version aur encrypted-disk setup ke hisaab se details change ho sakti hain. Live recovery se pehle backup/console access confirm karo.

### 7.3 `init=/bin/bash` ka meaning

`init=/bin/bash` kernel ko normal init/system manager ke badle Bash ko initial process/PID 1 start karne ko bolta hai. Isse login screen ke bina root-level maintenance shell mil sakti hai.

`rw` ka intent root filesystem ko writable mount karna hai, taaki password database update save ho sake.

### 7.4 Root filesystem verify karna

Recovery shell mein:

```bash
mount
```

Root `/` mount entry par `ro` (read-only) hai ya `rw` (read-write), check karo. Agar authorized recovery environment mein root read-only hai:

```bash
mount -o remount,rw /
```

Mount output aur filesystem state verify kiye bina password command ko success samajhna unsafe hai.

### 7.5 Password reset aur restart

```bash
passwd
```

New password set karne ke baad normal init/reboot process use karo. Transcript example:

```bash
exec /sbin/init
```

Kuch environments mein `reboot -f`, `systemctl reboot` ya VM power-cycle different result de sakte hain. PID 1 recovery shell ko abruptly kill karne ke bajay documented procedure follow karo.

### 7.6 Physical security lesson

Agar attacker ko physical access mil jaye aur boot parameters edit kar sake, to login password alone machine ko protect nahi karta.

Controls:

- GRUB/bootloader password
- BIOS/UEFI administrator password
- External-media boot restriction
- Full-disk encryption
- Secure physical server room/device access
- Recovery console access control

| Defence | Kis bypass ko reduce karta hai |
|---|---|
| GRUB password | Kernel boot parameter edit |
| BIOS/UEFI password | Boot order/firmware change |
| Full-disk encryption | Offline filesystem read/write |
| Physical access control | Machine tak direct access |

> Full-disk encryption ke bina live ISO se offline file access possible ho sakta hai. Recovery process ko secure karna system security ka part hai.

---

## 8. `sort` command

`sort` text lines ko order mein arrange karta hai:

```bash
sort filename.txt
```

Default sort lexical/alphabetical behavior use karta hai. Original file usually in-place change nahi hoti; output screen par aata hai. Save karna ho to redirect:

```bash
sort filename.txt > sorted.txt
```

### 8.1 Column/key sorting

```bash
sort -k1 filename.txt
sort -k2 filename.txt
```

`-k` sort key/field position specify karta hai. Whitespace-separated data mein column numbering context ke hisaab se samjho.

### 8.2 Reverse

```bash
sort -r filename.txt
```

Descending/reverse order.

### 8.3 Numeric sort

```bash
sort -n numbers.txt
```

String/lexical order aur numeric order alag hote hain:

```text
1
10
2
```

Lexical order mein `10` `2` se pehle aa sakta hai; `-n` numeric value ke according sort karta hai.

### 8.4 Unique sort

```bash
sort -u filename.txt
```

Sort ke saath duplicate lines remove karne ka compact form hai.

### 8.5 Mixed data par caution

Real data mein delimiter, header, numeric column aur locale matter karte hain. Advanced key options, delimiter (`-t`) aur numeric flags use karne se pehle sample output test karo.

---

## 9. `uniq` command

`uniq` duplicate lines ko remove karne ke liye use hota hai, lekin important condition hai:

> **`uniq` sirf adjacent/consecutive duplicate lines remove karta hai.**

Input:

```text
apple
banana
apple
```

Direct `uniq` se dono `apple` lines remove nahi hongi, kyunki adjacent nahi hain.

### 9.1 Correct pipeline

```bash
cat tmp.txt | sort | uniq
```

Steps:

1. `cat tmp.txt` contents output karta hai.
2. Pipe `|` output ko `sort` ka input banata hai.
3. `sort` identical lines ko adjacent/group karta hai.
4. Second pipe sorted output ko `uniq` ka input banata hai.
5. `uniq` consecutive duplicates ko one line mein reduce karta hai.

Shorter equivalent:

```bash
sort -u tmp.txt
```

Output save karna:

```bash
sort tmp.txt | uniq > cleaned.txt
```

### 9.2 Count duplicates

Useful extension:

```bash
sort tmp.txt | uniq -c
```

Har unique line ke saamne count show kar sakta hai.

### 9.3 Case sensitivity

`uniq` by default case-sensitive ho sakta hai:

```text
Apple
apple
```

different lines treat ho sakti hain. Case-insensitive grouping chahiye to sort aur uniq flags/locales carefully configure karo, example:

```bash
sort -f tmp.txt | uniq -i
```

Exact locale behavior verify karo.

---

## 10. Pipe recap

Pipe symbol:

```bash
|
```

ka meaning:

> **Pehli command ka standard output doosri command ka standard input ban jata hai.**

Example:

```bash
cat tmp.txt | sort
```

`sort` ko filename argument nahi diya gaya; usne data pipe se read kiya.

Day 3 ke redirection concepts se connection:

- `>` output ko file mein write karta hai.
- `>>` output append karta hai.
- `<` file ko input banata hai.
- `|` ek command ka output next command ka input banata hai.

Long pipeline debug karne ke liye stages alag test karo:

```bash
cat tmp.txt
cat tmp.txt | sort
cat tmp.txt | sort | uniq
```

---

## 11. Day 14 practical workflows

### 11.1 Command history review

```bash
history 20
Ctrl+R
```

### 11.2 Log lines sort and deduplicate

```bash
sort access.log | uniq > unique-lines.log
```

### 11.3 Frequency count

```bash
sort access.log | uniq -c | sort -nr > frequency.txt
```

Ye pipeline identical lines ko count karke count ke descending order mein arrange kar sakti hai. Actual log field extraction ke liye `awk`, `cut` ya `grep` add kar sakte ho.

### 11.4 Package/file inventory

```bash
dpkg -L package-name | sort | uniq
```

Day 12 ke package management ke saath direct connection.

---

## 12. Day 14 command summary

```bash
# History
history
history 10
!!
!prefix
!1634
history -c
history -d 17
history -a
history -w
Ctrl+R

# History variables
echo "$HISTFILE"
echo "$HISTSIZE"
echo "$HISTFILESIZE"
echo "$HISTCONTROL"

# Authorized Debian/Kali recovery overview
# GRUB edit -> authorized rw recovery shell -> verify mount -> passwd
mount
mount -o remount,rw /
passwd
exec /sbin/init

# Sort
sort file.txt
sort -r file.txt
sort -n numbers.txt
sort -k2 file.txt
sort -u file.txt

# Uniq and pipe
sort file.txt | uniq
sort file.txt | uniq -c
sort -u file.txt
cat file.txt | sort | uniq > cleaned.txt
```

---

## 13. Common mistakes aur safety points

1. Shell history ko complete/audit-proof command record samajhna.
2. Current session history file mein immediately written assume karna.
3. Leading-space history suppression ko every shell par guaranteed samajhna.
4. History clear karke audit evidence erase ho gaya samajhna.
5. Root password recovery steps ko wrong distribution par blindly apply karna.
6. Bootloader edit se pehle backup/console/recovery plan na rakhna.
7. Root filesystem read-only hote hue `passwd` success expect karna.
8. Physical access controls aur full-disk encryption ignore karna.
9. `sort` ko numeric data par `-n` ke bina use karna.
10. `uniq` ko unsorted/non-adjacent duplicates remove karne wala samajhna.
11. Pipeline ko stages mein debug na karna.
12. `sort -u` output ko original file mein automatically saved samajhna.
13. `history -d`/`history -c` ko system-wide logs delete karne wala samajhna.
14. Destructive recovery/password changes ko unauthorized machine par try karna.

---

## 14. Self-check questions

1. `history` command ka basic purpose kya hai?
2. `!!`, `!prefix`, `!number` aur `Ctrl+R` ka use compare karo.
3. `HISTFILE`, `HISTSIZE`, `HISTFILESIZE` aur `HISTCONTROL` kya control karte hain?
4. Current shell history disk par kab write ho sakti hai? `history -a`/`-w` ka role kya hai?
5. Leading-space history behavior kaunse setting par depend karta hai?
6. History clear karne ke baad bhi system mein evidence kahan reh sakta hai?
7. Root password recovery procedure kis family ke systems ke context mein hai?
8. `init=/bin/bash` aur `rw` boot parameters ka conceptual role kya hai?
9. Recovery shell mein `mount` kyu check karte hain?
10. Physical access se bachne ke four controls likho.
11. `sort -r`, `sort -n`, `sort -k2` aur `sort -u` ka meaning batao.
12. `uniq` sirf adjacent duplicates kyu remove karta hai?
13. `sort file | uniq` aur `sort -u file` ka relationship kya hai?
14. Pipe standard input/output ke saath kaise work karta hai?
15. `sort access.log | uniq -c | sort -nr` pipeline ko step by step explain karo.
16. Output file save karne ke liye redirection kyu chahiye?

---

## 15. Kali capsule course ka conclusion

Day 14 ke saath course ke primary Linux fundamentals complete hote hain:

- files/directories aur filesystem hierarchy,
- redirection aur pipelines,
- text-processing commands,
- users/groups aur privileges,
- standard/advanced file permissions,
- package management,
- variables, globbing aur shell control,
- history aur common text utilities.

Trainer ka next announcement **OSINT — Open Source Intelligence** course ka hai. OSINT ko general-purpose information gathering skill ke roop mein present kiya jata hai, jisme technical aur non-technical learners dono participate kar sakte hain.

---

## 16. Final takeaway

- `history` productivity shortcut bhi hai aur security/forensics artifact bhi.
- History file complete real-time record nahi hoti; shell settings aur write timing matter karte hain.
- Root-password recovery sirf owned/authorized Debian/Kali lab par practice karo; physical access security ko seriously lo.
- `sort` lines/order/keys ko arrange karta hai.
- `uniq` adjacent duplicates remove karta hai; duplicates group karne ke liye pehle `sort` useful hai.
- Pipe ek command ka output next command ka input banata hai.
- `sort | uniq`, `sort -u` aur count pipelines log/data analysis mein practical hain.

Kali Linux capsule course ka broader lesson hai: commands ko isolated tricks ki tarah nahi, balki users, permissions, processes, files aur shell automation ke connected system ki tarah samjho.
