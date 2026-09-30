# Day 13 — Kali Linux Capsule Course: Variables, `export` aur File Globbing (Hinglish Explanation)

**Source transcript:** `transcripts/013 - Kali Linux Free Capsule Course - Day 13 [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** Day 12 — package management, shell operators aur command-line workflow
**Note:** Ye explanation Hindi original transcript ko samajh kar likhi gayi hai; ye line-by-line literal translation nahi hai. Auto-captions mein shell variables, environment variables, `PATH`, `PS1`, `export`, `source`, `set`, `unset` aur globbing patterns kai jagah garbled mile. Context ke basis par intended concepts restore karke simple Hinglish mein explain kiya gaya hai.

---

## 1. Day 13 ka focus

Aaj ke do main topics hain:

1. **Shell variables aur environment variables**
2. **File globbing** — patterns ke through filenames generate/search karna

Trainer variables ko programming aur shell automation se connect karte hain. Phir `$PATH`, `$PS1`, shell hierarchy, `export`, persistence files, `set`/`unset` aur globbing ke `*`, `?`, `[ ]` patterns explain kiye jate hain.

---

## 2. Variable kya hota hai?

Variable ko ek labelled box ki tarah imagine karo:

- Box ke andar data/value rakha hai.
- Box ka label variable name hai.
- Name se value ko baad mein reference kar sakte ho.

Medical shop analogy:

- Labelled box = variable
- Medicine = stored value/data
- Label padhkar exact box access karna = variable ko reference karna

Shell example:

```bash
practice=sachin
echo "$practice"
```

Output:

```text
sachin
```

### 2.1 Assignment aur reference

```bash
name=value       # assignment: value variable mein store
 echo "$name"   # reference: value read
```

Command prompt par accidental leading space avoid karo; example mein `echo` se pehle space sirf explanation formatting ke liye nahi, command ka part nahi hona chahiye.

Formal/braced reference:

```bash
echo "${practice}"
```

Braces tab useful hote hain jab variable name ke immediately baad text attach karna ho:

```bash
name=Kali
echo "${name}Linux"
```

Without braces shell `nameLinux` ko variable name samajh sakta hai.

---

## 3. Variable naming rules

### 3.1 `=` ke around spaces nahi

Bash assignment mein spaces allowed nahi:

```bash
practice=sachin       # correct
practice = sachin     # wrong: shell ise command/arguments samjhega
```

Correct pattern:

```text
NAME=value
```

### 3.2 Name ka first character

Variable name letter ya underscore se start karna chahiye:

```bash
practice=value        # valid
_practice=value       # valid
2practice=value       # invalid
```

Baad mein letters, numbers aur underscores use kiye ja sakte hain:

```bash
user2_name=value
```

Special characters aur hyphen variable names mein avoid karo.

### 3.3 Uppercase/lowercase convention

Trainer system-defined variables ko uppercase aur user-defined variables ko lowercase naming convention ke roop mein discuss karte hain:

```bash
HOME=/root
PATH=/usr/bin:/bin
my_name=sachin
```

Ye convention readability ke liye hai, hard rule nahi. Shell technically lowercase/uppercase names ko alag variables treat karta hai.

---

## 4. `echo` ka role

`echo` value ko output par print karta hai:

```bash
name=Kali
echo $name
echo "$name"
echo "User: ${name}"
```

Double quotes spaces aur special characters ko preserve karne mein help karti hain. Variables use karte waqt quoted expansion safer default hai:

```bash
echo "$HOME"
```

Variable assign karte waqt `$` nahi lagta; reference karte waqt lagta hai:

```bash
name=Kali       # assignment
 echo "$name"  # reference
```

---

## 5. Variables scripts mein kyu useful hain?

Agar same value script mein 50 ya 1000 places par use ho rahi ho, to direct value repeat karna maintenance problem ban sakta hai.

### Without variable

- Har occurrence manually edit karni padegi.
- Ek occurrence miss ho sakti hai.
- Typing inconsistency aa sakti hai.

### With variable

```bash
base_dir=/opt/security-lab
```

Script mein:

```bash
mkdir -p "$base_dir/logs"
cp report.txt "$base_dir/reports/"
```

Base path change karna ho to ek assignment update karo. Script readable, reusable aur maintainable hoti hai.

---

## 6. Environment variables

Shell process ek environment ke saath run hota hai. Environment variables woh values hain jo shell aur child processes ke behavior ko configure kar sakti hain.

Common variables:

| Variable | Meaning |
|---|---|
| `$HOME` | Current user ka home directory |
| `$USER` | Current username |
| `$HOSTNAME` | Machine hostname |
| `$SHELL` | Default/login shell path |
| `$PWD` | Present working directory |
| `$PATH` | Commands search karne wali directories |
| `$PS1` | Primary shell prompt format |

Inspect:

```bash
echo "$HOME"
echo "$USER"
echo "$HOSTNAME"
echo "$SHELL"
echo "$PWD"
echo "$PATH"
echo "$PS1"
```

`env` ya `printenv` se environment variables list kar sakte ho:

```bash
env
printenv HOME
```

Environment variable aur normal shell variable ka key difference inheritance/export mein aata hai.

---

## 7. `$PATH` — shell command kaise dhoondhta hai?

Question: aap `passwd` type karte ho aur shell executable locate kar leti hai. Kaise?

Answer: `$PATH` colon-separated directories ki list rakhta hai:

```bash
echo "$PATH"
```

Example:

```text
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

