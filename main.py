#!/usr/bin/env python3
"""plan1 — emit one <=280-char agent-executable plan: $100 -> max money in 30 days."""

import os
import sys

PLAN = (
    "Day 1: buy $12 domain + $18 Canva Pro; build landing page with Stripe "
    "checkout listing $49 pin packs (10 pins/brand). Day 2: DM 50 Etsy/Shopify "
    "sellers, 10/day. Deliver within 24h in Canva. Weekly Stripe check; each "
    "$49 sale reinvested into ads. Target 30 sales = $1470 by day 30."
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
