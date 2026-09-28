# 002 — Kali Linux Free Capsule Course — Day 2

**Source transcript:** `transcripts/002 - Kali Linux Free Capsule Course - Day 2 [ Hindi ].hi-orig.srt`
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** the auto-generated captions for this session are noticeably garbled in places (e.g. `भूत` = "boot", `एटीसी`/`8c` = "etc", `करनाल` = "kernel", `आम`/`यार` = "rm"/"rmdir", `प्रोक` = "proc"). The translation below restores the technically intended word where the meaning is unambiguous, and keeps the speaker's original phrasing everywhere else.

---

Good evening. So this is Sachin from [Defronix] Cyber Security Private Limited company, and also the trainer of your [course].

Very few people are joining. Last time also there were few people, so I wasn't expecting that many — but it's much less than that. Okay, we have to start; we will start our [session]. We will continue from where we have been going.

So there is a request to you people: if you people feel that our content is good, that we are teaching well in this capsule course, then please do this — forward it to the maximum number of people, so that those who really need this course, okay, whoever really needs it more, they can take the benefit of it for free.

Because today's session will be a recording... The file system, which I have already taught — that probably everybody understood, and I have already told you. So today we will study about the **File System Hierarchy**. Okay? The 19, or around 19, that we had talked about — we are going to study about these. And secondly, we will learn our commands: how they work, how we can create [things] inside our machine.

---

## Getting familiar with the Kali desktop

So now let me familiarize you a bit. The taskbar you see in Windows — it is like this here. Here you get to see a **list of applications**; if you click here, these are all the list of applications. Here you are seeing an image of the desktop. Here it is showing you your **File System** — you get to see the file system here. File system means, for example, if you compare it with Windows, it is "This PC" in Windows 11, in Windows 10, or even before that, when it used to be [My Computer]. So this one — let me click and show you — this is your file system. In it, those 19 or around 18 folders that we talked about, you will get to see them right here, and you will get to see them in graphical mode.

That is why I am familiarizing you once, so that whenever you use this machine, you will know which thing is found where.

After that, what you are seeing here — this is your **text editor**. Okay? A text editor comes by default with our machine; you will get to see it here. After this, the next icon you see is **Firefox**, okay, the browser you have to look at. Sorry for the disturbance, I am sorry, because there is a bit of background [noise]. Okay.

I'll talk about the [terminal], on which we are going to do the complete practice. So I clicked on this — now our shell has opened. Let me increase the screen size a bit so it looks good and readable for you people; the size should be visible properly now. Okay.

So first of all, let me tell you: if we go inside these files... if you want to open a **new tab**, meaning to open one more terminal, then you do "New Tab" here and one more will open on the side, to work in. Okay? If you want to use multiple ones at once — in one terminal some task of yours is running, and you want to use another terminal, then in this itself you go to "New Tab" and you will be able to use the second terminal.

Otherwise, what can you do — if you don't want to do it like that, you can simply **split** it too. If I click the split option, then this will get split; your screen will be divided into two parts. Otherwise you can split it vertically too, by clicking like this.

---

## Reading the shell prompt

Next, let's talk about what is being shown on your screen. Okay? What is this thing I am highlighting? Look, first of all, the thing you will see is **root**. This is root. This first thing you see is root — meaning the **username**. This is your username of this machine; the current user name is root. Okay?

After this, the one you see at the end — this shows your **hostname**; it shows the hostname of the machine.

After that, the one you see in brackets — this **tilde (~) sign** you see. Basically, here its meaning right now is the **home directory**; meaning, the user — the root user, okay — it is showing its home directory.

Okay, after that, what you see is this icon. Okay, you see this hash. Here you will get to see two icons. Okay? You will either see [`#`] or you will see [`$`]. For example, let me open a new one — look here; if I increase its size and show you, here it is. If you see this **dollar** sign, it means that you have logged into this machine from a **normal user account**. And look here, this is that user's name — **kali**. Okay? This is its username. And here you see the tilde — that is its home directory.

Basically, [the tilde] is not [always] the sign here — basically what is there is the **present working directory**, meaning presently which directory you are working inside; that will appear here. This is the tilde sign — its meaning is that right now you are inside this user's home directory. If you shift into any other directory from here, then the directory's name will come here, basically. So the information that is shown here is the information of your present working directory. Okay?

---

## File System Hierarchy

Now let's talk about the File System Hierarchy, in which I am going to talk about... the complete file system. So that you know — I told you in the last class — first of all comes [`/`]. Okay? Around... it can be around anything. Okay? And inside it there are sub-directories, there are files; everybody knows this. But before this there is nothing. Okay? The start happens [at `/`]. Underneath this is the [user] defined data, and underneath this is your OS-defined data. The entire structure starts from here.

Now we are going to study this structure. Okay? Inside it, the around-19 — 17, 15, whatever it will be on our machine — we are going to find out about them, which ones are there.

So first of all, let me shift... one minute. What I mean is, you must be seeing it on your screen. Okay? Which directories these are — because this is the very first thing, this is the **root partition**. Okay? Inside the root partition, what had I told you — how many will be underneath it: around 19 or 17, whatever directories. These are those "around" directories.

What does it mean? You will get a bit of an idea that in every directory you get to see this kind of data, so that whenever you work, you will have an idea.

Keep one thing in mind: many people think — when I taught in the last class, many people still have a doubt, "why should I work in this? In this directory, can't I also create my file, can't I work in it too? So what is my need for these?"

Look, what is it — in Linux it has already been defined from before: for any particular file, for example a program file — first, where a program file has to be downloaded, it will go there itself. Okay? After that, where it will be installed, where it has to be executed, it will happen right there. By default, that is mentioned in their configuration files.

Meaning what — for the purpose of the work, defining permissions for it, depending on the policy, every directory has been defined from before. Now if you work according to that, then it will be comfortable. Otherwise, if you do the work of that directory inside some other directory, then you will face problems — of what? Of permissions.

