# Day 2 — Kali Linux Capsule Course: File System Hierarchy + Basic Commands (Hinglish Explanation)

**Source transcript:** `transcripts/002 - Kali Linux Free Capsule Course - Day 2 [ Hindi ].hi-orig.srt`  
**Note:** Ye explanation Hindi original transcript ko samajh kar likha gaya hai. Auto-captions mein `पढ़ा`/`फाइल`, `एब्सलूट पाठ`, `एम के दी यार`, `सीडी`, `एलएस`, `टच`, `कैट` jaise shabd garbled mile hain; unka intended technical meaning restore karke simple Hinglish mein explain kiya gaya hai.

---

## 1. Class start — Day 2 mein kya cover hoga?

Trainer pehle request karte hain ki agar content useful lag raha hai to course ko un logo tak forward karo jinko free cyber-security learning ki real need hai. Phir Day 2 ke 2 main parts clear karte hain:

1. **Linux File System Hierarchy** — Day 1 mein bola gaya tha ki root partition `/` ke neeche around 17–19 default directories hoti hain. Aaj un directories ka role samjhenge.
2. **Basic Linux Commands** — file/directory create, delete, copy, move, rename, type check, help/manual, path concepts.

Day 1 ka base yaad rakho: Linux mein random jagah file banana problem create karta hai. Aaj hum samjhenge kaunsi directory kis purpose ke liye bani hai, phir commands seekh kar usi planning ke hisaab se kaam karenge.

---

## 2. Desktop aur terminal chhota sa tour

Class practically Kali Linux machine par hoti hai. Trainer GUI mein batate hain:

- Left/taskbar area mein applications hote hain; “all applications” mein security categories aur tools milte hain.
- Default **text editor** aur **Firefox browser** jaise normal tools bhi installed hote hain.
- Main kaam ke liye **terminal/shell** open kiya jata hai.

Terminal ke useful features:

- **New tab:** ek hi terminal window mein dusra shell tab khol sakte ho. Agar ek tab mein koi task chal raha hai, dusre tab mein parallel kaam kar sakte ho.
- **Split:** terminal ko vertically/horizontally split kar sakte ho, taaki do shells side-by-side dikhen.

---

## 3. Root partition `/` aur `/root` ka difference — bahut important

Yahan beginners ka common confusion clear hota hai:

- **`/` (forward slash)** = root partition, parent folder/partition. Iske upar kuch nahi hai. Saara OS-defined aur user-defined data isi ke neeche aata hai.
- **`/root`** = super user `root` ka home directory. Ye root user ka private place hai.

Matlab dono ko log “root” bol dete hain, but dono same nahi hain. Day 1 wala point dobara yaad karo: around 17–19 default directories mein se sirf 2 user-home side hoti hain — `/root` root ke liye, `/home` normal users ke liye.

Trainer ek aur important baat repeat karte hain: directories pehle se purpose ke hisaab se aur permissions/policies ke saath define hoti hain. Koi program download/install/execute kahan hoga, uski config files mein ye bataya hota hai. Aap technically chahe `/boot`, `/media`, `/mnt` ya kisi aur directory mein bhi file bana lo, lekin wo directory usi purpose ke liye nahi bani; permission/breakage issue aa sakta hai. Comfortable kaam ke liye Linux ke planning ko follow karo.

---

## 4. File System Hierarchy — `/` ke neeche ki main directories

Trainer root partition par ja kar directories dikhate hain aur ek-ek ka role batate hain. Kuch captions garbled hain, lekin standard Linux hierarchy ke hisaab se intended meaning ye hai:

### 4.1 `/bin` — user binaries/commands

`/bin` mein binary executable files hoti hain — matlab commands/programs ki machine-runnable files.

- Koi bhi command run karne ke liye uske instructions program form mein hote hain.
- Program ko machine par chalane ke liye wo binary form (0/1) mein converted executable hota hai.
- Isliye common commands ki program files yahan mil sakti hain. Trainer `/bin` ke andar list dikhate hain.

Modern Kali/Debian systems mein `/bin` aksar `/usr/bin` ka symlink hota hai. Iska proof aage `ls -l /` mein arrows se bhi dikhaya jata hai.

### 4.2 `/boot` — boot loader aur boot sequence files

`/boot` mein booting se related cheezein hoti hain:

- **boot loader program** (jaise GRUB related files)
- kernel boot ke liye zaroori config/files
- boot sequence/configuration

