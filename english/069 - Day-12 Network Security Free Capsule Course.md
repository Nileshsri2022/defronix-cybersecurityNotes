# Day-12 Network Security Free Capsule Course — English Translation

*Translated from: `069 - Day-12 Network Security Free Capsule Course [ Hindi ].hi-orig.srt`*
*Style: faithful edited translation; repeated live-chat checks and caption stutters are condensed.*

---

The instructor opens Day 12 by recapping the previous TryHackMe Network Services room. Today's lab continues with less commonly examined network services. The workflow remains the same throughout: identify the host, enumerate the exposed service, understand its normal purpose, look for weak configuration, and only then attempt exploitation.

## NFS — Network File System

NFS lets a server share directories with clients over a network. It uses RPC for client/server communication. Begin with an Nmap scan, enumerate RPC/NFS exports, and use `showmount -e TARGET` to list exported paths. Create a local mount point and mount an export with `mount -t nfs TARGET:/export /tmp/mount -o nolock`. Once mounted, inspect permissions, owners, hidden files, and useful executables.

The important configuration is root squashing. Normally `root_squash` maps a remote root user to an unprivileged identity. A share exported with `no_root_squash` may allow a client-side root user to create a root-owned SUID executable on the share. When the target executes that file, it can provide local privilege escalation. The lesson demonstrates the lab sequence: discover export, mount it, inspect `/etc/exports`-style behavior, create/copy an executable, set the SUID bit, and execute it on the target. This is a deliberately vulnerable training machine; do not test systems without authorization.

## SMTP enumeration

SMTP transfers email. Typical ports are 25, 465, and 587. Before attempting credentials, enumerate the mail server and users. Nmap SMTP scripts and Metasploit's SMTP enumeration module can test names through commands supported by a poorly configured server. The instructor stresses gathering the hostname, software/version, and valid user names first. A discovered username can then be reused in the lab's SSH password-auditing step. Enumeration is what turns a broad attack into a precise one.

## MySQL enumeration

MySQL is a relational database service, commonly on TCP 3306. Scan it, identify the version and authentication behavior, and test only credentials supplied or discovered in the lab. Metasploit auxiliary modules can enumerate version, users, databases, and hashes when access is available. After connecting, use database-native commands to list databases and tables, select a database, describe a table, and query records. The instructor connects this back to earlier SQL lessons: network access is only the doorway; understanding schema and permissions determines what can actually be read or changed.

## Closing guidance

Record every command and result, distinguish service enumeration from exploitation, and understand the misconfiguration rather than copying commands blindly. The room is designed to show how legitimate sharing, mail, and database services become dangerous when exposed or configured with excessive trust.

<!-- DONE-069 -->