Otherwise, as for just doing it, whether you work inside `/boot` or you work inside `/media`, do it inside `/mnt` or work inside any directory — it won't make a difference. **The difference is made by permissions.** Meaning, the first question that comes into people's minds is, "I create a file over there too, so my work is running, so then this file is the same thing only?" Look, each of these was made with its own purpose, and you should use them according to that purpose.

### `/` vs `/root` — a common confusion

Now many people have one more new confusion. What is the new confusion? Whenever we talk about the root partition — okay — in the root partition, one is this **forward slash** that you will be seeing on the screen; and the second, let me show you one more — this one, we use it like this: **root**. This one too we sometimes call "root". Okay? Now we call both of them "root".

This [`/`] is your **root partition**, meaning it comes at the top level; at the topmost in the hierarchy. There is nothing above it, there is nothing else besides it — everything works underneath it.

Now this **root** that you see [`/root`] — this is your root user's, the super user's, **home account**. It is the information of his home account, meaning his private account — the one where we had talked about private and public places. So this one is his private home account that we are talking about here. Out of the 19, there are two directories: one stays for the super user's home account, and one stays for the normal users' home accounts. So here, this root user's home account is what this is about.

So this is the difference between them — because now some people may understand [it wrongly], and when working in it they'd say "but you had said it like this." I hadn't said that — because this is the difference between them: this [`/`] is the root partition, and this [`/root`] is root's home directory.

---

## Walking through the directories

### `/bin` — binary files

Come, now let me start. First of all, the directory that comes is `/bin`. What happens inside it — all the [binary] files that are there in your machine, okay, you will get to see them inside it.

Now what are binary files? Look, for any command — all the commands you use in your Linux machine — to run it, to execute it, programs are needed. Okay? And what are programs? They are **sets of instructions**. They are instructions. So later on, when it has to be executed on the machine, when it has to run on the machine, it is converted into a form — into the form of 0s and 1s — which we call the **binary form**. Okay?

So every single command has a program file, which is in binary form, and which we call **executable files**. So all those files — any command's files — you will get to see here.

If I go inside it and list it out for you: here it is. All of these that you see — all of these are binary files; each belongs to some command or another, some program's files you will get to see.

### `/boot` — boot loader

Now let's go into the next directory. Okay. And the most important directory inside it is **GRUB**. Okay? What is inside it — inside it is your **boot loader program**.

What is a program [here]? Look, whenever your machine boots — okay, whenever your machine boots, it has to boot in a **sequence**. Okay? It needs a lot of configuration files. Okay? From the partition, it needs the hardware, the hardware's modules, it needs the kernel, and a lot of things are needed for everything to come on together. So here, what is it — it works in a sequence.

Underneath this you will see one more thing, here it is — the configuration file. Okay. Let me know in the comments please, if it's comfortable. Okay, okay, come on, let's continue.

So I was telling you — okay, the one you are seeing here, `config-6.1.0-kali...` etc., okay, it depends on how you have updated your machine.

So what do you get inside it? Look, when your system boots up for the first time, okay — at the time of the first-time wake-up, meaning when it ran for the first time — what is it, which sequence is followed, and what does that sequence do? It wakes up the other components; it starts the other components.

Now what do I mean by that? Whenever you pressed the power-on button, when you press the machine's power button, what happens is that current flows in your machine, and first of all your machine starts — the machine started booting. That boot-up is done in a sequence. Okay?

First of all the **POST** check happens, the BIOS happens. Okay? After that, the **kernel** loads; along with the kernel, the hardware modules load. Okay? The modules — basically you can [call them] drivers. Okay. And before those, first of all the checking happens: all the components, your hardware components — whether they are fine or not. All those things — whenever you turn on your machine, if you have turned on your Linux machine, then a lot of lines run on a black screen. Okay? That is all work happening in a sequence. Okay? Which we call the **booting sequence**.

So whatever configuration is related to those — meaning, which work should happen in which sequence — that stays defined here in the configuration files. And in GRUB there is the boot loader program. Okay? How the machine will boot — what happens from that program, because in the configuration file it will be defined that GRUB, the boot loader program that is inside `/boot`, okay, how it has to be executed — that will be defined in this same configuration file, step by step. If you go and `cat` it, then you will come to know.

### `/dev` — device files

That was your... next directory has come. `/bin` is done, `/boot` is done, now comes `/dev`. Okay? Let's talk about the `/dev` directory. What happens in it — these are called **device files**.

Now what happens is that this is a **special type of file**. Whenever our hardware — whatever our hardware is — and the software: the one that works as an **interface between them** is your device file. Okay? That is your device file; it does this work between them.

Look, what happens is that in hardware our data is transmitted in two ways. Okay? Our data that is transmitted, it transfers in two ways: data in the form of **blocks**, and in the form of **characters**. The data that is in block form gets divided into chunks, and in chunks it flows. Okay? Basically, when data flows inside the hardware, it goes in block form.

Now which data goes in character form? Basically, let me take an example: the data that flows between a mic and a speaker — we can say that that data is flowing in character form.

Meaning, inside this directory, all the devices that are there, all the device files, okay, related to hardware, related to their interfaces — you will get to see them.

**Keep one thing in mind, my friends: in Linux, everything is a file.** Attach a hard disk, attach a pen drive, anything — Linux [treats] everything [as a file].

Let me go into it and show you. Here, you will get to see a lot of block files. If I do [`ls -l`], look — `c` is a character file, `d` is a directory. Apart from that, look, what you will see here going forward — basically, to identify:

- **d** means directory
- **c** means character file
- **b** means block file
- **s** means socket file

Okay? So here you get to see the information of all the block files.

### `/etc` — configuration / system settings

Next, let's move on. Now next we have `/etc`. Okay. Inside it you get to see the system's settings — whatever there is, you get to see it here.

### `/home` — normal users' home directories

What does this mean? Look, inside the **home** directory you get to see — normal users, the ones other than root — all of them you get to see inside this home directory.

If I go inside this directory and show you: here it is. And look, inside it right now what do I have — one user has been created for the machine, whose name is **kali**; that's why you are getting to see only one. Otherwise, if you had created two, four, five, however many users, all of them would be seen inside this same home directory.

