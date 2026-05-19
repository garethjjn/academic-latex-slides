#!/usr/bin/env python3
"""run_tests.py — golden tests for the audit-write mechanism layer (P5).

Stdlib only. Proves the P5 scripts actually work (not advisory):
  1. check_links resolves every reference in the SHIPPED plugin   -> exit 0
  2. lint_style FAILS the bad fixture (personalization + fab cite) -> exit 1
  3. lint_style PASSES the good fixture                            -> exit 0
  4. verify_quote FINDS a present quote                            -> exit 0
  5. verify_quote REJECTS an absent quote                          -> exit 1

Run:  python tests/run_tests.py     (from anywhere)
Exit: 0 = all pass · 1 = a test failed
"""
import os
import subprocess
import sys

PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(PLUGIN, "scripts")
FIX = os.path.join(PLUGIN, "tests", "fixtures")
PY = sys.executable


def run(script, *args):
    r = subprocess.run(
        [PY, os.path.join(SCRIPTS, script), *args],
        capture_output=True, text=True,
        encoding="utf-8", errors="replace",  # portable on GBK-locale Windows
    )
    return r.returncode, ((r.stdout or "") + (r.stderr or ""))


def main():
    cases = []

    rc, out = run("check_links.py", PLUGIN)
    cases.append(("check_links resolves shipped plugin", rc == 0, out.strip().splitlines()[-1:]))

    rc, out = run("lint_style.py", os.path.join(FIX, "bad_draft.md"))
    bad_ok = rc == 1 and "personalization" in out and "fabricated cite" in out
    cases.append(("lint_style fails bad fixture", bad_ok, [l for l in out.splitlines() if "ERROR" in l][:3]))

    rc, out = run("lint_style.py", os.path.join(FIX, "good_draft.md"))
    cases.append(("lint_style passes good fixture", rc == 0, out.strip().splitlines()[-1:]))

    corpus = os.path.join(FIX, "corpus_sample.txt")
    rc, out = run("verify_quote.py", corpus,
                  "we find a significantly negative association between auditor "
                  "industry range and the likelihood of an audit adjustment")
    cases.append(("verify_quote finds present quote", rc == 0, out.strip().splitlines()[-1:]))

    rc, out = run("verify_quote.py", corpus, "auditors prove fraud beyond doubt")
    cases.append(("verify_quote rejects absent quote", rc == 1, out.strip().splitlines()[-1:]))

    passed = 0
    for name, ok, detail in cases:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        if not ok:
            print(f"       detail: {detail}")
        passed += ok
    print(f"\n{passed}/{len(cases)} tests passed.")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    sys.exit(main())
