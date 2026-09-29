# Day-13 Network Security — Cleartext, MITM, ARP, and TLS — Explained

## The trust-boundary shift

Previous days treated each exposed service as a target to enumerate. Day 13 changes the question:

```text
Earlier: What service is listening, and how is it configured?
Today:   Can the communication itself be trusted on an untrusted network?
```

A correctly functioning cleartext protocol may still be insecure for sensitive data. “No software vulnerability found” does not imply confidentiality or authenticity.

---

# 1. Security properties

## Confidentiality

Only authorized parties can read data. Encryption primarily provides confidentiality.

## Integrity

Unauthorized alteration is detectable. Modern authenticated encryption protects both secrecy and integrity. Encryption without authentication can be malleable.

## Authentication

A party can verify who is on the other end. TLS commonly authenticates the server with certificates; mutual TLS can authenticate both endpoints.

## Availability

Systems remain usable. MITM positioning without correct forwarding may destroy availability even if it fails to read protected content.

These properties are independent. A checksum can detect accidental corruption without authenticating an attacker. Encoding can change representation without creating confidentiality.

---

# 2. What a packet observer learns

## Cleartext HTTP example

A capture may expose:

```http
POST /login HTTP/1.1
Host: example.test
Cookie: session=...
Content-Type: application/x-www-form-urlencoded

username=alice&password=secret
```

That can reveal credentials, session identifiers, personal data, and actions. Hashing a password in a database does nothing to protect it while an application sends the entered plaintext over HTTP.

## Encrypted HTTPS example

A passive capture still sees network-layer metadata:

- source/destination addresses;
- ports and transport behavior;
- timing, sizes, and connection duration;
- TLS handshake/version details;
- potentially hostname-related metadata depending on TLS/DNS configuration.

It should not reveal ordinary HTTP headers/body without access to endpoint/session secrets. Traffic analysis can still infer patterns; “encrypted” does not mean invisible.

## Wireshark workflow in a legal lab

Useful display filters:

```text
arp
http
ftp
smtp
pop
imap
tls
tcp.stream eq N
```

“Follow TCP Stream” reconstructs payload bytes from a selected connection. Capture filters and display filters are different: capture filters decide what is recorded; display filters choose what recorded traffic is shown.

Never collect third-party communications without authorization. Packet captures often contain credentials and personal data and must be handled as sensitive evidence.

---

# 3. Network visibility

## Hubs versus switches

A hub repeats frames to all ports, making passive observation easier. A switch learns MAC locations and normally sends unicast frames only to the relevant port. Broadcast/multicast behavior differs.

Therefore “same LAN” does not automatically mean “see every packet.” Visibility may arise through:

- legitimate switch port mirroring;
- gateway/access-point control;
- compromised network equipment;
- local protocol attacks;
- endpoint compromise;
- wireless capture under appropriate technical conditions.

Application encryption should assume the network may be observable anyway.

---

# 4. ARP mechanics and poisoning

## Normal ARP

A local IPv4 sender decides whether a destination is on-link using its route table and subnet. For an on-link next hop, it needs a MAC address:

```text
broadcast: Who has 192.0.2.1?
unicast:   192.0.2.1 is at aa:bb:cc:dd:ee:ff
```

The result enters a neighbor/ARP cache.

Linux inspection:

```bash
ip neigh show
ip route show
```

## Poisoning concept

An attacker transmits fraudulent association information so the victim and gateway cache the attacker's MAC for each other's IP. If forwarding is enabled, traffic traverses the attacker.

This is possible because basic ARP was not designed with cryptographic authentication. It is limited to the local broadcast domain; routers do not forward ARP requests across the internet.

## Defensive controls

- client isolation on suitable wireless networks;
- VLAN segmentation and minimal broadcast domains;
- DHCP snooping plus Dynamic ARP Inspection on managed switches;
- static mappings only where operationally manageable;
- monitoring for conflicting/rapidly changing IP–MAC associations;
- endpoint firewalls and secure application protocols;
- encrypted/authenticated network access.

ARP defenses reduce one positioning method. TLS remains necessary because many other intermediaries legitimately carry traffic.

---

# 5. TLS handshake mental model

A modern TLS 1.3 handshake, simplified:

```text
ClientHello
  supported versions, cipher suites, key share, extensions
        ↓
ServerHello
  selected parameters, server key share
        ↓
encrypted handshake messages
  certificate, certificate verification, Finished
        ↓
client verifies identity and handshake
        ↓
encrypted application data
```

