import pytest
from app.models import User


@pytest.fixture(scope='module')
def test_add_user_to_db(db):
    user1 = User(username='john', password='test')
    db.session.add(user1)
    db.session.commit()
    assert len(User.query.all()) == 1


def test_get_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data
