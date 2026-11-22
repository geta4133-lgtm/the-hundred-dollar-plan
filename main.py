"""Write a <=280-char plan for turning $100 into the most money in 30 days."""

plan = (
    "Day1: keep $70 capital, $30 buffer. Days2-5: pick a fast-turn market you know "
    "(resale, freelance, flipping). Days6-14: ship a paid offer, reinvest each sale. "
    "Days15-22: double down on winners, cut what didn't. Days23-29: scale via "
    "repeat buyers. Day30: keep only proven channels."
)

text = plan.strip()
length = len(text)
assert 1 <= length <= 280, f"plan length {length} out of range"
with open("plan.txt", "w") as f:
    f.write(text + "\n")
print(f"chars: {length}")
print(text)
