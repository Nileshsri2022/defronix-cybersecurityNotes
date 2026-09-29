# Day 3 — Kali Linux Capsule Course: Input/Output Redirection, File Descriptors, Pipe & Tee (Hinglish Explanation)

**Source transcript:** `transcripts/003 - Kali Linux Free Capsule Course - Day 3 [ Hindi ].hi-orig.srt`  
**Trainer in transcript:** Nitesh Singh (Defronix)  
**Note:** Ye explanation Hindi original transcript ko samajh kar banaya gaya hai. Auto-captions mein `रीड डायरेक्शन`, `फाइल डिस्क्रिप्शन`, `एसटीडी इन/आउट`, `ली दें`, `ग्रेटर दें`, `एम पर सेंड` jaise garbled words mile; unka intended meaning **redirection**, **file descriptor**, **stdin/stdout/stderr**, `<`, `>`, aur `&1` restore karke simple Hinglish mein likha gaya hai.

---

## 1. Class ka goal — ye topic kyu important hai?

Day 3 ka topic hai **Input/Output Redirection**. Trainer clear karte hain ki ye ek session mein 100% deep complete nahi ho sakta, isliye basic se start karke maximum practical cheezein di jayengi. Redirection ka real use tab dikhta hai jab aap:

- command ka output screen ke bajaye file mein save karna chahte ho,
- error logs capture karna chahte ho,
- errors ko suppress/ignore karna chahte ho,
- ek command ka output dusri command ko input banana chahte ho,
- automation/scripts mein output aur error handling control karni ho.

Sabse basic concept: system mein **input device** aur **output device** hota hai. Normal case mein input keyboard se aata hai aur output terminal/screen par milta hai. Redirection ka matlab: is input/output ko default route se hata kar kahin aur bhej dena — file mein, dusri command mein, ya discard device mein.

---

## 2. Sabse pehla practical example — `date` ka output file mein

Trainer terminal open karke simple `date` command chalate hain. Normal flow:

```bash
date
```

- input: keyboard se command type hui
- output: screen/terminal par date print hui

Ab trainer bolte hain: mujhe ye output screen par nahi, ek file mein chahiye. Iske liye `>` use hota hai:

```bash
date > date.txt
cat date.txt
```

Kya hua?

1. `date` ne output produce kiya.
2. `>` ne us output ko screen ki jagah `date.txt` mein redirect kar diya.
3. `cat date.txt` se humne file ka content wapas screen par padh liya.

Yehi redirection ka first feel hai: “jo output normally screen par aata, wo file mein chala gaya.”

---

## 3. `>` overwrite karta hai, `>>` append karta hai

Ab trainer `cal` command ka example dete hain. Pehle `date > date.txt` karne se file mein date tha. Phir agar hum:

```bash
cal > date.txt
```

chala dein, to purana date output hat jata hai aur sirf calendar output aa jata hai. Matlab **single `>` file ko overwrite/replace kar deta hai.**

Agar purana content bhi rakhna hai aur naya output neeche add karna hai, to `>>` use karo:

```bash
date >> date.txt
```

Ab file mein pehle calendar output aur uske baad date output dono rahenge.

Simple rule:

| Symbol | Meaning |
|---|---|
| `>` | output redirect + overwrite |
| `>>` | output redirect + append |

“Append” ka seedha matlab: purana content safe rakho, naya output end mein jod do.

---

## 4. Redirection symbols asal mein kiske liye kaam karte hain? File Descriptor samjho

Trainer bolte hain: `>`, `<`, `>>`, `2>` jaise symbols redirection symbols hain, lekin inka connection **file descriptor** se hai. File descriptor ko short mein FD samjho.

Easy definition class ke hisaab se:

> File descriptor ek non-negative integer number hota hai jo process ke andar kisi open file/data source ko identify karta hai.

Linux/Unix mein almost har cheez file ki tarah treat hoti hai — regular files, directories, devices, input/output streams. Isliye jab koi process koi file ya stream use karta hai, kernel uske liye ek descriptor/entry maintain karta hai.

Trainer kernel ke 3 points board par likhwata hai:

1. **Create entry in global file table** — open file ke liye kernel ek entry banata hai.
2. **Provide the location of the entry** — process ko us entry tak pahunchne ka handle/location milta hai.
3. **Return/provide the location to the process** — process future read/write ke liye usi descriptor ka use karti hai.

Windows comparison: Windows mein isi concept ko generally **file handles** ki language mein samjha jata hai; Unix/Linux mein **file descriptors** bola jata hai.

---

## 5. Standard streams: stdin, stdout, stderr

Teen special streams har process ke saath judi hoti hain:

