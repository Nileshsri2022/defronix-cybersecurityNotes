# Day 6 — Kali Linux Capsule Course: `cut`, `awk`, Compression & `tar` (Hinglish Explanation)

**Source transcript:** `transcripts/006 - Kali Linux Free Capsule Course - Day 6 [ Hindi ].hi-orig.srt`  
**Note:** Ye explanation Hindi original transcript ko samajh kar easy Hinglish mein banaya gaya hai. Auto-captions mein `कट/बट` = `cut`, `ए ब्लू के/अब` = `awk`, `डिल्ली मी/दिल्ली मी` = delimiter, `जड़ कैट` = `zcat`, `बी स कैट` = `bzcat`, `गिफ्ट/टावर` = `tar` jaise garbled words mile; unka intended technical meaning restore karke explain kiya gaya hai.

---

## 1. Day 6 ka focus

Trainer pehle students se poochte hain ki har session mein sirf commands chal rahi hain, topic change karna chahiye ya continue. Phir announce karte hain ki aaj commands continue hongi aur agle sessions mein **user management**, **group management**, **file security**, aur **permissions** aayenge. Aaj ke major topics:

1. **`cut`** — file ya command output se characters/fields cut karke sirf required data nikaalna.
2. **`awk`** — space-separated output ko smartly fields mein todkar formatted output banana.
3. **`gzip` / `gunzip`**, **`bzip2` / `bunzip2`** — file compress/decompress aur compressed file ka content dekhna.
4. **`tar`** — multiple files ko ek archive mein bundle karna, `.tar`, `.tar.gz`, `.tar.bz2` create/extract/list karna.

Trainer bolte hain: Linux admin ke liye ye commands bahut important hain kyunki har command ka apna role hota hai. Ek command apni limitation tak kaam karti hai, phir dusri command usko take over kar leti hai. Isi chain mein `cut`, `awk`, compression tools, aur `tar` practical workflow complete karte hain.

---

## 2. `cut` command — kaam kya hai?

`cut` ka kaam hota hai file ya kisi command ke output se:

- characters cut karna — jaise position 1 se 6, ya position 1 aur 3
- fields cut karna — delimiter ke basis par field 1, field 3, etc.

Do common syntax styles:

```bash
cut OPTION file
command | cut OPTION
```

Example idea:

```bash
cat sample.txt
tail -n 2 sample.txt | cut ...
df -h | cut ...
```

Yani `cut` kamal ka tab hota hai jab poora output nahi, sirf uska selected hissa chahiye.

---

## 3. `cut -c` — character positions se kaatna

`-c` ka matlab: **cut by characters**.

### Ek character

```bash
cut -c1 sample.txt
```

Isse har line ka 1st character milega.

### Continuous range

```bash
cut -c1-6 sample.txt
```

Isse har line ke 1st se 6th character tak text milega. Agar line mein `manish` type naam ho aur aap sirf pehle 6 chars chahte ho, ye approach kaam aayega.

### Multiple non-continuous positions

```bash
cut -c1,3 sample.txt
```

Isse har line se 1st aur 3rd character milega.

### Pipe ke saath

```bash
tail -n 2 sample.txt | cut -c1-6
```

Iska flow:

```text
tail → last 2 lines
cut -c1-6 → har line ke pehle 6 chars
```

Trainer ne is phase mein `grep -w` se combine karke bhi dikhaya: pehle exact line filter karo, phir us line se selected chars nikaal lo.

---

## 4. `cut -d` aur `-f` — delimiter ke sath fields

Field ka matlab: line ka ek logical column. Lekin `cut` ko tabhi field samajh aayega jab aap delimiter bataoge.

- `-d` = delimiter define karo
- `-f` = field number select karo

Example `/etc/passwd` style file colon `:` se fields rakhti hai:

```bash
cut -d ':' -f1 /etc/passwd
```

Isse field 1 — mostly username — milega.

Agar field 1 aur 3 dono chahiye:

```bash
cut -d ':' -f1,3 /etc/passwd
```

Agar field 1 se 3 tak chahiye:

