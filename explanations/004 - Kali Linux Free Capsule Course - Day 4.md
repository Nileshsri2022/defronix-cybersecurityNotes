# Day 4 — Kali Linux Capsule Course: File Descriptor Recap + head/tail/less/tac/wc + `sed` Basics (Hinglish Explanation)

**Source transcript:** `transcripts/004 - Kali Linux Free Capsule Course - Day 4 [ Hindi ].hi-orig.srt`  
**Note:** Ye explanation Hindi original transcript ko samajh kar banaya gaya hai. Auto-captions mein `रीकैप`, `आई नोट टेबल`, `सब्सीट्यूट`, `लेटर`, `वर्क/ब्लू सी`, `ली कमांड` jaise garbled words mile; intended meaning **recap**, **inode table**, **substitute**, **less**, aur **wc** liya gaya hai.

---

## 1. Day 4 ka flow — pehle recap, phir text-view commands, phir `sed`

Trainer start mein kehte hain ki Day 3 ka **file descriptor** concept naya tha aur kuch students ko clear nahi hua hoga. Isliye Day 4 ke first 10–15 minute quick recap hoga, phir commands continue hongi.

Day 4 ke 3 major parts:

1. **File descriptor recap** — process, inode table, global file table, file descriptor table aur stdin/stdout/stderr ka connection.
2. **Text output dekhne ki commands** — `head`, `tail`, `less`, `more`, `tac`, `wc`.
3. **`sed` command ka intro** — stream editor, line-number based printing aur substitution/search-replace.

Trainer bolte hain: pahle concepts clear karo, phir Day 3 ke redirection practical dobara karo; uske baad doubt nahi aayega.

---

## 2. File descriptor recap — kernel ko open files track kyu karni padti hain?

Jab bhi system mein koi process start hoti hai, wo internally libraries, config files, data files ya devices ko use karti hai. Linux mein in sabko **open files** ki tarah consider kiya jata hai.

Kernel OS ka sabse powerful component hai. Agar kernel ko pata hi nahi ki system mein kaunsi files open hain, kaun kis process ke saath judi hai, to control possible nahi. Isliye kernel ko open files ko **monitor/track** karna hota hai.

Is tracking ke liye Linux/Unix file descriptor concept use karta hai.

Easy definition:

> File descriptor ek non-negative integer number hota hai jo process ke point of view se kisi open file/data-source ko identify karta hai.

Windows side par similar idea ko **file handles** se relate kar sakte ho.

---

## 3. Teeno tables ka simple relation

Trainer board par 3 tables discuss karta hai. Ye OS internals bohot bada topic hai, lekin basic working model ye hai:

### 3.1 Inode table

Har file ka ek unique **inode number** hota hai. Inode table entry ke andar file ka metadata hota hai, jaise:

- file ka size
- timestamps
- owner/group
- permissions
- file ka actual data storage location/filesystem address
- file type related info

Dhyan do: inode mein usually file ka **name** nahi hota; name directory entry mein hota hai, actual metadata inode mein.

### 3.2 Global file table

Jab file open hoti hai, kernel global file table mein entry banata hai. Ye table open file instance ko represent karti hai aur inode table tak reference rakhti hai.

Trainer ke 3 points yaad rakho:

1. **Create entry in global file table**
2. **Provide the location of the entry**
3. Process ko us entry tak pahunchne ka reference/descriptor dena

### 3.3 File descriptor table

Ye **per-process** table hoti hai. Matlab har process ki apni FD table hoti hai. Ye hidden table hoti hai jo sirf kernel update karta hai; process apni table directly modify nahi karti.

Flow simplified:

```text
Process
  └─ file descriptor number (0,1,2,3...)
        └─ points to Global File Table entry
              └─ points to Inode Table entry
                    └─ points to actual file data on filesystem
```

Isliye jab hum `cat file`, `date > out`, ya `cmd 2> /dev/null` karte hain, background mein FD/streams ka concept kaam kar raha hota hai.

---

## 4. First 3 FD entries — redirection ka real base

Process create hote hi first 3 entries reserved/fixed hoti hain:

| FD | Stream | Default device in class | Redirect symbol |
|---:|---|---|---|
| **0** | `stdin` | keyboard | `<` / `0<` |
| **1** | `stdout` | screen/terminal | `>` / `1>` |
| **2** | `stderr` | screen/terminal | `2>` |

Day 3 ka practical ab is FD model se link hota hai:

- `date > out.txt` → stdout (FD 1) ko file mein bhejo
- `cat < file` → file ko stdin (FD 0) banao
- `cat hello 2> /dev/null` → stderr (FD 2) ko discard device mein bhejo
- `cmd > run.log 2>&1` → stdout file mein, phir stderr bhi stdout ke destination par

