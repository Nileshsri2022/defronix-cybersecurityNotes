# Bug Bounty Day 9 — AWS reconnaissance workstation — Explained

## Lesson reconstruction

Day 9 demonstrates creating an AWS virtual machine to run authorized reconnaissance with more stable compute and bandwidth than a local laptop. Cloud infrastructure improves convenience; it does not expand scope or remove program rate limits.

Create an AWS account securely, enable MFA, configure billing alerts/budgets, and understand that instances, storage, static IPs, and traffic may incur charges. Launch an EC2 instance in a suitable region using a supported Linux image. Choose an instance size based on the workload rather than assuming the largest or free-tier label is always appropriate.

Create or select an SSH key pair and protect the private key locally with restrictive permissions. Configure the security group with least privilege: allow SSH only from your current trusted IP where possible, and do not expose databases or arbitrary tool ports. Connect with the image's documented username and public address.

Update packages, install only required recon tools, and create a structured workspace. Use a non-root user for normal work, keep secrets out of shell history and repositories, and store program scope locally. Long jobs should run under `tmux` or a system service so a dropped SSH session does not terminate them. Limit concurrency and log commands/results.

Cloud IP addresses are externally visible and may be blocked or reported. Confirm that the bug-bounty program allows cloud-hosted automation. Do not rotate addresses to evade defenses. AWS acceptable-use terms and local law still apply.

Secure operations include patching, disabling password SSH, using key authentication, restricting IAM permissions, encrypting storage when needed, monitoring disk usage, and stopping or terminating resources after work. Download required results securely, remove sensitive evidence, release unused elastic IPs, and verify that snapshots/volumes are not left billing indefinitely.

The intended outcome is a reproducible, controlled recon worker—not a high-speed indiscriminate scanner.

## Engineering and safety notes

Before launch, estimate cost and define an automatic shutdown plan. Tag resources by project, never place AWS credentials directly on the instance when an IAM role with least privilege suffices, and rotate any exposed key immediately. A remote worker should consume a validated in-scope list and enforce request limits centrally.

## Verification checklist

- Reproduce the workflow only in an isolated lab or explicitly authorized scope.
- Validate inputs, quote paths and variables, and test failure behavior.
- Preserve source, date, command, and minimal evidence for every observation.
- Distinguish a lead from a verified finding; do not overstate impact.
- Remove secrets and personal data from notes before sharing.

## Review questions

1. What prerequisite or authorization boundary controls this workflow?
2. Which output justifies the next action, and which output is only a lead?
3. How can false positives or stale data appear?
4. What is the safest failure/cleanup behavior?
5. How would a defender prevent or detect the weakness discussed?

<!-- DONE-085 -->
