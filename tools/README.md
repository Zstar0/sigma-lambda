# ΣΛ Tools

This directory contains reference implementations for ΣΛ validation.

## sl_validate.py

A reference validator that checks trace logs against policy files.

### Usage

```bash
python sl_validate.py --policy <policy.ΣΛ.md> --trace <trace.log>
```

### Example

```bash
python sl_validate.py \
  --policy ../examples/deployment/policy/example_deploy.ΣΛ.md \
  --trace ../examples/deployment/trace/example_trace.log
```

### Output

```
==================================================
ΣΛ VALIDATOR
==================================================
Policy: ../examples/deployment/policy/example_deploy.ΣΛ.md
Trace:  ../examples/deployment/trace/example_trace.log
--------------------------------------------------
Policy clauses found: ['EX-001', 'EX-010', 'EX-020', 'EX-030']
Trace checks found: ['EX-010', 'EX-001']

✓ EX-010: PASS
✓ EX-001: PASS

⚠️  Unchecked clauses: ['EX-020', 'EX-030']
--------------------------------------------------
RESULT: ✅ COMPLIANT
```

### Exit Codes

| Code | Meaning                                |
| ---- | -------------------------------------- |
| 0    | COMPLIANT — All checked clauses passed |
| 1    | VIOLATION — One or more clauses failed |
| 2    | ERROR — Invalid input files            |

### Flags

- `--quiet` / `-q` — Only output final result

### Integration

This tool can be used in CI/CD pipelines:

```yaml
# GitHub Actions example
- name: Validate ΣΛ Compliance
  run: |
    python tools/sl_validate.py \
      --policy policy/deploy.ΣΛ.md \
      --trace trace/latest.log
```

A non-zero exit code will fail the pipeline.
