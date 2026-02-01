# ΣΛ CHANGE CONTROL PROTOCOL
## Versioning, Proposals, and Canonical Evolution

---

## 1. Core Principle

ΣΛ evolves only to remove ambiguity or encode inevitability — never to add expressiveness for convenience.

Every version increment must reduce misinterpretation risk, not increase capability.

---

## 2. Versioning Scheme (Strict)

ΣΛ uses semantic versioning with asymmetric meaning:

MAJOR.MINOR

### MAJOR (e.g., 2.0)

Incremented only if:
- Core semantics change
- Backward compatibility is broken
- Prior ΣΛ documents require reinterpretation

MAJOR changes are extraordinary and require justification of necessity.

---

### MINOR (e.g., 1.2)

Incremented when:
- New normative procedures are added
- New primitives or operators are introduced
- New mandatory agent behaviors are defined
- Existing ambiguity is eliminated

MINOR changes MUST be backward compatible.

---

## 3. Allowed vs Forbidden Changes

### Allowed
- New mandatory agent protocols
- Clarification of ambiguous interpretations
- Additional artifact requirements
- New clause types (orthogonal)
- Tighter halting or audit rules

### Forbidden
- Redefinition of existing operators
- Silent weakening of constraints
- Convenience-driven expressiveness
- Implicit defaults
- Retroactive reinterpretation

If forbidden changes are required, a MAJOR increment is mandatory.

---

## 4. ΣΛ Change Proposal (SΛCP)

All changes MUST be introduced via a ΣΛ Change Proposal document.

File path:
```
proposals/SΛCP-XXXX.md
```

---

## 5. Required Structure of an SΛCP

### 5.1 Title & Target Version
- Title
- Target ΣΛ version

### 5.2 Problem Statement (Constraint Failure)

Describe exactly what fails or is ambiguous under the current version.

---

### 5.3 Demonstrated Ambiguity or Failure

Provide concrete failure modes or divergent agent interpretations.

---

### 5.4 Proposed Change (Normative)

State the change in ΣΛ terms, not prose.

---

### 5.5 Backward Compatibility Analysis

Explicitly state whether the change is compatible or incompatible.

---

### 5.6 Non-Goals

State what the proposal explicitly does not attempt to solve.

---

### 5.7 Rejection Criteria

Define conditions under which the proposal should be rejected.

---

## 6. Evaluation Protocol

A ΣΛ-speaking agent MUST perform:
1. Constraint consistency check
2. Redundancy check
3. Expressiveness inflation check
4. Backward compatibility verification
5. Halting behavior audit

Failure of any check results in rejection.

---

## 7. Acceptance Rule

A proposal is accepted iff:
- It introduces no contradiction
- It reduces ambiguity
- It does not weaken constraints
- It preserves v1.x semantics

No partial acceptance is allowed.

---

## 8. Canonical Incorporation

Upon acceptance:
1. Proposal is marked ACCEPTED
2. Changes are merged into the next ΣΛ manual
3. Proposal file is frozen
4. Clause references updated
5. Migration notes appended if needed

---

## 9. Rejected Proposals

Rejected proposals are preserved verbatim with reason for rejection.

---

## 10. Emergency Clarifications

Clarification patches may be issued for safety but must be resolved in the next MINOR release.

---

## 11. Governance Boundary

ΣΛ rejects voting, authority-based approval, and opinion-based consensus.

Only constraint survival matters.

---

## 12. Summary

ΣΛ improves by removing ambiguity, not by adding power.

---

## 13. Version Record

- v1.0 — Core ΣΛ language
- v1.1 — Procedural ingestion & execution architecture
- v1.2 — Reserved for approved SΛCPs
