#!/usr/bin/env python3
"""
ΣΛ Reference Validator
Checks trace logs against policy files for compliance.

Usage:
    python sl_validate.py --policy policy.ΣΛ.md --trace trace.log
"""

import argparse
import re
import sys
from pathlib import Path


def extract_clause_ids(policy_path: Path) -> set[str]:
    """Extract all clause IDs from a ΣΛ policy file.
    
    Clause IDs are expected in format: [ID] statement
    Examples: [EX-001], [CL-042], [DEPLOY-003]
    """
    content = policy_path.read_text(encoding='utf-8')
    # Match clause IDs in brackets at start of a line or statement
    pattern = r'\[([A-Z]+-\d+)\]'
    return set(re.findall(pattern, content))


def extract_trace_checks(trace_path: Path) -> dict[str, str]:
    """Extract CHECK results from a trace log.
    
    Expected format: CHECK <ID>: PASS|FAIL
    Returns dict of {clause_id: result}
    """
    content = trace_path.read_text(encoding='utf-8')
    pattern = r'CHECK\s+([A-Z]+-\d+):\s*(PASS|FAIL)'
    matches = re.findall(pattern, content, re.IGNORECASE)
    return {clause_id: result.upper() for clause_id, result in matches}


def validate(policy_path: Path, trace_path: Path) -> tuple[bool, list[str]]:
    """Validate a trace against a policy.
    
    Returns (is_compliant, list of messages)
    """
    messages = []
    is_compliant = True
    
    # Extract data
    policy_clauses = extract_clause_ids(policy_path)
    trace_checks = extract_trace_checks(trace_path)
    
    if not policy_clauses:
        messages.append(f"WARNING: No clause IDs found in {policy_path}")
        return False, messages
    
    messages.append(f"Policy clauses found: {sorted(policy_clauses)}")
    messages.append(f"Trace checks found: {list(trace_checks.keys())}")
    messages.append("")
    
    # Check for violations
    for clause_id, result in trace_checks.items():
        if result == "FAIL":
            messages.append(f"❌ VIOLATION at clause {clause_id}")
            is_compliant = False
        else:
            messages.append(f"✓ {clause_id}: PASS")
    
    # Check for unchecked clauses
    checked_ids = set(trace_checks.keys())
    unchecked = policy_clauses - checked_ids
    if unchecked:
        messages.append("")
        messages.append(f"⚠️  Unchecked clauses: {sorted(unchecked)}")
    
    # Check for unknown clauses in trace
    unknown = checked_ids - policy_clauses
    if unknown:
        messages.append("")
        messages.append(f"⚠️  Unknown clauses in trace (not in policy): {sorted(unknown)}")
    
    return is_compliant, messages


def main():
    parser = argparse.ArgumentParser(
        description='ΣΛ Reference Validator - Check trace logs against policy files'
    )
    parser.add_argument(
        '--policy', '-p',
        type=Path,
        required=True,
        help='Path to ΣΛ policy file (.ΣΛ.md)'
    )
    parser.add_argument(
        '--trace', '-t',
        type=Path,
        required=True,
        help='Path to trace log file'
    )
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Only output final result'
    )
    
    args = parser.parse_args()
    
    # Validate inputs
    if not args.policy.exists():
        print(f"ERROR: Policy file not found: {args.policy}", file=sys.stderr)
        sys.exit(2)
    
    if not args.trace.exists():
        print(f"ERROR: Trace file not found: {args.trace}", file=sys.stderr)
        sys.exit(2)
    
    # Run validation
    is_compliant, messages = validate(args.policy, args.trace)
    
    # Output
    if not args.quiet:
        print("=" * 50)
        print("ΣΛ VALIDATOR")
        print("=" * 50)
        print(f"Policy: {args.policy}")
        print(f"Trace:  {args.trace}")
        print("-" * 50)
        for msg in messages:
            print(msg)
        print("-" * 50)
    
    if is_compliant:
        print("RESULT: ✅ COMPLIANT")
        sys.exit(0)
    else:
        print("RESULT: ❌ VIOLATION")
        sys.exit(1)


if __name__ == '__main__':
    main()
