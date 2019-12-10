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


def test_valid_register(client, db):
    response = client.post('/register',
                           data=dict(username='testing', email='testing@testing.com', password='testing',
                                     confirm='testing'),
                           follow_redirects=True)
    assert response.status_code == 200
    assert b"You are now logged in!" in response.data
    assert b'Hi !' in response.data
    assert b'Log out' in response.data


def test_change_password(client):
    client.get('/register', follow_redirects=True)
    client.register('foo fighter', 'Foo', 'Foo', 'foofighter@foo.com')
    response = client.post('/editCredentials', data=dict(password='Fighter'), follow_redirects=True)
    assert response.status_code == 200
    # self.assertIn(b'Password has been updated!', response.data)
    # self.assertIn(b'User Profile', response.data)


def test_authorized_links(client):
    response = client.post('/register',
                           data=dict(username='testificate', email='testificate@villager.com', password='testing',
                                     confirm='testing'),
                           follow_redirects=True)
    assert b'Log Out' in response.data
    assert b'Edit Credentials' in response.data
    assert b'Even Split' in response.data
    assert b'History' in response.data
