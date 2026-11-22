#!/usr/bin/env python3
"""Write the plan entry to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os
import sys

OUTPUT_FILENAME = "entry.txt"
MAX_CHARS = 280

PLAN = (
    "D1-3: bank $100 USDC; post 3 gigs: AI article $25, logo $40, "
    "automation $75. D4-7: close gig #1; $150. "
    "D8-14: resell the article gig weekly; list the $29 template on "
    "3 marketplaces. $400. D15-21: scale best channel, raise prices; "
    "$900. D22-30: reinvest in ads, close $1,500+."
)


def build_output_dir() -> str:
    """Resolve the output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def validate(plan: str) -> int:
    """Return plan length, or exit non-zero if out of range."""
    length = len(plan)
    if not 1 <= length <= MAX_CHARS:
        print(f"plan length {length} outside 1..{MAX_CHARS}", file=sys.stderr)
        sys.exit(1)
    return length


def write_entry(plan: str, out_dir: str) -> str:
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(plan)
    return path


def main() -> int:
    length = validate(PLAN)
    out_dir = build_output_dir()
    path = write_entry(PLAN, out_dir)
    print(f"wrote {path} ({length} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
