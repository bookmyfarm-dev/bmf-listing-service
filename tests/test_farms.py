import os
import pytest
from fastapi.testclient import TestClient

# must be set before the app is imported
os.environ.setdefault(
    "DATABASE_URL", "postgresql+psycopg://bmf:bmf@localhost:5432/listings_test"
)
from app.main import app  # noqa: E402


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_healthz(client):
    assert client.get("/healthz").json() == {"status": "ok"}


def test_create_and_get_farm(client):
    payload = {
        "owner_id": "o1", "name": "Green Acres", "city": "Aurangabad",
        "price_per_night": 8000, "capacity": 25,
    }
    created = client.post("/farms", json=payload)
    assert created.status_code == 201
    farm_id = created.json()["id"]

    fetched = client.get(f"/farms/{farm_id}")
    assert fetched.status_code == 200
    assert fetched.json()["name"] == "Green Acres"


def test_filter_by_city(client):
    r = client.get("/farms", params={"city": "Aurangabad"})
    assert r.status_code == 200
    assert all(f["city"] == "Aurangabad" for f in r.json())


def test_invalid_price_rejected(client):
    bad = {"owner_id": "o1", "name": "X1", "city": "A",
           "price_per_night": -5, "capacity": 10}
    assert client.post("/farms", json=bad).status_code == 422


def test_missing_farm_404(client):
    assert client.get("/farms/999999").status_code == 404