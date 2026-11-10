"""Створює навчальну БД із синтетичними записами (заміна БД з лабораторної №6)."""
import sqlite3
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "students.db"
db = sqlite3.connect(path)
with db:
    db.execute("DROP TABLE IF EXISTS students")
    db.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, grp TEXT NOT NULL)")
    db.executemany(
        "INSERT INTO students (name, grp) VALUES (?, ?)",
        [("Марія Коваленко", "ІПЗ-21"), ("Олег Шевченко", "ІПЗ-21"),
         ("Ірина Бойко", "ІПЗ-22"), ("Андрій Мельник", "ІПЗ-22")],
    )
db.close()
print("Створено", path)