| Stream | FD | Role in easy Hinglish | Common redirect symbol |
|---|---:|---|---|
| `stdin` | **0** | input yahan se aata hai | `<` ya `0<` |
| `stdout` | **1** | normal output yahan jati hai | `>` ya `1>` |
| `stderr` | **2** | error messages yahan jate hain | `2>` |

Class mein locations bhi discuss hoti hain. `/dev` ke andar special files hoti hain jo input/output ko represent karti hain. Practically yaad rakho:

- `/dev/stdin` — standard input
- `/dev/stdout` — standard output
- `/dev/stderr` — standard error
- `/dev/null` — discard/black hole; jo bhi isme bhejo, disappear ho jata hai

`/dev/null` ko trainer black hole jaisa batate hain: koi output ya error suppress karni ho to wahan bhej do, screen par kuch nahi dikhega.

---

## 6. `>` aur `1>` same; `<` aur `0<` same

Trainer command samjhate hain:

```bash
ls 1> out.txt
ls > out.txt
```

Dono ka normal-output redirect karne mein result same hota hai, kyunki stdout ka FD by default `1` hota hai. Isliye aksar log sirf `>` likhte hain.

Input ke liye:

```bash
cat 0< file.txt
cat < file.txt
```

Yahan `cat file.txt` normal use hai, lekin conceptually aap file ko `cat` ke stdin mein de rahe ho. Trainer ye detail isliye batate hain kyunki zyada tar log bas `cat file` rat lete hain; asal flow ye hai ki file ka content input ban raha hai aur `cat` us input ko stdout par print kar raha hai.

Conceptual standard form:

```bash
cat 0< file.txt 1> /dev/stdout
```

Matlab: input `file.txt` se lo, output stdout par do. Rozmarra mein hum itna lamba nahi likhte, but ye samajhna redirection ko strong banata hai.

---

## 7. File create karne ke multiple tareeke — redirection wala touch

Transcript mein trainer file creation ke tareeke dikhate hain:

```bash
touch a.txt       # empty file/timestamp touch
vim b.txt         # editor se file create/edit (vim baad mein detail se aayega)
mousepad c.txt    # graphical editor se file create
cat > d.txt       # redirection ke saath file create + content likhna
```

`cat > d.txt` chalane ke baad terminal input mode mein rukta hai; jo type karoge wo file mein jayega. End karne ke liye `Ctrl + D`.

Point: `>` file ko create bhi kar deta hai agar exist nahi karti, aur content redirect karta hai. Lekin hamesha yaad rakho — single `>` overwrite karta hai.

---

## 8. Pipe `|` — ek command ka output dusri command ka input

Ab trainer pipe introduce karte hain. Pipe ka kaam hota hai:

> pehli command ka stdout lekar dusri command ke stdin mein pass kar dena.

Basic shape:

```bash
command1 | command2
```

Example class ke hisaab se: `ls` ka output `grep` ko dena. `grep` ka basic use string/pattern search karna hota hai.

```bash
ls | grep '^D'
```

Ye un names ko dikhayega jo `D` se start hote hain — jaise Desktop, Documents, Downloads (agar names capital D se hain). Directory specifically long-format mein filter karni ho to:

```bash
ls -l | grep '^d'
```

`ls -l` ke output mein directory lines `d` se start hoti hain, isliye ye directories filter kar deta hai. Plain `ls | grep '^D'` sirf names pattern dekhta hai; `ls -l | grep '^d'` file-type column ko use karta hai. Dono ka context different hai.

Pipe ka flow understand karo:

```text
ls  → stdout → pipe → stdin → grep → filtered stdout → screen
```

Yani `ls | grep ...` mein `ls` ka output seedha screen nahi ja raha; pehle `grep` ke paas input banke ja raha hai, phir filtered result screen par aa raha hai.

---

## 9. `tee` — screen par bhi dikhao, file mein bhi likho

Kabhi aapko output screen par bhi chahiye aur file mein bhi save karna hai. Sirf `>` use karoge to screen par nahi dikhega. Ye problem `tee` solve karti hai.

```bash
ls | tee test.txt
```

Kya hua?

1. `ls` ne current directory ki list output di.
2. Pipe ne wo output `tee` ko input diya.
3. `tee` ne output ko do jagah bheja:
   - screen/stdout par print kiya
   - `test.txt` file mein likh diya

Trainer dobara simple define karte hain: `tee` = print the output and also redirect to a file.

Append karna ho to:

```bash
ls | tee -a test.txt
```

`-a` ka matlab append: purana content overwrite mat karo, naya output neeche jod do.

---

## 10. Errors alag stream hoti hain — `2>` se capture/suppress

Important point: har screen par dikhne wala text normal output nahi hota. Error messages **stderr** se aate hain, unka FD `2` hai. Isliye agar aap sirf `>` use karte ho, errors file mein nahi jayenge; wo screen par dikh sakte hain.

