# Getting Started

A quick primer so you don't lose time on setup. If anything here is unfamiliar,
ask your agent (Cursor / Claude Code) to explain it — that's part of the point.

## 1. What is this?

**My To-Do List** is a small Python program you run in the **terminal**. You
type commands like `python todo.py list` and it prints a colorful table of
your to-do items. There is no website and no server — it's just a Python script.

## 2. Set up and run

```bash
# from the project folder
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt

pytest                            # expect: 8 passed
python todo.py list               # see the colorful to-do list
```

## 3. The commands

```bash
python todo.py list                                  # show all items
python todo.py list --priority high                  # filter by priority
python todo.py add "Water the plants" --priority low # add an item
python todo.py done 1                                 # mark item #1 done
python todo.py delete 2                               # delete item #2
python todo.py --help                                 # see all commands
```

Your items are saved in a file called `todos.json` in the project folder, so
they're still there next time you run a command. Delete that file to start
fresh with the sample items.

## 4. Git: get the code and submit your work

**Get the code (fork + clone):**
1. Click **Fork** on the GitHub repo page to make your own copy.
2. Clone *your fork* and enter it:
   ```bash
   git clone <your-fork-url>
   cd <repo-name>
   ```

**Do the work on a branch:**
```bash
git checkout -b my-solution
# ...make your changes...
git add -A
git commit -m "Add search command and fix blank-title bug"
git push -u origin my-solution
```

**Submit (open a Pull Request):**
- Go to your fork on GitHub → it will offer to **"Compare & pull request"**.
- Open the PR and paste your short repo summary + your notes into the
  description.

See [`ASSIGNMENTS.md`](./ASSIGNMENTS.md) for the tasks.

## 5. Stuck?
- Reset your files back to the start: `git checkout -- .`
- Start the to-do data over: delete `todos.json`.
- Ask the agent: *"Explain how `python todo.py list` works in this repo, step
  by step."*