```bash
cut -d ':' -f1-3 /etc/passwd
```

Without delimiter sirf `-f1` likhne par `cut` many cases mein poori line ko ek field samajh lega ya expected output nahi dega. Isliye `-d` aur `-f` ko sath sochna chahiye.

### Delimiter koi bhi symbol ho sakta hai

Comma, colon, semicolon, space, `@` — jo data mein field separator hai, wahi delimiter bana sakte ho. Space delimiter ka example:

```bash
tail -n 5 /var/log/messages | cut -d ' ' -f1,2,3
```

Isse log entry ka month/date/time jaise starting fields mil sakte hain — exact field number log format par depend karta hai.

---

## 5. `cut` ki limitation — multiple/irregular spaces

Trainer ne limitation dikhayi: agar output mein ek se zyada spaces hain, simple `cut -d ' ' -fN` confuse ho sakta hai. Kyunki `cut` har exact delimiter occurrence ko count karta hai; extra spaces ke bich empty fields ban sakte hain.

Example concept:

```bash
df -h | cut -d ' ' -f1
```

Shayad kaam kar jaye ya na kare — output alignment ke multiple spaces ki wajah se fields galat aa sakte hain. Aise case mein `awk` better hota hai kyunki `awk` whitespace ko intelligently handle kar leta hai.

---

## 6. `awk` — `cut` ki limitation ka practical solution

`awk` shell scripting ki bahut important command hai. Is class mein basic field extraction use hui:

```bash
command | awk '{print $1}'
```

Yahan:

- `$1` = first field
- `$2` = second field
- `$6` = sixth field

`awk` by default spaces/tabs ko field separator maan leta hai, aur multiple consecutive spaces ko sensible tarike se handle karta hai.

### `df -h` se selected columns

Disk usage output dekho:

```bash
df -h
```

Agar sirf filesystem chahiye:

```bash
df -h | awk '{print $1}'
```

Agar filesystem + size + mounted-on chahiye:

```bash
df -h | awk '{print $1,$2,$6}'
```

Output ko table jaisa clean dikhane ke liye:

```bash
df -h | awk '{print $1,$2,$6}' | column -t
```

`column -t` ka kaam: output ko columns/table form mein arrange karna. Help chahiye to:

```bash
column --help
```

### Usage percentage

```bash
df -h | awk '{print $5}'
```

Isse `25%` type value milegi. Trainer ne practice question diya: output mein sirf `25` chahiye, `%` nahi. Simple solution Day 5 ke tools se:

```bash
df -h | awk '{print $5}' | tr -d '%'
```

Agar sirf root line ho to pehle `grep '/$'` jaisa filter bhi laga sakte ho depending on output.

---

## 7. Real pipeline — network output se IP nikalna

Trainer ne `ifconfig` jaisa network command use karke dikhaya ki poora output bahut bada hota hai, lekin report/monitoring ke liye sirf IP chahiye hoti hai. Modern systems mein `ip addr` common hai, lekin class flow ke hisaab se `ifconfig` concept samjho:

```bash
ifconfig | grep -w inet
```

Phir sirf address field:

```bash
ifconfig | grep -w inet | awk '{print $2}'
```

Modern equivalent idea:

```bash
ip -4 addr show | awk '/inet / {print $2}'
```

Agar IP ke andar bhi split karna ho, `awk -F` se custom field separator define kar sakte ho:

```bash
echo '192.168.1.45' | awk -F. '{print $1,$2,$3,$4}'
```

Agar sirf first three octets ko dotted form mein chahiye:

```bash
echo '192.168.1.45' | awk -F. '{print $1 "." $2 "." $3}'
```

Class ka main learning: pehle `grep` se line narrow karo, phir `awk` se desired column nikaalo, phir zarurat ho to `-F` se field ke andar bhi split karo.

---

## 8. Practice flow — kaise combine yaad rakhein

Common chain:

```bash
source_command | grep FILTER | awk '{print $N}' | column -t
```

Examples:

