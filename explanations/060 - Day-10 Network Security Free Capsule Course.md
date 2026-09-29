# Explained — 060 — Day 10: Network Security (Basic Protocols Room: Telnet, HTTP, FTP, SMTP, POP3, IMAP)

**Source:** Defronix Network-Security free capsule, Day 10 (~50 min, live TryHackMe walkthrough, AttackBox + telnet + ftp client + Wireshark screenshots). **Format:** a THM "basic protocols" REVISION room, completed end-to-end with five flags/quiz answers.
**Strategic position:** the last theory-wide pass before the course pivots to exploitation. Day-11 starts the apply phase: SMB → enumerate → exploit, then telnet & FTP the same way, then a Network-Security challenge room, then a Defronix-built CTF. **Nothing here is skipped content — it is the loading screen for the exploit rooms.**
**The one-sentence takeaway he wants tattooed:** *every protocol in today's room is clear-text* — and **telnet is the universal skeleton key that lets you type them all by hand**.

---

## A) Framing — what a protocol even is

> **"A protocol is a SET OF RULES for HOW communication happens."**

Every network service you'll ever probe advertises itself through such a ruleset. Two direct corollaries for an operator: (1) learn a handful of them deeply and the rest are dialects, (2) if the rules say *"commands are sent without encryption,"* then **any plain TCP socket — like the telnet client — can speak the protocol fluently.** That is the entire thesis of today's room.

## B) Telnet — the unencrypted remote terminal (and why it's still in your toolbox)

- **Purpose:** remote shell over TCP — username/password, then system commands — **no encryption anywhere.**
- **Default port: 23.** (`telnet <IP>` with no port ⇒ 23.)
- **The Wireshark moment:** sniff a telnet session and the **username & password ride by in readable plaintext** — the definitive demo of why it's deprecated for real logins. **Secure alternative: SSH.**
- **Why you still care:** telnet-the-*client* is not for remote shells anymore — it is a **raw, line-oriented TCP console**, and *every* clear-text protocol in this room (HTTP, SMTP, POP3, IMAP) plus banner-grabs of FTP can be driven through it: `telnet <IP> <port>`, then type protocol commands by hand. This exact skill is reused constantly in CTFs and manual service probing.

## C) HTTP by hand — the Host header lesson

- **Port 80**, request/response text protocol; you're fetching resources with **`GET`**, submitting with `POST`, etc.
- **Manual session:**
  ```bash
  telnet <IP> 80
  GET /flag.txt HTTP/1.1        # ← alone = 400 Bad Request
  Host: <IP>                    # ← required header for HTTP/1.1
  (press Enter twice — the second Enter dispatches the request)
  ```
- The 400 forced the teaching point: **HTTP/1.1 needs a Host header** because of **virtual hosting** — one server / one IP serving **many websites** (shared hosting); the server decides WHICH site you're asking for by reading `Host:`. Optional additives (`User-Agent:` etc.) mimic a real browser but weren't needed for the flag.
- Server landscape to name-drop correctly: **Apache & Nginx = open source; Microsoft IIS = closed source.** (Fast banner-recon via telnet/manual GET was re-shown and will keep paying rent.)

## D) FTP — two channels, two modes, one foot-gun of cleartext

- **File Transfer Protocol**, **default port 21**, **clear-text** like everything else today.
- Architecture: **TWO channels** — a **control (command) channel** and a separate **data channel** that carries file bytes.
- **Two modes for the data channel:**
  - **ACTIVE** — the **FTP SERVER originates** the data connection back to the client (from its side).
  - **PASSIVE** — the **CLIENT originates** the data connection (`PASV` command). *(Deep-dive deferred to the exploitation room — know the direction arrow today.)*
- Transfer types: **`type a`** = ASCII (text), **`type i`** = image/binary.
- Survival commands: `ls`, **`get <file>`** (download), `bye` (quit). Real-world daemons: **vsftpd, ProFTPD**.
- **Task mechanics done live:** `ftp <IP>` → user **frank** + password → `ls` reveals `ftp_flag.txt` → `get ftp_flag.txt` → `bye` → `ls` locally = file + flag. (Same warning as always — the "why is anonymous/weak-credential FTP dangerous" pendulum lands in the next room with misconfig exploitation.)

