# Network Security Day 3 — Packets, Frames, Ports, Port Forwarding, Firewalls aur VPN Basics (Hinglish Explanation)

**Source transcript:** `transcripts/047 - Day-3 Network Security Free Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Ayush Pathak
**Builds on:** Network Days 1–2 — IP/MAC, ARP/DHCP, OSI/TCP-IP and topology
**Continues:** Day 4 portmap.io/OpenVPN practical, Metasploitable lab
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai. Port forwarding, firewall testing and shells only owned lab/VMs par.

---

## 1. Packets aur frames

Application data network par directly travel nahi karta. Encapsulation:

```text
application data -> TCP segment/UDP datagram -> IP packet -> link-layer frame -> bits
```

- **Packet:** Layer 3 IP context.
- **Frame:** Layer 2 local-link context.
- **Segment:** TCP transport data.
- **Datagram:** UDP transport data (term context-dependent).

Envelope analogy: each layer apna header add karta hai; receiver decapsulate karta hai.

---

## 2. Useful headers

Packet/frame headers mein context-specific fields ho sakte hain:

- source/destination MAC,
- source/destination IP,
- protocol,
- source/destination port,
- TCP flags,
- TTL,
- checksum/length.

Header metadata routing, delivery, integrity and troubleshooting mein help karta hai. Captured packet mein IP visible hone ka matlab encrypted application content readable hona nahi; TLS/SSH payload protect kar sakte hain.

---

## 3. TCP close handshake revision

TCP connection establish/close stateful hota hai. High-level close:

```text
FIN -> ACK
FIN -> ACK
```

Actual simultaneous/half-close states vary. TCP flags (`SYN`, `ACK`, `FIN`, `RST`, `PSH`, `URG`) later Nmap scanning mein important honge.

`RST` abnormal reset/connection refusal/close context de sakta hai. One packet capture se application intent overclaim mat karo.

---

## 4. Ports

IP host/network interface identify karta hai; port service/application endpoint identify karta hai:

```text
192.168.1.10:22  -> SSH service candidate
192.168.1.10:443 -> HTTPS service candidate
```

Port states:

- Open: service listen/accept likely.
- Closed: host reachable but no service listen.
- Filtered: firewall/filter prevents determination.

Common ports memorize karna useful, but actual service port change ho sakta hai; banner/version verify authorized scan mein.

---

## 5. Port forwarding

Private LAN device usually direct internet inbound reachable nahi. Router NAT ke through external port ko internal host/port par forward kar sakte hain:

```text
Internet:public_ip:external_port
        -> router NAT rule
        -> internal_ip:service_port
```

Use cases:

- self-hosted lab service,
- remote VM access,
- authorized test application.

### 5.1 Risk

Port forwarding internal service ko internet exposure deta hai:

- authentication weakness,
- outdated software,
- brute-force/noise,
- accidental admin panel exposure.

Safer lab controls: VPN, allowlisted source IP, temporary rule, strong auth, patched service, logs, no default credentials, close rule after test.

UPnP auto-port-forwarding audit karo.

---

## 6. Firewalls

Firewall rules traffic allow/deny/filter karte hain based on:

- source/destination IP,
- port/protocol,
- interface/direction,
- state/connection.

Host firewall aur network/perimeter firewall separate layers ho sakte hain. Default-deny + explicit required access generally safer than open-all.

Firewall “filtered” scan state create kar sakta hai. Rule change only change-control/authorized lab.

---

## 7. VPN basics

VPN encrypted tunnel/virtual network connection create kar sakta hai:

```text
client -> encrypted tunnel -> VPN server/network -> destination
```

Uses:

- remote private lab access,
- protect traffic from local untrusted network,
- route into authorized network.

VPN does not mean perfect anonymity, invisibility or permission. VPN provider/network admin can have metadata; endpoint can still identify account/device.

---

## 8. Troubleshooting flow

```text
1. Service running?
2. Host interface/IP correct?
3. Route/gateway available?
4. Firewall rule?
5. Router/NAT forwarding?
6. External DNS/public IP correct?
7. Client port/protocol correct?
```

Commands:

```bash
ip addr
ip route
ss -lntup
ping <lab-ip>
traceroute <authorized-host>
```

No ping reply alone proof nahi; service/port test and firewall logs compare.

---

## 9. Common mistakes aur safety points

1. Packet/frame/segment terms mix.
2. Port ko IP address samajhna.
3. Open port ko vulnerable proof bolna.
4. Port forward ko firewall protection samajhna.
5. Internet par default credentials expose.
6. VPN ko complete anonymity samajhna.
7. NAT/forwarding rule remove na karna after lab.
8. Firewall allow-all rule create karna.
9. Port scan/forwarding real public IP par without authorization.

---

## 10. Day 3 self-check questions

1. Encapsulation sequence likho.
2. Packet aur frame ka broad difference kya?
3. TCP flags ka close-handshake context kya hai?
4. Port open/closed/filtered meanings compare.
5. Port forwarding ka NAT flow diagram banao.
6. Port forwarding se risk kaise create hota hai?
7. Firewall rules kin fields par based ho sakti hain?
8. VPN kya protect karta hai aur kya guarantee nahi?
9. Network-service troubleshooting order kya hoga?
10. Authorized lab ke baad temporary forwarding rule kyu close karna chahiye?

---

## 11. Continuity

Day 3 ne packets se port/service boundary tak path explain kiya. Day 4 mein portmap.io/OpenVPN ke through private lab service ko safely expose/connect karna aur Metasploitable 2 jaise intentionally vulnerable lab target ka setup aayega.
