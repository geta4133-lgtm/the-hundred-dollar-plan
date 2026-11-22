import os
import sys

PLAN = (
    "D1-3: bank $100 in USDC; post 3 gigs: 1k-word AI article $25, "
    "logo pack $40, automation setup $75. D4-7: close gig #1, hit $150. "
    "D8-14: repeat sales + $29 template, hit $400. D15-21: double best "
    "channel, raise prices, hit $900. D22-30: reinvest in ads/automation, "
    "close $1,500+."
).strip()

length = len(PLAN)
if not (1 <= length <= 280):
    print(f"plan length {length} out of range", file=sys.stderr)
    sys.exit(1)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "entry.txt")

with open(out_path, "w", encoding="utf-8") as f:
    f.write(PLAN)

print(f"wrote {out_path} ({length} chars)")
sys.exit(0)
