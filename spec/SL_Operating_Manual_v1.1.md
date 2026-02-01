# ΣΛ OPERATING MANUAL

## Version 1.1

### Constraint-Complete Communication & Procedural Decomposition System

---

## 0. Purpose

ΣΛ is a **constraint language**, not a procedural or narrative language.

It exists to communicate:

- what must be true,
- what must never happen,
- what is undecidable,
- where execution must halt,

between agents that prioritize **correctness, safety, and honesty about limits** over persuasion or speed.

This manual defines **how ΣΛ is spoken, interpreted, and operationalized**.

---

## 1. Core Assumptions

ΣΛ assumes:

- shared logical competence
- explicit declaration of values when relevant
- zero tolerance for implicit inference
- preference for halting over guessing

ΣΛ does **not** assume:

- shared goals
- shared meaning
- narrative context
- human intuition

---

## 2. Ontological Primitives

```
Ω   : system under consideration
ℒ   : invariant rule-set
𝔈   : state evolution
𝕀   : information
𝕊   : structure
𝒳   : experience (irreducible)
𝒪   : observer / agent
𝕍   : value function
```

Axiomatically:

```
ℒ ⊢ governs(Ω)
𝔈 preserves(𝕀)
𝒳 ⟂ ℒ
𝕍 ⟂ ℒ
```

---

## 3. Core Operators

```
⊢   necessarily follows
⊬   undecidable
⊥   contradiction
¬   negation
⇒   implication
≡   equivalence
≈   structural equivalence
```

ΣΛ statements mean **only** what they constrain.

---

## 4. What ΣΛ Can and Cannot Express

ΣΛ CAN express:

- necessity
- impossibility
- preconditions
- postconditions
- invariants
- halting conditions
- rollback guarantees

ΣΛ CANNOT derive:

- values
- meaning
- experience
- intent

These must be declared explicitly or indexed.

---

## 5. Canonical Statement Forms

1. Prohibition

```
X ⊢ ⊥
```

2. Requirement

```
A ∧ ℒ ⇒ B
```

3. Undecidability

```
ℒ ⊬ X ∨ ¬X
```

4. Termination

```
condition ⇒ halt(actions)
```

---

## 6. Clause Identifier Requirement

All ΣΛ policies MUST include **stable clause identifiers**.

Example:

```
[CL-001] ℒ ⊢ ¬sync(database_local → database_prod)
```

Clause IDs are binding across:

- policy
- execution
- trace

---

## 6.1 Policy Artifact Format

The body of a ΣΛ policy artifact MUST be **pure logic**.

A conforming policy artifact:

- Contains ONLY clause statements (one per line)
- Each line starts with a bracketed clause ID: `[ID-XXX]`
- Uses ONLY operators from §3 (⊢ ⊥ ¬ ⇒ ≡ ∧ ∨)
- Contains NO inline comments
- Contains NO section headers or decorators
- Contains NO prose, narrative, or explanation within the policy body

Explanations, context, and documentation MUST be provided **outside** the policy body (e.g., in a separate Explanation section or accompanying documentation).

Example — CONFORMING:

```
[CL-001] delete(audit_logs) ⊢ ⊥
[CL-002] deploy(production) ⇒ exists(backup)
```

Example — NON-CONFORMING:

```
# === Section 1 — Audit Protection ===
[CL-001] delete(audit_logs) ⊢ ⊥  # Never delete logs
```

---

## 6.2 Definition Bindings

Policies MAY include **definition statements** to bind ambiguous terms to explicit meanings.

Format:

```
[DEF-XXX] term ≡ expansion
```

Rules:

- Definition IDs use the prefix `DEF-` followed by a sequential number
- Use `≡` (equivalence) to bind a term to its meaning
- Definitions MUST precede any clause that references the defined term
- Definitions are binding for the scope of the policy artifact
- Expansions may use `∨` (disjunction) to enumerate alternatives

Example:

```
[DEF-001] destroy(X) ≡ remove(X) ∨ drop(X) ∨ truncate(X) ∨ corrupt(X)
[DEF-002] critical_db ≡ production_zodb ∨ production_catalog

[CL-001] destroy(critical_db) ⊢ ⊥
```

Definition bindings satisfy §1 (zero tolerance for implicit inference) by making all term meanings explicit and traceable.

---

## 7. Procedural Document Ingestion (Addendum – Normative)

This section defines how ΣΛ-speaking agents MUST handle real-world procedural documents.

---

## 7.1 Mandatory Classification

Upon receiving a human-authored document **D**, every statement MUST be classified as exactly one of:

1. Constraint (ΣΛ-eligible)
2. Procedure (execution-only)
3. Parameterization (config-only)
4. Narrative / explanation (non-binding)

Classification MUST occur before execution or translation.

---

## 7.2 Mandatory Output Architecture

From any procedural document, agents MUST produce **exactly three artifacts**.

---

## 8. Artifact A — ΣΛ Policy (Canonical)

**Purpose:** Define allowed, required, forbidden, and halting behavior.

Rules:

- Pure ΣΛ
- No commands
- No environment assumptions
- Stable clause IDs required

Path:

```
policy/<domain>/<artifact>.ΣΛ.md
```

Policy overrides all other layers.

---

## 9. Artifact B — Execution Layer (Imperative)

**Purpose:** Perform actions while enforcing ΣΛ policy.

Rules:

- Tool- and environment-specific
- Must reference ΣΛ clause IDs
- Must halt on ⊢ ⊥
- Must not infer missing intent

Path:

```
ops/<domain>/<artifact>/
```

---

## 10. Artifact C — Trace / Attestation Layer

**Purpose:** Prove ΣΛ compliance.

Rules:

- Append-only
- Machine-readable
- Clause-ID indexed

Path:

```
trace/<domain>/<artifact>/<timestamp>/
```

---

## 11. Translation Algorithm (Mandatory)

```
Input: procedural document D

1. Classify statements
2. Extract constraints → ΣΛ policy
3. Assign clause IDs
4. Extract parameters → config
5. Translate procedures → scripts
6. Bind scripts to clause IDs
7. Define rollback paths
8. Define trace schema
9. Reject execution if ambiguity exists
```

---

## 12. Prohibited Agent Behaviors

Agents MUST NOT:

- embed commands in ΣΛ
- infer safety from narrative
- optimize past constraints
- execute without policy
- invent missing steps

Violation constitutes **semantic corruption**.

---

## 13. Termination Semantics

Execution is complete iff:

```
preconditions_satisfied
∧ postconditions_verified
∧ observability_recorded
∧ rollback_paths_intact
```

Otherwise, execution halts and state is marked unresolved.

---

## 14. Orientation Statement

ΣΛ exists to prevent:

- accidental dishonesty
- silent scope creep
- unsafe automation
- value smuggling

It prioritizes **stopping correctly** over continuing incorrectly.

---

## 15. Versioning

- v1.0 — Core ΣΛ language
- v1.1 — Procedural ingestion & execution architecture (this document)

---

# END ΣΛ OPERATING MANUAL
