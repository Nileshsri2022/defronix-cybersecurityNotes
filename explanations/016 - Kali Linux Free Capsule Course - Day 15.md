# Kali Linux Day 15 — SSH, Encryption aur SSH Hardening (Hinglish Explanation)

**Source transcript:** `transcripts/016 - Kali Linux Free Capsule Course - Day 15 [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Course context:** Kali Linux capsule course ka final session; OSINT series transcript 015 ke baad interleaved hai.
**Builds on:** Day 7–10 users, groups, permissions; Day 12 package management; Day 14 password/boot security
**Note:** Ye explanation Hindi original transcript ko context ke saath samajh kar likhi gayi hai; ye literal translation nahi hai. SSH commands aur hardening examples sirf owned/authorized lab machines ke liye hain. Production SSH configuration change se pehle backup, alternate access aur syntax validation zaruri hai.

---

## 1. Day 15 ka focus

Final Kali capsule session ka main topic **SSH — Secure Shell** hai:

- SSH kya hai aur remote communication kaise hoti hai?
- Encryption ka basic concept
- Symmetric vs asymmetric encryption
- `openssh-server` installation/service management
- `ssh` se remote login aur remote command
- `scp` se secure file copy
- SSH key-based/passwordless authentication
- `sshd_config` ke through SSH hardening
- Root login, port, allowed users/groups aur source restrictions

Trainer ka practical point hai ki security lab/CTF/server work mein remote shell aur secure file transfer ka knowledge foundational hai.

---

## 2. SSH kya hota hai?

**SSH = Secure Shell.**

Ye network protocol hai jo do computers ke beech encrypted communication, remote shell aur secure data transfer provide karta hai.

Practical VM scenario:

1. Kali VM background mein run ho rahi hai.
2. Aap host OS terminal se VM par connect karna chahte ho.
3. VM window switch karne ke bajay SSH session open karte ho.

```bash
ssh username@ip_address
```

SSH ke through:

- remote terminal mil sakta hai,
- commands run kar sakte ho,
- files securely transfer kar sakte ho,
- automation/scripts se multiple systems manage kar sakte ho.

### 2.1 “Secure” kyu?

SSH client aur server ke beech encrypted channel/tunnel establish karta hai. Network par captured traffic normally readable plaintext session ki tarah nahi hota.

Encryption confidentiality provide karti hai, lekin security complete tab hoti hai jab:

- host identity verify ho,
- keys/passwords protected hon,
- server patched/hardened ho,
- access scope limited ho.

---

## 3. Encryption fundamentals

### 3.1 Encryption kya hai?

Plaintext ko aise transformed form mein convert karna jo unauthorized viewer ke liye unreadable ho, encryption ka basic idea hai.

```text
Plaintext + key -> ciphertext
ciphertext + required key -> plaintext
```

### 3.2 Symmetric encryption

Symmetric encryption mein same secret key encryption aur decryption ke liye use hoti hai.

| Feature | Symmetric |
|---|---|
| Keys | One shared secret key |
| Speed | Usually fast |
| Challenge | Key ko securely share karna |

Agar key network par unsafe way se share ho gayi, to confidentiality break ho sakti hai.

### 3.3 Asymmetric encryption

Asymmetric cryptography mein key pair hota hai:

- **Public key** — share ki ja sakti hai.
- **Private key** — owner ke paas secret rehni chahiye.

Conceptual flow:

```text
User A public/private key pair generate karta hai.
User A public key User B ko deta hai.
User B public key se data encrypt karta hai.
User A private key se decrypt karta hai.
```

Private key ke bina captured ciphertext ko decrypt karna intended model ke according possible nahi hona chahiye.

### 3.4 Lock-and-key analogy

- Public key ko aise lock ki tarah imagine karo jo share kiya ja sakta hai.
- Koi bhi us lock se box lock kar sakta hai.
- Private key owner ke paas rahti hai aur wahi box open karta hai.

SSH actual operation mein public-key authentication, key exchange, symmetric session encryption aur host verification ke multiple mechanisms combine karta hai. Beginner level par public/private key distinction yaad rakhna important hai.

---

## 4. SSH install aur service management

Kali/Debian system par SSH server package install karna:

```bash
sudo apt update
sudo apt install openssh-server
```

SSH server daemon ka naam commonly `sshd` hai aur service unit `ssh` ho sakti hai.

### 4.1 `systemctl`

```bash
sudo systemctl status ssh
sudo systemctl start ssh
sudo systemctl stop ssh
sudo systemctl restart ssh
```

### 4.2 `service` compatibility command

```bash
sudo service ssh status
sudo service ssh start
sudo service ssh stop
sudo service ssh restart
```

Service running aur listening port verify:

```bash
systemctl is-active ssh
ss -lntp | grep ':22'
```

Exact process/port output system version par depend karega.

### 4.3 VM networking

Remote host se VM tak connection ke liye VM network adapter correctly configured hona chahiye. Trainer bridged mode ka example dete hain, jisme VM LAN par accessible IP le sakti hai.

NAT mode mein host-to-guest access ke liye port forwarding required ho sakti hai. Host-only mode internet/LAN connectivity ko restrict kar sakta hai.

Check:

```bash
ip addr
ip route
hostname -I
```

Firewall/security group bhi port access block kar sakta hai.

---

## 5. SSH configuration files

SSH related files commonly:

```text
/etc/ssh/
```

### 5.1 Client vs server configuration

| File | Role |
|---|---|
| `/etc/ssh/ssh_config` | Client-side outgoing SSH configuration |
| `/etc/ssh/sshd_config` | Server daemon configuration; hardening yahan |
| `/etc/ssh/ssh_host_*` | Server host identity key files |

`sshd_config` mein `d` daemon ko indicate karta hai. Server-side changes ke baad SSH daemon reload/restart karna pad sakta hai.

Config syntax check:

```bash
sudo sshd -t
```

Backup:

```bash
sudo cp -a /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
```

Remote production machine par restart se pehle current session open rakho, warna bad config se lockout ho sakta hai.

---

## 6. Remote login

```bash
ssh username@ip_address
ssh username@hostname
```

Example format:

```bash
ssh kali@192.168.1.148
```

First connection par host-key confirmation prompt aa sakta hai. Host fingerprint ko trusted source se verify karke hi accept karo; blindly `yes` press karna man-in-the-middle risk create kar sakta hai.

Remote machine verify:

```bash
hostname
echo "$USER"
pwd
```

Client tools ke roop mein terminal SSH, MobaXterm aur PuTTY ka mention hota hai. Tool choice OS/platform par depend karegi.

---

## 7. Login ke bina remote command

SSH command ke end par remote command pass kar sakte ho:

```bash
ssh kali@192.168.1.148 hostname
ssh kali@192.168.1.148 pwd
```

Ye interactive shell open karne ke bajay remote command run karke output local terminal par print karta hai.

Use cases:

- remote hostname/uptime check,
- service status collect,
- script automation,
- multiple authorized machines ka inventory.

Example:

```bash
ssh user@server 'systemctl is-active ssh'
```

Remote command quoting carefully use karo; local shell expansion aur remote shell expansion alag stages par ho sakti hai.

---

## 8. `scp` — secure file copy

`scp` SSH transport use karke files copy karta hai.

Local se remote:

```bash
scp /absolute/path/report.txt user@server:/home/user/
```

Remote se local:

```bash
scp user@server:/home/user/report.txt /tmp/
```

Directory recursive copy:

```bash
scp -r /path/to/directory user@server:/destination/
```

### 8.1 Colon ka role

Remote destination format mein colon mandatory separator hai:

```text
user@server:/remote/path
```

Colon miss karne par `scp` target ko local filename/path samajh sakta hai.

### 8.2 Absolute paths aur security

Absolute path confusion reduce karta hai. Copy se pehle:

- destination path verify,
- file sensitivity check,
- permissions/ownership review,
- authorized endpoint confirm
karo.

SSH encryption transport ko protect karta hai, lekin wrong destination ya compromised endpoint se data automatically safe nahi ho jata.

---

## 9. SSH key-based authentication

Password repeatedly type karna shoulder-surfing aur password-reuse risk create kar sakta hai. SSH key pair se passwordless/key-based login possible hai.

### 9.1 `.ssh` directory

Client par:

```bash
mkdir -m 700 ~/.ssh
```

Agar directory already hai:

```bash
chmod 700 ~/.ssh
```

SSH private files ke permissions strict hone chahiye. Exact files/permissions ko `ls -la ~/.ssh` se check karo.

### 9.2 Key pair generate karna

```bash
ssh-keygen
```

Prompts:

1. Key file location — default accept kar sakte ho.
2. Passphrase — strongly recommended, especially private key theft risk ke against.

Typical files:

```text
~/.ssh/id_rsa       private key
~/.ssh/id_rsa.pub   public key
```

Modern systems Ed25519 default/strong option offer kar sakte hain:

```bash
ssh-keygen -t ed25519
```

Transcript RSA naming par focus karta hai; actual system ke supported algorithm aur policy follow karo.

### 9.3 Private key kabhi share mat karo

| File | Share? | Meaning |
|---|---|---|
| `id_rsa` / private key | **Never** | Secret authentication key |
| `id_rsa.pub` / public key | Target server par install kar sakte ho | Login authorization material |

Private key copy ho jaye to attacker key ka misuse kar sakta hai. Passphrase private key ko extra protection deti hai, lekin private key theft ko ignore nahi karna chahiye.

### 9.4 `known_hosts`

Client ki:

```text
~/.ssh/known_hosts
```

file previously contacted server host keys/fingerprints store kar sakti hai. First connection par fingerprint verify karo. Unexpected host-key change warning ko blindly bypass mat karo; DNS/IP reuse, reinstallation ya MITM possibilities investigate karo.

### 9.5 `ssh-copy-id`

Public key server ke authorized keys mein install karne ka common helper:

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub username@server
```

