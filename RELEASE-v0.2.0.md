# ΣΛ Release v0.2.0

This release adds **tooling and authoring support** to make ΣΛ practical.

## What's New

### Reference Validator

- `tools/sl_validate.py` — CLI that checks trace logs against policy files
- Exits 0 for COMPLIANT, 1 for VIOLATION
- Can be integrated into CI/CD pipelines

### Authoring Guides

- `guides/authoring_workflow.md` — 3-phase workflow: Intent → Validation → Lock
- `guides/validation_standard.md` — Manual checklist for policy validation

### LLM Templates

- `templates/system_prompt_v1.md` — Turn any LLM into a ΣΛ policy architect
- `templates/validation_prompt_v1.md` — Validate policies via reverse translation

### AI Agent Example

- `examples/agent/` — Complete example showing agent autonomy constraints
- Demonstrates policy, ops layer, and trace files
- Includes both passing and failing trace scenarios

### Enhanced Examples

- Human scenario sections added to all policy files
- Shows the full Intent → Policy → Explanation chain

## Stability

All changes are backward compatible with v0.1.0.

## Status

This release is intended for:

- Developers wanting to try ΣΛ in their projects
- Teams exploring AI governance patterns
- Contributors interested in extending the tooling
