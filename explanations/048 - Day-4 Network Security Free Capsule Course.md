# Network Security Day 4 — Portmap.io, OpenVPN aur Metasploitable 2 Lab (Hinglish Explanation)

**Source transcript:** `transcripts/048 - Day-4 Network Security Free Capsule Course [Hindi].hi-orig.srt`
**Trainer in transcript:** Ayush Pathak
**Builds on:** Network Day 3 — ports, forwarding, firewall and VPN basics
**Continues:** Day 5 active/passive reconnaissance
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai. Intentionally vulnerable VMs ko isolated lab mein rakho; internet exposure or exploitation without authorization nahi.

---

## 1. Problem: private lab ko safely reach kaise karein?

Agar vulnerable VM/private service local network ke andar hai, internet se direct access nahi. Router port forwarding possible but risky. Session portmap.io + OpenVPN ko remote lab connectivity example ke roop mein use karta hai.

```text
student client -> VPN tunnel/portmap service -> local lab service
```

Purpose: authorized learners same lab service access kar saken without exposing random router ports.

---

## 2. Portmap.io/OpenVPN workflow

High-level lab steps:

1. Portmap.io account/course-approved setup.
2. OpenVPN client/config download.
3. Credentials/config ko private rakho.
4. VPN connection start.
5. Portmap tunnel/forward create for the specific lab port.
6. Local vulnerable VM service running verify.
7. Remote test from authorized client.
8. Session ke baad tunnel/forward disconnect/delete.

Linux example concept:

```bash
sudo openvpn --config lab-client.ovpn
```

Exact command/platform configuration transcript/course-provided file par depend.

### 2.1 Credential safety

- `.ovpn` config mein certificates/keys ho sakte hain.
- File GitHub/public chat/screenshot mein upload mat karo.
- Strong unique account password/MFA where available.
- VPN logs and source IP behavior samjho.
- Course lab credentials rotate/disable after class.

---

## 3. VPN “two-minute think”

VPN encrypted tunnel provide karta hai, but:

- endpoint service vulnerable ho sakti,
- VPN server/admin metadata dekh sakta,
- public internet anonymity guarantee nahi,
- application authentication still required,
- exposed forwarded port scanners ko visible ho sakta.

Portmap/VPN ko authorization aur isolation ka replacement nahi. It is a controlled connectivity layer.

---

## 4. Metasploitable 2

Metasploitable 2 intentionally vulnerable Linux VM hai, learning labs ke liye. Use:

- host-only/internal network preferred,
- snapshot before experiments,
- no bridge/public internet unless controlled,
- known lab IP inventory,
- restore/cleanup after exercise.

Network connectivity check:

```bash
ip addr
ping <metasploitable-lab-ip>
```

Ping blocked ho sakta; service test only approved scope. Vulnerability exploitation walkthrough ko lab VM tak strictly limit karo.

### 4.1 Lab boundaries

- No production/home router/college network.
- No scanning random public IPs.
- No credential reuse.
- No outbound pivot from vulnerable VM.
- Snapshot/isolated NAT/host-only rules document.

---

## 5. Kali-side toolbox preview

Next reconnaissance phase ke liye Kali tools mentioned/used ho sakte hain:

```bash
ip addr
ip route
ping <target>
ss -lntup
nmap --version
```

Tool output ko understand karo; commands blindly copy-paste na karo. Service enumeration requires written scope and rate limits.

---

## 6. Lab troubleshooting

If remote connection fails:

1. VPN process/log status.
2. Tunnel interface/route.
3. Portmap forward active.
4. Local VM service listening.
5. Host firewall.
6. Correct lab IP/port.
7. Client network path.

```bash
ip addr
ip route
ss -lntup
sudo systemctl status openvpn
```

Exact OpenVPN service name distro/config par vary ho sakta hai. Secrets ko terminal screenshot se redact.

---

## 7. Common mistakes aur safety points

1. Portmap ko public exposure-free guarantee samajhna.
2. `.ovpn`/private key share karna.
3. Metasploitable VM bridged/public interface par chhodna.
4. Vulnerable target ko daily network se connect karna.
5. VPN tunnel active chhodna.
6. Wrong port/IP troubleshoot kiye bina exploit tool run.
7. Ping failure ko service failure proof.
8. Lab snapshot/rollback na banana.
9. Portmap account password reuse.
10. Intentionally vulnerable VM se outbound traffic allow.

---

## 8. Day 4 self-check questions

1. Private lab service ko direct router port forwarding se expose karne ka risk kya hai?
2. Portmap.io/OpenVPN workflow ke major steps kya hain?
3. `.ovpn` file sensitive kyu ho sakti hai?
4. VPN encryption kya protect karti hai aur kya nahi?
5. Metasploitable 2 ko host-only/internal network par kyu rakhna chahiye?
6. Vulnerable VM ka snapshot kyu?
7. Remote connection troubleshoot karne ke seven checks likho.
8. Nmap/exploitation commands ke liye scope kyu required?
9. Lab complete hone par tunnel/forward delete kyu?

---

## 9. Continuity

Day 4 ne safe lab connectivity banayi. Day 5 mein network reconnaissance—active vs passive, WHOIS, DNS, DNSDumpster, Shodan aur Wayback—ko defensive scope ke saath apply kiya jayega.
