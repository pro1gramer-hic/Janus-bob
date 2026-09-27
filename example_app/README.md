# Taskly

A small task tracking API.

## Setup

Set the `DATABASE_URL` environment variable to your database connection string.

## Run

```bash
python -m uvicorn app.main:app
```

The API serves on port 8000.

## Endpoints

- `GET /health`: health check
- `POST /tasks`: create a task
- `GET /tasks/{id}`: get a task
- `GET /report/top`: top tasks report

## Security

All credentials are read from environment variables. See `.env.example` for the full list of required variables.
