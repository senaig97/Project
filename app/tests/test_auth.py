import pytest
from app.models import User


@pytest.fixture(scope='module')
def test_add_user_to_db(db):
    user = User(username='john', email='john@john.com')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()
    assert len(User.query.all()) == 2


def test_nonauth_homepage(client):
    response = client.get('/home')
    assert response.status_code == 200
    assert b'<a href="http://127.0.0.1:5000/login">Log In</a>' in response.data


def test_auth_homepage(client):
    response = client.post('/register', data=dict(username='testificate', password='password',
                                                  confirmPassword='password', email='testificate@hmm.com'),
                           follow_redirects=True)
    assert response.status_code == 200

    # client.get('/register', follow_redirects=True)
    # client.register('testificate', 'password', 'password', 'testificate@hmm.com')

    response = client.post('/login', data=dict(username='testificate', password='password'), follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/home')
    assert response.status_code == 200
    assert b'<a href="http://127.0.0.1:5000/logout">Log Out</a>' in response.data


def test_get_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data


def test_valid_register(client, db):
    response = client.post('/register',
                           data=dict(username='testing', email='testing@testing.com', password='testing',
                                     confirmpassword='testing'),
                           follow_redirects=True)
    assert response.status_code == 200
    assert b"Username" in response.data
    assert b'Password' in response.data


def test_change_password(client, db):
    # client.get('/register', follow_redirects=True)
    client.post('/login', data=dict(username='testificate', password='password'), follow_redirects=True)
    response = client.post('/editCredentials', data=dict(password='Fighter', confirmPassword='Fighter'),
                           follow_redirects=True)
    assert response.status_code == 200
    assert b'Password' in response.data
    # self.assertIn(b'Password has been updated!', response.data)
