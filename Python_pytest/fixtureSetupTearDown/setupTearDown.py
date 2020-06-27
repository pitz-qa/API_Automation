#from .mathFunc import employee
from .mathFunc import employeeDB
import pytest
db=None
def setup_module(module):
    print('@@@@@@@@@@@@@SETUP@@@@@@@@@@@@@@@@')
    global db
    db = employeeDB()
    db.connect('data.json')

def teardown_module(module):
    print('$$$$$$$$$$$$$$$TEARDOWN$$$$$$$$$$$$$')
    db.close()

def test_piyush_data():
    piyush_data = db.get_data('Piyush')
    assert piyush_data['id'] == 1
    assert piyush_data['name'] == 'Piyush'
    assert piyush_data['position'] == 'SQA'

def test_ravindra_data():
    ravindra_data = db.get_data('Ravindra')
    assert ravindra_data['id'] == 2
    assert ravindra_data['name'] == 'Ravindra'
    assert ravindra_data['position'] == 'DevOps'