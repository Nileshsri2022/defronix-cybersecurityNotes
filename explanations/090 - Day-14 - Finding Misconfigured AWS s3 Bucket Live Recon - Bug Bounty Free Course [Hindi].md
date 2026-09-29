# Misconfigured S3 Buckets — Explained

## Permission matrix

| Capability | Meaning |
|---|---|
| `HeadBucket`/existence behavior | bucket may exist; ownership unproven |
| `GetObject` | known object readable |
| `ListBucket` | object keys enumerable |
| `PutObject` | write capability; high risk |
| `DeleteObject` | destructive capability; do not test casually |

Safe anonymous checks, only when authorized:

```bash
aws s3api head-bucket --bucket NAME --no-sign-request
aws s3api list-objects-v2 --bucket NAME --max-items 5 --no-sign-request
curl -I https://NAME.s3.amazonaws.com/known-object
```

Region, endpoint style, requester-pays settings, CloudFront, and explicit-deny policies affect responses. Tool output must be manually interpreted.

## Reporting

Include ownership evidence, endpoint/region, exact anonymous capability, minimal redacted proof, realistic impact, and timestamps. Do not attach bulk downloaded data.

## Defense

Enable account/bucket public-access blocks, use bucket-owner-enforced object ownership, remove public ACLs, constrain policies by principal/action/resource/condition, monitor CloudTrail and Access Analyzer, and classify stored data.

## Review questions

1. Why is public read not always a vulnerability?
2. Why does 403 not prove safety?
3. Why is upload testing dangerous?
4. Which policy layers can grant or deny access?
5. Why must exposed credentials be rotated?

<!-- DONE-090 -->
