from app import app


def test_invalid_url(client):

    response = client.post(
        "/shorten",
        json={
            "url": "hello"
        }
    )

    assert response.status_code == 400