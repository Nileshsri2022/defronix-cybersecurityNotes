# 016 — Kali Linux Free Capsule Course — Day 15 (Final)

**Source transcript:** `transcripts/016 - Kali Linux Free Capsule Course - Day 15 [ Hindi ].hi-orig.srt`
**Topics:** SSH · Encryption (symmetric & asymmetric) · Remote access · `scp` · Passwordless authentication · SSH hardening
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`श`/`स`/`ऐश`/`एसएमएस`/`असेट्स`/`एसएससी` = `SSH`, `सीकर सेल` = "Secure Shell", `लिरिक्स`/`लाइनेक्स` = "Linux", `ईटीसी`/`एटीसी`/`ए टी सी` = `/etc`, `इनफेक्टेड`/`इंक्रीस`/`बहन`/`बैंड` = "encrypted"/"encrypt", `समिटेड`/`सोमेट्रिक`/`स्मृति` = "symmetric"/"asymmetric", `डेमों`/`डायमंड` = "daemon", `नॉन हॉर्स`/`नॉनस्टॉप` = `known_hosts`, `ऑथराइज्ड की`/`ऑर्गेनाइज्ड की`/`राइस की` = `authorized_keys`, `क मोड` = `chmod`, `बम`/`विम` = `vim`, `छोड़ो`/`सुडो`/`स्टूडियो` = `sudo`, `ईटीएफ` = "CTF", `रोहिटेड`/`प्रोबेबिलिटी` = `PermitRootLogin`, `पीडी` = `pwd`, `आस होर्डिंग` = "OS hardening"). The intended technical term has been restored where unambiguous.

---

Hello everyone, good evening, welcome.

Today — I had requested you people anyway that **today is the last day**, so you people should attend; **it is quite an important session**, so we will continue with it.

One minute. Until then, tell me one thing: is my voice reaching all of you or not? Just confirm this — is my voice audible to everyone properly or not? Okay.

Come on then, let's start on our topic, **and don't waste our time.** Okay, come on. **It will be quite an interesting topic; it's quite a long topic.**

---

## Part 1 — What is SSH?

So let's talk. Today our topic is **SSH**; information about this.

Look — sorry for the disturbance.

> **SSH is a NETWORK COMMUNICATION PROTOCOL which does the work of making two computer devices communicate with each other.**
>
> **It ENABLES two computers to COMMUNICATE and SHARE DATA.**

### Why you need it

If we need **remote access** with any server — if what we have to do is: on my [host] machine I have run my Kali [VM], but the thing is, **all this work is of the terminal only** — so **why should I turn on the virtual machine again and again** and use it?

What I can do is: just turn on the virtual machine and **leave it in the background**. Rather than having to open it and log in again and again, **I can take REMOTE ACCESS of it** — from our [other] machine, our normal **host operating system** — I can remotely access it.

> **So if you have to remotely access it, for that we use the SSH protocol — SECURE SHELL.**

### Why it is "secure"

**Because the communication** — meaning, whenever we remotely access any machine, we use the SSH protocol in it.

> **What the SSH protocol does is CREATE A TUNNEL** between that server, that machine — **and it creates a SECURE tunnel**, through which **whatever data is shared, it is shared in ENCRYPTED form.**

---

## Part 2 — Encryption

So now let's talk a bit: **what is encrypted format? What is this thing, encryption?**

> **What does encryption mean:** if we **CONVERT** your **plain text** into such a form — into an **unreadable form** — [then that is encryption].
>
> **Plain text** — if we convert our plain text into an unreadable form, which cannot easily be read — **that is what we call encryption.**

### Two types of encryption

> **There are TWO TYPES of encryption.**

| Type | Keys used |
|---|---|
| **Symmetric** encryption | **ONE key** — the same key encrypts and decrypts |
| **Asymmetric** encryption | **TWO keys** — a **public key** and a **private key** |

**What asymmetric encryption does — it uses TWO keys.**

### How asymmetric works

**What does it mean: the PUBLIC key is SHARED.**

For example — a [user] creates a **private key**; [when] you have to send data to somebody... For example, **User 1** wants to communicate with **User 2.**

