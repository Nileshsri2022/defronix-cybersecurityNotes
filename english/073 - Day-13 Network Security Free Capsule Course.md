# Day-13 Network Security Free Capsule Course [Hindi] — English Translation

*Translated from: `073 - Day-13 Network Security Free Capsule Course [ Hindi ].hi-orig.srt`*
*Style: detailed edited translation. Repeated stream commentary and caption duplication are consolidated; technical clarifications are marked [TN].*

---

Hello guys, welcome to Day 13 of Network Security. The lectures through Day 12 are already uploaded. I hope you completed them in sequence instead of jumping directly here, because today's concepts build on the protocols and services we already studied.

In earlier rooms, we joined a network without initially knowing its architecture. We learned to identify live hosts, scan ports, enumerate services, and consider firewall behavior. In Network Services 1 and 2 we studied protocols including SMB, Telnet, FTP, NFS, SMTP, and MySQL.

Today we step back from exploiting one service and ask a larger theory question:

> What security problems occur when a protocol sends information in cleartext, and how do secure protocols solve them?

# Cleartext protocols

Several traditional application protocols were designed when network trust assumptions were very different:

- HTTP
- FTP
- Telnet
- SMTP
- POP3
- IMAP

In their original cleartext forms, anyone able to observe the traffic can read application data. TCP may deliver bytes reliably, but reliability is not confidentiality.

Suppose a user submits a username and password to a website over HTTP. A packet capture can reveal the request method, host, path, headers, form fields, cookies, and credentials. The same principle applies to FTP or Telnet authentication and to unencrypted mail traffic.

This threatens three main security properties:

1. **Confidentiality** — an unauthorized person can read data.
2. **Integrity** — someone in the path may change data.
3. **Authenticity** — the client may not know whether it is speaking to the genuine server.

# Sniffing traffic

Sniffing means capturing network packets for inspection. Wireshark can display the traffic visible to an interface and decode known protocols.

In the room demonstration, application-protocol filters are used to focus on relevant packets. An HTTP request is readable because HTTP itself does not encrypt its contents. You can follow a stream and reconstruct the conversation.

Merely being connected to the same modern switched network does not guarantee that every other host's unicast traffic appears on your interface. An observer needs an appropriate network position—for example, control of a gateway, a mirrored switch port, a compromised access point, or a successful man-in-the-middle technique.

On a wired network, physical and switch topology matter. On wireless networks, adapter mode, channel, association, Wi-Fi encryption, and key access matter. The simplified phrase “anyone on Wi-Fi can read everything” is not universally true, but local-network trust is still insufficient protection. Sensitive application traffic should protect itself cryptographically.

Only capture networks and systems you own or are explicitly authorized to assess.

# Man-in-the-middle attacks

A man-in-the-middle (MITM) attack places an attacker between two communicating parties:

```text
client ↔ attacker ↔ server
```

If the attacker forwards traffic, both endpoints may continue communicating without immediately noticing the intermediary. The attacker can passively observe data or actively alter it.

This is more serious than simple eavesdropping. If data lacks integrity protection, the intermediary might modify a download, change a request, inject content, or redirect a victim.

# ARP and ARP spoofing

Within an IPv4 local network, a host needs a destination MAC address to send an Ethernet frame. **ARP**, the Address Resolution Protocol, maps local IPv4 addresses to MAC addresses.

A host effectively asks:

```text
Who has this IP address? Tell me your MAC address.
```

The request is broadcast on the local segment, and the owner responds. Hosts cache mappings so they do not have to ask for every packet.

Classic ARP does not authenticate replies. In an ARP-spoofing/poisoning attack, a malicious machine sends false mappings, convincing:

- the victim that the attacker's MAC belongs to the gateway IP;
- the gateway that the attacker's MAC belongs to the victim IP.

Traffic can then be routed through the attacker's machine. To remain in the middle, it normally forwards packets onward; otherwise it causes denial of service rather than a transparent interception.

The room uses this to explain how an attacker could gain the necessary network position to inspect cleartext application protocols. The lesson is conceptual and belongs in an isolated lab.

