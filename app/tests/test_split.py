import pytest
from app.models import User, transactions, Transaction

@pytest.fixture(scope='module')
def test_evensplit(client, db):
    response = client.post('/evensplit', data=dict(cost = 20, people = 4, comment='testing'))
    assert b'$5.0' in response.data

