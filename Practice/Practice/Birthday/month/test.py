
import json
from collections import Counter

month = []

with open("info.json", "r") as f:
    birthdays = json.load(f)

for x in birthdays.values():
    month.append(x.split()[0])

print(Counter(month))