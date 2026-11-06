import json #cловарь и тп
import datetime #время
from pathlib import Path # представляет путь к файлу и умеет его проверять и открывать.
import argparse

FILE = Path("expenses.json") #Создаёт объект пути к файлу expenses.json и кладёт его в переменную FILE.

def load_expenses():
    if not FILE.exists():
        return []
    with FILE.open(encoding = "utf-8") as f:
        data = json.load(f) #из json в пайтон объект
        return data


def save_expenses(expenses):
    with FILE.open("w", encoding="utf-8") as f: #"w" значит write. Если файл уже есть, его содержимое стирается сразу при открытии. старое в новое.
        json.dump(expenses, f, ensure_ascii=False, indent=2)#превращает объект питона в json формат.


def add_expenses(amount, category, comment):
    expenses = load_expenses()
    parameters = {"amount": amount, "category": category, "comment": comment, "date":datetime.date.today().isoformat()}
    expenses.append(parameters)
    save_expenses(expenses)


def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("список пуст")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['date']} | {expense['category']} | {expense['amount']:.2f} | {expense['comment']} ")

def main():
    parser = argparse.ArgumentParser(description="трекер расходов")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="список")

    add_parser = subparsers.add_parser("add", help="добавить")
    add_parser.add_argument("amount", type=float)
    add_parser.add_argument("category")
    add_parser.add_argument("comment")

    args = parser.parse_args()

    if args.command == "list":
        list_expenses()
    elif args.command == "add":
        add_expenses(args.amount, args.category, args.comment)


if __name__ == "__main__":
    main()