Trainer boot sequence simple Hinglish mein samjhate hain: power button dabate hi current flow hota hai, machine boot start karti hai, POST/hardware checks hote hain, phir kernel aur hardware modules/drivers load hote hain, components sequence mein start hote hain. Linux/UNIX machine boot karte waqt black screen par lines chalti dikh sakti hain — wo sequence checks/services ko dikhati hain. `/boot` ke andar `config-<kernel-version>` jaise files aur boot loader configuration mil sakti hai.

### 4.3 `/dev` — device files

`/dev` = device files ki directory. Linux mein hardware aur software ke beech interface ka kaam device files karti hain.

Important concept: **Linux mein har cheez file hoti hai** — hard disk, pen drive, terminal, audio device, etc. Hardware ka data do common tareeke se flow hota hai:

- **Block form** — data chunks/blocks mein transfer hota hai (disk-type devices).
- **Character form** — data character/stream ki tarah hota hai (mic/speaker jaise stream example diya gaya).

`ls -l /dev` karne par first character se file type identify hota hai:

| First char | Meaning |
|---|---|
| `d` | directory |
| `c` | character device/file |
| `b` | block device/file |
| `s` | socket file |
| `l` | symlink/link |

Isliye `/dev` mein hardware-related interface files milti hain; inhe normal text files ki tarah samajh kar edit nahi karna chahiye.

### 4.4 `/etc` — system configuration/settings

`/etc` mein system settings aur configuration files hoti hain. Services, programs aur system behaviour ke config yahan milte hain. Trainer ke “system ki jo settings hoti hain wo yahan milti hain” line ka intended meaning `/etc` hai.

Baad mein jab aap web server, SSH, users, networking ya services configure karoge, to `/etc` ke andar ki config files bahut important hoti hain.

### 4.5 `/home` — normal users ka private area

`/home` ke andar sab normal users ke home directories hote hain. Agar machine par sirf ek normal user `kali` hai, to `/home/kali` dikhega. Agar 2, 5, 10 users banaye, sab `/home` ke andar apne-apne folders mein milenge.

Day 1 ke public/private concept se link: `/home/<username>` normal user ka private place hai.

### 4.6 `/lib` aur `/lib64` — library files

`/lib` mein shared library files hoti hain jo applications/commands ko run hone ke liye chahiye. Example: web server run ho raha hai to uski required libraries aur uske related modules ki files system library locations mein hoti hain.

Modern systems mein bhi `/lib` aur `/lib64` kai baar `/usr/lib` / `/usr/lib64` ke symlink hote hain. Ye symlink concept aage `ls -l` mein dikhaya jata hai.

### 4.7 `lost+found` — crash ke baad recovered fragments

`lost+found` ext filesystems par milta hai. Jab system sudden off ho jata hai, battery khatam ho jati hai, ya machine crash ho jati hai, to running programs/files properly close nahi hote. Filesystem check/recovery ke waqt kuch recovered fragments `lost+found` mein aa sakte hain.

Trainer isko digital forensics se jodte hain: agar system crash hua aur pata karna hai ki kaunsi process/file ki wajah se problem aayi, to kabhi-kabhi useful fragments/recovered information yahan mil sakti hai. Guarantee nahi hoti, lekin forensics ke time ye directory interesting ho sakti hai.

### 4.8 `/media` — removable media auto-mount point

`/media` removable media se related hai — CD/DVD drive, USB/pen drive jaise media auto-mount hone par yahan entry aa sakti hai. Aaj kal CD drive rare hai, but concept same hai: removable media ko access karne ke liye use mount hona zaroori hai.

### 4.9 `/mnt` — manual mount point

`/mnt` = mount. Jab aap khud kisi ISO image, pen drive, extra hard disk ya local repository ko manually mount karte ho, to traditionally `/mnt` use hota hai.

Mount ka meaning trainer analogy se samjhate hain: ek kamra hai, agar usme darwaza hi nahi hai, to andar kaise jaoge? Waahi tarah storage device ko mount karna matlab us tak pahunchne ka rasta banana. Jab tak device mount nahi hota, uske andar data flow/access nahi hota.

Example use cases transcript style mein:

- ISO image mount karna
- local repository configure karna
- corrupt program/kernel recovery ke liye media attach karna
- pen drive/hard disk insert kar ke use `/mnt` ke neeche mount karna

### 4.10 `/opt` — optional/third-party software

`/opt` optional software ke liye hota hai. Third-party tools/packages ko yahan install kar sakte ho. Kali mein kai security tools separately `/opt` mein bhi mil sakte hain.

### 4.11 `/proc` — live process/kernel information

Trainer jab “ye program directory directly kernel se update hoti hai” bolte hain, intended directory `/proc` hai. `/proc` ek virtual filesystem hai jisme running processes aur kernel-related live information hoti hai.

