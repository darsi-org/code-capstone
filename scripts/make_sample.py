"""Make sample.csv: 30 made-up pupils (no real names), with marks and days absent. Seeded, so it's the same every time."""
import csv
import random

random.seed(7)
FIRST = ["Mona", "Omar", "Salma", "Youssef", "Nour", "Karim", "Hana", "Ali", "Farida", "Ziad", "منى", "عمر"]
with open("sample.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "name", "maths", "arabic", "science", "days_absent"])
    for i in range(1, 31):
        w.writerow([f"P{i:03}", f"{random.choice(FIRST)} {chr(64 + i % 26 + 1)}.", *(random.randint(35, 100) for _ in range(3)), random.randint(0, 9)])
print("sample.csv written")