### 7.1 Search process

1. Shell `$PATH` ka first directory check karti hai.
2. Command executable wahan milti hai to run hoti hai.
3. Nahi milti to next directory check hoti hai.
4. Kahi nahi milti to `command not found` output aa sakta hai.

Command location inspect:

```bash
command -v passwd
type -a passwd
```

### 7.2 Full path ka use

Agar binary `$PATH` mein nahi hai:

```bash
mytool
# command not found

/opt/tools/mytool
# full path se run ho sakta hai
```

Current directory ko `$PATH` mein default se include na karna security practice hai. Isi liye local script run karne ke liye:

```bash
./script.sh
```

likhte hain, sirf `script.sh` nahi.

### 7.3 `$PATH` security risk

Agar attacker-controlled writable directory ko `$PATH` ke start mein add kar diya jaye, to same-name malicious executable legitimate command se pehle run ho sakta hai. Isliye:

- current directory ko blindly `$PATH` mein add na karo,
- writable directories ko `$PATH` mein avoid karo,
- scripts mein critical commands ke liye safe path/absolute path consider karo.

---

## 8. `$PS1` — shell prompt customize karna

`PS1` primary shell prompt ko control karta hai:

```bash
echo "$PS1"
```

Prompt mein username, hostname, current directory, date/time ya literal symbols show kiye ja sakte hain. Temporary test:

```bash
export PS1='lab> '
```

Prompt custom change ho jayega. Ye sirf current shell/process ke liye temporary hai.

### 8.1 Prompt customize karte waqt caution

Prompt ko aisa mat banao ki normal user/root distinction hide ho jaye. Security work mein current identity visible rehni chahiye.

Common prompt information:

- `\u` — username
- `\h` — hostname
- `\w` — current working directory
- `\$` — normal user ke liye `$`, root ke liye `#`

Example:

```bash
export PS1='\u@\h:\w\$ '
```

Permanent prompt customization ke liye `~/.bashrc` mein line add ki ja sakti hai.

---

## 9. Shell hierarchy aur `export`

### 9.1 Normal variable child shell mein kyu nahi milti?

```bash
var1=test
echo "$var1"

bash
echo "$var1"
```

Parent shell mein `var1` set hai. Naya `bash` child shell open karne par normal non-exported shell variable child ko inherit nahi hoti. Isliye second `echo` blank ho sakta hai.

### 9.2 `export` ka solution

```bash
var1=test
export var1

bash
echo "$var1"
```

Ya directly:

```bash
export var1=test
```

Exported variable child process ke environment mein pass hoti hai.

Current exported variables dekhne ke liye:

```bash
export -p
```

### 9.3 Parent ko child change nahi kar sakta

Environment inheritance one-way hota hai:

```text
parent shell -> child shell
```

Child ko exported value mil sakti hai, lekin child mein variable change karne se parent shell automatically update nahi hota. `source` current shell mein file commands run karne ke liye use hota hai.

---

## 10. Variable persistence ke four levels

| Level | Method | Scope | New child shell? | Logout ke baad? |
|---:|---|---|---|---|
| 1 | `var=value` | Current shell | No | No |
| 2 | `export var=value` | Current + child processes | Yes | No |
| 3 | `~/.bashrc` | Specific user | Yes, new interactive shell | Yes |
| 4 | `/etc/profile` | System-wide users | Yes | Yes |

### 10.1 Current shell only

```bash
var1=value
```

Logout ya shell close hone par value gone.

### 10.2 Current session + child processes

```bash
export var1=value
```

Child shells/processes inherit kar sakte hain, lekin logout ke baad permanent nahi.

### 10.3 User-specific permanent — `~/.bashrc`

```bash
vim ~/.bashrc
```

End mein:

```bash
export LAB_HOME=/home/kali/lab
```

Current shell mein immediately load karne ke liye:

```bash
source ~/.bashrc
```

Alternative:

```bash
. ~/.bashrc
```

`source` ka meaning hai current shell mein file ke commands read/execute karna. Naya terminal open karne par `.bashrc` automatically load ho sakta hai, shell type/configuration par depend karta hai.