Defenses at the local-network layer include segmentation, switch features such as Dynamic ARP Inspection where supported, secure wireless configuration, endpoint monitoring, and avoiding untrusted LANs. But the essential application defense remains end-to-end authenticated encryption.

# Why encryption is the answer

If intercepted packets contain ciphertext rather than readable application data, capture alone does not reveal the protected content. Secure communication should provide:

- encryption for confidentiality;
- integrity/authentication tags against modification;
- endpoint authentication so the client recognizes the intended server.

Simply inventing a new port or encoding text is not encryption. The protocol needs sound cryptography and correct key management.

# TLS

**TLS**, Transport Layer Security, is used to protect many application protocols. In OSI/TCP-IP diagrams, application protocols such as HTTP operate above TCP; TLS sits between the application behavior and the transport connection, protecting application records.

HTTPS is HTTP over TLS. Other protocols can also use TLS directly or upgrade an existing cleartext connection through a command such as STARTTLS, depending on the protocol.

A simplified TLS connection does the following:

1. Client and server negotiate supported protocol/cryptographic parameters.
2. The server presents a certificate containing its public-key identity.
3. The client validates the certificate and hostname through a trusted certificate chain.
4. The handshake establishes shared session keys.
5. Application records are encrypted and integrity-protected with those keys.

Modern handshakes are more precise than this summary, but the key point is that efficient symmetric session encryption is established through an authenticated handshake.

# Certificates and trust

A certificate connects a public key to an identity such as a DNS hostname. It is signed by an issuer. A browser or operating system has a trust store containing certificate authorities (CAs), allowing it to build and validate a chain from the site certificate to a trusted root.

Validation includes questions such as:

- Is the certificate within its validity period?
- Is it issued for the hostname being visited?
- Is the signature chain trusted?
- Is the certificate permitted for server authentication?
- Has policy/revocation information made it unacceptable?

A certificate warning should not be dismissed blindly. Encryption without authenticating the endpoint can still produce an encrypted connection to an attacker.

# Secure alternatives to older protocols

The room connects common cleartext services to protected alternatives:

| Cleartext/insecure use | Protected alternative |
|---|---|
| HTTP | HTTPS (HTTP over TLS) |
| Telnet | SSH |
| FTP | SFTP over SSH, or correctly configured FTPS |
| POP3 | POP3S / POP3 with TLS |
| IMAP | IMAPS / IMAP with TLS |
| SMTP | SMTP with TLS, plus correct certificate and downgrade policy |

SFTP and FTPS are not the same protocol. SFTP is an SSH file-transfer subsystem; FTPS is FTP protected with TLS.

A secure port number alone is not proof of security. Configuration, certificate verification, protocol versions, cipher choices, and downgrade resistance still matter.

# What packet capture looks like after TLS

With HTTPS, Wireshark can still observe metadata: endpoint IPs, ports, packet sizes, timing, and parts of handshake negotiation. Depending on protocol/version and features, some naming metadata may also be visible. But the HTTP request body, cookies, and credentials should not appear as readable plaintext to an ordinary passive observer.

This distinction matters: encryption protects content, not every possible traffic characteristic.

# Operational guidance

Organizations should:

- disable unnecessary cleartext services;
- redirect HTTP to HTTPS but also deploy HSTS where appropriate;
- use modern TLS versions and supported cryptography;
- validate certificates rather than disabling checks;
- protect private keys;
- segment sensitive systems;
- avoid transmitting credentials through protocols that do not protect them;
- use packet captures in an authorized environment to verify that secrets are not exposed.

Users should avoid entering passwords after browser certificate warnings or on plain HTTP pages. VPNs can protect a path to the VPN endpoint, but they do not replace correct end-to-end application security.

# Closing

The major lesson is not a list of secure port numbers. It is the difference between **transporting data** and **protecting data**.

Cleartext protocols allow a suitably positioned observer to read—and sometimes modify—communications. ARP spoofing is one local-network method that can create such a position. TLS and SSH provide authenticated cryptographic channels that defend application data even when the underlying network is not trusted.

In the next lessons, continue analyzing protocols by asking:

1. What information travels over the network?
2. Is it encrypted?
3. How are endpoints authenticated?
4. What happens if an attacker can observe or alter packets?

<!-- DONE-073 -->
