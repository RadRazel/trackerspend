import json
from pathlib import Path
FILE = Path("expenses.json")

def load_expenses():
    if not FILE.exists():
        return []
    with FILE.open(encoding = "utf-8") as f:
        data = json.load(f)
        return data


def save_expenses(expenses):
    with FILE.open("w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)
print(load_expenses())