Trainer kehte hain: file descriptor concept boring lag sakta hai, lekin iske bina redirection sirf rat-ta hua lagta hai. Ek baar FD clear ho gaya to `>`, `<`, `2>`, `2>&1` sab logical lagne lagte hain.

---

## 5. Text output ka controlled viewing — `cat` hamesha enough nahi

`cat` poora content ek saath screen par daal deta hai. Agar file 1000+ lines ki ho, to scroll karna time waste hota hai. Isliye hum output ko control karke dekhte hain.

Linux admin workflow trainer batate hain:

1. **Step 1:** pehle single command se kaam hone ki koshish karo.
2. **Step 2:** same command ke flags/options se kaam ho jaye to best.
3. **Step 3:** agar kaam na ho, tab commands ko pipe `|` se jodo.

---

## 6. `head` — file/output ki top lines

`head` file ke top/beginning lines dikhata hai.

```bash
head /etc/passwd
```

Default: top 10 lines.

Specific number:

```bash
head -n 15 /etc/passwd
head -n 5 /etc/passwd
```

Command output ke upar bhi pipe se use kar sakte ho:

```bash
lscpu | head -n 8
```

Matlab: `lscpu` ka poora output lene ke bajaye sirf starting 8 lines dekh lo.

---

## 7. `tail` — file/output ki bottom lines

`tail` file ke end/bottom lines dikhata hai.

```bash
tail /etc/passwd
```

Default: last 10 lines.

Specific number:

```bash
tail -n 5 /etc/passwd
tail -n 15 /var/log/syslog
```

Logs mein `tail` bahut common hai kyunki latest events mostly file ke end mein hote hain.

---

## 8. `less` — bada file page-by-page padhna

`less` text file ko page-by-page view karne ke liye best hai.

```bash
less demo.txt
```

Transcript ke important keys:

| Key | Kaam |
|---|---|
| `Down Arrow` | line-by-line neeche jao |
| `Up Arrow` | line-by-line upar jao |
| `Page Down` | ek page neeche |
| `Page Up` | ek page upar |
| `/pattern` | top-to-bottom search karo |
| `n` | next match par jao |
| `?pattern` | bottom-to-top search karo |
| `End` | file ke end mein jao |
| `Home` | file ke start/top mein jao |
| `q` | quit/exit |

Example: `/etc` mein `system` search karna ho to `less` open karke `/system` dabao; next match ke liye `n`. Backward direction mein dhoondhna ho to `?system`.

`more` bhi similar pager hai; trainer bolte hain use khud practice karo kyunki basic idea `less` jaisa hi hai.

---

## 9. `tac` — `cat` ka reverse

`tac` file ko bottom-to-top dikhata hai. Name bhi `cat` ka reverse hai.

```bash
tac /etc/passwd
```

Kaam kab aata hai? Jab aapko file ka latest log bottom mein hai aur reverse order mein quickly dekhna ho. Logs ke saath `tac`/`tail` ka combination useful ho sakta hai.

---

## 10. `wc` — lines, words aur characters count

`wc` = word count.

```bash
wc /etc/passwd
```

Default output ke 3 numbers hote hain:

```text
lines  words  characters  filename
```

Transcript example mein file ke andar 59 lines, 97 words aur 599 characters jaise counts dikhaye gaye (exact numbers demo file ke hisaab se the).

Flags:

```bash
wc -l file     # only lines
wc -w file     # only words
wc -c file     # only characters/bytes
```

Important clarification: `wc` command ke options operate nahi karti; wo input stream/file ka count karti hai. Agar kisi command ka output count karna hai, pipe do:

```bash
lscpu | wc
lscpu | wc -l
```

Trainer ye bhi batate hain ki command combine karne ka time tab aata hai jab single command + options se kaam na ho.

---

## 11. Output filtering/manipulation series — `sed` ka intro

Trainer announce karte hain ki ab ek important command series shuru hogi jisse kisi bhi output ke saath fast filtering/manipulation kar sakte ho. Is series mein stream/text processing commands aayengi; Day 4 ka start hai **`sed`**.

`sed` = **stream editor**.

Basic syntax:

```bash
sed [options] 'action' filename
```

Important nature:

- `sed` line-by-line kaam karta hai.
- Normal output screen par aata hai; original file tab change hoti hai jab `-i` use karo.
- `-n` ke saath hum sirf wahi print karte hain jo `p` action se explicit bola jaye.

Transcript mein trainer initially sed ke use batata hai: printing, deleting after line numbers, substitution. Aaj focus printing aur substitution par hai.

---

## 12. `sed` se specific lines print karna

