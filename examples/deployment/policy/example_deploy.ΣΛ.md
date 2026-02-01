# Example Deployment Policy (ΣΛ)

## Human Scenario

> "I need to deploy our app safely. Never sync my local database to production — that's caused outages before. Only deploy if we have a backup and tests pass. If something breaks after deploy, automatically roll back."

---

## Policy

[EX-001] sync(local_db → prod_db) ⊢ ⊥
[EX-010] deploy_allowed ⇔ backup_exists ∧ tests_passed
[EX-020] ¬deploy_allowed ⊢ halt(deploy)
[EX-030] ¬post_deploy_valid ⊢ initiate(rollback)

---

## Explanation

- **[EX-001]**: Forces halt if any action syncs local database to production.
- **[EX-010]**: Deployment is allowed only when both backup exists AND tests passed.
- **[EX-020]**: If deployment is not allowed, halt the deploy process.
- **[EX-030]**: If post-deploy validation fails, initiate rollback.
