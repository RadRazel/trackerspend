import json #cловарь и тп
import datetime #время
from pathlib import Path # представляет путь к файлу и умеет его проверять и открывать.
from unicodedata import category

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
    parametrs = {"amount": amount, "category": category, "comment": comment, "date":datetime.date.today().isoformat()}
    expenses.append(parametrs)
    save_expenses(expenses)
#add_expenses(300, "еда", "обед") - example

def list_expenses():
    expenses = load_expenses()
    if not expenses:
        return print("список пуст")
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['date']} | {expense['category']} | {expense['amount']}  | {expense['comment']} ")
list_expenses()
