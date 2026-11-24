from fastapi.testclient import TestClient


def _create_book(client, isbn="1111111111111"):
    return client.post("/books/", json={
        "title": "Livro", "author": "Autor", "isbn": isbn, "year": 2020
    }).json()


def _create_member(client, email="m@test.com"):
    return client.post("/members/", json={
        "name": "Membro", "email": email
    }).json()


def test_create_loan(client):
    book = _create_book(client)
    member = _create_member(client)
    response = client.post("/loans/", json={
        "book_id": book["id"],
        "member_id": member["id"]
    })
    assert response.status_code == 201
    assert response.json()["returned"] is False


def test_loan_unavailable_book(client):
    book = _create_book(client)
    member = _create_member(client)
    client.post("/loans/", json={"book_id": book["id"], "member_id": member["id"]})
    response = client.post("/loans/", json={"book_id": book["id"], "member_id": member["id"]})
    assert response.status_code == 400


def test_return_loan(client):
    book = _create_book(client)
    member = _create_member(client)
    loan = client.post("/loans/", json={
        "book_id": book["id"], "member_id": member["id"]
    }).json()

    response = client.post(f"/loans/{loan['id']}/return")
    assert response.status_code == 200
    assert response.json()["returned"] is True

    # Livro volta a ficar disponível
    book_check = client.get(f"/books/{book['id']}").json()
    assert book_check["available"] is True


def test_list_loans(client: TestClient):
    response = client.get("/loans")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_loan_by_id(client: TestClient):
    book = _create_book(client, isbn="1234567890123")
    member = _create_member(client, email="t@t.com")
    loan = client.post("/loans/", json={
        "book_id": book["id"],
        "member_id": member["id"]
    }).json()

    response = client.get(f"/loans/{loan['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == loan["id"]


def test_get_loan_not_found(client: TestClient):
    response = client.get("/loans/9999")
    assert response.status_code == 404