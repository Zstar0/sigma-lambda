# Example Deployment Policy (ΣΛ)
## Minimal demonstrator (generic)

[EX-001] sync(local_db → prod_db) ⊢ ⊥
[EX-010] deploy_allowed ⇔ backup_exists ∧ tests_passed
[EX-020] ¬deploy_allowed ⊢ halt(deploy)
[EX-030] ¬post_deploy_valid ⊢ initiate(rollback)
