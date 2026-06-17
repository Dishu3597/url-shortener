import json


def test_create_short_url(client):

    response = client.post(
        "/shorten",
        json={
            "url": "https://www.google.com"
        }
    )

    assert response.status_code == 201

    data = json.loads(response.data)

    assert "shortCode" in data
    assert "shortUrl" in data