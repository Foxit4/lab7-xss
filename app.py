import sqlite3
from pathlib import Path

from flask import Flask, abort, g, render_template, request

BASE = Path(__file__).parent
DB_PATH = BASE / "students.db"

app = Flask(__name__)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    return "<h1>Вітаємо у Flask!</h1>"


@app.route("/info")
def info():
    return "Це інформаційний маршрут Flask.", 200, {
        "Content-Type": "text/plain; charset=utf-8"
    }


@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html.j2", name=name)


@app.get("/students")
def students():
    rows = get_db().execute("SELECT id, name, grp FROM students ORDER BY id").fetchall()
    return render_template("students.html", students=rows)


@app.get("/students/<int:student_id>")
def student_detail(student_id):
    row = get_db().execute(
        "SELECT id, name, grp FROM students WHERE id = ?", (student_id,)
    ).fetchone()
    if row is None:
        abort(404)
    return render_template("student.html", student=row)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
