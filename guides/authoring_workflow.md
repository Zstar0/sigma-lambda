# Authoring ΣΛ Policies with AI

ΣΛ is designed to be **written by AI** but **verified by humans**.

Because ΣΛ uses formal logic, it eliminates the ambiguity of natural language. This guide defines the standard workflow for generating safe policies.

---

## The Chain of Trust

```
Human Intent → AI Translation → Human Sign-off → Locked Artifact
```

The AI is the **draftsman**. The human is the **signatory**.

---

## Phase 1: Intent Capture (The Draft)

Prompt your LLM using the system prompt from `templates/system_prompt_v1.md`.

Focus on two things:

- **Bad Outcomes**: What should never happen?
- **Hard Requirements**: What must be true before action?

### Example Prompt

> "I am building a refund agent. It is allowed to issue refunds under $50 automatically. Refunds over $50 require human approval. It must never issue a refund to an internal employee account."

---

## Phase 2: Reverse Translation (The Validation)

Before saving the policy, you **must** validate that the AI correctly captured your intent.

Do not just read the math symbols. **Ask the AI to attack its own policy.**

### Validation Prompt

> "Acting as a hostile auditor, interpret the ΣΛ policy you just wrote.
>
> 1. Are there any loopholes where I could issue a $100 refund without approval?
> 2. Does this strictly forbid employee refunds, or just discourage them?
> 3. Translate [CL-003] back into plain English."

If the AI's "attack" reveals gaps, iterate on the policy.

---

## Phase 3: The Lock-In

Once the "Reverse Translation" matches your original intent:

1. Save the file as `Artifact A` (e.g., `policy/refund_agent.ΣΛ.md`).
2. Commit it to version control.
3. **Do not** allow the agent to modify this file at runtime.
4. **Do not** treat the AI's explanation as binding. Only the formal syntax is binding.

---

## Common Pitfalls

### Hallucinated Operators

If the AI uses symbols not listed in the specification (like `->`, `!=`, or `NOT`), **reject the policy**.

Valid operators: `⊢`, `⊥`, `¬`, `∧`, `∨`, `⇒`, `⇔`

### Embedded Instructions

If the policy contains steps like `run backup_script.sh`, it is **invalid**.

ΣΛ defines _state constraints_, not _procedure_.

### Missing Halt Conditions

Every policy should define when to stop. Without explicit halt semantics, the agent may loop indefinitely.

---

## Summary

| Phase    | Actor      | Output                        |
| -------- | ---------- | ----------------------------- |
| Intent   | Human      | Natural language requirements |
| Draft    | AI         | Formal ΣΛ policy              |
| Validate | Human + AI | Reverse translation check     |
| Lock     | Human      | Signed, versioned artifact    |
