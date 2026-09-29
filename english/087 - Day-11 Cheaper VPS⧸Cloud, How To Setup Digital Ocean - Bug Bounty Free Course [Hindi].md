# Day-11 Cheaper VPS/Cloud, How To Set Up DigitalOcean — English Translation

*Translated from: `087 - Day-11 Cheaper VPS⧸Cloud, How To Setup Digital Ocean - Bug Bounty Free Course [Hindi].hi-orig.srt`*
*Style: detailed edited translation. Repeated live-chat checks, promotions, and rolling captions are consolidated.*

---

## Why use a VPS?

Welcome to Day 11. In the previous cloud session we discussed AWS. Today the objective is a simpler and potentially cheaper virtual private server for authorized bug-bounty reconnaissance, using DigitalOcean as the example.

A VPS is a remote Linux machine in a data center. It can remain online after your laptop disconnects, usually has stable bandwidth and a public IP, and can run long reconnaissance jobs. It does not make scanning legal, bypass a program's limits, or guarantee that tools run faster. Scope and rate restrictions remain exactly the same.

Cloud billing is continuous while resources exist. Before creating anything, understand the hourly/monthly price, storage, backups, snapshots, traffic allowance, taxes, and charges for reserved addresses. Configure a budget alert and plan how the server will be destroyed after use.

## Account and project setup

Create an account through the official DigitalOcean site. Use a unique password and enable multi-factor authentication. Complete billing verification directly with the provider rather than through an unknown link. Organize the work inside a project so droplets, volumes, and networking are easy to identify and remove.

Never expose an API token in screenshots, shell history, public GitHub repositories, or course chat. If a credential is exposed, revoke and replace it immediately.

## Creating a Droplet

A DigitalOcean virtual machine is called a **Droplet**. Choose **Create Droplet**, then make the following decisions:

1. **Region:** choose a data center with reasonable latency and acceptable program/provider jurisdiction. Region does not change authorization.
2. **Image:** select a supported Ubuntu LTS release unless a tool has another documented requirement.
3. **Plan:** begin with the smallest plan that has enough memory and CPU. Recon tools can exhaust low-memory machines, but oversizing wastes money.
4. **Authentication:** prefer an SSH key over a root password.
5. **Hostname:** use a clear neutral name such as `recon-worker-01`, not a target's brand.
6. **Backups/volumes:** enable only when needed and understand their cost.

## SSH key authentication

On the local machine, generate a dedicated key if necessary:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/do-recon -C "recon-worker"
```

The public file (`.pub`) can be uploaded to DigitalOcean. The private key must remain private and should have restrictive permissions:

```bash
chmod 600 ~/.ssh/do-recon
```

After creation, connect using the displayed public IP:

```bash
ssh -i ~/.ssh/do-recon root@SERVER_IP
```

A first-connection host-key prompt protects against silently connecting to a different machine later. Verify the fingerprint from the provider console when possible; do not habitually delete host-key warnings.

## Initial hardening

Update the supported operating system:

```bash
apt update
apt upgrade
```

Create a normal administrative user and grant sudo access:

```bash
adduser researcher
usermod -aG sudo researcher
```

Copy the authorized SSH key into that user's account using a safe method such as `ssh-copy-id`, then test a second session before changing root access.

After key login works, harden SSH according to current distribution guidance: disable password authentication and direct root login, keep the firewall rule for SSH, and restart/reload the service carefully. Locking SSH before testing the new account can strand you outside the server.

## Firewall

A recon worker normally needs no publicly reachable service except SSH. Configure DigitalOcean's cloud firewall and/or the host firewall to allow TCP 22 only from your trusted current IP where practical. Do not expose databases, development dashboards, or proxy ports to the internet.

Example host policy:

```bash
ufw allow from YOUR_IP to any port 22 proto tcp
ufw enable
ufw status verbose
```

If your source address changes frequently, update the rule deliberately; do not solve inconvenience with `0.0.0.0/0` plus weak passwords.

## Installing a working environment

Install only maintained dependencies needed by the approved workflow:

```bash
apt install git curl wget jq tmux unzip build-essential
```

Some recon tools use Go or Python. Install language runtimes from maintained sources, pin/document versions, and avoid piping unknown internet scripts directly into a root shell. Validate official repositories and release checksums.

Create a predictable workspace owned by the normal user:

```bash
mkdir -p ~/recon/{scope,raw,resolved,http,results,logs}
chmod 700 ~/recon
```

Put only a reviewed in-scope target list in `scope/`. Tools should consume that list rather than unfiltered internet discoveries.

## Long-running jobs

Use `tmux` so a dropped SSH connection does not terminate an authorized job:

```bash
tmux new -s recon
# run the job
# Ctrl-b then d to detach
tmux attach -t recon
```

Redirect output and errors to logs. Set concurrency and request rates explicitly. More bandwidth does not mean the target permits more traffic.

Monitor resources:

```bash
htop
df -h
free -h
```

A full disk can corrupt output and destabilize services. A process consuming all memory may be killed by the kernel.

## Cloud-provider and program rules

The source IP belongs to a cloud network and is visible to targets. Some programs disallow cloud-hosted scanning, some impose strict automation rules, and some block data-center ranges. Read the brief first. Never rotate IPs to evade blocking or rate limits.

Do not run open proxies, phishing pages, callback collectors, or vulnerable applications on a public droplet without an explicit controlled design. Keep evidence encrypted/restricted and avoid storing unnecessary personal data.

## Cleanup

When the authorized work is complete:

1. download only necessary sanitized results;
2. stop jobs and review logs;
3. delete sensitive temporary data;
4. destroy the droplet;
5. remove unattached volumes, snapshots, backups, and reserved IPs;
6. revoke unused API tokens and SSH keys;
7. verify billing/resources from the provider dashboard.

Powering off a droplet may not stop all charges because storage and reserved resources still exist. Destruction and dashboard verification are necessary.

## Closing

A VPS is valuable because it offers stable remote compute and repeatability. The professional workflow is not “create a fast server and scan everything.” It is:

```text
secure account
→ least-privilege server
→ validated scope
→ controlled rates
→ reproducible logs
→ prompt cleanup
```

<!-- DONE-087 -->
