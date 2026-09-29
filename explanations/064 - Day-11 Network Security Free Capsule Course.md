# Explained — 064 — Day 11: Network Security (TryHackMe "Network Services" — SMB, Telnet, FTP end-to-end)

**Source:** Defronix Academy Network Security free capsule course, Day 11 — instructor **Ayush Pathak** (not the Bash series' Nitesh). Full walkthrough of TryHackMe's *Network Services* room with live AttackBox + target machines.
**Arc of the class:** protocol theory → enumeration → exploitation for three services: **SMB**, **Telnet**, **FTP**. Every exploit lands through *misconfiguration*, not CVEs — and that's the class's explicit thesis.

---

## PART A — the enum → exploit rhythm (applies to all three services)

```
theory answers → nmap (discover ports) → service scripts (-A/-sV or enum tool)
→ find a misconfig (anonymous access, weak creds, moved-to-odd-port service)
→ loot files → credentials/keys → lateral connect (ssh/ftp/netcat) → flag
```

Two universal attack doors named each time: **(1) CVE route** — vulnerable version (e.g. Samba RCE affecting 3.5.0→4.6.4 window) — "no matter how perfect the config, if the version is bad it gets wrecked"; **(2) misconfiguration route** — the day's route, "because CTFs and real companies are *full* of it: anonymous login enabled for testing, never disabled."

## PART B — SMB

### Theory core
- **Server Message Block** — client-server, request-response protocol, over **TCP/IP** (reliability needed for file moves — contrast UDP's fire-and-forget). Purpose: **resource sharing** — file systems, folders, printers — with *or without* authentication, per server config.
- Native to **Windows since Win95**; the open-source Unix implementation is **Samba**.

### Enumeration answers (as found)
| Find | Value |
|---|---|
| SMB ports (also on Linux!) | **139 + 445** (+22 ssh) |
| Version (via `nmap -A`) | Samba smbd **4.7.6**-ish, OS Windows 6.1 |
| Tool | **enum4linux -a** ("do all basic enumeration") |
| Workgroup / machine | **WORKGROUP** / **POLOSMB** |
| OS version | **6.1** |
| Share worth investigating | **profiles** |

### Exploit chain — the anonymous-share snowball

1. **Method note:** default scan → spot 139/445 → re-scan just those with `-A` (scripts dig shares/workgroup/version), and **enum4linux** automates the rest.
2. Connect the share **anonymously**: `smbclient //IP/profiles -U Anonymous`, press Enter at the password prompt → **in**. (General syntax dr1lled: `smbclient //IP/SHARE -U user [-p port]`.)
3. **Loot:** `get "Working From Home Information.txt"` (double quotes for spaced names!) → the memo names **John Cactus** and says he works from home over **SSH**.
4. Hidden dir `.ssh/` inside the share → `get id_rsa` — the **private** SSH key (the pub key is harmless; the private one is the crown jewel).
5. Local key hygiene: **`chmod 600 id_rsa`** or `ssh` refuses it (permission-bits recap: 4=read, 2=write, 1=execute; user/group/others).
6. First attempt **fails**: `ssh -i id_rsa john@IP` → connection closes. The class's punchline: ***"a CTF is all about enumeration — TRY every possibility, even the one that 'can't be right.'"*** Username wasn't `john`; it was **cactus** → `ssh -i id_rsa cactus@IP` → **shell** → `ls` → `cat flag.txt` → **flag.**

**Takeaways:** no system-level RCE was needed — an exposed share leaked a private key that *became* a login; and the *username guessing* was pure enumeration discipline.

## PART C — Telnet

### Theory core
- Application protocol, **plaintext** (no **encryption**) → replaced by **SSH**. Connect: `telnet IP PORT` (default **23**).

### The enumeration lesson of the entire room
- Basic nmap (default **top-1000** ports) → **nothing open**. The author deliberately ran Telnet on **port 8012 — a non-standard port**.
- Only a full **`nmap -p-`** finds it (4-digit port — the question's hint). Re-running *without* `-p-` (the room literally asks you to) → 0 ports → **law: sweep fast for momentum, but ALWAYS finish with a full detailed scan.**
- His parallel habit: run quick scans (any tool) alongside; heavy/aggressive scans can even mislead; methodology is personal, not a constant.

### The backdoor & the closed-loop RCE
- `telnet IP 8012` → banner **"SKIDY'S BACKDOOR."** — the box was pre-compromised by "Skidy," who left an unauthenticated command service on a moved port.
- `.HELP` reveals the grammar: **`.RUN <command>`** executes… but prints **nothing** — *blind* command execution.
- **Proving execution without output** (elegant, learn this): run **tcpdump** on your box (attack-box interface = **tun0**), then `.RUN ping -c 1 <yourIP>` → your packets in tcpdump = remote execution confirmed.
- Blind RCE → so upgrade to a shell: fire **`nc -lvnp 4444`**, generate a **mkfifo+netcat reverse payload** (he used a revshell generator; notes it's nc invoked via mkfifo for evasion), `.RUN <payload>` → **reverse shell** lands → `ls` → `cat flag.txt` → **flag.**
- Terminology nail-down: victim calls *you* = **reverse shell**; you call victim = **bind shell**. If the backdoor had echoed output, no shell would have been needed — *the reverse shell exists because output didn't.*

## PART D — FTP

### Theory core
- **Two channels:** command + data are separate — so you can send commands **during** a transfer (one channel would force waiting — inefficient for big files/slow links).
- **Active mode:** client opens a port & listens; server actively connects to *it*. **Passive mode:** server opens & listens; client connects. → **2 modes.**
- Model: client-server (request-response); standard port **21**.

### Exploit chain — note → username → hydra → flag
1. nmap `-p 21 -A` → **vsftpd**, and the script already reports **anonymous login enabled**.
2. `ftp IP` → user **anonymous**, empty password → `ls` → **PUBLIC_NOTICE.txt** → `get` it.
3. The notice is signed "**Yours, Mike**" — a leaked **username**. (Small files are never just files.)
4. Brute force: **`hydra -t 4 -l mike -P <passlist> -vV <IP> ftp`** — `-t 4` parallel tasks, lowercase `-l` = single user (capital `-L` = a user *list*), `-P` = password file, `-vV` = verbose. Result: password is literally **`password`** ("bhai, the password IS password").
5. Login as `mike` → `cd ftp` → `get ftp.txt` → **flag** (plus a decoy `future_backup.rb` — noted and ignored).
6. Why this world exists, verbatim: *"For testing they enabled anonymous login, finished their work, and FORGOT to disable it — this happens in real companies; CTFs are loaded with it. CVE-y old systems are rarer prey than plain misconfiguration."*

## E) Session mechanics worth keeping

- Cross-series logistics: this capsule moves slowly *by design* so it can co-run with the live Bash series (9 lectures then).
- Study habits he pushes: pause and try to be **one step ahead** of the instructor; command memorization is optional, concept clarity is not ("broad-strokes knowledge is mandatory"); short notes > complete notes.
- Career funnel: LinkedIn page = course launches, cert discounts, first-come challenges/beta tests; share room completions tagging the company page; can't afford THM? — **build a local lab** (install your own SMB server etc.).
- Next lecture announced: **Network Services 2** room.

## F) Pitfall table

| Symptom | Root cause | Cure |
|---|---|---|
| nmap shows "no open ports" on a host that clearly has one | service moved to a non-standard (>1000) port | always finish with `nmap -p-` |
| `ssh -i id_rsa user@IP` closes instantly | (a) key too permissive → `chmod 600`; (b) **wrong username** | try every name the loot leaked (`john` vs `cactus`) |
| `.RUN id` gives no confirmation | backdoor is a **blind** RCE — no stdout | detect it out-of-band: `tcpdump` + ping-back / reverse shell |
| reverse shell never lands | wrong listener flag or wrong interface/IP in payload | `nc -lvnp 4444` + embed YOUR tun0 IP (`10.10.x.x`) |
| hydra hammers the wrong user-set | lowercase `-l` = ONE user; capital `-L` = user LIST | use `-l mike` once the notice leaked the name |
| `smbclient` won't connect though share exists | missing `//IP/SHARE` double-slash syntax or `-U` user | `smbclient //IP/profiles -U Anonymous` + Enter at pwd |
| spaced filenames break `get` | shell splits on spaces | quote it: `get "Working From Home Information.txt"` |

## G) Cheat card

```
SMB      : Server Message Block · client-server · TCP/IP · 139/445 · Samba = *nix impl
           enum4linux -a ; smbclient //IP/SHARE -U user [-p port] ; anonymous + Enter = test misconfig
           loot: .ssh/id_rsa → chmod 600 → ssh -i id_rsa USER@IP (try EVERY looted name)

TELNET   : plaintext app protocol (no encryption) · port 23 · SSH replaced it
           lesson: nmap default = top-1000 → moved ports hide → ALWAYS -p- finish
           backdoor grammar: .HELP → .RUN cmd  (blind exec)
           prove exec: tcpdump + ping-back · shell: mkfifo/nc payload → nc -lvnp 4444
           reverse = victim→you · bind = you→victim

FTP      : port 21 · 2 modes (active: server connects TO client · passive: passiv)
           2 channels (cmd + data) = commands don't wait on transfers
           anonymous/'' login → read the NOTICE → names → hydra -t 4 -l mike -P rockyou.txt -vV IP ftp
           cracked: password="password" → cd ftp → get ftp.txt → flag

GENOME   : 2 doors = CVE (vuln version) or MISCONFIG (anonymous/left-enabled) — today = misconfig 3×
           rules: sweep fast THEN full scan · loot→leads→creds→shell · try the "impossible" option too
```

**Next class (announced):** Network Services **part 2** room (NFS is the usual content of that sequel — not stated, don't bank it), same slow-pacing policy.
