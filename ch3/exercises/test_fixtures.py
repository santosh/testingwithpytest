import pytest


@pytest.fixture(scope='module')
def list_of_names():
    print('setup')
    l_names = ['Santosh', 'Roushan', 'Shiwanshu']
    yield l_names
    print('\nteardown')

def test__a_in_names(list_of_names):
    for name in list_of_names:
        assert 'a' in name

def test__s_in_names(list_of_names):
    for name in list_of_names:
        assert 's' in name