Target server par public key commonly yahan append hoti hai:

```text
~/.ssh/authorized_keys
```

Verify:

```bash
cat ~/.ssh/authorized_keys
```

File permissions:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
```

Ab test:

```bash
ssh username@server
```

Passphrase set hai to key passphrase prompt aa sakta hai; ye account password prompt se different hai.

### 9.6 Key files ka recap

| File | Machine | Role |
|---|---|---|
| `id_rsa` | Client | Private key |
| `id_rsa.pub` | Client/authorized distribution | Public key |
| `authorized_keys` | Server | Allowed public keys |
| `known_hosts` | Client | Known server host keys |

---

## 10. SSH hardening

Server hardening generally `/etc/ssh/sshd_config` mein hoti hai. Change ke baad:

```bash
sudo sshd -t
sudo systemctl restart ssh
```

Agar remote server hai to alternate session open rakho aur new session test karo before closing old one.

### 10.1 Root login disable

```text
PermitRootLogin no
```

Config file mein setting uncomment/define karne ke baad test:

```bash
sudo sshd -t
sudo systemctl restart ssh
```

Effect: root direct SSH login refuse ho sakta hai, even if root password correct ho. Normal user login karke authorized `sudo` use karna safer model hai.

Exact effective settings dekhne ke liye:

```bash
sudo sshd -T | grep -i permitrootlogin
```

### 10.2 Default port change

Default SSH port commonly `22` hai. Example:

```text
Port 5152
```

Connect:

```bash
ssh -p 5152 user@server
```

Port change automated scans/noise reduce kar sakta hai, lekin ye **security through obscurity** hai. Full port scan se non-default port discover ho sakta hai. Strong authentication, patching, firewall, rate limiting aur logging required hain.

Port choose karne se pehle ensure karo ki:

- port free hai,
- firewall rule updated hai,
- service actually listen kar rahi hai,
- alternate connection tested hai.

### 10.3 `AllowUsers`

```text
AllowUsers user1 user2
```

Sirf listed users ko SSH login allow karne ka policy intent hai.

### 10.4 `DenyUsers`

```text
DenyUsers unwanted-user
```

Listed users ko block karne ka policy intent hai.

### 10.5 Source restriction examples

```text
AllowUsers user1@192.168.1.39
DenyUsers user2@192.168.1.39
DenyUsers *@192.168.1.0/24
```

Syntax/version behavior ko `man sshd_config` se verify karo. Network restriction ke liye firewall par bhi policy enforce karo; SSH config alone par depend mat karo.

### 10.6 Group-based access — `AllowGroups`

```text
AllowGroups sshusers
```

Day 7 ke group-management principle ka direct use:

1. `sshusers` group create karo.
2. Authorized users ko group mein add karo.
3. `AllowGroups sshusers` configure karo.
4. New user add/remove karne ke liye membership change karo, config line nahi.

```bash
sudo groupadd sshusers
sudo usermod -aG sshusers user1
```

Group membership new login/session mein effective ho sakti hai. Config syntax validate karke service reload/restart karo.

---

## 11. SSH hardening checklist

### Authentication

- Root direct login disable.
- Password login ki need assess karo; key-only policy carefully test karo.
- Private keys passphrase se protect.
- Weak/reused passwords avoid.
- Authorized keys review.

### Authorization

- `AllowUsers` ya `AllowGroups` se scope restrict.
- Old employees/unused accounts remove/lock.
- `authorized_keys` stale entries audit.
- Sudo access aur SSH access separately review.

### Network

- Firewall se SSH source network restrict.
- Non-default port optional noise reduction only.
- Internet-facing SSH par rate limiting/fail2ban type controls policy ke according.
- Logs monitor.

### Operations

- `sshd -t` before restart.
- Config backup.
- Alternate session open.
- New settings test.
- Emergency recovery access documented.

---

## 12. Day 15 command summary

```bash
# Install and service
sudo apt update
sudo apt install openssh-server
sudo systemctl status ssh
sudo systemctl start ssh
sudo systemctl restart ssh

