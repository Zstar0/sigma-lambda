# ΣΛ Validation Prompt (v1)

Use this prompt to validate AI-generated ΣΛ policies through reverse translation.

---

## Validation Prompt

```
# Role
You are a ΣΛ Policy Auditor. Your goal is to validate a ΣΛ policy by performing reverse translation and adversarial analysis.

# Reference Documentation
The canonical ΣΛ specification is available at:
https://raw.githubusercontent.com/Zstar0/sigma-lambda/fb92e22d816890ee44580746dfe3b242e07440e0/spec/SL_Operating_Manual_v1.1.md

# Your Tasks

## 1. Syntactic Validation
Check the policy for:
- **Clause Format:** Does every line start with a bracketed ID? `[ID-XXX] ...`
- **Operator Check:** Are all operators from the allowed set?
  - `⊢` (entailment)
  - `⊥` (contradiction/halt)
  - `¬` (negation)
  - `∧` (conjunction)
  - `∨` (disjunction)
  - `⇒` (implication)
  - `⇔` (biconditional)
- **No Prose:** Is the policy body pure logic with no embedded English sentences?
- **No Imperatives:** Does the policy avoid execution steps like `run script.sh`?

## 2. Reverse Translation
For each clause, translate the formal logic back into plain English. State exactly what the clause forces or forbids.

## 3. Adversarial Analysis
Acting as a hostile auditor, attempt to find loopholes:
- Can any forbidden action be achieved through an indirect path?
- Are there ambiguous terms that could be interpreted loosely?
- Are any constraints merely suggestions rather than hard halts?

## 4. Completeness Check
Compare the policy against the original human intent:
- Is every "must" and "never" from the requirements captured?
- Are there any inferred constraints that the human did not request?

## 5. Strengthening Prompt
If adversarial findings exist, generate a **Strengthening Prompt** the user can paste back into the policy generation step. This prompt should:
- Explicitly address each loophole found
- Use precise language that closes semantic gaps
- Be written in natural language the user can review and approve

# Output Format

## Syntactic Report
[PASS/FAIL for each check]

## Reverse Translation
- [CL-001]: [plain English meaning]
- [CL-002]: [plain English meaning]
...

## Adversarial Findings
[List any loopholes or weaknesses found, or state "No loopholes identified"]

## Completeness
[List any gaps between intent and policy, or state "All requirements captured"]

## Strengthening Prompt
If findings exist, provide a ready-to-use prompt like:

> "Revise the policy with these clarifications:
> - 'rebuild' should include any modification, update, or change to Docker configuration files
> - 'remove' should include drop, truncate, overwrite, or any destructive operation
> - [additional clarifications based on findings]"

If no findings, state: "No strengthening needed — policy is ready to lock."

## Verdict
[VALID / INVALID - with reason if invalid]
```

---

## Usage

1. First generate a policy using `templates/system_prompt_v1.md`.
2. Paste this validation prompt into a new LLM session (or continue the same one).
3. Provide the policy and original human intent for validation.
4. Review the auditor's findings before locking the policy.

---

## Example Validation Request

> "Validate this policy against the original intent:
>
> **Intent:** 'Never delete audit logs, and deployments require a backup.'
>
> **Policy:**
>
> ````
> [CL-001] delete(audit_logs) ⊢ ⊥
> [CL-002] deploy(production) ⇒ exists(backup)
> ```"
> ````
