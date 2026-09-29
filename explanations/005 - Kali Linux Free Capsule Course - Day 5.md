# Day 5 — Kali Linux Capsule Course: `sed` Delete/Insert + `grep` In-Depth (Hinglish Explanation)

**Source transcript:** `transcripts/005 - Kali Linux Free Capsule Course - Day 5 [ Hindi ].hi-orig.srt`  
**Note:** Ye explanation Hindi original transcript ko samajh kar banaya gaya hai. Auto-captions mein `सीडी/सेट` = `sed`, `ग्राफ/गैप` = `grep`, `सरिता एडिटर` = stream editor, `एस कलेशन मार्क` = exclamation `!`, `डॉलर/ग्रेटर दें सिम` = anchors `$` / `^` jaise garbled words mile; unka intended meaning restore karke easy Hinglish mein explain kiya gaya hai.

---

## 1. Day 5 ka aim — bache hue `sed`, phir `grep` deep dive

Trainer pehle batate hain ki Day 4 mein find/replace tak `sed` chala tha, lekin `sed` delete/insert aur kuch cheezein bachi hain. Aaj ka plan:

1. **`sed` continue** — lines delete karna, except-line delete karna, line se pehle text insert karna, on-screen vs permanent (`-i`) difference.
2. **`grep` detail** — pattern search, line number, count, case-insensitive, only match, invert match, exact word, before/after context, anchors, quoted phrases, multiple patterns/files, recursive search.
3. **Class-end Q&A recap** — public/private place aur stdin/stdout/stderr ka practical meaning.

`cut` command ka naam agenda mein tha, lekin time ki wajah se aaj full cover nahi hua; trainer end mein sirf motivation dete hain ki bade output se specific column/text kaatne ke liye bhi commands aayengi.

---

## 2. `sed` delete operation — on-screen vs permanent

Day 4 yaad rakho: `sed` stream editor hai. `sed 'action' file` normally result screen par dikhata hai; original file change nahi hoti. Original file modify karne ke liye `-i` use hota hai.

### 2.1 Range of lines delete karna (screen output)

Line 1 se 15 tak delete karke baaki output dekhna ho:

```bash
sed '1,15d' sample.txt
```

- `1,15` = address/range
- `d` = delete action

Line numbers samajhne ke liye pehle file ko numbered dekh sakte ho:

```bash
cat -n sample.txt | less
```

Same kaam do tareeke se socho:

```bash
sed '1,15d' sample.txt
# ya review ke liye
cat -n sample.txt | sed '1,15d'
```

Important: ye delete screen output mein ho raha hai. Original `sample.txt` abhi bhi same hai.

### 2.2 Permanent delete — `-i`

```bash
sed -i '1,15d' sample.txt
```

Ab original file se lines 1–15 remove ho jayengi. Trainer style warning same: pehle on-screen run karo, output sahi ho tabhi `-i`.

### 2.3 “Except this line, delete everything” — `!`

Sirf line 12 rakhni ho aur baaki sab delete karni ho (screen output):

```bash
sed '12!d' sample.txt
```

Meaning:

- `12` address
- `!` NOT — is address ko chhod kar
- `d` delete

Yani rule invert ho gaya: line 12 ko delete mat karo, baaki sab delete karo. Permanent karne ke liye:

```bash
sed -i '12!d' sample.txt
```

Ye dangerous ho sakta hai kyunki file sirf ek line reh jayegi. Pehle backup ya screen test must.

### 2.4 Line se pehle text insert karna — `i`

Line 57 ke pehle `hello world` insert karke output dekhna ho:

```bash
sed '57i hello world' sample.txt
```

`sed` mein `i` ka kaam insert before address hota hai. Permanent insert:

```bash
sed -i '57i hello world' sample.txt
```

Numbering note: insert karne ke baad existing line 57 neeche shift ho jati hai, isliye output mein nayi line 57 ke aas-pas dikh sakti hai. Concept clear rakho: `Ni text` = line N se pehle insert.

---

## 3. `sed` ka golden safety workflow

Har edit ke liye same routine follow karo:

```bash
# Step 1: screen test
sed '1,15d' sample.txt | less

# Step 2: backup (important files par)
cp sample.txt sample.txt.bak

# Step 3: permanent edit
sed -i '1,15d' sample.txt
```

