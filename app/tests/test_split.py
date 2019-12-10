import pytest
from app.models import User


@pytest.fixture(scope='module')
def test_evensplit(client):
    client.get('/register', follow_redirects=True)
    client.register('foo fighter', 'Foo', 'Foo', 'foofighter@foo.com')
    response = client.post('/even', data=dict(cost = 20, people = 4, comment='testing'), follow_redirects=True)
    assert b'5.0' in response.data

def test_history(client):
    client.get('/register', follow_redirects=True)
    client.register('foo fighter', 'Foo', 'Foo', 'foofighter@foo.com')
    client.post('/even', data=dict(cost=50, people=2, comment='comment'))
    response = client.get('/history')
    assert b'foo fighter' in response.data
    assert b'50.0' in response.data
    assert b'2.0' in response.data
    assert b'25.0' in response.data
    assert b'comment' in response.data