Ephemeral key exchange derives shared secrets without transmitting the final symmetric session key directly. Authenticated encryption protects records.

Do not use this simplification to implement cryptography yourself. Use maintained TLS libraries and secure defaults.

## What certificates prove

A valid web PKI certificate supports the claim:

> A trusted issuer verified, under its policy, control/identity associated with these names and signed this public key binding.

It does not prove the site is honest, bug-free, or safe to give data to. It proves authenticated transport identity under the PKI model.

## Hostname validation

A certificate for `example.com` should not authenticate `login.example.net`. Clients compare the requested hostname with certificate Subject Alternative Names. Disabling hostname checks defeats a central defense against MITM.

## Private keys

If a server's certificate private key is stolen, an attacker may impersonate that server while the certificate remains trusted. Protect keys with restricted access, secure deployment, rotation, and revocation/incident procedures.

---

# 6. Protocol upgrade pitfalls

## Implicit TLS versus STARTTLS

Some protocols use a dedicated port where TLS begins immediately (“implicit TLS”). Others begin cleartext and issue `STARTTLS` to upgrade.

An upgrade design must prevent downgrade stripping. If client/server policy treats TLS as optional and continues after the upgrade disappears, an active intermediary may force cleartext.

## HTTPS redirect limitation

An HTTP-to-HTTPS redirect occurs after an initial HTTP request. HSTS tells supporting browsers to use HTTPS directly for future visits, reducing downgrade exposure. Preloading can protect the first visit under program requirements.

## Secure alternatives are not aliases

- SSH replaces Telnet's remote-shell role but is a different protocol.
- SFTP runs over SSH and is not “FTP with an S.”
- FTPS extends FTP with TLS and retains FTP's control/data-channel complexity.

Architecture and firewall rules differ.

---

# 7. Certificate warnings

A warning may indicate:

- expired/not-yet-valid certificate;
- hostname mismatch;
- unknown/self-signed issuer;
- interception proxy not trusted by the client;
- incomplete certificate chain;
- incorrect system time;
- captive portal or malicious interception.

In a controlled Burp/Wireshark lab, a locally installed test CA may be intentional. Scope that trust to a dedicated browser/profile and remove it afterward. Never normalize “click through every warning.”

---

# 8. Defensive verification checklist

For each service:

1. Inventory protocol and listening port.
2. Determine whether TLS is implicit, upgraded, or absent.
3. Test supported protocol versions and certificate chain.
4. Confirm hostname validation in every client—not only browsers.
5. Verify cleartext alternatives are disabled or safely redirected/upgraded.
6. Capture authorized traffic and search for secrets.
7. Test downgrade/failure behavior: does the client fail closed?
8. Protect keys and document renewal.
9. Monitor certificate expiry and configuration drift.

A server can support TLS and still leak credentials if an alternate cleartext endpoint remains available.

---

# 9. Common misconceptions

**“It uses TCP, so it is secure.”**  
TCP provides ordered reliable transport, not secrecy or peer identity.

**“The password is hashed in the database.”**  
At-rest password hashing does not protect login traffic.

**“The URL has a lock, so the business is trustworthy.”**  
The lock indicates a validated encrypted connection to the named endpoint, not ethical intent.

**“A VPN makes HTTP end-to-end secure.”**  
It encrypts traffic to the VPN endpoint. Traffic beyond that endpoint and the application itself still require HTTPS.

**“Changing the port hides the protocol.”**  
Service fingerprinting and packet contents can identify it; obscurity is not cryptographic protection.

**“Base64 is encryption.”**  
It is reversible encoding without a secret key.

---

# Review card

```text
ARP: IP-to-MAC resolution on local IPv4 segment; unauthenticated by design.
MITM: attacker obtains an in-path position and may observe/alter traffic.
TLS: authenticated handshake + key establishment + protected records.
Certificate: signed binding between public key and identity/name.
HTTPS: HTTP carried through TLS.
SSH: secure remote login/channel protocol; replacement for Telnet use cases.
```

## Review questions

1. Why does switched Ethernet not guarantee confidentiality?
2. Which properties distinguish encryption from authenticated encryption?
3. Why is ARP poisoning local to a broadcast domain?
4. What must an attacker do to remain a transparent MITM rather than cause only denial of service?
5. What does certificate hostname validation prevent?
6. What metadata can remain visible even when HTTPS protects content?
7. Why can opportunistic STARTTLS be vulnerable to downgrade?
8. Why is SFTP not the same as FTPS?

<!-- DONE-073 -->
