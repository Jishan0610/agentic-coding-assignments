"""Storage for to-do items, backed by a small JSON file on disk.

Because each ``python todo.py ...`` run is a separate process, items are
saved to a file (``todos.json`` by default) so they persist between commands.
The file is created and seeded with sample items the first time you run it.
"""
import json
import os

from .models import Task

DEFAULT_DB = "todos.json"


class TaskStore:
    def __init__(self, path=DEFAULT_DB, seed_if_missing=True):
        self.path = path
        if os.path.exists(self.path):
            self._load()
        else:
            self._tasks = {}
            self._next_id = 1
            if seed_if_missing:
                self._seed()
            self._save()

    def _seed(self):
        samples = [
            ("Write onboarding doc", "high", False),
            ("Reply to emails", "low", True),
            ("Plan sprint", "medium", False),
            ("Fix flaky test", "high", False),
            ("Water the plants", "low", False),
        ]
        for title, priority, done in samples:
            task = self.add(title, priority, _save=False)
            task.done = done

    def _load(self):
        with open(self.path) as f:
            data = json.load(f)
        self._tasks = {t["id"]: Task.from_dict(t) for t in data["tasks"]}
        self._next_id = data["next_id"]

    def _save(self):
        data = {
            "next_id": self._next_id,
            "tasks": [t.to_dict() for t in self._tasks.values()],
        }
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def list(self):
        return list(self._tasks.values())

    def get(self, task_id):
        return self._tasks.get(task_id)

    def add(self, title, priority="medium", _save=True):
        task = Task(id=self._next_id, title=title, priority=priority)
        self._tasks[task.id] = task
        self._next_id += 1
        if _save:
            self._save()
        return task

    def update(self, task_id, changes):
        task = self._tasks.get(task_id)
        if task is None:
            return None
        for key in ("title", "priority", "done"):
            if key in changes:
                setattr(task, key, changes[key])
        self._save()
        return task

    def delete(self, task_id):
        existed = self._tasks.pop(task_id, None) is not None
        if existed:
            self._save()
        return existed
