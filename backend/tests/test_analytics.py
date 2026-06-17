import json


def test_analytics(client):

    response = client.post(
        "/shorten",
        json={
            "url": "https://www.google.com"
        }
    )

    data = json.loads(response.data)

    short_code = data["shortCode"]

    analytics = client.get(f"/analytics/{short_code}")

    assert analytics.status_code == 200

    analytics_data = json.loads(analytics.data)

    assert analytics_data["shortCode"] == short_code