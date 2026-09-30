# Day 11 — Kali Linux Capsule Course: `vi` / `vim` Editor (Hinglish Explanation)

**Source transcript:** `transcripts/011 - Kali Linux Free Capsule Course - Day 11 [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** Day 10 — advanced permissions aur `find`
**Note:** Ye explanation Hindi original transcript ko samajh kar likhi gayi hai; ye line-by-line literal translation nahi hai. Auto-captions mein `vi`, `vim`, command modes, visual mode aur editor shortcuts kai jagah garbled mile. Context ke basis par intended editor commands restore karke simple Hinglish mein explain kiya gaya hai.

---

## 1. Day 11 ka focus

Aaj ka main topic **`vi`/`vim` editor** hai. Trainer `locate` command ko bhi briefly mention karte hain, lekin usko later session ke liye defer kar dete hain.

Aaj ke goals:

- `vi`/`vim` ko bina mouse use karna
- Command, insert, last-line aur visual modes samajhna
- File open, edit, save aur quit karna
- Cursor movement aur word/line operations
- Delete, undo, replace, cut, copy aur paste
- Visual character, line aur block selection
- Search forward/backward
- File ya command output ko current file mein read karna

Trainer ka security-specific reason hai: compromised ya minimal Linux machine par `nano` ya graphical editor installed na ho, lekin `vi` aksar available hota hai. Agar shell milne ke baad editor use nahi kar paoge, to configuration file edit karna difficult ho sakta hai.

> `vi` seekhne ka goal sirf ek editor chalana nahi, balki keyboard-only Linux workflow ke saath comfortable hona hai.

---

## 2. `vi`/`vim` kyu seekhna chahiye?

Linux machines par editor availability same nahi hoti. Kisi system par `nano`, GUI editor ya IDE ho sakta hai; kisi minimal server/container par nahi. Lekin `vi` ya uska compatible implementation bahut systems par default mil jata hai.

Security/lab scenario:

1. Kisi authorized target/lab machine par shell milti hai.
2. Aapko configuration, script ya temporary file edit karni hai.
3. GUI nahi hai aur `nano` installed nahi hai.
4. `vi` available hai.

Agar basic commands aati hain, to aap file edit/save kar sakte ho. Agar modes ka concept clear nahi hai, to simple typing bhi command ban sakti hai aur confusion ho sakta hai.

---

## 3. `vi` ke modes

`vi` ka sabse important concept hai **mode**. Same key ka effect current mode par depend karta hai.

| Mode | Kaise enter hota hai | Main purpose |
|---|---|---|
| Command/normal mode | File open karte hi default; `Esc` se return | Navigation, delete, copy/paste, replace |
| Insert mode | `i`, `a`, `I`, `A`, `o`, `O` | Text type karna |
| Ex/last-line mode | `:` | Save, quit aur command-based operations |
| Visual mode | `v`, `V`, `Ctrl+v` | Text select/highlight karna |

### 3.1 Default command mode

```bash
vim file.txt
```

File open hone ke baad aap normally **command mode** mein hote ho, insert mode mein nahi. Agar seedha letters type karoge, to `vi` unhe editor commands samjhega.

> Jab bhi lost ho jao, `Esc` press karo. Ye aapko command mode mein laane ka standard reset key hai.

### 3.2 Insert mode indicator

Insert mode mein jaane ke baad bottom area mein `-- INSERT --` dikh sakta hai. Text type karne ke liye isi mode mein enter karo.

Insert mode se command mode:

```text
Esc
```

---

## 4. Insert mode mein enter karne ke six ways

```bash
vim file.txt
```

File open karke command mode mein ye keys use karo:

| Key | Action | Cursor/text position |
|---|---|---|
| `i` | Insert | Cursor se pehle text type |
| `a` | Append | Cursor ke baad text type |
| `I` | Insert at line start | Current line ke beginning par |
| `A` | Append at line end | Current line ke end par |
| `o` | Open below | Current line ke neeche new line |
| `O` | Open above | Current line ke upar new line |

### 4.1 `i` vs `a`

- `i` current cursor position se pehle insert karta hai.
- `a` cursor ke baad insert karta hai.

### 4.2 `I` vs `A`

Long line ke end tak arrows press karne ke bajay:

- `I` se line ke beginning par insert.
- `A` se line ke end par append.

### 4.3 `o` vs `O`

- `o` current line ke neeche blank line open karta hai.
- `O` current line ke upar blank line open karta hai.

Ye commands `vi` ke “intent combine karo” style ko show karti hain: movement aur insert mode ek key mein.

---

## 5. Save aur quit

Save/quit commands **command mode** se `:` ke saath type hoti hain. Pehle `Esc`, phir command:

| Command | Meaning |
|---|---|
| `:w` | Write/save, editor mein raho |
| `:q` | Quit |
| `:wq` | Save karke quit |
| `:q!` | Changes discard karke force quit |
| `:wq!` | Force write and quit; permissions hone par |
| `:w newname.txt` | Current content ko new filename mein write/save |
| `ZZ` | Save and quit shortcut; colon nahi |

Example:

```text
Esc
:wq
Enter
```

### 5.1 Unsaved changes ka error

Agar changes unsaved hain aur `:q` run karoge, `vi` quit se rok sakta hai. Decide karo:

- Changes rakhne hain: `:wq`
- Changes discard karne hain: `:q!`

> `:q!` ko habit se press mat karo; ye current edits discard kar deta hai.

---

## 6. Navigation

Arrow keys kaam kar sakti hain, lekin `vi` keyboard navigation ke shortcuts ke liye famous hai.

### 6.1 Word navigation

| Key | Action |
|---|---|
| `w` | Next word ki taraf move |
| `b` | Previous word ki taraf move |

`vi` ke commands count ke saath combine ho sakte hain. Example:

```text
3w    teen words forward
2b    do words backward
```

Exact cursor landing punctuation aur word-boundary rules par depend kar sakti hai.

### 6.2 Command grammar

Trainer ke examples se ek pattern samjho:

```text
[count] [operation] [target]
```

Example:

```text
3dw
```

- `3` = count
- `d` = delete operation
- `w` = word target

Ye pattern yaad hone par commands compose karna easy hota hai.

---

## 7. Delete aur undo

### 7.1 Character delete

| Key | Action |
|---|---|
| `x` | Cursor ke neeche/current character delete |
| `X` | Cursor se pehle character delete |
| `u` | Last change undo |

### 7.2 Word delete

```text
dw     one word delete
2dw    two words delete
3dw    three words delete
```

### 7.3 Line delete

```text
dd     current line delete/cut
2dd    current line aur next line delete/cut
```

`dd` ke baad deleted line register mein rehti hai, isliye baad mein `p` se paste bhi ki ja sakti hai.

### 7.4 Undo

```text
u
```

Galti se delete/change ho jaye to command mode mein `u` press karke undo try karo. Complex edits mein small checkpoints aur regular saves useful hote hain.

---

## 8. Insert mode ke bina single-character replace

Agar sirf ek typo fix karna ho to insert mode mein jaane ki zarurat nahi:

```text
r<char>
```

Example:

1. Cursor wrong character par rakho.
2. `r` press karo.
3. Correct character press karo.

`rX` current character ko `X` se replace karega. Ye single-character correction ke liye fast hai.

---

## 9. Cut, copy aur paste

`vi` mein line delete (`dd`) practically cut operation ki tarah bhi work kar sakta hai.

| Keys | Action |
|---|---|
| `dd` | Current line cut/delete |
| `2dd` | Two lines cut/delete |
| `p` | Register ka content cursor ke neeche/baad paste |
| `P` | Register ka content cursor ke upar/pehle paste |
| `xp` | Character ko delete karke next position par paste; adjacent characters swap ho sakte hain |

Basic workflow:

```text
dd       line cut
movement destination tak
p        paste
```

> `dd` ko destructive samajhkar use karo, lekin undo/paste register se recovery possible ho sakti hai.

---

## 10. Visual mode

Mouse unavailable ho to text select karne ke liye visual modes use hote hain. Visual mode enter karne se pehle command mode mein hona zaruri hai.

| Key | Mode | Selection |
|---|---|---|
| `v` | Visual | Character-by-character |
| `V` | Visual Line | Complete lines |
| `Ctrl+v` | Visual Block | Rectangular columns/block |

Selection extend karne ke liye arrow keys ya movement commands use kar sakte ho.

### 10.1 Character visual mode — `v`

```text
Esc
v
```

Cursor move karne par characters highlight hote hain. Selected text par `d` press karke delete ya `y` press karke yank/copy kiya ja sakta hai.

### 10.2 Line visual mode — `V`

```text
Esc
V
```

Complete lines select hoti hain. Multiple lines ke saath cut/copy/delete useful hai.

### 10.3 Visual block — `Ctrl+v`

```text
Esc
Ctrl+v
```

Rectangular column select hota hai. Aligned config files ya table-like text mein column edit karne ke liye useful hai.

### 10.4 `v` aur `Ctrl+v` ka difference

- `v` normal flowing text ke characters/lines select karta hai.
- `Ctrl+v` rectangular block select karta hai; har line ka sirf selected column area include hota hai.

Insert mode mein `v` type karoge to wo normal character insert hoga; visual mode ke liye pehle `Esc` press karo.

---

## 11. Search

`vi` ke search keys `less` command ke search behavior se milte-julte hain.

| Command/key | Action |
|---|---|
| `/word` | Forward search |
| `?word` | Backward search |
| `n` | Next match |
| `N` | Previous match |

Example:

```text
/PermitRootLogin
Enter
n
```

Search enter karne ke baad `n` next occurrence aur `N` previous occurrence par le ja sakta hai.

> Day 4 ke `less` search keys yaad hain to `vi` navigation familiar lagegi. Unix tools mein shortcut consistency deliberately useful hoti hai.

---

## 12. File aur command output read karna

Last-line mode se current file mein external content insert kiya ja sakta hai.

### 12.1 Existing file ka content read karna

```text
:r filename
```

Current cursor position par `filename` ka content insert hota hai.

### 12.2 Command output read karna

```text
:r !lsblk
:r !ls -l
```

`!` ke baad shell command run hoti hai aur uska output current file mein insert hota hai.

Useful workflow:

1. Report/notes file `vi` mein open karo.
2. Cursor required location par rakho.
3. `:r !command` run karo.
4. Command output report ka part ban jata hai.

Ye feature command output ko manually copy-paste ya separate redirection ke bina notes mein include karne mein useful hai.

---

## 13. `vi` command cheat sheet

```text
# MODES
Esc              command/normal mode mein return
i / a            cursor se pehle / baad insert
I / A            line start / line end par insert
 o / O           line below / above open