- Processes ki real-time state yahi se milti hai.
- `top`, `ps`, process status jaise commands background mein `/proc` ka reference lekar output dikhate hain.

Ye normal storage directory nahi hai; yahan ki files kernel/runtime information ko represent karti hain.

### 4.12 `/root` — root user ka home

`/root` super user ka home directory hai. Trainer andar ja kar dikhate hain: Desktop, Documents, Downloads, Music etc. — normal user ke home jaise hi structure, lekin ye root ka private place hai.

### 4.13 `/sbin` — superuser binaries

`/sbin` mein bhi binary files hoti hain, lekin ye wahi commands/programs hote hain jinhe generally **root/superuser** run kar sakta hai. Normal user ke daily commands `/bin`, administration/system commands `/sbin` side hote hain. Modern systems mein `/sbin` bhi `/usr/sbin` ka symlink ho sakta hai.

### 4.14 `/srv` — service/served data

`/srv` ko trainer serving directory ki tarah explain karte hain. Agar FTP, NFS, proxy ya koi server/service configure ki hai, to users ko serve karna ya temporarily hold karna wala data service ke purpose ke hisaab se yahan rakh sakte ho. Idea: jaise cache memory speed badhati hai, waise service data organized rakha jata hai taaki service fast response de.

### 4.15 `/sys` — kernel/hardware subsystem info

`/sys` bhi virtual filesystem hai jisme kernel aur hardware se related information hoti hai. Trainer andar ja kar entries dikhate hain jaise:

- `block` — block devices
- `bus` — data lanes/buses related
- `class` — device classes
- `firmware`
- kernel modules/drivers related information

Purpose: basic pata hona chahiye ki kernel/hardware details kahan milti hain. One-day mein pura deep dive nahi; use karte-karte familiarity aati hai.

### 4.16 `/tmp` — temporary directory with sticky bit

`/tmp` temporary directory hai. Har user yahan apna temporary kaam kar sakta hai. Lekin important rule: jis user ne file create ki, wahi us file ko delete kar sakta hai; dusra normal user us file ko delete nahi kar sakta. Root alag baat hai.

Reason: `/tmp` par **sticky bit** set hota hai. Isliye shared temporary space hone ke baawajood users ek dusre ki files delete nahi kar paate.

Example: `kali` user ne `/tmp` mein file banayi; baad mein `sachin` user aakar sab users ki files delete nahi kar sakta. Files temporary nature ki hoti hain aur cleanup ho sakta hai.

### 4.17 `/usr` — user system resources

`/usr` ke andar binary files, library files, documentation, local data jaise resources milte hain. Trainer batate hain ki asli files aksar `/usr` ke neeche hoti hain aur root-level `/bin`, `/lib`, etc. unke shortcuts/symlinks ho sakte hain.

Modern layout example:

- `/bin` → `/usr/bin`
- `/sbin` → `/usr/sbin`
- `/lib` → `/usr/lib`
- `/lib64` → `/usr/lib64`

Isliye same binary root par bhi dikhti hai kyunki symlink root partition ke neeche rakh hota hai.

### 4.18 `/var` — variable files

`/var` mein wo files hoti hain jo time-to-time change hoti rehti hain — variable data. Examples transcript style: mail files, cache, logs, spool type data. Web server ki files bhi usually `/var/www` ke under milti hain.

Short rule: `/etc` config, `/var` changing operational data/logs.

---

## 5. Symlink aur `ls -l /` ka output

Trainer `ls -l /` jaisa output dikhate hain. Usme aapko columns milte hain:

```text
permissions  links  user  group  size  timestamp  name
```

Aur kuch entries mein arrow hota hai:

```text
bin -> usr/bin
lib -> usr/lib
lib64 -> usr/lib64
vmlinuz -> boot/vmlinuz-...
initrd.img -> boot/initrd.img-...
```

Iska matlab ye entries hard/direct copy nahi, balki links hain. Link/hard link ke detail next classes mein aayenge; abhi ke liye bas itna samjho: root par dikhne wali kuch entries actual location ka shortcut hain.

---

## 6. Navigation commands — `cd`, `pwd`, `ls`, absolute vs relative path

### 6.1 `cd` — change directory

`cd` sirf directory ke andar jaane ke liye hota hai; file ka naam nahi dete.

```bash
cd /dev
cd /home
```

Windows GUI mein folder par double-click karke andar jaate ho; Linux CLI mein `cd` se jaate ho.

### 6.2 `pwd` — present working directory

`pwd` batata hai aap current mein kahan ho.

