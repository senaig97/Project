import pytest
from app.models import User, transactions, Transaction


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
    assert b'Log In' in response.data


def test_auth_homepage(client):
    client.post('/login',
                data=dict(username='testificate', password='password'),
                follow_redirects=True)
    response = client.get('/home')
    assert response.status_code == 200

    assert b'Log Out' in response.data


def test_get_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data


def test_get_survey(client):
    response = client.get('/survey')
    assert response.status_code == 200
    assert b'Site Survey' in response.data


def test_get_evensplit(client):
    response = client.get('/evensplit')
    assert response.status_code == 200
    assert b'Total Cost' in response.data
    assert b'Number of People' in response.data


def test_nonauth_block(client):
    response = client.get('/editCredentials', follow_redirects=True)
    assert b'Login' in response.data


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


def test_history(client, db):
    transactions.append(Transaction('100', '5', '20', 'tester', 'test comment'))
    response = client.get('/history')
    assert b'tester' in response.data
