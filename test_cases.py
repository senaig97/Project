import pytest
from app.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User('foo fighter', 'foo')
    return user

def test_new_user(new_user):
    assert new_user.username == 'foo fighter'
    assert new_user.password_hash != 'foo'
    assert not new_user.authenticated