This is the same home directory we had spoken about — this is the **private place of a normal user**; all the normal users, this is their private place. Okay?

### `/lib` — library files

Now let me talk about the next one. Now look, these things — what is this thing? These files that are your boot-related files — this boot directory too, it has been taken from inside this. I will show you how you will identify it, because these are from inside this, but it will bring them onto the screen — here in front.

This **library** one too — `lib`, okay. What is this? Here, you get to see the information of **library files** in this directory.

Look, for any application to run, libraries are needed. Okay? And that information you will get to see inside this. If I go inside it and show you — if I do [`ls`], look, you will get: all of these belong to some program or another. For example, our web server — its library files, okay, a directory is being made for it inside this, and the library files that are needed for it, that are its requirement, to run it — they are stored inside this. Basically I said: the library files that are the requirement for an application to run, you will get to see them here.

### `/lost+found`

Now let's talk about... here it is. Now let's talk about an important one — `lost+found`. Okay, let's talk about the `lost+found` directory.

Now what happens is that whenever any particular program gets corrupted, or what you are doing — you are working on your operating system and suddenly it what? It turned off; there was no battery left in your laptop, and suddenly it turned off. Now what came in it — a lot of programs would have been running. Okay? Now the programs are in a running condition. Okay? Automatically they get recovered. Now some programs will also be such that they could not be recovered properly. Okay? So those you may get to see here.

Let me tell you one thing, it is important information. What happens — look, when a system crashes, it must have crashed because of some particular process. Okay? Now what happens is that when digital forensics is done, then it will be found out: this particular process — because of whom would it have crashed? Because of which program did it crash, because of which files would it have happened? Okay?

So it is possible that that information may come into `lost+found` and you may get to see it. Okay? It is possible that it recovered fully even after crashing, so you may not find it here — but the chances are there. At the time of digital forensics, if you want to find out that if some particular process went bad, crashed, then because of which process or file it would have happened — generally you get to see that information inside this, inside the `lost+found` directory. **For digital forensics people, this often becomes an important directory.**

### `/media` — removable media

Now let's talk about the **media** directory. Okay, in this media directory — basically, it's a straightforward matter: we are talking about media files, meaning all the **removable media**: CD drive, USB, okay. So you will get to see that inside this. Okay?

Whenever you boot — okay — if there is a CD drive in your system (nowadays no system has one), if there is a CD drive in your system, then what will happen: either it will automatically be mounted here. What "mount" means, I will tell you right now. Okay? So this is related to removable media — the files, the information you get to see inside this directory.

### `/mnt` — mount point

Now let me talk about the **mnt** directory. Okay. `/mnt` means **mount**. Okay. Now normally you will find it empty. Okay?

Whenever we use any **ISO image** — when do we use an ISO image? It may be that you have to configure a local repository; it may be that your program got corrupted, okay, your kernel got corrupted and you have to recover it — then what do we do? Your ISO image, we **mount** it. Okay? Or we inserted some pen drive, inserted a hard disk — so when we mount it, the entry that is made, the mount that happens, it gets mounted inside this directory.

Now what does **mount** mean? Okay, mount means that if we have to exchange data with any device — okay, with a pen drive or a hard disk — then it is necessary to mount it. Until we mount it, data cannot flow inside it.

Basically, mounting means... let me give you the meaning: it's like, you have a house. Okay? There is a room. If you didn't install any window or any door in it, then how will a person come and go inside it? How will he be able to use it?

So basically, mount means exactly that: there is a room, and if I have to use it, there is a door installed in it. Okay? Through that door your coming and going happens. In the same way it works here: until you mount any removable media, or any hard disk or such, you cannot use it.

### `/opt` — optional software

Now let me talk about **opt** — **optional software**. It has been given [for this]. If you want, you can install your **third-party software** here and use it. Okay? That was its meaning: optional software.

### `/proc` — process information

Now what happens is that this **proc** directory — this directory is updated from the kernel. Anything at all that changes in a process, any process that has been loaded, a process that is working — everything process-related is in that directory.

And many times, when... the other commands that work — many times we look at process-related information; we use the `top` command, we look at the process's information, we look at the state. So from where do we see that? It is through this. What do they do — they take its reference in the background, and after that show you the output.

### `/root` — super user's home

Now let's talk about **root**. About this I was talking: this is the root/super user's home account. Okay? It is the directory of his home account.

If I go inside it and show you — if I do `ls`, then this is it: this is the super user's — his Desktop, his Documents, his Downloads, his Music, like that. Similarly, the normal users' home account — the user named `kali` that was created — if you go and check inside that too, you will get to see this kind of information inside it too. Okay? So this is his private place, the information inside it. Let me go back.

### `/sbin` — super user binaries

Now let's talk about **sbin**. What does it mean? Inside it too you will get to see binary files, but which binary files will you get to see in it? The **super user's**. Meaning, in the Linux machine there are some commands which only the super user can run, only the super user can execute — and their binaries, all of them, you get to see inside this `/sbin` directory. Okay?

### `/srv` — service data

Now let's talk about the **srv** directory. You get to see the **serving directory**. What does it mean — FTP, NFS, or you configured some proxy server. Okay?

Now many times what happens is that for the users we have, their temporary data has to be held. So that whenever I use that service, I can quickly access that data. Meaning, **like a cache** — the way you use cache memory in a system, so that your speed, your processing power increases. In the same way you can say that whenever you use these services — configured some proxy server, some server configuration, configured anything like that, or an FTP server — then what happens there is that there are some temporary files which you save inside this for your users, so that as soon as you use that service you get a fast response and we can access those files, that data.

Basically, this is its meaning — that is why I wrote its name as a serving directory.

### `/sys` — kernel and hardware details

Now let's talk about yours — what happens inside it. Inside it you get to see all the details related to the **kernel** and related to the **hardware**. Okay? Kernel-related, hardware-related things.

