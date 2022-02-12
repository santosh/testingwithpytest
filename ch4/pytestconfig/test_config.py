import pytest

def test__option(pytestconfig):
    print('"foo" set to:', pytestconfig.getoption('foo'))
    print('"myopt" set to:', pytestconfig.getoption('myopt'))


@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo

@pytest.fixture()
def myopt(pytestconfig):
    return pytestconfig.option.myopt

def test__fixtures_for_options(foo, myopt):
    print('"foo" set to:', foo)
    print('"myopt" set to:', myopt)
    
def test__pytestconfig(pytestconfig):
    print('args:', pytestconfig.args)
    print('inifile:', pytestconfig.inifile)
    print('invocation_dir:', pytestconfig.invocation_dir)
    print('rootdir:', pytestconfig.rootdir)
    print('-k EXPRESSION:', pytestconfig.getoption('keyword'))
    print('-v,--verbose:', pytestconfig.getoption('verbose'))
    print('-q,--quiet:', pytestconfig.getoption('quiet'))
    print('-l,--showlocals:', pytestconfig.getoption('showlocals'))
    print('--tb=style:', pytestconfig.getoption('tbstyle'))
