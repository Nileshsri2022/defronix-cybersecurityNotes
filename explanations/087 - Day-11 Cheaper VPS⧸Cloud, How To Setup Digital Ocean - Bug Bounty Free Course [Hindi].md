# DigitalOcean VPS for Authorized Recon — Explained

## Architecture

```text
local workstation
  └─ SSH with dedicated key
       └─ DigitalOcean Droplet
            ├─ reviewed scope file
            ├─ maintained recon tools
            ├─ rate/concurrency controls
            ├─ raw and normalized output
            └─ restricted logs/evidence
```

A VPS separates long jobs from a laptop, but creates a new internet-facing asset that must be patched, monitored, paid for, and eventually destroyed.

## Cost controls

Before launch, record:

- hourly and estimated monthly compute cost;
- root-disk size;
- backup/snapshot price;
- volume price;
- included and excess transfer;
- reserved/static IP rules;
- tax and currency conversion.

Use provider budgets/alerts, resource tags, and a calendar/automatic shutdown reminder. “Powered off” commonly retains allocated storage and may remain billable.

## SSH trust model

The public key is safe to upload; the private key authenticates the holder and must not leave the trusted workstation.

Recommended local config:

```sshconfig
Host do-recon
    HostName SERVER_IP
    User researcher
    IdentityFile ~/.ssh/do-recon
    IdentitiesOnly yes
```

Then connect with:

```bash
ssh do-recon
```

Protect `~/.ssh` with mode 700 and private keys with mode 600. Use a passphrase and local agent where operationally appropriate.

The server's host key authenticates the server to the client. An unexpected changed-key warning can indicate reprovisioning, address reuse, or interception. Verify before updating `known_hosts`.

## Safe bootstrap order

1. Create droplet with key authentication.
2. Update packages.
3. Create normal sudo user.
4. Install/copy that user's authorized key.
5. Open a second terminal and prove login/sudo works.
6. Configure cloud and host firewalls.
7. Harden SSH.
8. Test again before closing the original recovery session.

This order prevents accidental lockout.

## SSH hardening concepts

Use distribution-supported configuration, commonly through a drop-in under `/etc/ssh/sshd_config.d/`. Desired controls include:

```text
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
```

Validate before reload:

```bash
sshd -t
systemctl reload ssh
```

Exact service name varies. Keep the provider console/recovery method available. Changing SSH to a nonstandard port reduces noise, not the need for strong authentication.

## Firewall layers

A DigitalOcean cloud firewall filters traffic before the droplet. UFW/nftables filters on the host. Defense in depth is useful, but mismatched rules complicate troubleshooting.

Typical worker posture:

- inbound SSH from one trusted address;
- established/related return traffic;
- outbound DNS, package repositories, and authorized target traffic;
- no public tool dashboards/listeners.

If a callback listener is explicitly required for an authorized test, scope it by source, time, authentication, and port; remove it immediately afterward.

## Tool installation risks

Security tools often suggest commands such as:

```bash
curl URL | sudo bash
```

This grants remote content root execution. Prefer signed packages, official releases, reviewed installers, checksums, or source builds under a non-root account. Document:

```text
tool name
source URL
version/commit
checksum
install date
configuration
```

Use Python virtual environments and pinned dependencies; use versioned Go installs. Do not let one tool's dependencies alter the base system unpredictably.

## Scope enforcement

Cloud speed makes accidental out-of-scope traffic more damaging. Build guardrails:

```bash
# candidate discoveries
raw/all-hostnames.txt

# reviewed authorization boundary
scope/in-scope.txt

# only this file enters active tools
```

Validate each discovered hostname against program rules and ownership before adding it. IP-based scanning is especially risky on shared cloud/CDN hosting; an in-scope hostname does not authorize neighboring IP tenants.

## Rate control

Control three different dimensions:

- **rate:** requests per second;
- **concurrency:** simultaneous workers/connections;
- **total volume:** overall requests/data.

Start low, observe target behavior and program limits, and back off on errors or `429`. A remote machine should never be used to evade controls or rotate identity.

## Reliable jobs

`tmux` preserves a terminal session, but not across a server reboot unless work is restarted. For repeatable scheduled jobs, consider a constrained systemd user service/timer with explicit paths, environment, resource limits, and logging.

Capture command metadata:

```bash
printf '%s\t%s\n' "$(date -Is)" "command description" >> ~/recon/logs/run.log
```

Avoid writing tokens/passwords into logs. Use restrictive `umask 077` for sensitive output.

## Data protection

Recon output may contain:

- tokens and API keys;
- internal hostnames;
- user information;
- screenshots;
- request cookies;
- vulnerability evidence.

Restrict permissions, collect the minimum, encrypt transfers, redact reports, and follow program retention rules. Do not put evidence in public object storage or repositories.

Secure transfer example:

```bash
scp -i ~/.ssh/do-recon researcher@SERVER_IP:~/recon/results/report.json ./
```

Verify downloaded files before deleting the server.

## Monitoring

Useful checks:

```bash
uptime
free -h
df -h
ss -lntup
journalctl -p warning
last
```

Watch for unexpected listening ports, failed authentication bursts, disk growth, and unknown processes. Cloud servers receive continuous unsolicited traffic.

## Incident response

If a private key/API token is exposed:

1. revoke it—not merely delete the local file;
2. rotate affected credentials;
3. inspect account audit logs and server access;
4. snapshot only if needed for investigation;
5. rebuild from a trusted image if integrity is uncertain;
6. notify the provider/program where required.

If a droplet is compromised, patching one visible symptom is not proof the host is clean.

## Teardown checklist

- [ ] Stop and inventory jobs.
- [ ] Export required sanitized results.
- [ ] Verify local copies.
- [ ] Remove sensitive remote data.
- [ ] Destroy droplet.
- [ ] Delete volumes/snapshots/backups.
- [ ] Release reserved IP/load balancer/firewall if unused.
- [ ] Revoke project tokens and obsolete SSH keys.
- [ ] Check billing page for zero unintended resources.
- [ ] Record teardown date in project notes.

## Review questions

1. Why does a powered-off VPS potentially remain billable?
2. Why test a normal user's SSH session before disabling root login?
3. What is the difference between user authentication and server host-key verification?
4. Why is a reviewed scope file a technical safety control?
5. Which dimensions must rate limiting control?
6. Why can scanning an IP be riskier than probing an in-scope hostname?
7. What data in recon output requires protection?
8. Which resources can survive after droplet deletion?

<!-- DONE-087 -->