If I go inside it and show you — so I did `ls` here. Now look, what is in it: kernel and hardware related, quite important. **Block** — information about block devices. **Bus** — the ones that work for carrying data back and forth. **Class** devices. Okay. **Firmware**. Okay. **Kernel modules**, which are drivers.

Meaning what — the information related to the modelling/modules of the hardware or the kernel part, you get to see inside this.

---

## A note on how deep to go

You people basically should know: "yes, where will I find my configuration file, yes, where will I find my binary file, yes, where do I have to work." Okay? What will I get in `/opt`, okay; in `/proc`, ah yes, it updates live from the kernel.

You should have a basic idea. But as you become user-friendly with it, as you start using them, then automatically you will come to know about these by yourself — "ah, this means I have to work here."

Because how much can I do in one day? How deep should I go? You won't understand, because there will be a lot of beginner people who won't have any idea at all what the thing is. So what is it — you just need to know about them: "yes, this thing is there; I am working in Linux, there are these many folders, these many directories, their meaning is this."

Basically, whatever work you do, if you hear a name related to it anywhere, if some work related to it is happening, then it will come straight into your mind: "ah yes, I should go into this folder and check." It's possible you will find it there. So you won't have to grope around; you won't have to spend hours searching for something. You will work with just one minute of memory.

### `/tmp` — temporary directory and the sticky bit

Now let's talk about the **tmp** directory. This is your `/tmp` directory — meaning, this is a **temporary directory**. Okay? Everybody can access it, can delete [in it]. But what happens in it is that **whichever user created a file, only that user can delete that file**; nobody can delete that user's file.

I'm not talking about root, I'm talking about normal [users]. Okay? Meaning, this user named `kali` on this machine — if the user named `kali` did some work of their own inside the `/tmp` directory, okay, created their file, then tomorrow someone comes — like, my name is Sachin, I am a user, I opened it — [and since] everyone has access, [could] delete everything? That cannot happen, because here a **sticky bit** is applied, because of which what happens is that the file — whoever created it, only he can delete it; nobody else can delete it.

Basically it's such a place where anybody can do their work; all the permissions are here, it's temporary. Okay? These files of yours get deleted — basically for doing temporary work.

### `/usr`

Now I am talking about [`/usr`]. Inside this too you will get to see binaries. Okay? You will also get to see library files, and you will get to see documentation-related things, inside this `/usr` directory.

### `/var` — variable files

Now, at the end, let me give you a full intro of the side [links], and after that I'll tell you how they are related. Now after that let me tell you about **var**.

Now I am talking about **var** — **variable files**. Okay. Inside this directory there are some files — inside that directory you will get to see files that **change from time to time**. Okay? The ones that change from time to time: like temporary mail files, like caches, like **logs**. Okay? Those keep getting updated with time; that type of file you get to see inside this.

If I go inside it and show you: the library files that are for any programs — they are actually here [in `/var/lib`]; and over there [at `/`] a shortcut has been made, the way in Windows when we create some software it creates it in this fashion, here its [link] has been created.

Okay. Some files related to local data — you will get to see the information here. And here, the rest are temporary. Whenever... whatever is happening in your machine — the web server's files that are put, they are put inside [`/var/www`], so you get to see them right here; you get to see them by going into the file there. Okay.

`/run` — I have already told you about this just now.

---

## Symbolic links at `/`

Now, what is appearing back there — what actually is it? Okay, `/dev`, `/mnt`... okay, the kernel's files. Let me show you how I will prove it now.

Look, let me do this once. Okay, right now you are seeing one thing — here it is. Now, what had I told you until now? Look, the `bin` that you see here is actually a **shortcut** — of what? Of the `bin` that is inside `/usr`, which I showed you just now. From inside that, a shortcut has been made here, on the desktop. Okay?

There, inside its root partition, `boot` is a directory in itself, `home` is a directory in itself. Now take this one — where did it come from? I told you `boot` is there; `boot` is a directory, and inside it there are some configuration files. Look, this is a shortcut of that.

Basically, there are a lot of such files which are shortcuts of theirs, on top, underneath your partition. Now this one I told you is a shortcut of the directory inside `/usr`. You will be seeing `lib32`, `lib64`; `media` is an individual directory. Like this — look, `sbin` is taken from `/usr`... programs you don't get to see; there are some particular directories in the system which have been made [as links]. If I talk in Linux terminology — someone has asked in the comments — we call them **symbolic links**. Okay?

Right now you will be seeing a lot of information. Okay? Let me give you a bit of an idea, but I will tell you about this in a coming class. What you see here are the **permissions**. Okay? Here you get to see link information. This is your **user** information. Okay? This is your **group** information. This is its **size**. Okay? This is its **timestamp**. And this is the name of the file/directory. You are getting to see all this information.

Alright, so now our file system [walkthrough is done]. Okay? Basically, you came to know that all that we talked about — under our root partition — a small introduction of them happened; you came to know "yes, what is inside which one."

Okay, now going forward, if you work — because if someone attended my first class properly, and most people would have attended it properly — whoever attended it properly, the concept I explained in it, you will easily be able to collate it with this in the coming classes.

---

## Commands

So now let's start ours: how we can easily create and delete files. Okay, let's start. Right now the viewership is very low, yaar, there are very few people. Okay.

### `cd` — change directory

So look, what happens next — what do I have to do? For example, let me do `ls`. Right now, what do I do first... okay yaar. Now what I have to do is: this is the home directory, I have to go inside it. Okay. Or this `dev` directory that is free — I have to go inside it. To go inside it there is a command: **`cd`**. Okay? Which I have been using until now. `cd` means **change directory**.

What do I have to do — this is my present working [directory], I am at the root partition, I am right at the top. Okay? I have to go inside this directory from here, meaning I have to change. What will I have to take? `cd`, and after that the directory you have to go inside. So we only go inside directories — you cannot give a file name here, you can only give a directory name. So I wrote `cd dev` — went inside this directory.

In the case of Windows, how do we do it? We double-click on any folder and we enter inside it. In this manner, if you have to go inside any file folder, then what will you have to do here — you will have to use this command.

