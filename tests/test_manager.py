import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task_manager.manager import TaskManager

def test_add_task():
    tm = TaskManager()
    task = tm.add_task("Buy milk")
    assert task["description"] == "Buy milk"
    assert task["done"] is False
    assert len(tm.list_tasks()) == 1

def test_delete_task():
    tm = TaskManager()
    tm.add_task("Task to delete")
    assert tm.delete_task(1) is True
    assert len(tm.list_tasks()) == 0

def test_mark_done():
    tm = TaskManager()
    tm.add_task("Task to complete")
    assert tm.mark_done(1) is True
    assert tm.list_tasks()[0]["done"] is True

def test_delete_nonexistent():
    tm = TaskManager()
    assert tm.delete_task(999) is False