v / V / Ctrl+v   visual / visual-line / visual-block

# SAVE AND QUIT — command mode se
:w               save
:q               quit
:wq              save and quit
:q!              quit without saving
:w newname.txt   save as
ZZ               save and quit shortcut

# NAVIGATION
arrows           character/line movement
w / b            next word / previous word

# DELETE/UNDO
x / X            character under / before cursor
dw / 2dw / 3dw   one / two / three words
dd / 2dd         one / two lines
u                undo

# REPLACE/CUT/PASTE
r<char>          one character replace
p                paste below/after
P                paste above/before
xp               adjacent characters swap pattern

# SEARCH
/word            forward search
?word            backward search
n / N            next / previous match

# READ IN
:r file          file content insert
:r !command      command output insert
```

---

## 14. Practice workflow

Safe practice file banao:

```bash
printf '%s\n' 'first line' 'second line' 'third line' > vi-lab.txt
vim vi-lab.txt
```

Practice sequence:

1. `i` se text insert karo.
2. `Esc`, `:w` se save karo.
3. `w`/`b` se words navigate karo.
4. `dd` se ek line cut karo aur `p` se paste karo.
5. `u` se undo karo.
6. `/line` se search karo; `n` se next match.
7. `:r !date` se current date insert karo.
8. `:wq` se save and quit.

Har operation ke baad file ko `cat vi-lab.txt` se verify karo. `/etc/passwd`, `/etc/sudoers` ya production config files par practice mat karo.

---

## 15. Trainer ki learning advice

Trainer beginner ko teen practical suggestions dete hain:

1. **Cheat sheet/notes rakho.** `vi` commands ek session mein memorize nahi hote.
2. **Daily practice karo.** Regular editing se modes aur commands naturally yaad hone lagte hain.
3. **Gradually familiarity build karo.** Pehle open/insert/save/quit; phir navigation, delete, visual mode, search aur read-in features.

Trainer intentionally beginner level par stop karte hain, kyunki `vi` ka complete course kaafi lamba ho sakta hai. Goal ye hai ki learner essential work kar sake aur editor dekhkar stuck na ho.

---

## 16. Day 11 mein deferred topic

`locate` command ka mention class ke beginning mein hota hai, lekin trainer use is session mein detail se cover nahi karte. Isko package management aur control operators ke saath next class ke context mein continue kiya jata hai.

---

## 17. Common mistakes aur safety points

1. `vi` ko insert mode mein open samajhna; default command mode hota hai.
2. Mode confuse hone par `Esc` na press karna.
3. `:w`, `:q`, `:wq` se pehle command mode mein na hona.
4. `:q!` se unsaved work accidentally discard kar dena.
5. `i`/`a` aur `I`/`A` ka difference bhoolna.
6. `dd` ko delete samajhkar recovery/register behavior ignore karna.
7. `v` ko insert mode mein type karna aur visual selection expect karna.
8. `v` aur `Ctrl+v` ke selection shape ko mix karna.
9. Search ke baad `n`/`N` ka direction bhoolna.
10. `:r !command` ko shell prompt samajhna; ye command output current file mein insert karta hai.
11. Unknown configuration file ko save karke service break kar dena.
12. Practice ke liye real `/etc` files edit karna.
13. SUID/root shell ke context mein editor ko unsafe way se use karna; privileged editor commands carefully review karo.

---

## 18. Self-check questions

1. Security context mein `vi` seekhna kyu useful hai?
2. `vi` ka default mode kya hota hai?
3. Command, insert, last-line aur visual modes ka purpose kya hai?
4. Lost hone par command mode mein kaise return karoge?
5. `i`, `a`, `I`, `A`, `o` aur `O` ka difference batao.
6. Save, quit, save-and-quit aur discard changes ke commands likho.
7. `ZZ` kya karta hai?
8. `x` aur `X` ka difference kya hai?
9. `3dw` ko count/operation/target grammar mein break karo.
10. `dd`, `2dd`, `p` aur `u` ka use explain karo.
11. `r<char>` ko insert mode ke bina typo fix karne ke liye kaise use karoge?
12. `v`, `V` aur `Ctrl+v` mein difference kya hai?
13. Forward/backward search aur next/previous match ke keys likho.
14. `:r file` aur `:r !command` mein difference kya hai?
15. `:r !lsblk` ka output kahan insert hoga?
16. `vi` practice karte waqt real system files avoid kyu karni chahiye?
17. `vi` seekhne ke liye trainer ne kaunse practice habits suggest kiye?

---

## 19. Final takeaway

Day 11 ka core message:

- Minimal Linux machine par `vi`/`vim` available hone ki possibility high hoti hai, isliye security learner ko basic editor skills honi chahiye.
- `Esc` se command mode mein return karna sabse important recovery habit hai.
- Insert mode text typing ke liye, command mode navigation/editing ke liye aur `:` last-line commands ke liye hota hai.
- `i/a/I/A/o/O` insertion ke different positions provide karte hain.
- `dd`, `dw`, `x`, `u`, `p`, visual modes aur search keys daily editing ko fast banate hain.
- `:r file` aur `:r !command` files/command output ko current document mein insert karte hain.
- Cheat sheet aur daily practice se `vi` ka fear gradually khatam hota hai.

Agli classes mein deferred `locate`, package management aur shell control operators cover honge.