> **So User 1 will SHARE ITS PUBLIC KEY with User 2**, and will say: *"Whatever communication happens between us — whatever data you want to share with me, User 2 — what you have to do is, with MY PUBLIC KEY, ENCRYPT it and share it."*
>
> So [User 2] will use **User 1's public key to encrypt the data.**

### What's the benefit?

> **The benefit is this: if there is any hacker, or any attacker — even if they capture the data in between, they will NOT be able to [decrypt] it.**
>
> **[Only the one] who has the PRIVATE key [can decrypt it].**

Now User 1 can do [the same in reverse]: **they will also create two [keys] — one public key and one private key — and share their public key** with [the other user]. And they will say: *"If you have to send any data to me, then encrypt it with my public key and share it with me."*

> **The benefit of that is: only the one who has the PRIVATE key can [decrypt] that data.** So who will have the private key? **User [1] will.**

### The lock-and-key analogy

> **That is why asymmetric encryption is SECURE** — because it's like **one lock with two keys**: one key always stays with the one whose lock it is, and **the second key is shared**.
>
> *"Whenever you have to share data, lock it [with this].* But the benefit is that **the lock can only be fully opened by the one who has the other key.**"
>
> **So this is the whole game of PUBLIC KEY and PRIVATE KEY.**

### Summary

| | **Symmetric** | **Asymmetric** |
|---|---|---|
| Keys | **One key only** | **Public + Private** |
| Private key | — | **Always stays with the user who needs the data** |
| Public key | — | **Shared with whoever sends data** |
| Decryption | Same key | **Only the private key holder can decrypt** |

**SSH uses [asymmetric encryption]** — it uses **RSA** [and other algorithms].

That was a small overview about SSH.

---

## Part 3 — Installing and managing the SSH service

Now let's talk about SSH in detail. Let's start; let's come to our terminal.

### Installing

Look — if you have to use SSH in your Linux machine, **first you will have to install its package in your machine.** The package that should be there is called **`openssh-server`**:

```bash
sudo apt install openssh-server
```

Right now, in my machine, the `openssh` package is already installed, so there is no need to install it.

If you are a normal user then you need `sudo`; **if you are from the root user account then you don't need to put `sudo`** — you know this well.

> **Until this package is installed in your machine, you cannot use the SSH service.**

### Starting, stopping and checking the service

After you have installed the package once in your machine, **after that you have to START the SSH service.**

**You can check it in two ways:**

```bash
# Method 1 — the "service" command
sudo service ssh status
sudo service ssh start
sudo service ssh stop

# Method 2 — systemctl
sudo systemctl status ssh
sudo systemctl start ssh
sudo systemctl stop ssh
sudo systemctl restart ssh
```

So this will start your service. **If you want to see whether the SSH service started in your machine or not**, for that the command is `sudo systemctl status`; after that you will see the service [state] appearing on your screen.

If you have to **stop** it, then simply write `sudo service ssh stop` — so **it will stop your SSH service.** If you want to see the status, you can see it; **so right now your SSH service is INACTIVE**, as you would see on your screen. Now let me start my SSH service again.

> **In both ways we can start it, stop it, and see its status.**

### ⚠ VirtualBox/VMware network setting

Second — **if you are [using] a virtual machine**, then what you have to do: go to your **network settings.** Let me show you.

What you will do: **right click on your machine**, go to **Settings**, after that see the **Network** [adapter].

> **It should be in BRIDGED MODE; otherwise you will not be able to use it properly.** Basically, you will have to be in this LAN to use it.