```bash
pwd
# output example: /root/Downloads
```

New/latest Kali prompt full path dikhata hai, lekin purani UNIX-style systems ya minimal setups sirf current folder dikh sakte hain; isliye `pwd` important hai.

### 6.3 Absolute path vs Relative path

**Absolute path** root `/` se start hota hai. Isse aap kisi bhi current location se target tak pahunch sakte ho.

```bash
cd /root/Downloads
cd /tmp
```

**Relative path** current directory ke relative hota hai.

```bash
cd Downloads     # tabhi chalega jab Downloads current ke andar ho
```

Trainer example: aap `/root` home mein ho; `cd Downloads` chal jayega kyunki `Downloads` current ke neeche hai. Agar aap aur jagah ho aur seedha `cd Downloads` doge to error dega; wahan absolute path dena safe hai.

### 6.4 Useful `cd` shortcuts

```bash
cd /      # root partition par jao
cd ~      # apni home directory mein jao
cd -      # previous directory par wapas jao
```

`.` aur `..`:

| Symbol | Meaning |
|---|---|
| `.` | current directory ka address hold karta hai |
| `..` | parent/previous directory ka address hold karta hai |

Ye entries hidden hoti hain; `ls -a` se dikhti hain.

### 6.5 `ls` — list files/directories

Basic:

```bash
ls
ls /etc
ls -a
ls -l
ls -la
```

- `ls` current directory list karta hai, ya path dene par us directory ko.
- `-a` hidden files including `.` aur `..` dikhata hai (captions mein `-A` bhi bola gaya; dono ka use hidden listing context mein hota hai, `-A` `.`/`..` ko usually skip karta hai).
- `-l` long listing detail deta hai: permissions, links, user, group, size, timestamp, name.
- flags combine ho sakte hain: `ls -la`.

### 6.6 Help aur manual

Command ka use nahi aata to help/manual dekho:

```bash
ls --help
man ls
```

`--help` short usage/options deta hai. `man` manual page hai — detailed reference; usme scroll karke padh sakte ho. Linux ki beauty yehi hai: command yaad ho to details help/manual se recover ho jati hain.

### 6.7 Tab-completion — typing shortcut

Agar `D` type kar ke `TAB` dabate ho, shell matching names dikhata hai — Desktop, Documents, Downloads. Agar `Do` ke baad `TAB` dabao, to unique match `Documents` complete ho sakta hai.

Points:

- Poora naam baar-baar type karne ki zaroorat nahi.
- Linux **case-sensitive** hai; spelling/case galat hua to completion/execute nahi hoga.
- Cyber-security/Linux speed ke liye tab completion must-have habit hai.

---

## 7. Directory create/remove — `mkdir`, `rmdir`, `rm -r`

### 7.1 `mkdir` — directory create

```bash
mkdir capsule_course
mkdir /tmp/unix
```

Absolute path dene se aap current location se bahar bhi directory bana sakte ho. Trainer sit-na-wise dikhate hain: pehle `cd /tmp` karne ki zaroorat nahi; direct `mkdir /tmp/unix` kar sakte ho.

Parent-child chain banana:

```bash
mkdir -p /tmp/unix1/linux/commands
```

`-p` matlab parents: agar `/tmp/unix1` ya `/tmp/unix1/linux` nahi hai, to pehle bana do, phir final `commands` bana do.

### 7.2 `rmdir` — sirf empty directory remove

```bash
rmdir capsule_course
```

Agar directory empty nahi hai, `rmdir` fail karega: “Directory not empty”.

### 7.3 Non-empty directory remove — `rm -r`, safety warning

```bash
rm -r /tmp/unix1
```

`-r` recursive hai — starting se last tak andar ki files/subdirectories bhi delete karega.

Trainer strong advice dete hain: `rm -rf` bahut powerful aur dangerous hai. Beginner ho to jab tak confidently hands-on na ho jao, use mat karo. Ek space/path mistake system uda sakta hai. Example danger: path likhte waqt extra space aa jaye aur command arguments ko alag-alag samajh le; galat jagah recursive delete chala de. Force options se bachna aur pehle path verify karna safe practice hai.

---

## 8. File create/timestamps — `touch`, `stat`

### 8.1 `touch` ka main purpose

Kaafi log `touch` ko sirf empty file create karne ke liye samajhte hain, lekin transcript mein trainer clarify karte hain: **`touch` ka main purpose timestamp update karna hai.** Empty file create hona side-effect ho sakta hai, but editing/file creation ke liye `nano`, editors, ya `cat > file` jaise tareeke bhi hain.