Trainer class mein baar-baar isiliye kehte hain: `sed` powerful hai, galat address/action original file ko turant bigaad sakta hai.

---

## 4. `grep` kyu? Log monitoring wala example

Trainer real-world scenario dete hain: aap SOC/log monitoring kar rahe ho. Koi attacker machine/server ko hit karne ki koshish karta hai. Us event mein IP address, username, service name (`ftp`, `dns`, `ssh`, etc.) ya koi unusual entry aa sakti hai.

Ab user bolta hai: “maine ye nahi kiya.” Lekin log file continuously update hoti rehti hai; usme manually search karoge to ghanton lag jayenge aur phir bhi miss ho sakta hai. Isliye log file mein pattern search ke liye `grep` use karte hain.

`grep` ka basic kaam: file ya input stream mein se un lines ko nikalna jinme pattern match ho jaye.

Basic syntax:

```bash
grep pattern file
```

Example:

```bash
grep root demo.txt
```

Ye `demo.txt` ki un lines ko screen par dikhayega jinme `root` milta hai.

---

## 5. `grep -n` — match ke saath line number

Agar sirf match nahi, uski line number bhi chahiye:

```bash
grep -n root demo.txt
```

Output style:

```text
390:....root....
```

Ye investigation/reporting mein useful hai kyunki aap exact location quote kar sakte ho: “line 390 par ye entry hai.”

---

## 6. `grep -c` — kitni lines mein pattern mila

```bash
grep -c root demo.txt
```

Ye un lines ka count deta hai jinme pattern at least ek baar mila. Dhyan do: ye basically matching lines count karta hai, har extra occurrence ko alag se count karne ke liye additional processing chahiye hoti hai (advanced topic).

---

## 7. `grep -i` — case-insensitive search

Linux case-sensitive hai. `DNS`, `dns`, `Dns` same nahi hote.

```bash
grep -i dns demo.txt
```

Ye sab case variations match karega: `DNS`, `dns`, `Dns`, etc.

Logs mein case-insensitivity useful hai, lekin jab exact case matter karta ho (config keys, usernames), `-i` mat lagao.

---

## 8. `grep -o` — sirf matched pattern print karo

Normal `grep root demo.txt` puri matching line dikhata hai. Agar aapko sirf matched text chahiye:

```bash
grep -o root demo.txt
```

Use case: report mein sirf extracted tokens chahiye, puri noisy line nahi.

---

## 9. `grep -v` — invert match / except pattern

Agar `root` wali lines chhod kar baaki sab lines dekhni hain:

```bash
grep -v root demo.txt
```

Trainer example style: attendance register mein present students ko mark kiya aur unhe chhod kar baaki list dekhni ho. System/logs mein use: known-good/noisy pattern hata kar baaki suspicious entries dekhna.

Multiple flags combine ho sakte hain, jaise line number ke saath invert:

```bash
grep -nv root demo.txt
```

---

## 10. `grep -w` — exact word match

Example: user `manish` dhoondhna hai, lekin `manisha` nahi chahiye.

```bash
grep -w manish /etc/passwd
```

`-w` word boundaries respect karta hai. Isliye `manisha` match nahi hoga jab exact `manish` word boundary complete nahi hoti.

Investigation mein ye false positives kam karta hai.

---

## 11. Context ke saath search — `-B`, `-A`, `-C`

Kabhi sirf matched line enough nahi hoti. Attack ya error ko samajhne ke liye uske upar/neeche ki lines bhi chahiye hoti hain.

### Before context — matched line se pehle ki N lines

```bash
grep -n -B 4 DNS app.log
```

Matlab: jahan `DNS` mila, us line ke pehle ki 4 lines bhi dikhao.

### After context — matched line ke baad ki N lines

```bash
grep -n -A 4 DNS app.log
```

Matlab: matched line ke baad ki 4 lines bhi dikhao.

### Combined context — upar + neeche

```bash
grep -n -C 4 DNS app.log
```

Matlab: matched line ke upar 4 aur neeche 4 lines bhi.

Trainer iska point: matched pattern ke aas-pas ka context dekh kar aap zyada confidently decide karte ho ki jo mila wo meaningful hai ya sirf coincidence.

---

