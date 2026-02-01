# ΣΛ (Sigma–Lambda)

ΣΛ is a **constraint protocol** for safe, auditable AI systems. It preserves human intent under automation by separating:

- **Policy** (what must be true / what must never happen / when to stop)
- **Procedure** (how work is executed: agents, scripts, CI/CD)
- **Evidence** (what actually happened: verifiable traces)

ΣΛ is **not** a programming language and does **not** execute workflows. It is the governance layer that makes systems stoppable, auditable, and defensible.

## Why ΣΛ

As AI agents gain autonomy and persistence, failures increasingly come from:

- inferred intent
- silent scope expansion
- “helpful” optimization past safety boundaries
- lack of explicit halting semantics

ΣΛ makes limits explicit and enforceable.

## Repository structure

- `spec/` — Canonical specification and governance
- `proposals/` — ΣΛ Change Proposals (SΛCP)
- `examples/` — Minimal examples (policy / ops / trace)
- `tools/` — Reference validator (`sl_validate.py`)
- `templates/` — System prompts for AI-assisted authoring
- `guides/` — Authoring and validation workflows
- `docs/` — Public-facing materials (whitepaper, one-pager)

## Start here

1. Read the **Operating Manual**: `spec/SL_Operating_Manual_v1.1.md`
2. **Write your first policy**: `guides/authoring_workflow.md`
3. **Use the system prompt**: `templates/system_prompt_v1.md`
4. See a worked example: `examples/agent/`

## License

Apache-2.0 (see `LICENSE`)
