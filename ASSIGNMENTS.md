# Assignment: Understand, Extend, Verify (~1–2 hours)

You'll work in this unfamiliar Python repo using your agentic coding tool
(Cursor or Claude Code). This is a short, fun exercise — don't over-engineer it.

> **Golden rule:** Read every line the AI writes. You own the code, not the AI.

First, get it running and commit a baseline so you can roll back:

```bash
pip install -r requirements.txt
pytest                       # should be 8 passing
python todo.py list          # see the colorful to-do list
git init && git add -A && git commit -m "baseline"
```

---

## Part 1 — Understand (~20 min)

Use the agent to explain the repo: what happens when you run
`python todo.py list`, how a command travels from `todo.py` into the
`todolist/` package, and where items are saved.

**Deliverable:** a **3-sentence summary in your own words** (don't paste the
agent's answer).

## Part 2 — Add a `search` command (~40 min)

Use your tool's **plan mode** to plan it, then build it with the agent:

> Add a new command so that
> `python todo.py search docs`
> prints only the items whose title contains the text `docs`
> (case-insensitive), using the same colorful table as `list`.

Try it out and confirm it works. Bonus if you feel fast: also add a `stats`
command that shows how many items exist per priority.

**Deliverable:** the working `search` command (committed).

## Part 3 — Verify (~15 min)

The agent (and existing code) can produce things that *look* right but aren't.
Do a quick check:

1. Try adding an item whose title is only spaces:
   ```bash
   python todo.py add "   "
   python todo.py list
   ```
   Did it create a blank item? Should it have?
2. Try your new search with text that isn't in any title, and with an empty
   search. Does it behave the way you'd expect?

Pick **one** issue you found and fix it.

**Deliverable:** 2–3 sentences on what you found, plus your fix (committed).

---

## What to submit
Push your branch and open a pull request containing:
- your 3-sentence repo summary (put it in the PR description)
- the `search` command
- the one fix from Part 3 + your short note

## What you're graded on
- Did you understand the repo **before** changing it?
- Did you use plan mode / the agent effectively?
- Did you actually **read and check** the output instead of blindly accepting it?

That's it — keep it tight and have fun with it.
