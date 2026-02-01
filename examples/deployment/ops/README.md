# Example Ops Layer (Conceptual)

This directory contains the **execution layer** for a deployment workflow.  
Scripts here perform actions while enforcing constraints from `../policy/example_deploy.ΣΛ.md`.

---

## Expected Artifacts (Conceptual)

| File          | Purpose                                    |
| ------------- | ------------------------------------------ |
| `env.prod.sh` | Environment parameters (non-binding)       |
| `deploy.sh`   | Performs the deployment action             |
| `verify.sh`   | Post-deploy validation checks              |
| `rollback.sh` | Rollback path if `post_deploy_valid` fails |

---

## Contract with Policy Layer

All scripts **MUST**:

1.  Reference ΣΛ clause IDs in output.
2.  Emit `CHECK <ID>: PASS` or `CHECK <ID>: FAIL` to the trace.
3.  Halt immediately on `FAIL`.
4.  Never infer missing intent.

---

## Pseudo-Script: `deploy.sh` (Illustrative)

```bash
#!/bin/bash
# Ops Layer: deploy.sh
# Bound to: ../policy/example_deploy.ΣΛ.md

TRACE_LOG="../trace/$(date +%s).log"

# --- CHECK EX-001: Prohibition on local→prod sync ---
if [ "$SYNC_LOCAL_TO_PROD" = "true" ]; then
  echo "CHECK EX-001: FAIL (sync local→prod is forbidden)" >> "$TRACE_LOG"
  exit 1
fi
echo "CHECK EX-001: PASS" >> "$TRACE_LOG"

# --- CHECK EX-010: Preconditions ---
if [ ! -f "$BACKUP_PATH" ] || [ "$TESTS_PASSED" != "true" ]; then
  echo "CHECK EX-010: FAIL (backup or tests missing)" >> "$TRACE_LOG"
  exit 1
fi
echo "CHECK EX-010: PASS" >> "$TRACE_LOG"

# --- EXECUTE DEPLOY ---
echo "RUN deploy: STARTING" >> "$TRACE_LOG"
# ... actual deploy commands here ...
echo "RUN deploy: OK" >> "$TRACE_LOG"

# --- CHECK EX-030: Post-deploy validation ---
./verify.sh
if [ $? -ne 0 ]; then
  echo "CHECK post_deploy_valid: FAIL" >> "$TRACE_LOG"
  echo "RUN rollback: INITIATING (per EX-030)" >> "$TRACE_LOG"
  ./rollback.sh
  exit 1
fi
echo "CHECK post_deploy_valid: PASS" >> "$TRACE_LOG"

echo "TERMINATE: deploy_complete" >> "$TRACE_LOG"
```

---

## Key Observations

- **No inference**: The script checks explicit conditions, not assumed states.
- **Clause binding**: Every `CHECK` line references a policy clause ID.
- **Halting**: Any `FAIL` results in immediate termination.
- **Trace generation**: All output is append-only to the trace log.

This is **illustrative**, not executable. Real implementations would vary by environment and tooling.