### `ls` — list

I did `cd`. Now, if I have to see how many sub-directories there are inside this directory — meaning how many folders inside the folder, and along with that how many files, meaning how many directories are inside this directory, inside the `dev` directory, okay, and how many files are inside it — so if you have to see that information, for that there is the command **`ls`**. `ls` means "list out the files and directories inside it."

Hit enter — so now you get to see, inside it there are so many files and directories. Okay? So many sub-directories and files. If I talk in [Windows] form: there are folders inside the folder, and there are files. Okay? To see this information inside this directory — now you must have come to know.

### `pwd` — present working directory

Now let me tell you. Look, now let me do one thing — I'm going out once, let me tell you. Now let me do this: look, right now, if somebody asks you "what is your present working directory?" — what is mine right now? This is the present working directory: **`pwd`**. Okay?

Look, what is it — now we have the latest machine, okay, our machine is the latest, so it shows you the full path. Now here a concept comes in. Okay? What concept comes, I will tell you. But first of all let me tell you one thing.

Look, what is it — right now I have to see what its full path is. Actually, the Downloads folder — where is it in our machine, in our file system? Okay? Here it is showing [the full path]. But there will be some machines — if you use a Red Hat machine, use an older UNIX machine — there you won't be able to see it; there you will only be able to see the current working directory. So here it is, the current working directory you will see — here it is, `Downloads`.

If I have to see the full path — which directory I am inside now, what its full path is — to see that there is the `pwd` command: **present working directory**. Hit enter and you will get to see it.

`/root/Downloads`: inside the forward slash, which is the root partition, inside it is my home account, root's, okay — and inside that there is a directory named `Downloads`, inside which I am. This is my full path. Okay? I do `pwd`. Okay, so this shows its full path.

### Absolute path vs relative path

Now let me do this. First let me do [`cd`] — there is nothing. Now what do I have to do — let me tell you a concept. Right now here the indication has come that I am inside the home directory.

A concept comes here: your **absolute path** and **relative path**. Let me tell you about it. A concept comes — what does it mean? Inside it, `Downloads`. Okay. And one is the second: the second one is that it is not the full path. Okay?

Now what do I have to do — from here I have to go inside the Downloads directory. From here I can go in two ways: either by giving the absolute path, or by giving the relative path.

But the thing is: by giving the **absolute path**, you can go inside any directory from anywhere — sitting right here you can go inside any directory from anywhere, but by giving the absolute path.

Now with a **relative path** I cannot do that; it is [relative to] the present working directory. From this onward, if I have to go inside some directory, then I can go.

So now I have to go inside this `Downloads` directory, so simply how will I do it? I did `cd` and I did `Downloads` — I wrote `Downloads` and hit enter, and I went inside it. So that is what I used [a relative path].

If I had to use the absolute path, let me show you — this is its absolute path. Let me use the absolute path: how do I do it? I do `cd`, and after that Ctrl+Shift+V [paste]. Okay? This is my absolute path — this is my absolute path. Meaning, what do I have to do: inside `/root` there is a directory `Downloads`, I have to go inside it. So I hit enter — here it is; now I went and again came inside it.

So these were the two ways. Now let me show an example of the absolute path. Look, right now I am inside this home directory. Okay?

Now let me do this — on the side, what do I have to do... yes, let me understand its meaning. If I have to go to my root partition, okay, then simply I did `cd /` — went to the root partition.

If I have to directly go into the home directory, then I will do `cd`, change directory, and for the home directory I will use this symbol [`~`] — then too I will go inside the home directory.

Again, if I have to... because last time I was in the root partition, but right now presently mine is this one. So if I have to go into the previous directory, how will I go? For that: I did `cd -`, and what did I do — the directory that was in the previous command, meaning the command I had given previously, `cd /`, I will go onto that. I hit `cd -` and entered — look, now what is it: what was my previous command? I was on this one. Okay?

Basically, when I did `cd -`, then it did this, [taking] the previous command — it ran the previous command. In the previous command, what was there? `cd /`. Now again what did I do — take, from that the previous command. Okay? It works very well.

Now let me show you how to do the absolute path way. Let me do [this] once. What do I have to do — my home directory, root's home directory... right now I have to go inside `Downloads`. Okay?

Now simply, I did `cd` and — "the `Downloads` directory isn't there?" Because, brother, you have used a relative path here; it didn't understand it here, the machine. Okay? So now, to make it understand, what will you have to do — you have to give the **absolute path** here. Absolute means: this `Downloads` directory — what do I have to do, I have to `cd`; the `Downloads` directory is inside the root directory: here, `/root/Downloads`.

I hope absolute path and [relative path], both changes, have become clear to you people. Okay?

### `.` and `..`

Now let's continue. Next, let me show you: there is a command of mine, `ls`. I did `ls` — now let me show you one thing. Every directory — however many directories — you will find these. What is their meaning?

- Your current working — **current directory** — okay, the current directory is your single dot **`.`**
- And the **double dot `..`** — this is the current directory's... it represents its **parent directory**.

Meaning: inside the single dot the current directory's address is stored, and the double dot — inside it, its previous [parent] directory.

I used it and hit [enter] — look where I came: inside `/root`. Because if I do `pwd`, look, now I am inside root itself, because that is its home account. So here the address that is stored — whose is it? Its **parent's** address is stored [in `..`], and this dot — its **current** one's is stored.

You will get to see it here too, because it will always be hidden — you will get to see it [with `-a`]. Look, you'll have to look inside... they are hidden. Okay? There are hidden files, and there are hidden directories, sorry. So you will be getting to see this. So this was a small piece of information for you people.

### `ls` options

Now let me tell you a bit about the `ls` command. Okay. Let me give you a bit of info about the `ls` command, let me tell you. Okay, it does listing.

Now what do I have to do — I have to look at the files and sub-directories inside some particular directory; so how can I see them? So what I did: `ls /etc` — I have to [see] all the directories inside `/etc`. Okay, okay, hit enter. Now what did it do — it listed out, that inside the `/etc` directory, all the files that are there, it listed out their information. Okay?