```bash
df -h | awk '{print $1,$2,$5,$6}' | column -t
cut -d ':' -f1 /etc/passwd | less
tail -n 10 app.log | grep ERROR | awk '{print $1,$2,$3}'
```

Regular practice ke liye command ka matlab socho:

- `grep` → kaunsi line chahiye?
- `cut` → kaunsa fixed character/delimited field chahiye?
- `awk` → whitespace-separated smart field selection?
- `column -t` → output clean table?

---

## 9. Compression kyu?

Trainer scenario dete hain:

- File ka size zyada hai aur share karni hai.
- Kuch important files kaafi time se use nahi ho rahi, lekin delete nahi kar sakte.

Aise case mein compression useful hai. Single text file compress karne ke common tools: `gzip` aur `bzip2`.

---

## 10. `gzip`, `zcat`, `gunzip`

### Compress karna

```bash
gzip demo.txt
```

Result: `demo.txt.gz` ban jata hai aur original `demo.txt` normally replace ho jata hai. Size compare karo:

```bash
ls -lh demo.txt.gz
```

### Content bina decompress kiye dekhna

```bash
zcat demo.txt.gz
```

`zcat` compressed `.gz` file ka content screen par dikhata hai without permanently decompression.

### Decompress karna

```bash
gunzip demo.txt.gz
```

Result: `demo.txt` wapas aa jayega aur `.gz` archive normally remove ho jayega.

---

## 11. `bzip2`, `bzcat`, `bzmore`, `bunzip2`

`bzip2` generally better compression deta hai, lekin thoda slower ho sakta hai.

### Compress

```bash
bzip2 demo.txt
```

Result: `demo.txt.bz2`.

### Content dekhna

```bash
bzcat demo.txt.bz2
```

Page-by-page dekhne ke liye pager style command:

```bash
bzmore demo.txt.bz2
```

### Decompress

```bash
bunzip2 demo.txt.bz2
```

Important: `.gz` ke liye `gunzip` aur `.bz2` ke liye `bunzip2`. Ek doosre par blindly `gunzip`/`bunzip2` mat chalao; format match important hai.

---

## 12. In compression tools ki limitation

`gzip`/`bzip2` mainly single files compress karte hain. Agar 10, 15, 20 files ko ek archive mein bundle karna ho, in commands se directly ek combined archive banana expected workflow nahi hai.

Is problem ka answer: **`tar`**.

---

## 13. `tar` — multiple files ko ek archive mein

`tar` ka basic create syntax:

```bash
tar -cvf archive.tar file1 file2 file3
```

Example class-style:

```bash
tar -cvf practice.tar demo.txt sample.txt test1.txt
```

Flags:

- `-c` = create archive
- `-v` = verbose; screen par kaam dikhata rahe
- `-f` = file name of archive; `-f` ke turant baad archive ka naam aana chahiye

After create:

```bash
ls -lh practice.tar
```

Verbose mein files add hote hue dikhengi.

---

## 14. `.tar.gz` create karna — gzip compression ke saath

```bash
tar -czvf practice.tar.gz demo.txt sample.txt test1.txt
```

Extra flag:

- `-z` = gzip compression use karo

Result: bundle + gzip compressed archive.

Order note jo class mein emphasize hua: compression type flag (`z`/`j`) `f` se pehle define ho, aur `f` ke baad archive filename aana chahiye.

---

## 15. `.tar.bz2` create karna — bzip2 compression ke saath

```bash
tar -cjvf practice.tar.bz2 demo.txt sample.txt test1.txt
```

Extra flag:

- `-j` = bzip2 compression use karo

Result: `practice.tar.bz2`.

Ye formats isliye important hain kyunki Linux packages/tools aksar `.tar.gz`, `.tgz`, ya `.tar.bz2` mein milte hain. Manual package unpack/install ke liye `tar` aana zaroori hai.

---

## 16. Archive ke andar kya hai? list/search

Archive list karne ke liye:

```bash
tar -tvf practice.tar
```

- `-t` = list contents

Compressed archive par bhi same basic idea:

```bash
tar -tvf practice.tar.gz
tar -tvf practice.tar.bz2
```