## E) The e-mail machine — four agents, two fetch protocols

### The cast (learn the words, not by memorization but by role)

| Agent | Abbr | Job (one line) |
|---|---|---|
| **Mail User Agent** | **MUA** | your mail client (Thunderbird, phone app — *analogous to the browser for web*) |
| **Mail Submission Agent** | **MSA** | receives YOUR outgoing mail, **error-checks** it, hands on |
| **Mail Transfer Agent** | **MTA** | **transfers/routes** the mail across the internet to the recipient's MTA — *routing, not checking* |
| **Mail Delivery Agent** | **MDA** | final landing spot — stores the mail until the recipient's MUA picks it up |

**Compression reality:** MSA & MTA are *"commonly hosted on the same server"*, and MTA & MDA likewise — **so your typical mail server is all three server-side roles at once.** Also possible: a fully private mail service between two machines **with no internet access** (the room's self-host remark).

### The flow, as deliverable sentences

`You(MUA) → MSA (checks) → MTA (routes over the internet) → recipient's MTA → MDA (stores) → recipient MUA (fetches)`

His **post-office retelling**: you, the sender, are an MUA handing a letter at the counter; the clerk who inspects and accepts it = **MSA**; the sorting office that reads the address and dispatches it to the *right town's* post office = **MTA**; that town's post office + your street-side mailbox = **MDA**; the recipient peering into their mailbox every morning = their **MUA**. He repeats the full chain twice in Hindi on his own diagram, marking the inter-server hop explicitly as **"OVER THE INTERNET."** The most important *protocol mapping* falls out of it:

| Conversation | Protocol |
|---|---|
| MUA ↔ MSA/MTA (submitting mail) | **SMTP** |
| MUA ↔ MDA (retrieving mail) | **POP3** or **IMAP** |

## F) SMTP by hand (port 25)

Simple Mail Transfer Protocol, clear-text ⇒ **telnet-talkable**:
```bash
telnet <IP> 25            # NOT 23 — he almost types 23 aloud, self-corrects ("sorry, 25 hoga")
HELO telnet               # greeting/handshake
MAIL FROM: a              # envelope sender
RCPT TO: defronix         # envelope recipient → here: "address rejected — user unknown in local table"
DATA                      # enter message mode …type the body…
.                         # on a line by itself, i.e. <CR><LF>.<CR><LF> = "Enter, DOT, Enter" to submit
```
- His `RCPT TO` hit **"user unknown in local table"** — the lab ships no dest users, which he flags honestly and **promises a real end-to-end SMTP practical once he finds a good resource**. (The connect banner itself carried the room's flag.)
- Replies worth squinting at: `250`-family positives vs `5xx` rejects — they'll matter during SMTPenumeration (VRFY/EXPN) later in pentest training.

## G) POP3 — download & (by default) destroy (port 110)

```bash
telnet <IP> 110
USER frank   →  +OK
PASS <pw>    →  +OK logged in
STAT         →  +OK nn mm      # nn = NUMBER of mails · mm = TOTAL size in bytes
LIST                            # enumerate messages
RETR 1                          # fetch message #1
QUIT
```
- **The default behavior everyone underestimates:** once the client downloads the mail, **the server DELETES it** — changeable in client settings, but even then POP3 keeps **no read/unread state synchronized across devices**. One phone reading a mail = every other device blind about it.
- Live task answer: `+OK 0 0` → quiz: zero mails, zero bytes.
- Where you've seen its name before: adding an email account to an old phone → "POP or IMAP?" — this is *that* choice.

## H) IMAP — synchronization as a protocol feature (port 143)

**Internet Message Access Protocol** = POP3's grown sibling: **the authoritative mail store lives on the server; all changes (read, move, delete, flags) are saved ON the server** ⇒ every device sees one synced truth. That is the entire reason the modern mail world migrated.
**One syntactic novelty:** every IMAP command is **prefixed by a random tag** so that pipelined requests can be matched to replies:
```bash
telnet <IP> 143
c1 login frank <pw>      →  c1 OK login completed
c2 LIST "" *             →  INBOX, Drafts, Sent/Outbox, Trash, Spam, …  (mail FOLDERS)
c3 EXAMINE INBOX         →  selects INBOX (0 mails in today's lab)
…(fetch/logout per room)…
```
The tag `c1/c2/c3` is arbitrary ("kuch bhi likhiye — aapki marzi") — it echoes back verbatim in the matching response, so clients can track "which answer belongs to which question." *(Your GUI client hides all of this behind the refresh button — his internal-working reminder.)*

## I) The anti-memorization sermon (whenever protocols repeat, he repeats this)

> "We don't need to memorize the commands. The things you use daily — keep CHEAT-SHEETS. The rest — don't even try. **Understand HOW it works**; names will glue themselves with use."

Applies verbatim to SMTP/POP3/IMAP verb sets: know the *shape* (greet → auth/envelopes → act → quit), look the words up when needed.

## J) Roadmap announced (next classes)

1. **Day-11 → THM "Network Services" room** — **SMB from zero**: what it is → **enumeration** → **exploitation**. (SMB isn't in the module, but he inserts it anyway: "major role in network security.")
2. Same room, then **Telnet — enumerate & exploit**, **FTP — enumerate → misconfigurations → exploit**.
3. **Network-Security CHALLENGE room** (THM-built).
4. Back to the module path; later a **pure-network CTF**, and eventually a **Defronix-designed challenge** (possibly run live) on THM or another platform.
Rationale stated again: **structured path > module completion** — TryHackMe supplies the structure; he injects what it lacks.

## K) Pitfalls & context worth retaining

| Symptom | Cause | Fix |
|---|---|---|
| `400 Bad Request` on a hand-typed GET | missing `Host:` header (HTTP/1.1) | always send `Host: <target>`; vhost servers route by it |
| telnet → nothing on port 23 | confusing service ports | telnet=**23**, SMTP=**25**, HTTP=**80**, FTP=**21**, POP3=**110**, IMAP=**143** |
| `get` behaves oddly / corrupt binary files | ASCII transfer against binary content | `type i` before `get` for binaries |
| mail "disappeared" from the server | POP3 default = delete-after-download | client setting to keep copies — or use IMAP when multi-device |
| multi-device mail out of sync | POP3 has no server-side state | IMAP (state lives on server) |
| `c1: command not found`-style confusion in IMAP | forgot the **tag** prefix | every IMAP verb gets a tag: `c1 LOGIN …` |
| sniffed creds on legacy boxes | telnet/FTP/SMTP/POP3/IMAP are all cleartext | wrap with SSH/TLS equivalents (courses ahead) |

## L) Cheat card

```
protocol  = standard set of RULES for "how to communicate"
all of today's room = CLEAR-TEXT  ⇒  telnet <IP> <port> = universal manual client

telnet :23   remote shell, plaintext creds over the wire → replaced by SSH
                 reuse: raw TCP console for every text protocol + banner grabs

http   :80   GET /flag.txt HTTP/1.1 + Host: <IP>  (2× Enter to send)
             Host header ⇒ virtual-hosting: many sites, one IP — server routes by Host
             Apache/nginx = open · IIS = closed

ftp    :21   clear-text · control channel + data channel
             active = SERVER opens data conn · passive = CLIENT opens (PASV)
             type a (ascii) / type i (binary) · ls · get · bye · vsftpd / ProFTPD

MAIL   ┌ MUA  (client) ──SMTP──► MSA(check) ─► MTA(route) ══internet══► MTA ─► MDA(store) ──POP3/IMAP──► MUA
       └ roles collapse: MSA+MTA+MDA usually ONE server

smtp   :25   HELO · MAIL FROM: · RCPT TO: · DATA · body · <CRLF>.<CRLF>
pop3   :110  USER/PASS · STAT → "+OK nn mm" (count/total-bytes) · LIST · RETR n · QUIT
             default: downloads then DELETES on server · no multi-device sync
imap   :143  sync source of truth ON server; EVERY command prefixed by A TAG: c1 login · c2 LIST "" * · c3 EXAMINE INBOX

rule   : don't memorize verbs → learn the shape, keep cheat-sheets (his standing sermon)
```

**Next class (announced):** Day-11 = **THM "Network Services"** — **SMB deep-dive: understand → enumerate → exploit**, then telnet & FTP the same sequence; after it, the **Network-Security CHALLENGE** room.
