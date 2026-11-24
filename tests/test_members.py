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