Now the next flag. Which next flag can we use with `ls`? If I have to [see] — it's possible that inside the `/etc` directory some **hidden file** is hidden. Okay? It's possible there are no hidden files either. If I have to see that information, how will I see it? `ls`, okay — and I again did `/etc`, okay — and did `-a`. Now what did it do in this — it showed. Look now: what it did was, along with the hidden files, those two [dot entries] came. Okay? Along with that, it showed that result on your screen.

One more thing there is. Let me do it with this — simply, if I want... now I simply hit [`ls`] without giving any path, so it means it will list out the information inside the present working directory; it will show that. Hit enter — the present working directory, what information is inside it, it showed.

**`-l`** means — what it did was, that particular file or directory, it showed its **detailed information** in front of you. What information? Its **metadata**: look, what permissions are on it, okay; what its size is; who its user is; which group it is part of, okay; when it was created; what that file's name is. All this information you get to see with it.

If [you want], you can use these flags together as well. I did `ls` — if I want to see its hidden files, I did `ls -al` — I can do this too. Enter. Now what did it do: inside it, look — normally only four or five were showing; now see how many files and directories you get to see, because inside it there were a lot of files that were hidden files. Look, here they are — this is the information of your hidden files, come in front of you. Okay?

So you came to know how you people have to use the `ls` command.

### `--help` and `man`

Yes, one more thing let me tell you: if you don't know how to use a command — how to use any command at all — then every command has a **help file**. And how do we see the help file? I wrote the command name, and after that I wrote **`--help`**, hit enter — and then it wrote what the command does, which flags you can use with it, how you can use this command: the command name, with it you'll use a flag, you'll use an option, and after that the file name. Okay?

After that it wrote "list information about the files", okay; after that "sort entries alphabetically" — okay, "note entries alphabetically". Now all of these are those options: the one with which I had used `-a`, okay — `-a` means including hidden files; capital `-A` means almost all; `-b`; capital `-B` — all these things. There are a lot of flags; the commonly used ones I have shown you.

If you want to see only directories, if you want to [list] only directories inside some file, then you can see that too. Okay, `-d`. If you want to see only files, okay; if you want to see [`-h`] — then you can see that too: there the size that will be showing, the file's size, it will show in [human-readable form]. Okay? You got to see this — meaning, so many options can be used with it. Okay?

So these are the many options; its help menu is about this. This is its beauty: if you know the name of a command but don't know how to use it, it simply has a help file — look at the help file, use its flags, you will understand it.

Yes, one more thing there is: if you have to read more detailed information about any particular command, there is a command — **`man`**. Now you will be able to see, this is its entire **manual**. Okay? Meaning, it's a book; everything is written in it with even more detail. If you want, you can go through it, and this is of the command — this is its manual file. If you get stuck anywhere, if you don't understand, if you don't know what task to do and what not to do, then you can do it with its help; you can see it. Okay?

### Tab auto-completion

Now let's talk about a very good thing in Linux: **auto-completion**. How? Look, what happens is that you won't remember every time, in Linux, the directories or files. Okay? But what auto-completion is: you remember this much — "yaar, yes, inside this directory there is something with the name `D`, or with the name `Da`" — maybe there are more directories. Okay?

Right now I did [`ls`]. Okay. Now I know this much, that there is a directory named `D` or `Doc` in it — "Doc" — you don't remember that much, "something like `Doc`, some directory; I have to go inside it." Okay?

Simply, what do you do: you have to change into it. Now what is it — here you will use `D`. I am using a relative path here, because here I can use it. Now we used `D`. Now, as soon as... right now it is showing this; this is its beauty. Otherwise, as soon as you hit **Tab** — look, as soon as you hit Tab, it will show you: "yes, brother, with `D` — in your machine there is one `Desktop`, one `Documents`, one `Downloads`." Okay?

So it became clear to you which one to use. In that, simply, whichever `D`... you'll click and simply go. Then too it will be [fine]. Otherwise, now you'll do `Do` — you'll come to know there is `Doc`; you did it, now you remember this much. Now you hit Tab again — as soon as you hit Tab, what did it do? It will **auto-complete**. It auto-completed it, meaning you won't need to write the full name every time.

Now, if you are in cyber security, if you are on the Linux side, if you don't know auto-completion then you'll keep typing the whole thing all day. Simply hit enter. Now `cd` went back; now what did I do — again I went and I hit `Doc` and Tab — there, it completed. Work happens quickly. Okay?

Otherwise, what is it: if the spelling of `Doc` went wrong, then still it will be a mess. Why did it get messed up? Because **Linux is case-sensitive** — the machine you are using. Okay?

### `mkdir` — create directory

Now let me teach you one thing: how you can create any directory. Okay? How can you create any directory? There is a command **`mkdir`**, and after that you write the name of the directory that you want to keep.

For example, I want to keep the directory's name [`capsule-course`]. It did it — now it created that directory. If you want to see it, I did `ls`, so here you will get to see: yes, a directory named `capsule course` has been created. Okay?

What do I want to do — I want to make a directory whose name I want to keep as `unix`. `unix` — I want to keep this name. Now how will I create this? Now I will do it sitting right here — not that first I'll `cd`, go outside, do the `/tmp` directory, no.

Now how will I do it? Simply: I did `mkdir`, yaar, and I'll give the full path — "yes, brother, inside `/tmp`, okay, a directory named `unix` — what do I have to do, I have to create a directory." Okay? And I hit enter. Now what it did was create a directory named `unix` inside `/tmp`. If you have to cross-check, then take it, I'll do `ls` — sitting from here I'll check. It went inside `/tmp` and I did [`ls`] — look, inside `/tmp` it created a directory named `unix` inside it.

### `mkdir -p` — parent/child in one go

Now one more thing. Now what do you have to do — you want that inside `unix1` I want a [directory] named `tom`. Hit enter — now it created it in this. **`-p`** means: **maintaining the parent–child relationship**, create the directory.