## 12. Space wale patterns — quotes zaroori

Agar pattern mein space hai, quotes do:

```bash
grep "model name" file
lscpu | grep -i "model name"
```

Galat approach:

```bash
grep model name file
```

Yahan `grep` `model` ko pattern samajh sakta hai aur `name` ko alag filename. Isliye phrases hamesha quotes mein do.

---

## 13. Anchors — starting `^` aur ending `$`

Agar pattern line ke beginning mein ho tabhi match chahiye:

```bash
grep '^root' /etc/passwd
```

`^` ka matlab: line start.

Agar pattern line ke end mein ho tabhi match chahiye:

```bash
grep 'nologin$' /etc/passwd
```

`$` ka matlab: line end.

Demo mein `grep 'root$' file` par kuch nahi mila kyunki `root` kisi line ke end mein nahi tha; same tarah `nologin$` match ho sakta hai agar line usi par khatam ho.

---

## 14. Command output par `grep` — pipe ke saath

`grep` sirf files par nahi, kisi command ke output par bhi chalta hai:

```bash
lscpu | grep -i model
lscpu | grep -i "model name"
```

Flow:

```text
lscpu → stdout → pipe → grep → filtered stdout → screen
```

Practical use: report ke liye sirf relevant parameter nikalna. Poora hardware dump share karne ke bajaye `model name`, architecture, cores jaise exact fields filter kar sakte ho.

---

## 15. Multiple patterns — `egrep` / modern `grep -E`

Trainer kehte hain: ek pattern ke liye `grep`, lekin multiple patterns ke liye extended behaviour use hota hai. Class mein `egrep` bola gaya; modern systems mein recommended equivalent generally `grep -E` hai.

Example: ek hi file mein `root`, `ftp`, aur `dns` teeno search karne hain:

```bash
egrep 'root|ftp|dns' demo.txt
```

Modern style:

```bash
grep -E 'root|ftp|dns' demo.txt
```

Alternative: repeated `-e` expressions:

```bash
grep -e root -e ftp -e dns demo.txt
```

Note: agar koi pattern file mein exist nahi karta, wo simply output mein nahi aayega. `grep` sirf matches dikhata hai; “ye pattern missing tha” alag se nahi batata.

---

## 16. Multiple files mein search

Ek pattern ko multiple files mein dhoondhna:

```bash
grep root /etc/passwd /etc/group
```

Multiple files dene par output generally filename ke saath aata hai, taaki pata chale match kis file se aaya. Filename control:

```bash
grep -H root file1 file2   # filename force show
grep -h root file1 file2   # filename hide
```

Investigation/reporting mein `-H` useful hai.

---

## 17. `grep -F` / fixed-string search

Jab pattern mein regex special characters ho aur aap unhe literal text ki tarah search karna chahte ho, fixed-string mode useful hai.

```bash
grep -F 'root|ftp' file
```

Class mein `fgrep` bola gaya; modern equivalent: `grep -F`. Difference simple:

- normal/extended grep mein `|`, `.`, `*` jaise symbols special meaning rakhte hain
- `grep -F` mein pattern plain string ki tarah treat hota hai

Agar aapko regex nahi chahiye, sirf exact text chahiye, `-F` fast aur predictable hota hai.

---

## 18. Path bhool gaye? Recursive search `grep -R`

Trainer scenario: yaad hai ki `/etc/defaults` ke andar bahut files hain; pattern kisi ek file mein pakka hai, lekin exact file yaad nahi. Tab recursive search:

```bash
grep -R 'pattern' /etc
```

Ye directory tree ke andar files mein search karega. Investigation mein powerful hai, lekin bade directories par slow/noisy ho sakta hai. Permission errors hatane ke liye kabhi-kabhi taarike se suppress kiya jata hai:

```bash
grep -R 'pattern' /etc 2>/dev/null
```

Dhyan: errors suppress karne se kuch permission-related clues bhi chhup sakte hain; investigation mein pehle errors dekhna better.

---

## 19. Homework/logic question — sirf line 25–35 ke andar pattern

Trainer practice question deta hai: puri file grep mat karo; sirf line 25 se 35 ke beech pattern search karo. Best approach: pehle range cut karo, phir grep.

```bash
sed -n '25,35p' file | grep 'pattern'
```

