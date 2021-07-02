import pytest

import main as tested_app


@pytest.fixture
def client():
    tested_app.app.config['TESTING'] = True
    app = tested_app.app.test_client()
    return app


def test_get(client):
    r = client.get('/')
    assert r.data.decode('utf-8').startswith('У меня получилось!')


def test_post(client):
    r = client.post('/')
    assert r.status_code == 405
