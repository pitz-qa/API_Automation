from .mathFunc import employeeDB
import pytest

@pytest.fixture(scope='module')
def db():
    print('----------setup----------------')
    db = employeeDB()
    db.connect('data.json')
    yield db
    print('----------teardown----------------')
    db.close()

def test_piyush_data(db):
    piyush_data = db.get_data('Piyush')
    assert piyush_data['id'] == 1
    assert piyush_data['name'] == 'Piyush'
    assert piyush_data['position'] == 'SQA'

def test_ravindra_data(db):
    ravindra_data = db.get_data('Ravindra')
    assert ravindra_data['id'] == 2
    assert ravindra_data['name'] == 'Ravindra'
    assert ravindra_data['position'] == 'DevOps'