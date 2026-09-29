# Network Security Day 8 — Nmap Port-Scanning Toolbox: States, TCP Flags aur Scan Types (Hinglish Explanation)

**Source transcript:** `transcripts/052 - Day-8 Network Security Free Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Ayush Pathak
**Builds on:** Day 7 — host discovery, CIDR/ranges, ICMP/TCP/UDP probes
**Continues:** Later Nmap/network-security scanning and service enumeration lessons
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai. Nmap commands only owned/authorized lab ranges par. Spoofing/decoys firewall-evasion theory hai; real networks par use nahi.

---

## 1. Discovery se port scanning tak

Day 7 mein “kaunse hosts alive?” answer kiya. Aaj question:

> Host par kaunse TCP/UDP ports open, closed ya filtered hain?

Command examples mein `<authorized-target>`/`<lab-range>` ko actual approved scope se replace karo.

```bash
nmap <authorized-target>
nmap -p 22,80,443 <authorized-target>
```

Port scan service/protocol exposure identify karta hai; open port vulnerable proof nahi.

---

## 2. Port states

Nmap common states:

| State | Meaning |
|---|---|
| `open` | Application/service listen and accepts/probes |
| `closed` | Host reachable, port par no service listening |
| `filtered` | Firewall/filter response block; open/closed decide nahi |
| `unfiltered` | Accessible but state determine nahi via scan type |
| `open|filtered` | Nmap cannot distinguish |
| `closed|filtered` | Ambiguous response |

Open port high-interest exposure hai, but service/version/configuration further verify only authorized.

---

## 3. TCP flags refresher

TCP header flags:

- `SYN` — connection start request
- `ACK` — acknowledgement
- `FIN` — graceful close
- `RST` — reset/refuse/abort context
- `PSH` — push buffered data
- `URG` — urgent pointer context

Three-way handshake:

```text
client SYN -> server
server SYN+ACK -> client
client ACK -> server
```

Then data transfer. Scan types different flag combinations/responses use karte hain; firewall/OS implementation behavior varies.

---

## 4. TCP Connect scan — `-sT`

```bash
nmap -sT -p 22,80 <authorized-target>
```

Full TCP connection establish karne ki koshish. Unprivileged users ke liye commonly available.

Pros:

- straightforward,
- result easy interpret.

Cons:

- application/OS logs mein connection visible,
- more traffic/noise,
- full handshake overhead.

“Connect scan” stealth guarantee nahi; authorization required.

---

## 5. SYN/half-open scan — `-sS`

```bash
sudo nmap -sS -p- <authorized-target>
```

SYN send, SYN/ACK par normally RST/connection complete na karna. Root/raw packet privileges often required.

Broad interpretation:

- SYN/ACK → open candidate,
- RST → closed,
- no/filtered response → filtered/unknown.

“Stealth” name historical hai; modern IDS/firewall/logging detect kar sakte hain. `-p-` all TCP ports is high-traffic; lab/rate limit.

---

## 6. UDP scan — `-sU`

```bash
sudo nmap -sU -p 53,123,161 <authorized-target>
```

UDP connection handshake nahi. Responses/silence interpretation difficult:

- UDP response → open,
- ICMP port unreachable → closed,
- silence → open|filtered.

UDP slow/noisy ho sakta; common ports targeted and `-T`/timeouts carefully. UDP open service vulnerable proof nahi.

---

## 7. Choosing ports and speed

Port selection:

```bash
-p 22,80,443
-p 1-1024
-p-
--top-ports 100
```

Speed/timing:

```bash
-T2
-T3
-T4
```

Higher speed can:

- overload fragile service,
- trigger IDS,
- drop packets/false negatives,
- violate rate limits.

Start narrow/slow; document command/time/source.

Other useful safe options:

```bash
-oN scan.txt
-v
```

Output files may contain sensitive asset/service data; store securely.

---

## 8. NULL, FIN, Xmas scans

```bash
nmap -sN <authorized-target>  # NULL
nmap -sF <authorized-target>  # FIN
nmap -sX <authorized-target>  # Xmas
```

These set unusual TCP flag combinations:

- NULL: no flags,
- FIN: FIN only,
- Xmas: FIN+PSH+URG.

RFC behavior and OS/firewall responses differ. Modern firewalls/IDS may detect, and many systems return ambiguous results. Don’t treat them as universal stealth or reliable port truth.

---

## 9. ACK and Window scans

```bash
nmap -sA <authorized-target>
nmap -sW <authorized-target>
```

ACK scan primarily firewall rule mapping:

- `unfiltered` means probe can reach,
- not necessarily port open.

Window scan uses TCP window field behavior on some systems; unreliable/OS-dependent. Firewall mapping is sensitive; explicit assessment scope needed.

---

## 10. Custom flags — `--scanflags`

Nmap can craft flag combinations:

```bash
nmap --scanflags SYNFIN <authorized-target>
```

This is advanced research/defensive lab only. Custom packets can trigger IDS, instability or attribution issues. Understand protocol before testing.

---

## 11. Source spoofing and decoys

Transcript `-S` source spoofing and `-D` decoy concepts discuss karta hai:

```bash
# Theory only—do not run outside an explicit lab
nmap -S <approved-spoof-source> <authorized-target>
nmap -D decoy1,decoy2,ME <authorized-target>
```

Technical limits:

- Replies spoofed source ko nahi mil sakte; scan results incomplete.
- Decoys anonymity guarantee nahi; timing/traffic correlation possible.
- Third-party decoy IPs ko involve karna harm/abuse.
- Firewall/IDS and provider policies may block.

Defensive testing mein source spoof/decoy only written ROE, isolated network, pre-approved addresses and monitoring. Normal learning ke liye standard scan sufficient.

---

## 12. Scan decision flow

```text
1. Written scope and target range
2. Host discovery result
3. Small top-port TCP scan
4. State interpretation
5. UDP only where required
6. Service/version enumeration with approval
7. Save output securely
8. Stop and report/remediate
```

`-sS` vs `-sT` privilege/logging; `-sU` UDP; `-sA` firewall; weird scans troubleshooting/OS fingerprint caveat.

---

## 13. Common mistakes aur exam-worthy corrections

1. Open port = vulnerable service.
2. Closed port = host down.
3. Filtered = definitely closed.
4. SYN scan fully invisible/stealth.
5. UDP silence = open.
6. `-p-` harmless default.
7. Higher `-T` always better.
8. NULL/FIN/Xmas universal bypass.
9. ACK scan open ports identify karta hai.
10. Spoof/decoy anonymity guarantee.
11. Scan output public chat/GitHub mein upload.
12. Production/Internet range scan without authorization.

---

## 14. 20-second cheat card

```text
-sT  TCP connect/full handshake
-sS  SYN/half-open
-sU  UDP
-sN  NULL flags
-sF  FIN flag
-sX  Xmas flags
-sA  ACK/firewall mapping
-sW  Window behavior (OS-dependent)
-p   port selection; -p- all TCP ports
-T   timing; higher = faster/noisier/riskier
-S   source spoof theory—authorized lab only
-D   decoys—no anonymity guarantee
```

---

## 15. Day 8 self-check questions

1. `open`, `closed`, `filtered`, `unfiltered` states explain karo.
2. TCP three-way handshake mein flags ka role kya?
3. `-sT` aur `-sS` compare.
4. `-sU` silence ko ambiguous kyu treat karta hai?
5. `-p-` aur `--top-ports` ka difference.
6. Timing templates service/network risk kaise change karte hain?
7. NULL/FIN/Xmas scans OS/firewall-dependent kyu?
8. ACK scan open port proof kyu nahi?
9. Source spoofing/decoy ke practical limits kya?
10. Authorized Nmap assessment ka safe workflow likho.

---

## 16. Continuity

Network Security Days 1–8 ne network fundamentals se host discovery aur port-state scanning tak foundation banayi. Next sessions service/version enumeration, Nmap advanced options aur later vulnerability testing ko authorized labs mein connect karenge.