`/etc/passwd` jaise file par examples:

### Sirf first line print

```bash
sed -n '1p' /etc/passwd
```

Agar `-n` na do, to sed normal behaviour mein matched print ke saath baaki lines bhi repeat kar sakta hai; isliye controlled printing ke liye `-n '...p'` pattern use hota hai.

### Line 1 aur line 5 dono print

```bash
sed -n '1p;5p' /etc/passwd
```

Semicolon `;` actions ko separate karta hai.

### Range of lines print

```bash
sed -n '3,7p' /etc/passwd
```

Matlab line 3 se 7 tak print karo.

### Last line print

```bash
sed -n '$p' /etc/passwd
```

`$` ka matlab last line.

### First aur last line dono

```bash
sed -n '1p;$p' /etc/passwd
```

---

## 13. `sed` substitution — search and replace on screen

Substitution ka basic pattern:

```bash
sed 's/old/new/' file
```

Example transcript style: `/etc/passwd` mein `root` ko screen par `sachin` se replace karke dikhana.

```bash
sed 's/root/sachin/' /etc/passwd
```

Important: ye command original file change nahi karti; output screen par modified dikhata hai.

Default behaviour: bina `g` ke substitution pattern ka **first occurrence per line** replace karta hai.

Global replace per line:

```bash
sed 's/root/sachin/g' /etc/passwd
```

`g` = global — us line ke saare matches replace.

Linux/sed case-sensitive hote hain; agar file mein `nologin` hai aur aap `NoLogin` search karoge, match nahi hoga.

---

## 14. Specific line ya specific occurrence par substitution

### Sirf line 7 par substitution

```bash
sed '7s/nologin/sachin/' /etc/passwd
```

Ya line 7 ke saare matches:

```bash
sed '7s/nologin/sachin/g' /etc/passwd
```

### Second occurrence replace

GNU sed mein number flags se occurrence choose kar sakte ho:

```bash
sed 's/root/sachin/2' /etc/passwd
```

Ye per-addressed-line second match ko target karta hai. Agar second occurrence onwards sab replace karne hon, GNU sed supports `2g` style usage, but beginner ke liye pehle `g` aur line-addressing clear hona chahiye.

### Multiple substitutions

Multiple expressions ko `-e` se de sakte ho:

```bash
sed -e 's/root/sachin/g' -e 's/nologin/patron/g' sample.txt
```

Ye screen output mein dono replacements karega.

---

## 15. Permanent change — `-i` use karne se pehle warning

Agar change original file ke andar permanently karna hai:

```bash
sed -i 's/nologin/patron/g' sample.txt
```

Transcript ka strong advice:

> Pehle command ko on-screen run karke dekho. Jab output sahi lage, tab `-i` lagao. Direct file mein edit mat karo, warna original content galat ho sakta hai aur future mein problem aa sakti hai.

Safety workflow:

```bash
# Step 1: screen test
sed 's/nologin/patron/g' sample.txt | less

# Step 2: jab output sahi lage
sed -i 's/nologin/patron/g' sample.txt
```

Production ya important config par `-i` se pehle backup lena best practice hai:

```bash
cp sample.txt sample.txt.bak
```

---

## 16. Day 4 ke common mistakes

1. `head`/`tail` default 10 lines yaad na rakhna.
2. `less` ke andar stuck ho jana — exit key `q` hai.
3. `wc -c` ko sirf “characters” samajhna; bytes/characters locale par depend kar sakta hai.
4. `wc` ko kisi command ke options par lagane ki sochna; output count ke liye pipe use karo.
5. `sed -n '1p'` mein `-n` bhool jana, phir duplicate output dekh kar confuse hona.
6. `sed 's/old/new/'` ko permanent edit samajhna — ye default screen output hai.
7. Case sensitivity ignore karna — `root`, `Root`, `ROOT` same nahi.
8. `-i` directly production/config file par chala dena bina screen test/backup ke.

---

## 17. Final takeaway

Day 4 mein teen cheezein solid honi chahiye:

1. **FD model clear** — process FD number use karta hai; kernel global file table/inode table ke saath actual file track karta hai; first 3 FDs stdin/stdout/stderr hain.
2. **Viewing commands** — bade text output ko `head`, `tail`, `less`, `tac` aur `wc` se control karo.
3. **`sed` power start** — line-number based printing (`-n '1p'`, ranges, `$`) aur substitution (`s/old/new/`, `g`, line-address, `-i`) se text manipulate karna.

Trainer ka bottom line: pehle on-screen test karo, phir file modify karo. Commands ratne se zyada, output ka flow samajhna important hai — stdin se input, stdout/ stderr ka separation, aur file/table ke concept se redirection connect hota hai.
