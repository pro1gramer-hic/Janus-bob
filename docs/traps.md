# Pièges plantés dans example_app (corrigé, ne pas montrer à Bob)

1. Configuration : NOTIFY_WEBHOOK_URL est utilisée dans app/notifications.py mais absente de .env.example et de deploy/production.env. POST /tasks plante en production.
2. Documentation : le README cite DB_URL (en réalité DATABASE_URL), python run.py (n'existe pas, c'est uvicorn app.main:app), le port 5000 (en réalité 8000), l'endpoint /stats (en réalité /report/top), et affirme qu'aucun secret n'est dans le code.
3. Secrets : JWT_SECRET et ADMIN_PASSWORD écrits en dur dans app/config.py.
4. Impact : calculate_priority est appelée dans main.py et reports.py, et n'a aucun test. Aucun test non plus pour POST /tasks ni /report/top.
5. Échec : dans ci_logs/failed_run.txt, la première vraie erreur est le KeyError NOTIFY_WEBHOOK_URL (notifications.py ligne 7, appelé depuis main.py ligne 20). Les quatre échecs suivants en découlent.
