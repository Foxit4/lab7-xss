# Лабораторна робота №4. Найпростіший вебсервер. Flask: перші кроки

## Структура
- `simple_server.py` — HTTP-сервер на `http.server` (порт 8000)
- `app.py` — застосунок Flask (порт 5000)
- `templates/hello.html.j2` — шаблон Jinja2
- `requirements.txt` — залежності

## Встановлення
```bash
python -m venv venv
source venv/bin/activate        # Windows PowerShell: venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m flask --version
```

## Запуск
```bash
python simple_server.py         # http://127.0.0.1:8000/
python app.py                   # http://127.0.0.1:5000/
```

## Маршрути
| Сервер | Маршрут | Відповідь |
|---|---|---|
| simple_server | `/`, `/test`, `/info` | 200, text/plain |
| simple_server | інші | 404 |
| Flask | `/` | 200, HTML |
| Flask | `/info` | 200, text/plain |
| Flask | `/hello/<name>` | 200, HTML із шаблону |
| Flask | інші | 404 |