It is saying: "brother, inside `/tmp`, first check whether `unix1` is there or not — if not, create it; [then check whether] the next one is there or not, if not, create it" — so we have to create it, so what did it do, it did all this.

If I show you, `ls /tmp`, hit enter — look, it created `unix1`; earlier it wasn't created. And let me show you inside `unix1` too: if I show you `/tmp` and then `unix1`, do `ls` — look, inside it, it did [create it].

### `rmdir` and `rm -rf` — removing

How do we remove any directory? How do we remove any directory? To remove a directory there is the command **`rmdir`**. Okay? If this directory is **empty**, then it will get deleted right now. Okay? If it is an empty directory, then it will be deleted.

So `mkdir` — sorry — `rm`, remove directory. Okay. And simply, after that I [write] the directory's name: `rmdir capsule...` okay. I hit enter — what did it do, it deleted it, removed the directory.

Now what do I have to do — now I have to delete the directory that has the [nested] structure. So how will I do it? I'll do `rmdir` too, and after that `unix1`. Okay? What do I have to do, I have to delete it, so `rmdir`, and after that what did I do — after that I did `unix`... but I wanted to delete this one — sorry. Now I hit enter. It said "failed to..." because — because the **directory is not empty**.

If the directory is not empty, then you cannot delete it with the `rmdir` command. For that you will have to use [something else]. Okay? You have to use the `rm` command — remember, giving the full path, give it [to `rm`]. First you would have to delete this one, after that you would have to [delete] `unix1`. Okay?

So after that, for this, how can I say it — for that there is the command **`rm`**. Okay? Remove. **`-r`** means [recursive]. Okay? After that, what will I do — I deleted it. Okay?

Now what does this do — this **force** [option]... **This is a very powerful command.** I will give you people one advice here: if you are not [comfortable] with this command, okay — if you are not comfortable with it — then **please don't prefer this command.** Okay? Don't try to use this command, because it is such a dangerous command that if you made any mistake in your path, it will blow up your entire system.

How? For example, you are a beginner, okay, you used the command `rm -rf`. Now you gave [a path], and somewhere carelessly a **space** got inserted; then you gave `/tmp`. Okay? You don't know [the danger]. Now you gave `unix`, okay — you gave `unix`.

Now, brother, look what happens. The **first argument** — because all of them count as arguments, okay; when the first thing is the command, then apart from that, all the space-separated things are understood by it as **arguments**. Now it understood up to here; after this, what did it think? "Oh, this — what is it? Your **root partition**." Okay? Next to it there is a space. Now it won't even pay attention to the rest, because — as soon as it does this, it will blow up your file system, it will delete it. And from that, you are not going to get any benefit at all. Okay?

And this — you are using the command on your system — until you become familiar with it, until you become comfortable with it, don't try to do this. Okay? Up to here you people would have understood.

### `touch` — create files and update timestamps

Now let me talk: if you have to create any file in Linux, then how can you do it? To create a file there are many commands: there is also `cat`, okay; there is also the [`vi`] command, okay; and there is the `touch` command — many [belong to this] family. Okay?

But let me do this — right now let me show you a file related to the `touch` command. Okay? I did `touch` and I created [a file]. Okay, inside it I created... I'm using it [for creation], but basically look: the `touch` command has this feature, but **this is not the main purpose of `touch`.**

Let me tell you: the `touch` command has three or four features. Three or four people say that the `touch` command is used to create any file — so specially it's done for doing some work; for that there are a lot [of editors]: there is nano, there is vi, okay, and there are many of those; with the `cat` command too one can create them.

But what is in the `touch` command — what is the basic purpose of the `touch` command? **To update the timestamp.** What is the main purpose? To update the time. Okay? If I write it out for you: to update the time, basically. Okay?

Now, to update this time: whenever a file is created — when was the file seen, when was it opened, and when is this file accessed — that's the basic meaning. That's the **access time**.

Now the second thing that is attached with it is the **modify time**, meaning: when was this file last modified, when was anything edited in it, when was any data added, when was it last edited. That is the second one.

The third thing that goes with this same thing, we call the **change time**. What does it mean — that if last time you changed the file's location, okay, permissions changed — then its [metadata] changes. About the file: its permissions, where it is stored, okay — meaning basically the information about it, what its size is, what its name is — that is its **metadata**. So when was that last changed.

These three things happen with any file. Now I have to see the information of these three things — for that there is the command **`stat`**. `stat`, and after that you write the file's name.

Today's date is [shown], the current time is there, okay, and in so many seconds — this is showing its modify time, this is showing its change time, this is showing its birth time: when this file [was created] and [became] familiar.

Now I can use the features of the `touch` command. What can I do — I can change all three of these timestamps at once, or one at a time; and the modify time I can change. Okay? The **change** time I **cannot** change directly. Okay? It changes by itself, along with access or along with modify. Okay? And this particular timestamp I can change.

So now, with the `touch` command I can create **multiple files** too. How? For example, I did: `touch linux1 linux2 linux3` — multiple empty files, it created them. Okay?

Now let me show you one thing. I have some timestamp — I just did, one minute, let me `cd` and hit [enter]. After that, `file1`'s time... okay. If I want to change all three of them, of this `file1` — okay, I want to change all three times — then simply what will I do? Now watch. Now, look at its time: its complete time got updated to the current one. Okay?

If I have to update **only the access time** — what do I have to do, update only the access time — then how will I update it? What I'll do: simply, let me once take `stat` of the file... [`file2`]. Okay, this is its [current state]. Now I want to change only `file2`'s access time. How will I do it? I did `touch`, and after that **`-a`**, meaning the access time, and gave that file's name — simply I [gave] the file and hit enter.

Now let me show it to you again: look, only its **access time** changed — and the change time, meaning whenever it is accessed, so that became three times... the rest, the **modify time** did not change.

If I want to change the modify [time] of some particular file, how will I do it? Let me show it on the third file. So what I did: I did `touch` and did **`-m`**, used a flag, and I wrote the file's name, `file3`. Okay? Now let me `stat` it and show you — of `file3`. So you will get to see that only... meaning, every time what will come is the **change** [time]: the metadata's change time — how is it? Because whenever you do any modification in a file, whenever you do anything, it will be updated automatically. So what is it — these two got updated, but this access time hasn't happened.

