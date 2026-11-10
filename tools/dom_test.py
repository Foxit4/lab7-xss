import sys
from playwright.sync_api import sync_playwright
port = sys.argv[1]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 900, "height": 360})
    logs = []; pg.on("dialog", lambda d: (logs.append("dialog:" + d.message), d.dismiss()))
    pg.goto(f"http://127.0.0.1:{port}/dom-check")
    for val in ["<b>Марія</b>", "<script>alert('XSS')</script>"]:
        pg.fill("#source", val); pg.click("#show")
        print("textContent ->", repr(val), "| дочірніх елементів у #result:", pg.evaluate("document.querySelector('#result').children.length"), "| текст:", pg.inner_text("#result"))
    pg.screenshot(path="evidence/dom_textcontent.png")
    pg.fill("#source", "<b>Марія</b>")
    pg.evaluate("document.querySelector('#result').innerHTML = document.querySelector('#source').value")  # лише для порівняння
    print("innerHTML   -> '<b>Марія</b>' | дочірніх елементів:", pg.evaluate("document.querySelector('#result').children.length"), "| тег:", pg.evaluate("document.querySelector('#result').firstElementChild.tagName"))
    pg.screenshot(path="evidence/dom_innerhtml_compare.png")
    print("діалоги:", logs); b.close()
