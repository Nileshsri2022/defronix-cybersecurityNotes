# Day-14 — Finding Misconfigured AWS S3 Buckets — English Translation

*Translated from: `090 - Day-14 - Finding Misconfigured AWS s3 Bucket Live Recon - Bug Bounty Free Course [Hindi].hi-orig.srt`*

---

Amazon S3 stores objects inside globally named buckets. During authorized recon, bucket names may appear in DNS, JavaScript, source maps, GitHub, image URLs, or error responses. Discovery does not authorize access: confirm that the bucket belongs to the in-scope organization and that cloud testing is permitted.

Separate four controls: bucket existence, object read access, object listing, and write/delete access. A public website may intentionally permit reads while correctly denying listing and writes. A `403 AccessDenied` proves neither vulnerability nor ownership; `404 NoSuchBucket`, region redirects, and website-endpoint errors each mean something different.

Use a normal browser or a minimal HEAD/GET request against a known public object. AWS CLI commands should use `--no-sign-request` only for intentionally anonymous checks. Do not recursively copy a bucket or download personal data. Listing, if allowed, should be stopped after minimal evidence. Never test upload/delete by modifying a real bucket unless the program expressly provides a safe path and authorizes it.

Potential impact includes exposed backups, logs, source archives, credentials, customer files, or unauthorized writes enabling content replacement. Severity depends on actual data and permissions, not the words “public bucket.” Redact object names and content in the report.

Remediation includes S3 Block Public Access, least-privilege bucket/IAM policies, disabled ACL usage where possible, restricted website content, encryption, access logging, inventory, and continuous policy monitoring. Rotate every secret found because making the object private does not invalidate copied credentials.

<!-- DONE-090 -->
