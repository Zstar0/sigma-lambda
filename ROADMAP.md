# ΣΛ Roadmap

This document outlines the planned evolution of ΣΛ from specification to integrated tooling.

---

## v0.1.0 ✅ (Released)

**Foundation**

- Core specification (Operating Manual, Change Control)
- Governance framework
- Deployment example (policy / ops / trace)

---

## v0.2.0 ✅ (Current)

**Authoring & Validation**

- Reference validator (`sl_validate.py`)
- Authoring workflow guide
- LLM prompts for policy generation and validation
- AI agent autonomy example

---

## v0.3.0 (Planned)

**Linting & CI Integration**

- `sl_lint.py` — Syntax validation for `.ΣΛ.md` files
- Pre-commit hooks
- GitHub Actions workflow template
- VS Code extension (syntax highlighting)

---

## v0.4.0 (Planned)

**IDE Integration**

- Slash commands for AI coding assistants:
  - `SL:CreatePolicy` — Generate policy from intent
  - `SL:ValidatePolicy` — Validate via reverse translation
  - `SL:Implement` — Scaffold ops layer with clause hooks

---

## v1.0.0 (Vision)

**Runtime Enforcement**

- Agent harness with built-in policy checking
- Automatic trace recording
- Real-time compliance monitoring
- Integration with LangChain, AutoGPT, CrewAI

---

## Contributing

See `GOVERNANCE.md` for how changes are proposed via SΛCP.