Agar line number context bhi chahiye, pehle numbered range lo:

```bash
sed -n '25,35=' file
sed -n '25,35p' file | grep -n 'pattern'
```

Yaad rakhna: pipe ke baad `grep -n` ka number filtered mini-output ka hota hai, original file number nahi. Original number chahiye to pehle `cat -n`/`sed -n '25,35='` style approach sochna padta hai.

---

## 20. Mixed practical recipes jo class se bante hain

### Investigation: keyword + line number + context + filename

```bash
grep -nH -C 3 'failed password' /var/log/auth.log
```

### Report ke liye exact phrase command output se

```bash
lscpu | grep -i "model name"
```

### Known normal service noise hatao, baaki lines dekho

```bash
grep -viE 'cron|systemd' app.log | less
```

### Ek exact username only

```bash
grep -w manish /etc/passwd
```

### Phrase search in many configs, filename ke saath

```bash
grep -RHEn "PermitRootLogin" /etc/ssh 2>/dev/null
```

---

## 21. Common mistakes jo avoid karne hain

1. `sed -i` pehle chala dena bina screen test ke.
2. `grep word1 word2 file` mein quotes na dena — `word2` filename ban jata hai.
3. `grep -c` ko occurrences count samajhna; ye primarily matching lines count karta hai.
4. `grep -v` ka galat use — important matched lines hi hide ho jati hain.
5. Space/regex characters ko handle na karna; zarurat ho to `-F` ya proper quoting/escaping.
6. Pipe ke baad `grep -n` se original file line number expect karna.
7. Recursive search par permission errors ko bina soche suppress kar dena.
8. `^`/`$` anchors ko `sed` line address `$` se confuse karna — dono contexts alag hain.

---

## 22. End-class Q&A — public/private place dobara clear

Student doubt par trainer dobara samjhate hain: Linux mein root/admin aur normal users hote hain. File-system hierarchy ke andar default directories par pehle se permissions defined hoti hain.

- **Private place** = apna home area. Root ke liye `/root`, normal user ke liye `/home/<user>`. Yahan read/write/execute apne hisaab se kar sakte ho.
- **Public place** = home ke bahar ki system locations. Yahan pehle se defined permissions follow karni padti hain; aap un rules se bahaar nahi ja sakte. Root government jaise powerful ho sakta hai, lekin normal user ke liye boundaries fixed hain.

Real-world compare: apne ghar mein aap owner ho; ghar se bahar public/system rules follow karne padte hain. Is mindset se future mein “kahan file create karni hai / kahan nahi” clear rehta hai.

---

## 23. stdin/stdout/stderr Q&A — file descriptor se practical link

Trainer dobara link karte hain:

- `stdin` default keyboard hota hai.
- `stdout` aur `stderr` default screen/terminal hote hain.
- Error ko bhi dikhana zaroori hai; agar output aaya hi nahi aur error bhi suppress kar di, to aap wait karte rahoge ki kaam ho raha hai jabki fail ho chuka hai.

Redirection ka matlab:

```text
file ko stdin banao        → command < input.txt
stdout file mein bhejo      → command > out.txt
stderr file/null mein bhejo → command 2> err.log  OR  command 2>/dev/null
ek output dusre ka input    → command1 | command2
```

Yehi Day 3/4/5 ko connect karta hai: file descriptor concept → redirection → `sed`/`grep`/pipe workflow.

---

## 24. Final takeaway

Day 5 ka power combo:

1. `sed` se lines selectively delete/insert karo — lekin `-i` tabhi jab screen test pass ho jaye.
2. `sed '12!d'` jaise negation powerful hai; carefully use karo.
3. `grep` logs/investigation/reports ki backbone command hai — pattern, line number, count, context, invert, exact word, anchors, multiple patterns/files, recursive search.
4. Phrase patterns quote karo; exact regex na chahiye to `-F`; multiple regex patterns ke liye `-E`/`egrep`.
5. Investigation mein sirf match nahi, context (`-A/-B/-C`) aur filename/line number bhi capture karo.

Trainer ka closing point: ye commands scripting aur Linux speed ki foundation hain. Abhi concept chal raha hai; jab scripting aayegi, in sab commands ko jod kar bade outputs se seconds mein exact data nikalna aayega.
