#!/usr/bin/env python3
"""Fail if plugin copy publishes HOLD phone, invented live metros, or custody claims."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK = json.loads((ROOT / "references" / "east-bay-live.json").read_text())

SCAN_GLOBS = (
    "README.md",
    "SECURITY.md",
    "agents/**/*.md",
    "docs/**/*.md",
    "skills/**/*.md",
    "references/**/*.md",
)

# Placeholder tel / display from live config — never ship as a callable number.
PHONE_BANS = (
    "tel:+18130000000",
    "tel:+1-813-000-0000",
    "+18130000000",
)

# Invented live metros (Tampa Bay is the only live matching metro).
METRO_BANS = (
    r"\blive now[:\s].{0,40}\b(orlando|miami|jacksonville|atlanta|nashville|houston)\b",
    r"\b(orlando|miami|jacksonville)\b.{0,40}\b(first live|live metro|roster is live)\b",
)

CUSTODY_BANS = (
    r"\bescrow-ready\b",
    r"\bsend the deposit to east bay\b",
    r"\bpaid from hold\b",
    r"\bwe(?:'ll| will) (?:run the job|send a crew|install|mow|encapsulate)\b",
    r"\bour guys\b",
)


def iter_files() -> list[Path]:
    files: list[Path] = []
    for pattern in SCAN_GLOBS:
        files.extend(ROOT.glob(pattern))
    return sorted({p for p in files if p.is_file()})


def main() -> int:
    errors: list[str] = []
    live = LOCK["live_matching"]
    if live["metros"] != ["Tampa Bay"]:
        errors.append("lock: live metros must be Tampa Bay only")
    if live["depth_zips"] != ["33569", "33578", "33579"]:
        errors.append("lock: depth ZIPs drifted")
    if LOCK["contact"]["email"] != "hello@eastbayservices.com":
        errors.append("lock: email drifted")
    if LOCK["founder_hold"]["phone"]["status"] != "HOLD":
        errors.append("lock: phone must stay HOLD")
    geo = LOCK.get("product_geography") or {}
    if geo.get("scope") != "United States" or geo.get("kind") != "countrywide_app":
        errors.append("lock: product must stay a United States countrywide app")

    for path in iter_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        lower = text.lower()
        for i, line in enumerate(text.splitlines(), 1):
            line_l = line.lower()
            documenting_hold = any(
                x in line_l
                for x in ("do not", "never", "hold", "placeholder", "must not", "do_not")
            )
            if documenting_hold:
                continue
            for ban in PHONE_BANS:
                if ban.lower() in line_l:
                    errors.append(f"{rel}:{i}: publishes HOLD tel `{ban}`")
            if re.search(r"\b813-\d{3}-\d{4}\b", line):
                errors.append(f"{rel}:{i}: publishes a live 813 number")
        for pat in METRO_BANS:
            if re.search(pat, lower):
                errors.append(f"{rel}: invents a live metro ({pat})")
        if rel.name in {"README.md", "yard-buyer.md"} and "united states" not in lower:
            errors.append(f"{rel}: missing United States product geography")
        if rel.parts[0] in {"agents", "skills"} or rel.name in {
            "README.md",
            "CURSOR-SUBMISSION.md",
        }:
            for pat in CUSTODY_BANS:
                if re.search(pat, lower):
                    errors.append(f"{rel}: custody / contractor-voice ban ({pat})")

    if errors:
        print("east-bay copy check FAILED")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"east-bay copy check OK ({len(iter_files())} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
