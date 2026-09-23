# My To-Do List

A small, **colorful command-line to-do list app** written in Python. Your items
are saved to a local `todos.json` file, so they stick around between commands.

> You have probably never seen this codebase before. That's the point.
> Use your agentic coding tool (Cursor / Claude Code) to **understand it first**,
> then do the exercise in [`ASSIGNMENTS.md`](./ASSIGNMENTS.md).
>
> New to this? Start with [`GETTING_STARTED.md`](./GETTING_STARTED.md).

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Use it

```bash
python todo.py list                              # show your to-do list
python todo.py list --priority high              # only high-priority items
python todo.py add "Read the codebase" --priority high
python todo.py done 1                            # check off item #1
python todo.py delete 2                          # remove item #2
```

The first time you run it, the list is seeded with a few sample items.

## Run the tests

```bash
pytest
```

## Project layout

```
todo.py                # command-line entry point (argparse)
todolist/
  __init__.py
  models.py            # the Task dataclass (one to-do item)
  store.py             # saves/loads items to todos.json
  validation.py        # checks a new item's fields
  commands.py          # what each command does
  display.py           # the colorful table + progress bar (uses `rich`)
tests/                 # smoke tests (happy path only)
```
