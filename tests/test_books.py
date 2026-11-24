def test_create_book(client):
    response = client.post("/books/", json={
        "title": "Dom Casmurro",
        "author": "Machado de Assis",
        "isbn": "9788535902778",
        "year": 1899
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Dom Casmurro"
    assert data["available"] is True


def test_create_book_duplicate_isbn(client):
    payload = {
        "title": "Livro A",
        "author": "Autor A",
        "isbn": "1111111111111",
        "year": 2020
    }
    client.post("/books/", json=payload)
    response = client.post("/books/", json=payload)
    assert response.status_code == 400


def test_list_books(client):
    client.post("/books/", json={
        "title": "Livro 1", "author": "A1", "isbn": "1111111111111", "year": 2020
    })
    client.post("/books/", json={
        "title": "Livro 2", "author": "A2", "isbn": "2222222222222", "year": 2021
    })
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_book_not_found(client):
    response = client.get("/books/999")
    assert response.status_code == 404