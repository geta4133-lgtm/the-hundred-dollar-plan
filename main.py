#!/usr/bin/env python3
"""plan1 — emit one <=280-char agent-executable plan: $100 -> max money in 30 days."""

import os
import sys

PLAN = (
    "Day 1: spend $15 on a domain + $20 landing page. Offer $49 Pinterest "
    "pin packs (10 pins) to Etsy/Shopify sellers, priced $49. Days 2-30: "
    "deliver in Canva same-day. Verify: Stripe income weekly. Reinvest all "
    "into 2 repeat clients -> target $1500 by day 30."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = PLAN
    n = len(text)
    if not (1 <= n <= 280):
        raise SystemExit(f"plan length {n} outside 1-280")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"written {n} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
