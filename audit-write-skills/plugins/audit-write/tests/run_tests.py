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

    slop_ok = "em-dash overuse" in out and "rhetorical" in out
    cases.append(("lint_style WARNs AI-slop tells on bad fixture", slop_ok,
                   [l for l in out.splitlines() if "WARN" in l
                    and ("em-dash" in l or "rhetorical" in l)][:2]))

    rc, out = run("lint_style.py", os.path.join(FIX, "good_draft.md"))
    good_clean = rc == 0 and "em-dash overuse" not in out and "rhetorical" not in out
    cases.append(("lint_style passes good fixture (no slop false-positives)",
                   good_clean, out.strip().splitlines()[-1:]))

    rc, out = run("check_structure.py", os.path.join(FIX, "bad_draft.md"),
                  "--section", "intro")
    cs_bad = rc == 0 and "[ N]" in out
    cases.append(("check_structure flags N on bad fixture (advisory, exit 0)",
                   cs_bad, out.strip().splitlines()[-1:]))

    rc, out = run("check_structure.py", os.path.join(FIX, "good_draft.md"),
                  "--section", "abstract")
    cs_good = rc == 0 and "[ Y] C5 abstract" in out
    cases.append(("check_structure passes good fixture abstract check",
                   cs_good, out.strip().splitlines()[-1:]))

    # intro signed-prediction-must-be-a-formal-H check (Round 2 mechanization)
    rc, out = run("check_structure.py", os.path.join(FIX, "intro_signed_no_h.md"),
                  "--section", "intro")
    cs_noh = rc == 0 and "[ N] C5 signed prediction stated as formal H" in out
    cases.append(("check_structure flags signed prediction with no formal H",
                   cs_noh, [l for l in out.splitlines() if "formal H" in l][:1]))

    rc, out = run("check_structure.py", os.path.join(FIX, "intro_formal_h.md"),
                  "--section", "intro")
    cs_h = rc == 0 and "[ Y] C5 signed prediction stated as formal H" in out
    cases.append(("check_structure passes intro with a displayed formal H",
                   cs_h, [l for l in out.splitlines() if "formal H" in l][:1]))

    # design §3 mandatory-element checks (Round 3 mechanization)
    rc, out = run("check_structure.py", os.path.join(FIX, "design_complete.md"),
                  "--section", "design")
    cs_dc = rc == 0 and "0 N ->" in out
    cases.append(("check_structure passes a complete design section",
                   cs_dc, out.strip().splitlines()[-1:]))

    rc, out = run("check_structure.py", os.path.join(FIX, "design_no_descriptives.md"),
                  "--section", "design")
    cs_dn = rc == 0 and "[ N]" in out and "descriptive-statistics block" in out
    cases.append(("check_structure flags design missing descriptive statistics",
                   cs_dn, [l for l in out.splitlines() if "descriptive" in l][:1]))

    rc, out = run("check_structure.py", os.path.join(FIX, "design_flat_controls.md"),
                  "--section", "design")
    cs_ft = rc == 0 and "[ N]" in out and "controls tiered" in out
    cases.append(("check_structure flags design with flat (untiered) controls",
                   cs_ft, [l for l in out.splitlines() if "tiered" in l][:1]))

    # robustness numbered-battery check (Round 3)
    rc, out = run("check_structure.py", os.path.join(FIX, "robustness_battery.md"),
                  "--section", "robustness")
    cs_rb = rc == 0 and "[ Y]" in out and "numbered/enumerated battery" in out
    cases.append(("check_structure passes a numbered robustness battery",
                   cs_rb, [l for l in out.splitlines() if "battery" in l][:1]))

    rc, out = run("check_structure.py", os.path.join(FIX, "robustness_thin.md"),
                  "--section", "robustness")
    cs_rt = rc == 0 and "[ N]" in out and "numbered/enumerated battery" in out
    cases.append(("check_structure flags a thin (un-enumerated) robustness section",
                   cs_rt, [l for l in out.splitlines() if "battery" in l][:1]))

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
