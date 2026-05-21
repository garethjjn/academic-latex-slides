#!/usr/bin/env python3
"""eval_harness.py — re-runnable regression harness for audit-write section drafts.

Scripts the *deterministic* half of the Stage-1 Phase F eval so any future skill
change is measured, not guessed. For each eval task it runs the mechanical gates
(lint_style.py + check_structure.py) on the draft and reports a compliance line,
then emits the exact `audit-write-critic` invocation prompt for the orchestrator
to spawn (the critic is an LLM, so it cannot be scripted here — but its input is
standardized). Optionally folds in critic composites to compute lift vs baseline.

Usage:
  eval_harness.py gates  [--drafts DIR] [--suffix S]   # run gates + print critic prompts
  eval_harness.py report --scores k=v[,k=v...] [--drafts DIR] [--suffix S]
        # k = "<code>_<section>", v = critic composite; computes lift + writes eval md

Defaults: --drafts quality_reports/eval/phase_f_drafts  --suffix postC_v2
Exit: 0 always (advisory).
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "audit-write-skills" / "plugins" / "audit-write" / "scripts"
LINT = SCRIPTS / "lint_style.py"
STRUCT = SCRIPTS / "check_structure.py"

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass

# The Phase F eval task set. baseline=None for the no-baseline "new" task.
TASKS = [
    {"code": "14-FPW", "section": "intro", "baseline": 76},
    {"code": "17-CMOX", "section": "hypothesis", "baseline": 76},
    {"code": "14-HLM", "section": "results", "baseline": 82},
    {"code": "16-CKPW", "section": "intro", "baseline": None},
]


def run(cmd):
    # force UTF-8 decode: the linters emit em-dashes/smart-quotes, and the Windows
    # GBK default decoder crashes the capture thread and silently returns empty.
    r = subprocess.run([sys.executable, *map(str, cmd)], capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def draft_path(drafts, code, section, suffix):
    return Path(drafts) / f"{code}_{section}_{suffix}.md"


def gate_task(t, drafts, suffix):
    p = draft_path(drafts, t["code"], t["section"], suffix)
    if not p.exists():
        return {"missing": True, "path": str(p)}
    lc, lout = run([LINT, p])
    sc, sout = run([STRUCT, p, "--section", t["section"]])
    lint_line = lout.strip().splitlines()[-1] if lout.strip() else "?"
    # actionable WARNs = real ": WARN " lines (not the "0 WARN(s)" summary),
    # excluding the em-dash density advisory
    warns = [w for w in lout.splitlines()
             if ": WARN " in w and "em-dash" not in w]
    struct_N = [s for s in sout.splitlines() if s.strip().startswith("[ N]")]
    mechanical_ok = (lc == 0) and not warns and not struct_N
    return {"missing": False, "path": str(p), "lint_line": lint_line,
            "actionable_warns": warns, "struct_N": struct_N, "ok": mechanical_ok}


def critic_prompt(t, p):
    sec = t["section"]
    return (f'Agent(subagent_type="audit-write-critic"): Score the drafted **{sec}** at '
            f'`{p}` against rubric.md (5 dims + integrity gate). Placeholders '
            f'`[AUTHOR:]`/`[PLACEHOLDER:]` are intentional — not fabrication. Return the '
            f'canonical Score block (composite/100, per-dim bands, C1–C7, integrity).')


def cmd_gates(drafts, suffix):
    print(f"# eval_harness gates — drafts={drafts} suffix={suffix}\n")
    for t in TASKS:
        r = gate_task(t, drafts, suffix)
        tag = f'{t["code"]} {t["section"]}'
        if r["missing"]:
            print(f"## {tag}: MISSING ({r['path']})\n")
            continue
        verdict = "MECHANICAL-PASS" if r["ok"] else "MECHANICAL-FAIL"
        print(f"## {tag}: {verdict}")
        print(f"   lint: {r['lint_line']}")
        for w in r["actionable_warns"]:
            print(f"   ! {w.split(': WARN ',1)[-1][:90] if ': WARN ' in w else w[:90]}")
        for s in r["struct_N"]:
            print(f"   ! struct {s.strip()}")
        print(f"   critic-prompt: {critic_prompt(t, r['path'])}\n")
    print("After spawning the critic prompts, run:  eval_harness.py report --scores "
          + ",".join(f'{t["code"]}_{t["section"]}=<score>' for t in TASKS))


def cmd_report(scores, drafts, suffix):
    out = ["# Eval harness report", f"\n_drafts={drafts} suffix={suffix}_\n",
           "| Task | Baseline | Composite | Lift | Mechanical |", "|---|---|---|---|---|"]
    lifts = []
    for t in TASKS:
        key = f'{t["code"]}_{t["section"]}'
        comp = scores.get(key)
        r = gate_task(t, drafts, suffix)
        mech = "missing" if r.get("missing") else ("PASS" if r["ok"] else "FAIL")
        base = t["baseline"]
        if comp is not None and base is not None:
            lift = comp - base
            lifts.append(lift)
            lift_s = f"{lift:+d}" if isinstance(lift, int) else f"{lift:+.0f}"
        else:
            lift_s = "—"
        print(f"  {key}: composite={comp} baseline={base} mechanical={mech}")
        out.append(f"| {key} | {base if base is not None else '—'} | "
                   f"{comp if comp is not None else '—'} | {lift_s} | {mech} |")
    if lifts:
        mean = sum(lifts) / len(lifts)
        out.append(f"\n**Mean lift over {len(lifts)} baselined tasks: {mean:+.1f}** "
                   f"(target ≥ +5, no task decline).")
    rep = ROOT / "quality_reports" / "eval" / f"harness_report_{suffix}.md"
    rep.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"\nwrote {rep}")


def parse_scores(s):
    out = {}
    for kv in s.split(","):
        if "=" in kv:
            k, v = kv.split("=", 1)
            try:
                out[k.strip()] = int(round(float(v)))
            except ValueError:
                pass
    return out


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 0
    mode = args[0]
    drafts = "quality_reports/eval/phase_f_drafts"
    suffix = "postC_v2"
    scores = {}
    i = 1
    while i < len(args):
        if args[i] == "--drafts" and i + 1 < len(args):
            drafts = args[i + 1]; i += 2
        elif args[i] == "--suffix" and i + 1 < len(args):
            suffix = args[i + 1]; i += 2
        elif args[i] == "--scores" and i + 1 < len(args):
            scores = parse_scores(args[i + 1]); i += 2
        else:
            i += 1
    if mode == "gates":
        cmd_gates(drafts, suffix)
    elif mode == "report":
        cmd_report(scores, drafts, suffix)
    else:
        print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main())
