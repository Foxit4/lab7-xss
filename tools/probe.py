"""Знімає тіло відповіді та заголовок CSP для навчальних запитів (Flask test client)."""
import sys
from urllib.parse import quote

sys.path.insert(0, ".")
from app import app  # noqa: E402

PAYLOAD = "<script>document.querySelector('body').style.backgroundColor = 'black'; alert('Марія');</script>"
CASES = ["Марія", PAYLOAD, "Марія&Олег", "<b>Марія</b>", 'a"b\'c', "&lt;b&gt;"]
c = app.test_client()
for name in CASES:
    r = c.get("/hello2?name=" + quote(name))
    body = r.get_data(as_text=True)
    line = next((l.strip() for l in body.splitlines() if "<h1>" in l), "")
    print(f"name={name!r}\n  status={r.status_code}  CSP={r.headers.get('Content-Security-Policy')}\n  {line}")
r = c.get("/hello2")
print("без name ->", next(l.strip() for l in r.get_data(as_text=True).splitlines() if "<h1>" in l))
r = c.get("/students")
print("\n/students:")
for l in r.get_data(as_text=True).splitlines():
    if "<a href" in l:
        print(" ", l.strip())
print("  CSP =", r.headers.get("Content-Security-Policy"))