### 10.4 Global — `/etc/profile`

System-wide environment ke liye:

```bash
sudo vim /etc/profile
```

Add:

```bash
export COMPANY_TOOL=/opt/company-tool
```

Ye all users ko affect kar sakta hai. Global file edit karne se pehle backup aur syntax review karo.

### 10.5 `.bashrc` backup

```bash
cp ~/.bashrc ~/.bashrc.backup
```

Bad syntax `.bashrc` mein new interactive shell ko errors de sakti hai. Recovery ke liye existing shell open rakho aur backup restore karo:

```bash
cp ~/.bashrc.backup ~/.bashrc
source ~/.bashrc
```

---

## 11. `set` aur `unset`

Shell state inspect karne ke liye:

```bash
set
```

`set` shell variables, functions aur shell settings ki large listing de sakta hai.

Variable remove karna:

```bash
unset var1
```

Verify:

```bash
echo "$var1"
```

`unset` current shell se variable remove karta hai. Agar variable profile file mein defined hai, to next `source`/new shell par wapas aa sakti hai.

---

## 12. File globbing kya hai?

**Globbing command nahi, shell technique hai.**

Shell command execute hone se pehle filename pattern ko matching filenames mein expand kar sakti hai. Isliye globbing `ls`, `cp`, `mv`, `rm`, `grep` aur other commands ke saath work kar sakti hai.

Example:

```bash
touch file1 file2 filea fileb filec filed
ls file*
```

Shell `file*` ko matching names ki list mein expand karegi, phir `ls` ko arguments milenge.

### 12.1 Globbing vs `find`

- `find` filesystem search command hai.
- Globbing shell ka pattern expansion mechanism hai.
- `find -name "*ila*"` mein pattern `find` ko pass hota hai kyunki quoted hai.
- `ls file*` mein shell current directory ke matching names pehle expand karti hai.

Quoting behavior samajhna important hai.

---

## 13. `*` wildcard

`*` zero ya multiple characters match kar sakta hai:

```bash
ls file*
```

Match ho sakte hain:

```text
file1
file2
filea
fileb
```

Substring search pattern:

```bash
ls *ila*
```

Iska meaning:

- `ila` se pehle kuch bhi ho sakta hai,
- `ila` ke baad kuch bhi ho sakta hai,
- matching filename current directory mein hona chahiye.

`*` length-independent hai. Ek `*` exactly one character nahi, zero/multiple characters represent kar sakta hai.

### 13.1 No match behavior

Agar pattern match nahi karta, shell configuration ke hisaab se pattern literal pass ho sakta hai ya error/empty expansion behavior aa sakta hai. `find` ke patterns ko quote karna safe habit hai:

```bash
find /path -name '*ila*'
```

---

## 14. `?` wildcard

`?` exactly **one character** match karta hai:

```bash
ls file?
```

Match:

```text
file1
file2
filea
```

But `file10` match nahi karega, kyunki `?` ke baad exactly one character chahiye aur yahan two characters hain.

```bash
ls file??
```

Exactly two characters after `file`.

```bash
ls file???
```

Exactly three characters after `file`.

| Pattern | Meaning |
|---|---|
| `*` | Zero ya multiple characters |
| `?` | Exactly one character per `?` |
| `file??` | `file` + exactly two characters |

---

## 15. Character set — `[ ]`

Square brackets ek position par allowed characters ka set define karte hain:

```bash
ls file[abc]
```

Match:

```text
filea
fileb
filec
```

Not match:

```text
filed
file1
```

### 15.1 Ranges

```bash
ls file[1-9]
ls file[a-z]
```

- `[1-9]` — one digit range
- `[a-z]` — one lowercase letter range

### 15.2 Negated set

```bash
ls file[!2]*
```

Common Bash glob syntax mein `[!2]` ka meaning second position par `2` ke alawa character. Some tools/locale contexts mein negation syntax differ kar sakta hai; shell documentation check karo.

### 15.3 Multiple allowed choices

```bash
ls File*la[123]
```

End position par `1`, `2` ya `3` match karega.

`[ ]` exactly one character position control karta hai, bilkul `?` ki tarah, lekin acceptable characters aap define karte ho.

---

## 16. Globbing ka practical use

Aksar exact filename yaad nahi hota, sirf partial clue hota hai:

> Naam ke beech mein `ila` characters the; beginning/end ya extension yaad nahi.

Current directory glob:

```bash
ls *ila*
```

`find` ke saath:

```bash
find / -type f -name '*ila*' 2>/dev/null
```

`locate` ke saath:

```bash
locate '*ila*'
```

`grep` ke saath file pattern:

```bash
grep -H "keyword" /var/log/*.log
```

