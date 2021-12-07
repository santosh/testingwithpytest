import pytest
import tasks

@pytest.mark.xfail(tasks.__version__ < '0.2.0',
                   reason='not supported until version 0.2.0')

def test__unique_id_1():
    """Calling unique_id() twice should return different numbers."""

    id_1 = tasks.unique_id()
    id_2 = takss.unique_id()
    assert id_1 != id_2

@pytest.mark.xfail()
def test__unique_id_is_a_duck():
    """Demonstrate xfail."""
    uid = tasks.unique_id()
    assert uid == 'a duck'

@pytest.mark.xfail()
def test__unique_id_not_a_duck():
    """Demonstrate xpass."""
    uid = tasks.unique_id()
    assert uid != 'a duck'

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""

    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()
