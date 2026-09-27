# Decisions

| Date | Drift | Change | Why |
|------|-------|--------|-----|
| 2025-07-10 | `JWT_SECRET` and `ADMIN_PASSWORD` hardcoded in `app/config.py` | Replaced with `os.environ.get()`; added empty keys to `.env.example` and `deploy/production.env` | Secrets must never live in source code |
| 2025-07-10 | `NOTIFY_WEBHOOK_URL` missing from `.env.example` and `deploy/production.env` | Added empty keys with comment to both files | App crashes at runtime without this var in production |
| 2025-07-10 | `PORT` missing from `.env.example` | Added to `.env.example` | All used env vars must be documented |
| 2025-07-10 | README said `DB_URL`; code reads `DATABASE_URL` | Updated README to `DATABASE_URL` | README must match code exactly |
| 2025-07-10 | README start command `python run.py`; `run.py` does not exist | Changed to `python -m uvicorn app.main:app` | README must reflect the real invocation |
| 2025-07-10 | README said port 5000; app runs on 8000 | Updated README to 8000 | Port must match config |
| 2025-07-10 | README documented `GET /stats`; route does not exist | Removed phantom endpoint from README | Only real routes may be documented |
| 2025-07-10 | `GET /report/top` existed in code but not in README | Added to README endpoint list | Every route must be documented |
| 2025-07-10 | `GET /report/top` had no test | Added `test_report_top` in `tests/test_main.py` | Every route must have at least one test |
