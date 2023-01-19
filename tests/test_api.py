from pytest import fixture

from app import app


@fixture
def client():
    return app.test_client()


def test_api_posts(client):
    resp = client.get("/api/alldata/")
    assert resp.status_code == 200
    assert isinstance(resp.json, list)
    assert len(resp.json) > 0


def test_api_post(client):
    resp = client.get("/api/data/1")
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    assert len(resp.json) > 0