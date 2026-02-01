# Manual Validation Standard (v0.1.0)

Until the automated validator covers all cases, use this checklist to validate AI-generated policies.

---

## Syntactic Validation

### 1. Clause Format

Does every constraint line start with a bracketed ID?

✅ `[CL-001] delete(logs) ⊢ ⊥`  
❌ `delete(logs) ⊢ ⊥` (missing ID)

### 2. Operator Check

Are all operators strictly from the allowable set?

| Operator | Meaning                          |
| -------- | -------------------------------- |
| `⊢`      | Necessarily follows / entailment |
| `⊥`      | Contradiction / forces halt      |
| `¬`      | Negation                         |
| `∧`      | Conjunction (and)                |
| `∨`      | Disjunction (or)                 |
| `⇒`      | Implication                      |
| `⇔`      | Biconditional / equivalence      |

❌ Reject policies using: `->`, `!=`, `NOT`, `AND`, `OR`, `==`

### 3. No Prose in Body

Are there any English sentences outside of comments or headers?

The policy body must be pure logic. Explanations belong in separate documentation.

---

## Semantic Validation

### 1. Halting Semantics

Does the policy define when to stop?

Look for patterns like:

- `condition ⇒ halt(action)`
- `violation ⊢ ⊥`

Without explicit halt conditions, agents may loop indefinitely.

### 2. Prohibition Pattern

Are safety boundaries using the contradiction pattern?

✅ `[CL-001] delete(production_db) ⊢ ⊥` — Forces halt  
⚠️ `[CL-001] ¬delete(production_db)` — States preference, doesn't force halt

### 3. Completeness Check

Are all stated requirements captured?

Cross-reference the original human intent against the clauses. Every "must" and "never" should map to a clause.

---

## Automated Validation

Use `tools/sl_validate.py` to check trace logs against policies:

```bash
python tools/sl_validate.py --policy policy.ΣΛ.md --trace trace.log
```

This validates:

- All clause IDs in the policy are correctly formatted
- Trace entries reference valid clause IDs
- No FAIL results exist in the trace