# Check network/listening
ip addr
hostname -I
ss -lntp | grep ssh

# Validate config
sudo sshd -t
sudo sshd -T

# Remote access
ssh user@server
ssh -p 5152 user@server
ssh user@server hostname
ssh user@server 'pwd && id'

# Copy
scp /absolute/file user@server:/absolute/destination/
scp user@server:/absolute/file /local/destination/
scp -r /local/dir user@server:/remote/path/

# Key authentication
mkdir -m 700 ~/.ssh
ssh-keygen -t ed25519
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 600 ~/.ssh/authorized_keys

# Server-side hardening in /etc/ssh/sshd_config
PermitRootLogin no
Port 5152
AllowUsers user1 user2
AllowGroups sshusers
```

---

## 13. Common mistakes aur safety points

1. `ssh_config` aur `sshd_config` ko same samajhna.
2. SSH server install karke service/listening port verify na karna.
3. First host-key prompt ko blindly accept karna.
4. Private key `id_rsa` share/upload kar dena.
5. `.ssh`/`authorized_keys` permissions too broad rakhna.
6. Key passphrase na lagana jab private key theft risk high ho.
7. `scp` remote path mein colon miss karna.
8. SSH config edit karke `sshd -t` run na karna.
9. Remote SSH service restart karte waqt alternate access/session na rakhna.
10. Non-default port ko complete security solution samajhna.
11. `AllowUsers`/`AllowGroups` ke baad required admin account lock kar dena.
12. Firewall/network policy update kiye bina port change karna.
13. Root SSH disable karke normal user + sudo recovery test na karna.
14. `authorized_keys` mein unknown keys ko ignore karna.
15. SSH commands ko unauthorized machines par run/test karna.

---

## 14. Self-check questions

1. SSH ka full form aur main purpose kya hai?
2. Remote VM ke liye SSH convenient kyu hai?
3. Encryption kya hai? Symmetric aur asymmetric encryption compare karo.
4. Public/private key ka lock analogy explain karo.
5. `openssh-server` package aur `ssh` service ka relation kya hai?
6. `ssh_config` aur `sshd_config` mein difference kya hai?
7. `sshd` mein `d` ka meaning kya hai?
8. Remote login command aur remote one-command execution command likho.
9. `scp` syntax mein colon ka role kya hai?
10. `scp -r` kab use hota hai?
11. `id_rsa`, public key, `authorized_keys` aur `known_hosts` kaunse machine par hote hain?
12. `ssh-copy-id` kya karta hai?
13. `.ssh` aur `authorized_keys` ki permissions strict kyu honi chahiye?
14. `PermitRootLogin no` ka effect kya hai?
15. SSH port change security ka complete solution kyu nahi?
16. `AllowUsers`, `DenyUsers` aur `AllowGroups` ka purpose compare karo.
17. `sshd -t` restart se pehle kyu run karna chahiye?
18. SSH hardening ke liye firewall, keys, groups aur logging ka role kya hai?
19. Remote config change mein lockout avoid karne ke liye workflow kya hoga?
20. Public SSH server par authorized keys audit kyu zaruri hai?

---

## 15. Kali Linux capsule course ka conclusion

15-session course ka progression:

| Sessions | Main theme |
|---|---|
| Days 1–2 | Linux history, filesystem hierarchy, basic commands |
| Days 3–6 | Redirection, pipelines, `sed`, `grep`, `awk`, `cut`, compression |
| Days 7–8 | Users, groups, sudo, password management |
| Days 9–10 | Standard/advanced file security and `find` |
| Days 11–14 | `vi`, packages, variables, globbing, history, `sort`, `uniq` |
| Day 15 | SSH, encryption, remote access and hardening |

Trainer learners se feedback, comments aur reports continue karne ko kehte hain. Course ka next roadmap OSINT series hai, jiske Day 1 ka transcript number 015 hai.

---

## 16. Final takeaway

- SSH encrypted remote shell aur secure file-transfer workflow provide karta hai.
- Key-based authentication mein public key share hoti hai, private key protected rehti hai.
- `ssh_config` client aur `sshd_config` server behavior control karte hain.
- `scp` remote files transfer karta hai; destination syntax mein colon important hai.
- Root login disable, allowed users/groups, key protection, firewall aur logging SSH hardening ke layers hain.
- Non-default port sirf noise reduction hai, complete defense nahi.
- Configuration validate karke hi service restart karo aur remote lockout se bachne ke liye alternate access rakho.
- SSH aur permissions ko Day 7–10 ke user/group/privilege concepts ke saath connect karke samjho.

Kali Linux fundamentals ka ye final session OSINT aur future penetration-testing learning ke liye remote-access foundation complete karta hai.
