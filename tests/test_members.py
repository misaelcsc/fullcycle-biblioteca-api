from fastapi.testclient import TestClient


def test_create_member(client):
    response = client.post("/members/", json={
        "name": "Misael",
        "email": "misael@test.com",
        "phone": "11999999999"
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Misael"


def test_create_member_duplicate_email(client):
    payload = {"name": "A", "email": "dup@test.com"}
    client.post("/members/", json=payload)
    response = client.post("/members/", json=payload)
    assert response.status_code == 400


def test_list_members(client: TestClient):
    response = client.get("/members")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_member_by_id(client: TestClient):
    member = client.post("/members/", json={"name": "T", "email": "t2@t.com"}).json()
    response = client.get(f"/members/{member['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == member["id"]


def test_get_member_not_found(client: TestClient):
    response = client.get("/members/9999")
    assert response.status_code == 404