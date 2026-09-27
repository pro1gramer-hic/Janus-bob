import os

settings = {
    "DATABASE_URL": os.getenv("DATABASE_URL", "sqlite:///./taskly.db"),
    "APP_ENV": os.getenv("APP_ENV", "development"),
    "PORT": int(os.getenv("PORT", "8000")),
}

JWT_SECRET = os.environ.get("JWT_SECRET", "")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")
