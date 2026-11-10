"""Скриншоти + Console/діалоги для навчальних запитів. Використання: python tools/shots.py <порт> <префікс> <шлях1> [шлях2 ...]"""
import sys
from playwright.sync_api import sync_playwright

port, prefix, paths = sys.argv[1], sys.argv[2], sys.argv[3:]
with sync_playwright() as p:
    b = p.chromium.launch()
    for i, path in enumerate(paths, 1):
        pg = b.new_page(viewport={"width": 900, "height": 360})
        log = []
        pg.on("console", lambda m, log=log: log.append(f"[console.{m.type}] {m.text}"))
        pg.on("dialog", lambda d, log=log: (log.append(f"[dialog] {d.message}"), d.dismiss()))
        r = pg.goto(f"http://127.0.0.1:{port}{path}")
        pg.wait_for_timeout(300)
        bg = pg.evaluate("getComputedStyle(document.body).backgroundColor")
        log.append(f"[body background] {bg}")
        log.append(f"[CSP header] {r.headers.get('content-security-policy')}")
        pg.screenshot(path=f"evidence/{prefix}_{i}.png")
        open(f"evidence/{prefix}_{i}.log", "w", encoding="utf-8").write(path + "\n" + "\n".join(log) + "\n")
        print(prefix, i, path[:60], "|", " | ".join(log))
    b.close()
