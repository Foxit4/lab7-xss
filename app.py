from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
