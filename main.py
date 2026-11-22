plan = (
    "D1-3: bank $100 in USDC; list 3 agent-delivered gigs. D4-7: close gig #1, "
    "hit $150. D8-14: repeat sales + $29 template, hit $400. D15-21: double "
    "best channel, raise prices, hit $900. D22-30: reinvest in ads/automation, "
    "close $1,500+."
)

text = plan.strip()
length = len(text)
assert 1 <= length <= 280, f"plan length {length} out of range"

with open("plan.txt", "w") as f:
    f.write(text + "\n")

print(text)
print(f"chars: {length}")
