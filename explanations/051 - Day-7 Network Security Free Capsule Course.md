# Network Security Day 7 — Bind/Reverse Shells aur Nmap Host Discovery (Hinglish Explanation)

**Source transcript:** `transcripts/051 - Day-7 Network Security Free Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Ayush Pathak
**Builds on:** Network Days 1–6 — ports, TCP, VPN, reconnaissance and diagnostic tools
**Continues:** Day 8 Nmap port scanning
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai. Shell and Nmap commands only isolated, owned lab machines/ranges par; real systems par unauthorized access/scanning nahi.

---

## 1. Shell kya hai?

Shell = command interpreter/interface jahan commands execute hoti hain. Security labs mein shell milne par:

- command input,
- process/output,
- filesystem/system info,
- network actions
possible hote hain.

Shell access itself admin/root access proof nahi. Least privilege and authorization maintain karo.

---

## 2. Bind vs reverse shell

### Bind shell

Target/listener apne port par listen karta hai; attacker/client target ke port se connect karta hai:

```text
client -> target listener
```

Challenges:

- target inbound port reachable,
- firewall/NAT allow,
- target IP/port known,
- exposure detector ko visible.

### Reverse shell

Target outbound connection attacker/listener ki taraf initiate karta hai:

```text
target -> listener
```

NAT/firewall ke cases mein outbound path easier ho sakta hai, but egress filtering, detection and authorization remain.

Reverse shell malware/backdoor technique ho sakti hai; only lab.

---

## 3. WSL two-terminal demo concept

Transcript Windows/WSL-style two terminal setup se shell communication demonstrate karta hai:

- one terminal listener,
- another lab process/client,
- commands and output exchange.

Production/public interface par listener bind mat karo. Localhost/host-only lab IP use:

```bash
ss -lntup
ip addr
```

Lab teardown ke baad listener/process terminate, firewall rule remove, snapshots restore.

---

## 4. Discovery Nmap se start

Before port/service enumeration, alive hosts identify karne hain. Nmap target range:

```bash
nmap -sn 192.168.56.0/24
```

`-sn` host discovery/no port scan intent. Replace with authorized lab CIDR only.

Single/range notation:

```bash
nmap -sn 192.168.56.10
nmap -sn 192.168.56.10-20
```

CIDR/range carefully calculate; accidentally public/production range scan mat.

---

## 5. ARP discovery

Same LAN par ARP host discovery effective ho sakta hai. Nmap privileged/local context mein ARP probes use kar sakta; `arp-scan` separate tool:

```bash
sudo arp-scan --localnet
```

Output IP/MAC/vendor clues de sakta hai. Vendor inference exact device/person proof nahi. Wi-Fi/VLAN/router boundaries ARP visibility limit karte hain.

---

## 6. Nmap probe types

### ICMP echo

```bash
nmap -PE -sn 192.168.56.0/24
```

Firewall ICMP block se false negatives.

### ICMP timestamp/address mask

```bash
nmap -PP -sn <authorized-range>
nmap -PM -sn <authorized-range>
```

Network/device support varies; unnecessary probes avoid.

### TCP SYN ping

```bash
sudo nmap -PS22,80,443 -sn <authorized-range>
```

### TCP ACK ping

```bash
sudo nmap -PA80,443 -sn <authorized-range>
```

### UDP ping

```bash
sudo nmap -PU53,161 -sn <authorized-range>
```

Probe response/ICMP errors se host inference; no response means unknown, not definitely down.

---

## 7. Privilege/location matrix

Nmap root/admin privileges par raw packet/ARP options use kar sakta; unprivileged mode TCP connect/other behavior use karega. Local LAN vs routed network par probe availability differ.

Command output mein:

- `Host is up` = probe response/evidence,
- no result = firewall/route/probe/host uncertainty.

`-Pn` host discovery skip karke hosts “up” assume kar sakta; only when authorized and you know ping blocked. It is not a bypass for unauthorized target scanning.

---

## 8. DNS during scanning

Nmap reverse DNS lookup kar sakta. Names helpful but slow/noisy/misleading ho sakte. Options (version/man page check):

```bash
nmap -n ...       # no DNS resolution
nmap -R ...       # always resolve
nmap --system-dns ...
```

DNS name old/shared/automated ho sakta. Report IP and resolved name with timestamp.

---

## 9. Discovery decision flow

```text
1. Written scope/CIDR confirm
2. Local vs routed network identify
3. ARP discovery for same LAN
4. ICMP/TCP/UDP probes as needed
5. DNS resolution policy choose
6. Host list save with timestamp
7. Only then authorized port scan
8. Stop/rate limit/log
```

Discovery is not exploitation. Alive-host list mein personal device data minimize.

---

## 10. Common mistakes aur safety points

1. Bind/reverse shell difference reverse karna.
2. Shell access ko root access samajhna.
3. Reverse shell payload public target par use.
4. Nmap `-sn` ko harmless anywhere samajhna.
5. CIDR/range typo se broad scan.
6. ICMP no response = host down.
7. `-Pn` ko authorization bypass.
8. ARP scan routed internet range par.
9. DNS name ko verified identity.
10. Listener/firewall/temporary access cleanup na karna.

---

## 11. Day 7 self-check questions

1. Bind aur reverse shell data-flow compare karo.
2. Reverse shell NAT/firewall context mein often easier kyu ho sakta?
3. Shell access aur privilege escalation alag kyu?
4. `nmap -sn` ka intended purpose kya?
5. Nmap target CIDR carefully define kyu?
6. ARP discovery same LAN mein useful kyu?
7. `-PE`, `-PS`, `-PA`, `-PU` broad purpose kya?
8. ICMP/TCP/UDP no response interpret kaise karoge?
9. `-Pn` ka effect kya hai?
10. DNS `-n`/`-R` choices ka purpose kya?
11. Lab shell/listener cleanup steps kya hain?

---

## 12. Continuity

Day 7 ne live hosts locate karne ke safe methodology di. Day 8 mein Nmap port states, TCP flags aur scan types (`-sT`, `-sS`, `-sU`, NULL/FIN/Xmas/ACK) explain honge—same authorized-range boundary ke saath.