So these were the `touch` command's [features] — how we can use it. Basically, let me go into my home directory.

### `cat` — create, read, concatenate

Now I was showing you one thing: how we can do it with the `cat` command too. `cat`'s meaning: it is used for **reading content**.

If I have some file... right now let me do it once first. Okay. If I show you one thing — I can do the `cat` command — let me show that. What I did: `cat`, okay, **greater-than sign** — I will tell you its meaning; this is a **redirection symbol** — and I wrote the file's name. Here I am saying: I wrote the file [name] and I wrote [it], and did [enter].

Now what will happen here — it stopped. Meaning, now what is it: "brother, the file has been created; now whatever you write inside it, you will be able to write it." I wrote: "this is a new file". [Music] So this is its new file, and I hit enter. Then the next line came. Until I do **Ctrl+D**, it won't close.

Now let me do it and show you. And now what do I have to do — I have to read its content: what is written inside it. So what will I write for that — I [write `cat filename`], hit enter.

So in this manner, you can use the `cat` command to create a file, and to read the content inside it you can also use the `cat` command.

If you want to [merge] the data of two files — if you want to concatenate them into one file — `cat`'s meaning is to concatenate; you want to concatenate, then you can do that too, you can do it here, there's no [problem]. What will you do — with `cat` you will use both files' names, after that you will use the greater-than sign.

So, once — for example, I created one more file, and [used] the redirect symbol and `file.txt`. I put it inside this file; the file [was] read. Now both lines have been added inside it.

### `rm` — removing files

How do we remove files? Okay, how do we remove a file? For that there is the command **`rm`**. Okay? After that, either give the full path, or the absolute path — give the absolute path, or give the relative path. Okay? When to give the relative path, you know.

I did `rm` — whom? `file1.txt`. What do I have to do — so simply, removed it. Okay, the `rm` command. If I have to remove `file2.txt`, then I did that: `file2.txt` — removed. Okay?

If a video file isn't there, then what will I do — I hit enter.

You can use `--help` — you can look at its help file too. **`-f`** means forcefully. If you use **`-i`** — always try that when you remove, use `-i`. If you are a beginner, you will get [a prompt]: do you really want to delete that file? Maybe you are doing it by mistake, so it will give you a prompt: "think about it, should I delete it or not?" [So] give `-i`.

**`-r`** means recursive: in a line, up to whatever path has been given last, it will keep deleting in a line, from the start to the last. Okay? **`-d`** deletes only a directory; only an empty [directory] it will remove. You can do it like that too.

So this is the `rm` command; if you had to use it, then you can do it like this.

### `cp` — copy

Now let me show you one more command that we'll learn to use: if you have to **copy** from one directory to another directory, how can you do it? Okay?

If I do `ls`, okay — this is mine; I have to copy it inside the `/tmp` directory, so I will use... for that there is the command **`cp`** — copy. After that, what is it, give its absolute path. Okay? Always try — give the absolute path. Okay? Right now I am not giving the path: first `note file3.txt`, and after that the **destination**, meaning where it has to be copied. So where will I do it — inside `/tmp`, because this is above... on the root partition, inside `/tmp` I want to copy this. Simply, and I hit enter.

Now this — your copy has been made. If I do `ls` and show you — let me show you `ls /tmp`, hit enter — you will get to see here: this `file3.txt`, you will get to see it here. Okay?

### `mv` — move and rename

If you have to **move** [a file], or to rename a file, then how will you do it? Okay? For that there is the command [**`mv`**]. Okay?

What do I have to do — first, the file I have in mine, I have to [rename] it; I have to give it a name: `newfile3.txt`. Simply, to rename, I have to give the name right here. Okay? So how can I do it — right here, what I did: I wrote its name `newfile.txt`. Now what it did — it moved it, and with that name. Let me hit enter first — you will get to see.

If I had to move it from one directory to another directory, simply it's the same, the same `mv` command. Okay? Now what I am doing: `newfile.txt`, okay, and what do I have to do with it — I have to do it inside `/tmp`, and now I want to give it a new name here. Here is that file — if I want... here it is, inside your `/tmp`; look, here it will be.

The `mv` command — you can use it for both. Okay?

### `cp -r` — recursive copy

If you feel that... an important feature of the copy command is this: many times a condition came in front of you that you have to copy some file from one directory into another directory, but the thing is, with the full path — for example, inside `/tmp`, `file3.txt` — you [want] `/tmp` plus the file along with it, meaning the whole thing **recursively**.

If you have to do it, then how do you do it? With the `cp` command, what will you do — give the absolute path, put **`-r`**, and after that the absolute path. Okay? After that the source's full [path], then the destination — so you'll write it and simply you will be able to copy it.

So I hope here everyone, in my opinion, would have understood.

### `file` — identify file type

One more thing there is: if these files — how do I come to know whether it's a binary file or which file it is? For that there is the command **`file`**. Okay?

I have to see of this, what type of file it is. I wrote `file` and simply give its name: I have an updated file, `file.jpg`, okay. For example, what I did — and what did it do — we'll know: "oh, this is a JPG file", you will get to see it.

So what will I do with this — simply, to identify it. It comes in very useful for you when you work in security. Okay? With this too you will come to know it's empty. Okay? So `file` basically tells you the **type of file**.

---

## Closing

Now let's talk. Okay, so what I told you today — how you create any directory, how you create any file, or how you copy/move any [file] — I think you people would have understood.

So I feel that today's session should be only this much. Okay? The rest we'll do from tomorrow onwards; from tomorrow we will continue in this same [flow]. Meaning, our next plan — right now the next sessions are there; right now it's one and a half [hours], so from next time it will go a bit longer.

I hope... how many people are with us — 21. It has become very... yaar, how is it? I don't know what to do. Okay, so that we also get motivated, with you people. Okay.
