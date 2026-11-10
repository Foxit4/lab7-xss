"""Додає навчальний маркер до імені студента в КОПІЇ БД (синтетичні дані)."""
import sqlite3
import sys

path, student_id = sys.argv[1], int(sys.argv[2])
db = sqlite3.connect(path)
original_name = db.execute("SELECT name FROM students WHERE id = ?", (student_id,)).fetchone()[0]
changed_name = original_name + " <script>alert('XSS')</script>"
with db:
    cur = db.execute("UPDATE students SET name = ? WHERE id = ?", (changed_name, student_id))
    if cur.rowcount != 1:
        raise ValueError("Не знайдено рівно одного студента")
db.close()
print(f"id={student_id}: {original_name!r} -> {changed_name!r}")