Because right now [we're doing this] within the **local area network, within our LAN** — if you [want to] remotely access a server, [this is] how you have to do it.

---

## Part 4 — SSH configuration files

Let me show you one thing: **whenever you install the SSH package in your machine, [the configuration files are created].** Let me show you the location:

```bash
ls -l /etc/ssh/
```

> **Whenever you install the openssh package in your machine, by default all those configuration files get created inside `/etc/ssh`.**

**This is SSH's main configuration directory**, inside which you get to see a lot of files. For example:

| File | Purpose |
|---|---|
| **`ssh_config`** | The **CLIENT** configuration file |
| **`sshd_config`** | The **DAEMON (server) SSH** configuration file |
| `ssh_host_*_key` | Host private keys |
| `ssh_host_*_key.pub` | Host public keys |
| `banner` / others | Related files |

### What a daemon is

> **`sshd_config` is the configuration file of your DAEMON service.**
>
> **What is a daemon service:** whatever packages you install — after installing the package, **a SERVICE is created; a PROCESS is created.** Understand? **That process we call a service, and that service we call a DAEMON** — in Linux it's called a daemon.
>
> **So `sshd_config` is the daemon configuration file.**

The rest of the files are related files. **And, as I told you, it uses a public key and a private key, and along with that it uses [an] algorithm.**

> **So if anyone asks you "where will SSH's main configuration files be found?" — the location is inside `/etc/ssh`.**

---

## Part 5 — Remote access via SSH

Now let me teach you **how you can remotely access**, how you can access this machine through another machine.

Let me clear the screen. Right now let me show you my `ifconfig`:

```bash
ifconfig
```

So my IP address for this machine is `192.168.1.148`.

### The syntax

> Whenever you try to take remote access into any machine through SSH — like, this is my Kali machine, and if I have to remotely access it from my Windows machine — **there is a syntax:**

```bash
ssh username@ip_address
ssh username@hostname
```

`ssh` — the command's name; after that the **username**; then **`@`**; after that the **IP address** — **or you can write the HOSTNAME too**, okay. **But the best [is the] IP address.**

### The demonstration

Now let me take you to my Windows machine. Here I have **MobaXterm**.

> **You can do it with PuTTY too, but I prefer MobaXterm more, because in it you can remote access MULTIPLE machines at once.**

So [I'll] go there. To do remote access, what I do:

```bash
ssh kali@192.168.1.148
```

I write `ssh`, the command's name, after that the username — **my username is `kali`** — after that `@`, after that the **IP address**.

It prompted me for a **password**, so I will enter its password. Enter.

**Now what happened — you [are] inside it.** Look, you would be seeing: **this is [the same] interface** as the terminal that was appearing over there; it's showing like that here.

### Confirming where you are

If you want to confirm, then simply run a command:

```bash
hostname          # confirms which machine
echo $USER        # confirms which user
```

So this has become `kali`. **If you want to confirm which user it is**, then `echo $USER` — the user's name — **so this will show you: okay, `kali` is its user.**

Now let me switch — let me become root and show you, if you don't believe [it]:

```bash
sudo su
pwd               # /home/kali
ls
cd /home/
```

**So all these files and directories appear here.** All these files [that] you see on the [remote terminal] — **in this manner we can remotely access any machine within the LOCAL AREA NETWORK, within our LAN.**

---

## Part 6 — Running a command WITHOUT logging in

Okay, so that was one way. Now let me log out, exit.

Let me teach you one thing: **if you want to execute a command on any machine WITHOUT logging in.**

> If I want: my Kali machine — **without logging in I want to execute a command inside it**; I don't want to log in, but I want to see my command's output. **You can do that too.**

**How? Simply:**

```bash
ssh kali@192.168.1.148 hostname
ssh kali@192.168.1.148 pwd
```

Simply, what you have to do — **the name of the command** you want to fire, [placed after the address].

I want to see `hostname`; I want to execute the `hostname` command. Simply hit enter. Now what will this do — as you put in the password, **it will NOT log in to that machine; [it will] just [run the command].**

*[He mistypes first]* — okay, `hostname`, H-O-S-T-N-A-M-E, that's the spelling. Okay, let me do it again.

**Look at this — now it did NOT log in, but it showed that command's output on your screen**, printed it. Similarly if I do `pwd`, I can do `pwd` too, and again I put in the password.

> **So in this manner you can fire any command [on a remote machine] without logging in.**

---

## Part 7 — `scp` — copying files over SSH

[Now suppose] you want to **share a file** from one machine to another machine through SSH — **you can do that too.**

Let me give you another example. For example, I will use two machines. Right now let me close this.

I have a **Red Hat machine**; I have a **Kali machine.** Okay, [here's] the terminal.

For example, what I did:

```bash
touch demo.txt
cal > demo.txt        # put a calendar inside the file
cat demo.txt          # it's a calendar
```

**Now I want to share this file onto my Kali machine.** So how can I do it? **For that there is the command `scp`.**

> **Because this will come in very useful whenever you play a CTF anywhere** — because today's topic is very, very important. **Until you have knowledge about SSH, you cannot do anything.**

### The syntax

```bash
scp /full/path/to/file username@ip_address:/destination/path
```

`scp` — and if the need arises to share a file, you have to do it like this. **You'll have to give the FULL PATH:**

```bash
scp /home/matrix/demo.txt kali@192.168.1.148:/home/kali/
```

I hit enter. **Why didn't it prompt for a password?** Actually, why didn't it? **Because before your class I had practised for you**, and in that I had **configured passwordless authentication** for the protocol — **that's why it did not prompt for a password.**

### Note the colon

After the username and `@IP`, **you have to put a COLON**; after giving the colon you have to **mention the PATH** — first a forward slash, after that you have to mention the path of **where you want to put it.**

Where do I want to give it — `/home/kali`; I want to share it there. Hit enter.

**Now look, what it did — it shared the `demo.txt` file very securely.**

> **It is a VERY SECURE way.** It's not that it isn't secure — **it is quite secure. If you share a file in this manner, it will not be compromised.**

### Verifying on the other side

Now let me go to the Kali machine and do `ls`:

```bash
ls
cat demo.txt
```

**Look, here you would be seeing a file by the name `demo.txt` which was not there before.** And if we `cat demo.txt`, then you will get to see the calendar which we had put inside this file over there.

### Recap so far

> **So you have understood:**
> 1. **How to remotely access your machine** from any terminal
> 2. **How to fire a command in a machine WITHOUT logging in**
> 3. **How to share any file** — using the `scp` command

**Syntax recap:**

```bash
scp <source_full_path> <username>@<ip>:<destination_absolute_path>
scp -r <source_dir> <username>@<ip>:<path>      # for directories
```

---

## Part 8 — ⭐ Passwordless authentication

Now let's move ahead. **Up to now, whenever we used the command, what was it doing — it was asking you for a PASSWORD.**

**Now I want that — due to security [reasons], or for OS HARDENING purposes — I want to set up PASSWORDLESS AUTHENTICATION.**

### Why you'd want this

> **Such a requirement arises.** For example, **you work in such a place, sitting in a PUBLIC PLACE** — you are working in a public place, and there you feel that **a lot of people come and go; someone is sitting behind you watching**, someone is doing something.
>
> **From that, what can happen — your password can become known to anybody.**
>
> **If, for security purposes, you want that you don't have to type the password again and again — [so that] nobody can SHOULDER-SURF your password**, [so that nobody] can look over your shoulder — **then what will you do? You can set up passwordless authentication**, which I just [described], using encryption, using public/private keys.

---

### Step 1 — The `.ssh` directory

So, **whenever you install the openssh package, in your HOME DIRECTORY** — for example, let me set it for [a] normal [user]:

```bash
cd ~
pwd
ls -la
```

> **Whenever you install the openssh package, you get to see a directory created by the name `.ssh`** — a **hidden** directory named `.ssh` gets created.

**But there is a problem with the Kali machine:**

> **In most machines this works** — by default the `.ssh` directory gets created. **But in some machines — the latest ones — by default it is NOT getting created.**
>
> So **you will have to CREATE this directory** in your machine.

### What's inside it

Let me `cd` into `.ssh`. Right now there's nothing inside it. **But inside it you get to see a file — `known_hosts`.**

> **What information stays in `known_hosts`:** the **PUBLIC KEYS of the known [hosts]** are available there.
>
> **Which will the "known hosts" be? Those with whom you are communicating, with whom your communication has been established.** Their information is found inside `known_hosts` — you get to see their public keys there.

---

### Step 2 — Creating the directory with correct permissions

**If the `.ssh` directory is not created in your machine, don't worry** — let me show you all the steps.

> **Keep one thing in mind: [set it up] on whichever machine you want to [log into].**

For example: my **Kali machine** — and the **Red Hat machine** which is my server — I want to set up **passwordless authentication** with it.

**So on whichever machine you are setting up passwordless authentication, in that machine you first need the `.ssh` directory to be created.**

```bash
mkdir .ssh
chmod 700 .ssh
ls -la
```

Or in one step:

```bash
mkdir -m 700 .ssh
```

**After that you have to set PERMISSIONS on it.** If I show you with `ls -l`, its permission would be showing as 750.

> **The permission that the `.ssh` directory should have is 700.**

So `chmod 700` — I put 700 permissions on the `.ssh` directory. Now if I do `ls -la`:

> **The permission you would now see on `.ssh` is SEVEN ZERO ZERO — only the root user, who is its owner, has [full] permission; apart from that, nobody has any permission.**

---

### Step 3 — Generating the key pair

Now simply, what you have to do — `cd` into `.ssh` and run the command:

```bash
ssh-keygen
```

**Now what is it saying:** *"Generating public/private RSA key pair. Enter file in which you want to save [the key]."*

> Now — if you use the `ssh-keygen` command, then [note that] I created the `.ssh` directory and showed you, **but actually you didn't need to create it, because by DEFAULT `ssh-keygen` creates that directory itself** and then stores your private key and public key in it.

Now it was saying: **if you want to save it to some other location** [you can]. No — I hit enter.

### The passphrase question

**Here it [asks]: do you want a PASSWORD on your private key or not?**

> **Keep one thing in mind: keeping a passphrase is ONE MORE STEP for you** [of security].

**Why?** For example — suppose what happened: *"I forgot, I set a password on my machine"* — **but think: IF SOME USER GETS YOUR PRIVATE KEY, then what will you do?**

> **So if you want that your private key should have a password** — *"I want to SECURE my private key, so that whenever I use passwordless authentication, instead of putting in my user's password, I use the private key's password"* — **you can do that too.**

Right now I am not setting any password on it; I leave it empty and hit enter.

### The result

**So it generated TWO keys for you:**

| File | What it is |
|---|---|
| **`id_rsa`** | **your PRIVATE key** — never share this |
| **`id_rsa.pub`** | **your PUBLIC key** — this is shared publicly |

> *"Let me show you `id_rsa.pub` with `cat`; I will not show the private key, since it is my privacy."*

---

### Step 4 — Sharing the public key

**We have generated the public and private key. Now what do I have to do — I have to [establish] secure communication.**

So how? **The public key that is mine — I will SHARE this public key** — with whom? **With my Red Hat server.**

**But how will I share it?** Either I will take it in a USB, store the key, then go to that server and share it there. **But the USB route isn't possible, because nobody will give you entry into a server room.**

### First, check the other machine

Let me go to my Red Hat server once. I check here whether this directory is created here or not.

```bash
pwd
ls -la
mkdir -m 700 .ssh        # if it doesn't exist
```

> **If the directory isn't created in your machine, use the `mkdir` command** — `mkdir -m 700 .ssh` — **so the directory will be created with that permission.**
>
> **Keep one thing in mind: after the directory exists, you have to MAKE SURE its permissions are 700.** Apart from that, no permission should be on it.

*(For this demonstration two Linux machines are needed: "I already have two Linux machines, so I am showing you the experiment.")*

---

### Step 5 — `ssh-copy-id` — the easy way ⭐

> **There is a very easy way to share it — it will be done with just one command.**

**If you have to share your public key, for that there is a command:**

```bash
ssh-copy-id -i /root/.ssh/id_rsa.pub username@ip_address
```

`ssh-copy-id`, after that **`-i`**, after that **the full path** of where your key is. My [key] is in my home directory, `.ssh`, and then [the key name]. After that the **username** and its **address**.

**I hit enter.**

### The first-connection prompt

**Now it said: *"Are you sure you want to continue connecting? yes/no"*.**

> **When does this come? It comes when you connect with a machine through SSH for the FIRST TIME**, because in the background it is **exchanging keys** — whenever a key exchange happens.

**Yes.** Okay — then it asks for the password. I entered its password too.

> **So now what happened: our machine is READY for passwordless [authentication].**

### Verify on the server

Look here — **a file will have been created by the name `authorized_keys`** — *"this is the very public key I showed you on screen."*

```bash
cd ~/.ssh
ls
cat authorized_keys
```

**And `cat authorized_keys` — this is the SAME file; look, this is the very same thing.**

### Test it

```bash
ssh username@ip_address        # no password prompt
```

> **So in this manner we can set up PASSWORDLESS AUTHENTICATION with any machine.**

### One more secure step

> **If you want one more secure step in this:** whenever you use the `ssh-keygen` command, when you generate the key, **it asks you for a passphrase — SET A PASSWORD THERE.**
>
> **So that if someone steals your private key — even if they steal it — they will not be able to use it, because for that they will have to [supply the passphrase].**

---

## Part 9 — ⭐ SSH Hardening

So that was the passwordless authentication method. Tell me once whether you people understood everything about SSH up to now.

Now let me [show you] something creative.

---

### 9.1 Disabling root login — `PermitRootLogin`

> **If I want that no user — even I, whenever I try to log in through SSH — due to SECURITY REASONS, should NOT be able to log in as ROOT.** They should never be able to log in from the root account; **if they log in, it should only be from a normal user account.**

**How do I restrict that?** Simply, **I will have to go inside the main configuration file.** Before that I have to become root:

```bash
cd /etc/ssh
ls
vim sshd_config
```

**Here you get to see a lot of settings inside it.**

I want that **if any user tries to remotely access my machine, they should NOT be able to access it via the root user account.**

For that, first let me search in it — **you know how to search in `vim`** [`/PermitRootLogin`].

**Look — this appeared on your screen.** It's showing `prohibit-password`, **but it is COMMENTED.** *[i.e. it is only showing the default.]*

> So what do I want: due to security reasons, **I go into INSERT MODE, uncomment it, and write `PermitRootLogin no`.**

```
PermitRootLogin no
```

**I say that if any person accesses my machine through SSH, they should NEVER be able to access it through my root user.**

**After that I save it** — Escape, then `:wq`.

### Restart the service

> **After that I will have to RESTART the service, so that the daemon service reads the changes I made properly.**

```bash
sudo systemctl restart ssh
# or
sudo service ssh restart
```

### Testing it

Now let me try to SSH. Let me log out. Now I do:

```bash
ssh root@192.168.1.148
```

I put in root's password. **Now what will come? Nothing** — no matter how many times you try: **"Permission denied (publickey, password)."**

**Even though every time, all three times, I am putting in my password correctly.**

> **So one thing you can do: you can RESTRICT anybody [from logging in as root].**

---

### 9.2 Changing the default port

**Second thing you can do — due to security reasons.**

> **What do you want: whenever someone [scans] your machine** — because if you are an attacker, you too would want to hide yourself, right? **When you want to hide yourself, what will you do?**
>
> **The default port [for SSH] is 22.** But what happens — **when someone scans your services**, they scan the services and come to know: *"Okay, yes — on your machine a service named SSH is running on port number 22."*
>
> **So what will they do — they will try to ENUMERATE it, will try to attack it.**
>
> **But due to security reasons, what do we do — we CHANGE that default port.**

**So how is the default port changed?** Let me show you that too. Open the SSH configuration file again:

```bash
vim /etc/ssh/sshd_config
```

**First you will get to see `Port 22` written.** Here, what you can do — **go into insert mode** and [put] whichever port you want.

> ⚠ **But you have to put a port that is AVAILABLE in your [machine]** — not just anything; **one that is FREE in your machine.**

Like, I took **5152**; I put that port. Okay, and then I did Escape mode, after that `:wq`, and now I **restart my service again:**

```bash
systemctl restart ssh
```

### Testing the port change

Now I try to log in to my machine again. **Now I have changed the default port**, so now what I do — I `ssh` normally. As soon as I hit enter:

**Look, now it gave no response — "connection [refused], connection to host ... port 22"** — meaning **there is no connection at all on 22.**

**Now if you have to connect, then simply you have to give the `-p` flag; after that you have to mention which port:**

```bash
ssh -p 5152 username@192.168.1.148
```

**On 5152 it prompted you, [and] you entered your machine.**

> **So in this manner you can change any port.** After that, when you SSH, **you will have to specially mention that port; otherwise [it tries] 22** — **and you have disabled [22]; this means you will not be able to log in with it.**

*[He then reverts it to the default for convenience.]*

---

### 9.3 Restricting which users may log in — `AllowUsers`

**Next example:** if you use [SSH] on Kali and **you want that only particular users** — suppose there are just three of you — **you want that only you can access this machine.**

For example: *"I say my `user1` and `user2` should be the ones who can access my machine remotely through SSH."*

**If I want to do this too, I can.** For that I will have to change one parameter.

> **I have to go to the very LAST of this file — to the END OF THE FILE** — and go into insert mode, **and add a line there:**

```
AllowUsers user1 user2
```

A-L-L-O-W `Users`, after that you have to [write] the user's name: `user1`, after that `user2`.

*[He confirms the actual usernames first, then tests.]*

### Testing

Now let's check — **only [those] will be able to access.** So [logging in as] the allowed user: **look, I was able to log in through this.** Let me do `pwd` — here it is.

Now let me try with the second user — **through this too I was able to enter my machine.** Let me log out, exit.

**Now let me try with `user3`, because we must not give permission to it.** So again I [try]:

> **Look — now this will NOT get permission.**

---

### 9.4 The other restriction forms

> **So in this manner you can ALLOW any particular user; you can DISALLOW too.**

Let me also teach you [the others]:

**If you want to BAN three particular users and allow everybody else**, then instead of `AllowUsers` you use **`DenyUsers`:**

```
DenyUsers user1 user2 user3
```

**If you want to ban a particular IP address — all users from that IP:**

```
DenyUsers *@192.168.1.39
```

What I did — [`*`] after that `@`, after that I wrote the IP. **Any user from that [IP] who tries to access us, I am DENYING; they will not be able to access it.**

**If you want, you can ban the whole [subnet]:**

```
DenyUsers *@192.168.1.0/24
```

Simply — `@192.168.1.0` after that the whole **subnet mask.** **So it did the whole subnet too** — whoever from `192.168.1.0` tries to access, **it will deny them.**

**And if you want to ALLOW a particular IP address** — all users from that IP:

```
AllowUsers *@192.168.1.39
```

**If a condition like this arises with you** — for example, it turns out **there are 10 of you** — then **instead of making entries for 10 users, what will you do? You will CREATE A GROUP**, and add all 10 users into that group, **and then you can give SSH permission to that whole group:**

```
AllowGroups groupname
```

**Simply you will write that group's name** which you have made the entry for.

### Summary of hardening directives

| Directive | Effect |
|---|---|
| `PermitRootLogin no` | **Block root login** entirely |
| `Port 5152` | **Change from the default port 22** |
| `AllowUsers user1 user2` | **Only** these users may log in |
| `DenyUsers user1 user2` | These users are **blocked** |
| `DenyUsers *@IP` | Block **all users from an IP** |
| `DenyUsers *@IP/24` | Block a **whole subnet** |
| `AllowUsers *@IP` | Allow all users **from one IP** |
| `AllowGroups groupname` | Allow an **entire group** |

> ⚠ **Remember to RESTART the SSH service after every change.**

**So in this manner you can allow any particular user, deny a particular [user], allow a particular IP address, deny a particular IP or subnet mask.**

---

## Closing

Okay — so [in this] session there is a lot more to study, **but you people don't need to study to that level; you don't need to know more than this.**

**SSH — if we want, we could extend it another half hour or an hour; it's such a big topic in itself.**

*[A learner reports being unable to comment on LinkedIn; he offers team support.]*

So then let's end the session.

> **So this was our LAST SESSION of our Linux capsule course.** I hope you people enjoyed the whole course. And after this, our next course has already started.
>
> I hope you people didn't get bored and I didn't [overload] you too much. **If you people feel that I did not teach you properly, or that I left some gaps in concept delivery, or that I didn't teach something — for that we are really sorry. I gave 100% from my side**, as much as I could give you in 15 days. Nobody else can deliver [this] content.

**And please, if you people liked our course** — whether you are watching the recorded session or the live session — **please don't forget to subscribe and comment.** If you came to the channel to watch, I hope you people enjoyed a lot and got to learn a lot in the whole series.

**And one more request:** as soon as [a session] is uploaded — we have a **LinkedIn page** of our website, the link is given below in our link — **go there.**

> **And please — whether you are watching this video after 10 days, after a month, or even after 1 YEAR — whenever you watch this video or this whole series, please: for every single series, for every single video, there is a web page available on our LinkedIn. Go there and please COMMENT and tell whether you understood or not**, and how much you liked our course or didn't.
>
> **Please don't forget to comment.** From this, we will get a lot of help — and from this **you will benefit not just yourself but other people too**, because they will come to know that there is genuinely something to learn here. **And if you did NOT get to learn, then please tell that too**, and going forward we will keep that in mind a bit more.

So for this capsule course we say bye bye. **Bye bye, take care.**
