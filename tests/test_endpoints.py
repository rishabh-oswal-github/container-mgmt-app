from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_container():
    response = client.post("/containers", json={
        "container_id": "CONT1",
        "arrival_date": "2023-06-01",
        "departure_date": "2023-06-10"
    })
    assert response.status_code == 201
    assert response.json() == {
        "container_id": "CONT1",
        "arrival_date": "2023-06-01",
        "departure_date": "2023-06-10",
        "status": "active"
    }

def test_update_container():
    response = client.post("/containers", json={
        "container_id": "CONT4",
        "arrival_date": "2023-06-10",
        "departure_date": "2023-06-20"
    })
    response = client.put("/containers/CONT4", json={
        "arrival_date": "2023-06-10",
        "departure_date": "2023-06-30"
    })
    assert response.status_code == 201
    assert response.json() == {
        "container_id": "CONT4",
        "arrival_date": "2023-06-10",
        "departure_date": "2023-06-30",
        "status": "active"
    }

def test_get_container():
    response = client.get("/containers/CONT1")
    assert response.status_code == 200
    assert response.json() == {
        "container_id": "CONT1",
        "arrival_date": "2023-06-01",
        "departure_date": "2023-06-10",
        "status": "active"
    }

def test_get_all_containers():
    response = client.get("/containers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_calculate_fees():
    response = client.post("/calculate_fees", json={
        "container_id": "CONT1",
        "days_on_terminal": 12,
        "days_with_consignee": 5
    })
    assert response.status_code == 200
    assert response.json() == {
        "container_id": "CONT1",
        "days_on_terminal": 12,
        "days_with_consignee": 5,
        "demurrage_fee": 410,
        "detention_fee": 140,
        "total_fee": 550
    }

def test_get_fees():
    response = client.get("/fees/CONT1")
    assert response.status_code == 200
    assert response.json() == {
        "container_id": "CONT1",
        "days_on_terminal": 12,
        "days_with_consignee": 5,
        "demurrage_fee": 410,
        "detention_fee": 140,
        "total_fee": 550
    }

def test_generate_statistics():
    response = client.get("/statistics")
    assert response.status_code == 200
    assert "total_containers" in response.json()
    assert "average_days_on_terminal" in response.json()
    assert "average_days_with_consignee" in response.json()
    assert "total_demurrage_fee" in response.json()
    assert "total_detention_fee" in response.json()
    assert "average_demurrage_fee_per_container" in response.json()
    assert "average_detention_fee_per_container" in response.json()
