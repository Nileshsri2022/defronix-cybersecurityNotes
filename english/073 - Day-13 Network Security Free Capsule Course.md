# Day-13 Network Security Free Capsule Course — English Translation

*Translated from: `073 - Day-13 Network Security Free Capsule Course [ Hindi ].hi-orig.srt`*
*Style: faithful edited translation; repeated live-chat checks and caption stutters are condensed.*

---

The instructor returns to TryHackMe's network-security path and connects the earlier service-enumeration rooms to a broader question: what can go wrong when application protocols send data in cleartext?

## Why cleartext is dangerous

Protocols such as HTTP, FTP, Telnet, SMTP, POP3, and IMAP were originally designed without transport encryption. Anyone who obtains a suitable position on the network may inspect usernames, passwords, requests, messages, and transferred files. The lesson separates the security goals:

- **Confidentiality:** outsiders must not be able to read the data.
- **Integrity:** data must not be altered unnoticed in transit.
- **Authentication:** each endpoint needs confidence about the other's identity.

A packet capture is used to show readable application data, including an HTTP request and login fields. Filtering traffic in Wireshark makes clear that TCP delivery does not make application content confidential.

## Sniffing and man-in-the-middle position

On a wired or switched network, an attacker normally needs visibility of the victim's traffic rather than merely being connected somewhere on the LAN. On wireless networks, capture depends on adapter mode, channel, encryption, and network access. The instructor explains ARP: hosts map IPv4 addresses to MAC addresses through local broadcasts and cached replies. Because classic ARP has no authentication, forged replies can poison caches and place an attacker between a client and its gateway.

Once traffic is redirected, an attacker may passively read it or actively alter it. Forwarding must continue or the connection simply breaks, making the attack obvious. These demonstrations belong only in an isolated, authorized lab.

## Secure replacements and TLS

The remedy is not to hide protocol names or ports; it is authenticated encryption. TLS can wrap application protocols and provide confidentiality, integrity, and server authentication through certificates. Common secure alternatives include HTTPS instead of HTTP, SSH instead of Telnet, and encrypted variants of mail and file-transfer protocols.

A certificate binds a public key to a hostname through a chain of trust. During a TLS handshake the parties negotiate cryptographic parameters, authenticate the server, derive shared session keys, and then protect application records. Certificate warnings matter: encryption to an unauthenticated endpoint can still leave a user talking to an impostor.

The practical conclusion is to prefer modern secure protocols, disable obsolete cleartext services, validate certificates, segment networks, and use packet analysis to verify that secrets are not exposed.

<!-- DONE-073 -->