Specific file check karni ho:

```bash
tar -tvf practice.tar demo.txt
```

Ya pipe ke saath search:

```bash
tar -tvf practice.tar | grep 'demo.txt'
```

Agar file exist nahi karti, `tar: demo.txt: Not found in archive` type error mil sakta hai.

---

## 17. Archive extract karna

Generic modern style:

```bash
tar -xvf practice.tar
tar -xvf practice.tar.gz
tar -xvf practice.tar.bz2
```

- `-x` = extract

Older/explicit style:

```bash
tar -xvzf practice.tar.gz
tar -xvjf practice.tar.bz2
```

Modern `tar` aksar format auto-detect kar leta hai, lekin flags samajhna phir bhi useful hai. Extract ke baad `ls -lh` karke files confirm karo.

---

## 18. Command summary table

| Kaam | Command |
|---|---|
| 1st char of every line | `cut -c1 file` |
| chars 1–6 | `cut -c1-6 file` |
| chars 1 and 3 | `cut -c1,3 file` |
| colon file se field 1 | `cut -d ':' -f1 /etc/passwd` |
| multiple fields | `cut -d ':' -f1,3 /etc/passwd` |
| disk output se field | `df -h \| awk '{print $1}'` |
| multiple fields format | `df -h \| awk '{print $1,$2,$6}' \| column -t` |
| gzip compress | `gzip file` |
| gzip content view | `zcat file.gz` |
| gzip decompress | `gunzip file.gz` |
| bzip2 compress | `bzip2 file` |
| bzip2 content view | `bzcat file.bz2` |
| bzip2 pager view | `bzmore file.bz2` |
| bzip2 decompress | `bunzip2 file.bz2` |
| tar create | `tar -cvf bundle.tar files...` |
| tar + gzip | `tar -czvf bundle.tar.gz files...` |
| tar + bzip2 | `tar -cjvf bundle.tar.bz2 files...` |
| archive list | `tar -tvf bundle.tar` |
| archive extract | `tar -xvf bundle.tar` |

---

## 19. Common mistakes

1. `cut -f` use karke `-d` delimiter define na karna.
2. Multi-space aligned output par `cut -d ' '` blind use karna; `awk` better rehta hai.
3. `.gz` ko `bunzip2` ya `.bz2` ko `gunzip` se kholne ki koshish.
4. `tar -f` ke baad archive filename dena bhoolna.
5. `tar -czvf` mein destination archive naam aur source files ka order confuse karna.
6. Archive list/extract karne se pehle `ls -lh` aur `tar -tvf` se verify na karna.

---

## 20. Class-end doubt recap — `-d` aur `-f`

Doubt session mein trainer `cut` ke `-d` aur `-f` dobara samjhate hain:

- `-d ':'` ka matlab: is symbol ko delimiter maano. `:` se pehle ka part field 1, agle `:` tak field 2, aur aise hi aage.
- `-f1` ka matlab: delimiter ke basis par bane fields mein se field 1 print karo.
- Agar field empty hai, output mein empty value aa sakti hai.

Aur ek system update related doubt par trainer officially share kiye gaye page ke steps follow karne bolte hain, especially source list / old Linux setup problem ke case mein.

---

## 21. Final takeaway

Day 6 ka core skill:

1. `cut` se fixed characters aur simple delimiter fields nikaalo.
2. Irregular/multiple spaces ho to `awk` use karo.
3. `awk '{print $N}'` field selection aur `column -t` formatting ko pipeline mein jodo.
4. Single file compression ke liye `gzip`/`bzip2` samajho.
5. Multiple files ko ek package/archive mein rakhne ke liye `tar` must-know command hai.
6. Downloaded `.tar.gz`/`.tar.bz2` tools ko list/extract/install karne ke liye ye workflow almost daily use hota hai.

Trainer ka closing point: commands ka chain samajhna hi asli power hai. Individual commands chhoti lagti hain, lekin `grep + awk + cut + tar` mil kar server management, logs, reports, compression, aur package handling ko seconds ka kaam bana dete hain.