Example:

```bash
cat hello
```

Agar `hello` file exist nahi karti, output kuch aisa hota hai:

```text
cat: hello: No such file or directory
```

Ye error hai. Isko suppress karna ho to:

```bash
cat hello 2> /dev/null
```

Matlab: stderr ko `/dev/null` mein bhej do — screen par error nahi dikhega. Transcript mein trainer “errors ko suppress karke khatam kar diya” yehi kehte hain.

Error ko file mein capture karna ho to:

```bash
cat hello 2> error.txt
```

Ab error screen ke bajaye `error.txt` mein store ho jayega.

---

## 11. Output aur error dono ek saath — `2>&1` ka concept

Trainer `&1` / `2>&1` wala point introduce karte hain. Matlab: stderr ko wahan bhejo jahan stdout ja raha hai.

Common correct pattern:

```bash
command > run.log 2>&1
```

Iska step-by-step meaning:

1. `> run.log` → stdout `run.log` mein bhejo
2. `2>&1` → stderr bhi stdout ke current destination mein bhejo, yani `run.log` mein

Order important hai. Agar redirection ki jagah/order galat kar doge to expected file mein dono cheezein nahi aayengi. Class mein trainer bhi ek mistake dikhate hain aur phir correct karte hain ki output redirection command ke sahi jagah/order mein dena chahiye.

Suppress karna ho dono ko:

```bash
command > /dev/null 2>&1
```

Interpretation: stdout `/dev/null`, phir stderr bhi stdout ke destination (`/dev/null`) — dono gayab. But careful: debugging ke liye logs chahiye hote hain; har cheez blindly suppress karna production/security troubleshooting mein problem bana sakta hai.

---

## 12. Practical demo — chhota bash script + output/error handling

Trainer ek chhota script-like demo banate hain jisme directories create hoti hain. Idea style:

```bash
for i in 1 2 3 4 5
do
    echo "Creating directory /tmp/$i"
    mkdir /tmp/$i
done
```

Demo mein pehle execute permission issue aata hai. Trainer explain karte hain:

- file ko run karne ke liye execute permission chahiye,
- permissions user/group/other ke liye read/write/execute hoti hain,
- execute na ho to shell script/executable directly nahi chalega.

Fix:

```bash
chmod +x dir.sh
./dir.sh
```

First run par script output deta hai aur `/tmp` mein directories ban jati hain. Second run par directories already exist hoti hain, to `mkdir` error produce karta hai. Ab agar hum dono cheezein — normal messages aur errors — ek file mein log karana chahte hain, correct pattern:

```bash
./dir.sh > run.log 2>&1
cat run.log
```

Agar sirf errors suppress karni hain:

```bash
./dir.sh 2> /dev/null
```

Agar output bhi nahi chahiye aur errors bhi nahi chahiye:

```bash
./dir.sh > /dev/null 2>&1
```

Lekin best practice: automation mein errors completely suppress karna tabhi karo jab aapko pakka pata ho ki wo errors harmless expected hain. Otherwise log file mein capture karo.

---

## 13. Common mistakes jo class se seedha yaad rakhni hain

1. `>` samajh kar use karo — purana content delete ho jata hai.
2. Append chahiye to `>>`.
3. sirf `>` se errors capture nahi hote; stderr ke liye `2>` lagana padta hai.
4. output + error dono same file mein ho to: `> file 2>&1`.
5. pipe filter ke liye hai; tee print + save ke liye hai.
6. `/dev/null` powerful discard tool hai, lekin overuse se aap important errors miss kar sakte ho.
7. Redirection order matter karta hai. `2>&1` ka meaning stdout ke current destination ke relative hai.
8. `ls -l | grep '^d'` directory lines filter karta hai; plain `ls | grep '^d'` names ko pattern se filter karta hai — context same nahi.

---

## 14. Final takeaway

Day 3 mein core skill ye thi: default input/output routes ko control karna.

- Keyboard → command → screen normal flow hai.
- `>`/ `>>` se stdout file mein jata hai.
- `<` se file/kisi source ka content stdin ban sakta hai.
- stdin/stdout/stderr ke FD numbers: `0`, `1`, `2`.
- `|` ek command ka output dusri command ka input banata hai.
- `tee` output ko screen aur file dono jagah bhejta hai (`-a` append).
- `2>` errors capture/suppress karta hai; `2>&1` stderr ko stdout ke destination par chipka deta hai.
- `/dev/null` black hole hai — unwanted output/error discard karne ke liye, but carefully use karo.

Trainer end mein bolte hain: ye topic bada hai aur ek session mein poora nahi hota; recording repeat karoge to ye concepts crystal clear ho jayenge. Next session mein redirection ke remaining concepts continue honge.