Globbing search pattern ko flexible banata hai; command khud search semantics determine karti hai.

### 16.1 Safety with destructive commands

Ye dangerous pattern hai:

```bash
rm *
```

Current directory ke matching files delete ho sakte hain. Pehle:

```bash
printf '%s\n' *
```

ya:

```bash
ls -- *
```

se expansion review karo. Important file names ke saath `rm --` use karna option confusion reduce karta hai, lekin delete se pehle backup/confirmation best hai.

---

## 17. Day 13 command summary

```bash
# Shell variables
name=value
echo "$name"
echo "${name}"
set
unset name

# Environment variables
printenv
env
echo "$HOME"
echo "$USER"
echo "$SHELL"
echo "$PWD"
echo "$PATH"
echo "$PS1"

# Command lookup
command -v passwd
type -a passwd

# Export and persistence
export name=value
export -p
source ~/.bashrc
. ~/.bashrc
cp ~/.bashrc ~/.bashrc.backup

# Globbing
ls file*
ls file?
ls file??
ls file[abc]
ls file[1-9]
ls file[!2]*
find / -name '*ila*' 2>/dev/null
locate '*ila*'
grep -H 'ERROR' /var/log/*.log
```

---

## 18. Common mistakes aur safety points

1. Variable assignment mein `name = value` spaces use karna.
2. Variable reference mein `$` aur assignment mein `$` ko mix karna.
3. Variable name number se start karna.
4. Uppercase convention ko hard requirement samajhna.
5. `$PATH` mein writable/current directory blindly add karna.
6. `./script.sh` aur `script.sh` ka difference ignore karna.
7. Normal variable ko child shell mein automatically available samajhna.
8. `export` ke baad bhi logout ke baad variable permanent expect karna.
9. `.bashrc` ko backup ke bina edit karna.
10. `source ~/.bashrc` na run karke current shell mein change expect karna.
11. Global `/etc/profile` edit karke all users ko unintentionally affect karna.
12. Globbing ko command samajhna; actual expansion shell karti hai.
13. `*` ko exactly one character samajhna; `?` exactly one character hota hai.
14. `[abc]` ko string `abc` samajhna; ye one-character set hai.
15. `rm *` ya broad glob ko expansion review kiye bina run karna.
16. `find` pattern ko quote na karna, jisse shell pehle expand kar de.
17. Case-sensitive filename matching mein `-name`/`-iname` ka difference ignore karna.

---

## 19. Self-check questions

1. Variable ko box/label analogy se explain karo.
2. Bash variable assignment mein `=` ke around spaces kyu nahi hote?
3. Valid aur invalid variable names ke examples do.
4. Variable reference ke liye `$name` aur `${name}` ka use kab hota hai?
5. Variables scripts ko maintainable kaise banate hain?
6. `$HOME`, `$USER`, `$SHELL`, `$PWD`, `$PATH` aur `$PS1` ka role batao.
7. Shell `$PATH` use karke command kaise locate karti hai?
8. Current directory se script run karne ke liye `./script.sh` kyu likhte hain?
9. Normal variable child shell mein kyu nahi milti?
10. `export` ka effect kya hai?
11. `var=value`, `export var=value`, `~/.bashrc` aur `/etc/profile` ke persistence levels compare karo.
12. `source ~/.bashrc` ka practical purpose kya hai?
13. `set` aur `unset` ka use kya hai?
14. File globbing command hai ya shell technique?
15. `*` aur `?` mein length ka difference kya hai?
16. `file[abc]` kis filenames ko match karega?
17. `[1-9]` aur `[!2]` ka broad meaning kya hai?
18. `ls *ila*` aur `find / -name '*ila*'` mein glob processing ka difference kya hai?
19. Destructive glob command run karne se pehle kaunsa safety check karoge?
20. `.bashrc` edit karte waqt backup kyu useful hai?

---

## 20. Final takeaway

Day 13 ka core message:

- Variables labelled storage boxes hain; assignment aur reference ka syntax samjho.
- `=` ke around spaces nahi hote aur variable name number se start nahi hota.
- Environment variables shell ka working context provide karti hain.
- `$PATH` command lookup aur `./script` behavior samjhata hai.
- `export` variables ko child processes tak pass karta hai.
- `~/.bashrc` user-specific persistence aur `/etc/profile` system-wide persistence provide kar sakte hain.
- `source` modified profile ko current shell mein reload karta hai.
- Globbing command nahi, shell-side filename pattern expansion hai.
- `*` multiple/zero characters, `?` exactly one character aur `[ ]` defined character set match karta hai.
- Broad globbing, especially `rm *`, ko review ke bina run nahi karna chahiye.

Day 14 mein course ke remaining shell utilities, history, password-recovery discussion aur `sort`/`uniq` jaise text-processing workflows continue honge.
