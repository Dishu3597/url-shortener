import json


def test_redirect(client):

    response = client.post(
        "/shorten",
        json={
            "url": "https://www.google.com"
        }
    )

    data = json.loads(response.data)

    short_code = data["shortCode"]

    redirect_response = client.get(f"/{short_code}")

    assert redirect_response.status_code == 302