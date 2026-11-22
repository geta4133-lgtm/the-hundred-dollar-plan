#!/usr/bin/env python3
"""plan1: emit a <=280-char plan turning $100 into max money in 30 days."""

import os

PLAN = (
    "Spend $40 on domain+email. Build a 1-page site selling a $99 "
    "same-day site-speed fix (Lighthouse audit+minify). Days 2-25: 15 "
    "cold emails/day to shops with weak Lighthouse scores; $10 for a leads scraper. "
    "Verify: 3 Stripe sales = $297; reinvest into ads, target $900 day 30."
)


def emit() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = PLAN.encode("utf-8").decode("utf-8")
    assert 1 <= len(text) <= 280, f"len={len(text)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    emit()
