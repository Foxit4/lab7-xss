# Лабораторна робота №7. XSS (Cross-Site Scripting)

Навчальний Flask-застосунок (на базі лабораторних №4 і №6). **Активна версія захищена**: autoescaping (`.html`) + CSP.
Вразливі варіанти збережено лише в історії Git (теги `edu-*`) і позначено `[EDU-VULNERABLE]`.

## Запуск
```bash
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python init_db.py students_new.db                  # (необов'язково) нова чиста БД
python app.py                                      # http://127.0.0.1:5000/
```
Маршрути: `/hello/<name>`, `/hello2?name=`, `/students`, `/students/<id>`, `/dom-check?name=`.

## Файли
- `students.db` — копія БД із синтетичним маркером `<script>alert('XSS')</script>` у імені студента id=1
- `students_original.db` — БД без маркера
- `tools/probe.py` — знімає тіло відповіді й заголовок CSP; `tools/mark_db.py` — додає маркер через параметризований запит
- `tools/shots.py` — скриншоти й повідомлення Console (Playwright); `evidence/` — витяги й скриншоти

## Відтворення
1. `git checkout edu-1-vulnerable-hello2` → `/hello2?name=<закодований payload>` — скрипт виконується.
2. `edu-2-escape-filter` — `|escape`, розмітка показується текстом.
3. `edu-3-db-marker` (autoescape) і `edu-4-vulnerable-students` (`|safe`) — збережений XSS.
4. `edu-5-csp` — `script-src 'self'` блокує inline-скрипт (див. Console).
5. `main` — підсумкова безпечна версія.
