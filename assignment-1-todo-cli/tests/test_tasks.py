"""Smoke tests for the To-Do List.

These cover the happy path only. Part of the assignment is discovering
what they *don't* cover. Run with:  pytest
"""
import pytest

from todolist.store import TaskStore
from todolist.validation import ValidationError, validate_new_task


@pytest.fixture
def store(tmp_path):
    # Each test gets its own fresh, seeded data file.
    return TaskStore(path=str(tmp_path / "todos.json"))


def test_seeds_five_tasks(store):
    assert len(store.list()) == 5


def test_add_task(store):
    task = store.add("New task", "high")
    assert task.id == 6
    assert store.get(6).title == "New task"
    assert len(store.list()) == 6


def test_mark_done(store):
    store.update(1, {"done": True})
    assert store.get(1).done is True


def test_delete(store):
    assert store.delete(2) is True
    assert store.get(2) is None


def test_delete_missing_returns_false(store):
    assert store.delete(999) is False


def test_persistence_across_runs(tmp_path):
    path = str(tmp_path / "todos.json")
    first = TaskStore(path=path)
    first.add("Persisted task", "low")
    # A brand-new store pointed at the same file should see the task.
    second = TaskStore(path=path)
    assert any(t.title == "Persisted task" for t in second.list())


def test_validation_requires_title():
    with pytest.raises(ValidationError):
        validate_new_task("", "medium")


def test_validation_rejects_bad_priority():
    with pytest.raises(ValidationError):
        validate_new_task("ok", "urgent")
