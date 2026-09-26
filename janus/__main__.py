"""Janus command line: python -m janus check <path>"""

import argparse
import json
import sys
from pathlib import Path

from janus import scan_config, scan_docs, scan_secrets

SCANNERS = {
    "config": scan_config.scan,
    "secrets": scan_secrets.scan,
    "docs": scan_docs.scan,
}

SEVERITY_ORDER = ["critical", "high", "medium", "low"]


def run_check(target: Path, as_json: bool) -> int:
    results = {name: scan(target) for name, scan in SCANNERS.items()}
    findings = [f for result in results.values() for f in result["findings"]]
    findings.sort(key=lambda f: SEVERITY_ORDER.index(f["severity"]))

    out_dir = target / ".janus"
    out_dir.mkdir(exist_ok=True)
    report_path = out_dir / "report.json"
    report = {
        "target": str(target),
        "count": len(findings),
        "summaries": {name: r["summary"] for name, r in results.items()},
        "findings": findings,
    }
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    if as_json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Janus check: {target}")
        if not findings:
            print("  No issues found.")
        for f in findings:
            loc = f"{f['file']}:{f['line']}" if f.get("line") else f["file"]
            print(f"  {f['severity'].upper():<9} {f['detail']}  ({loc})")
        print(f"\n{len(findings)} issue(s). Report: {report_path}")

    # Non-zero exit code blocks a CI pipeline when something serious is found
    return 1 if any(f["severity"] in ("critical", "high") for f in findings) else 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="janus", description="Looks before. Checks after. Never forgets.")
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check", help="scan a project for drift")
    check.add_argument("path", nargs="?", default=".", help="project to scan")
    check.add_argument("--json", action="store_true", help="print the JSON report")
    args = parser.parse_args()

    target = Path(args.path).resolve()
    if not target.is_dir():
        print(f"Not a directory: {target}", file=sys.stderr)
        return 2

    if args.command == "check":
        return run_check(target, args.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
