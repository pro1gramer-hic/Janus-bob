from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_report_top():
    response = client.get("/report/top")
    assert response.status_code == 200
    assert "top" in response.json()
