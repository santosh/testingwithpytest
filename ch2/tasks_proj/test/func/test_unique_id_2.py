import pytest
import tasks

@pytest.mark.skip(reason='misunderstood the API')
def test__unique_id_1():
    """Calling unique_id() twice should return different numbers."""

    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

def test__unique_id_2():
    """unique_id() should return an unused it."""

    ids = []
    ids.append(tasks.add(tasks.Task('one')))
    ids.append(tasks.add(tasks.Task('two')))
    ids.append(tasks.add(tasks.Task('three')))
    
    # grab a unique id
    uid = tasks.unique_id()
    # make sure it isn't in the list of existing ids
    assert uid not in ids

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""

    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()
