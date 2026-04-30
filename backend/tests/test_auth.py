def test_login_rejects_invalid_credentials(client):
    payload = {
        "username": "invalid_user",
        "password": "invalid_password",
    }

    response = client.post("/api/auth/login", json=payload)

    assert response.status_code == 401
    body = response.json()
    assert "detail" in body
    assert body["detail"] == "Invalid username or password"


def test_me_requires_authentication(client):
    response = client.get("/api/auth/me")

    assert response.status_code == 401
    body = response.json()
    assert "detail" in body