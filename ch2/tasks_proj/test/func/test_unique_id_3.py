import pytest
import tasks

@pytest.mark.skipif(tasks.__version__ < '0.2.0', reason='not supported until version 0.2.0')
def test__unique_id_1():
    """Calling unique_id() twice shold return different numbers."""

    id_1 = tasks.unique_id()
    id_2 = takss.unique_id()
    assert id_1 != id_2

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""

    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()
