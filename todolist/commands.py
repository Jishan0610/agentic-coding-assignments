"""Command handlers. Each takes a store and prints the result."""
from . import display
from .validation import ValidationError, validate_new_task


def cmd_list(store, priority=None):
    tasks = store.list()
    if priority:
        tasks = [t for t in tasks if t.priority == priority]
    display.render_tasks(tasks)
    return 0


def cmd_add(store, title, priority):
    try:
        data = validate_new_task(title, priority)
    except ValidationError as exc:
        display.error(exc.message)
        return 1
    task = store.add(data["title"], data["priority"])
    display.info(f"Added task #{task.id}: {task.title}")
    return 0


def cmd_done(store, task_id):
    task = store.update(task_id, {"done": True})
    if task is None:
        display.error(f"no task with id {task_id}")
        return 1
    display.info(f"Marked #{task_id} as done ✔")
    return 0


def cmd_delete(store, task_id):
    if not store.delete(task_id):
        display.error(f"no task with id {task_id}")
        return 1
    display.info(f"Deleted #{task_id}")
    return 0
