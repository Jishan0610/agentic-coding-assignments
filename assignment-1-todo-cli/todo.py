"""My To-Do List -- a small, colorful command-line to-do list app.

Examples:
    python todo.py list
    python todo.py list --priority high
    python todo.py add "Read the codebase" --priority high
    python todo.py done 1
    python todo.py delete 2
"""
import argparse
import sys

from todolist import commands
from todolist.models import VALID_PRIORITIES
from todolist.store import TaskStore


def build_parser():
    parser = argparse.ArgumentParser(
        description="A colorful command-line to-do list."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="show all tasks")
    p_list.add_argument(
        "--priority", choices=VALID_PRIORITIES, help="filter by priority"
    )

    p_add = sub.add_parser("add", help="add a new task")
    p_add.add_argument("title", help="the task title")
    p_add.add_argument(
        "--priority", choices=VALID_PRIORITIES, default="medium"
    )

    p_done = sub.add_parser("done", help="mark a task as done")
    p_done.add_argument("id", type=int)

    p_delete = sub.add_parser("delete", help="delete a task")
    p_delete.add_argument("id", type=int)

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    store = TaskStore()

    if args.command == "list":
        return commands.cmd_list(store, priority=args.priority)
    if args.command == "add":
        return commands.cmd_add(store, args.title, args.priority)
    if args.command == "done":
        return commands.cmd_done(store, args.id)
    if args.command == "delete":
        return commands.cmd_delete(store, args.id)
    return 0


if __name__ == "__main__":
    sys.exit(main())
