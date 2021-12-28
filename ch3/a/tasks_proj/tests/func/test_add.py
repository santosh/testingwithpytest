import pytest
import tasks
from tasks import Task


def test__add_returns_valid_id(tasks_db):
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized tasks db
    # WHEN a new taks is added
    # THEN returned taks_ids of type int
    new_task = Task("do something")
    task_id = tasks.add(new_task)

    assert isinstance(task_id, int)

def test__add_increase_count(db_with_3_tasks):
    """Test tasks.add() affect on tasks.count()."""
    # GIVEN a db with 3 tasbs
    # WHEN another taks is added
    tasks.add(Task('throw a party'))

    # THEN the count increases by 1
    assert tasks.count() == 4