Har file ke saath timestamps judte hain:

| Timestamp | Meaning in easy Hinglish |
|---|---|
| **Access time (atime)** | file ko last kab open/access kiya gaya |
| **Modify time (mtime)** | file ke content/data ko last kab edit/modify kiya gaya |
| **Change time (ctime)** | file ka metadata last kab change hua — permissions, location, name, inode info etc. |
| **Birth time** | file kab create hui (support filesystem/tool par depend karta hai) |

Inhe dekhne ke liye:

```bash
stat file.txt
```

`stat` access/modify/change/birth jaise times dikhata hai.

### 8.2 `touch` ke flags

```bash
touch file1 file2 file3     # multiple files create/update
touch file1                 # access+modify time update (ctime bhi change ho sakta hai)
touch -a file2              # sirf access time update
touch -m file3              # sirf modify time update
```

Important: `change time (ctime)` ko `touch` seedha set nahi karta; jab access/modify/metadata kuch bhi change hota hai to ctime apne aap update ho jata hai.

---

## 9. `cat` — content read, combine, aur file create

`cat` ka matlab **concatenate**. Ye mainly content read karne/jodne ke liye hota hai, but redirection ke saath file create/edit bhi kar sakta hai.

### 9.1 File create + likhna

```bash
cat > newfile.txt
```

Ab jo type karoge wo file mein jayega. End karne ke liye:

```text
Ctrl + D
```

### 9.2 Content read

```bash
cat newfile.txt
```

### 9.3 Do files ka data combine karna

```bash
cat file1.txt file2.txt > combined.txt
```

Trainer style mein: pehli file ka content + dusri file ka content ek nayi/destination file mein likh diya jata hai.

---

## 10. File remove — `rm`

Files remove karne ke liye:

```bash
rm file1.txt
rm /tmp/file3.txt
```

Path absolute ya relative de sakte ho.

Common flags discussed:

```bash
rm -f file        # forcefully remove, confirmation kam
rm -i file        # interactive — har delete se pehle poochhe
rm -r dir         # recursive — directory tree delete
rm -d emptydir    # empty directory remove
```

Beginner ke liye `rm -i` useful hai, kyunki delete se pehle confirm karne ka mauka deta hai — galti se delete hone se bachata hai.

---

## 11. Copy aur Move — `cp`, `mv`

### 11.1 `cp` — copy

```bash
cp /root/file3.txt /tmp/
cp -r /tmp/unix1 /backup/
```

Tips: jab confusion ho to absolute path use karo. Directory copy karne ke liye recursive `-r` lagana padta hai.

### 11.2 `mv` — move ya rename

Same command move aur rename dono karti hai:

```bash
mv file3.txt newfile.txt          # same location mein rename
mv newfile.txt /tmp/renamed.txt   # /tmp mein move + new name
```

Matlab destination path ke hisaab se `mv` decide karta hai: same dir new name = rename; dusri directory = move; dusri directory + new name = move with rename.

---

## 12. File type check — `file`

Kabhi extension dekh kar samajh nahi aata file actual mein kya hai. `file` command type batati hai:

```bash
file image.jpg
file suspicious
file unknown
```

Security work mein useful hai, kyunki attacker ya user extension badal sakta hai; `file` content/magic bytes ke base par better idea deta hai.

---

## 13. Day 2 final takeaway

1. `/` root partition hai; `/root` root user ka home hai — dono alag.
2. `/` ke neeche ki default directories ka predefined purpose hota hai; unko randomly personal dumping ground mat banao.
3. `/bin`, `/sbin` binaries; `/lib` libraries; `/etc` config; `/var` changing logs/cache/mail; `/tmp` temporary shared + sticky bit; `/dev` hardware interface; `/proc` `/sys` live kernel/hardware/process info; `/root` aur `/home` private user areas.
4. `/media` removable media auto-mount, `/mnt` manual mount ke liye.
5. Modern systems mein root-level kuch directories `/usr` ke symlinks hoti hain; `ls -l` mein arrow se pehchano.
6. `cd`, `pwd`, `ls`, `mkdir`, `rmdir`, `touch`, `stat`, `cat`, `rm`, `cp`, `mv`, `file` Day 2 ke working commands hain.
7. Sabse bada safety lesson: destructive commands — especially recursive/force remove — se pehle path double-check karo. Absolute path, tab completion, `--help`, aur `man` tumhe fast + safe banate hain.

Trainer end mein bolte hain: agla session isi command line ko continue karega. Aaj ka goal tha ki file-system hierarchy aur basic CRUD/navigation commands clear ho jayein.
