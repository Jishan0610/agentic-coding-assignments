"""Pretty terminal output using the `rich` library."""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

PRIORITY_STYLE = {
    "high": "bold red",
    "medium": "yellow",
    "low": "green",
}


def render_tasks(tasks, heading="My To-Do List"):
    """Print the tasks as a colorful table plus a progress summary."""
    table = Table(title=heading, header_style="bold cyan", title_style="bold magenta")
    table.add_column("Done", justify="center", width=4)
    table.add_column("ID", justify="right", width=3)
    table.add_column("Priority", width=8)
    table.add_column("Title")

    for task in tasks:
        check = "[green]✔[/green]" if task.done else "[dim]○[/dim]"
        style = PRIORITY_STYLE.get(task.priority, "white")
        priority = f"[{style}]{task.priority}[/]"
        title = f"[strike dim]{task.title}[/]" if task.done else task.title
        table.add_row(check, str(task.id), priority, title)

    console.print(table)
    console.print(_progress_panel(tasks))


def _progress_panel(tasks):
    total = len(tasks)
    done = sum(1 for t in tasks if t.done)
    fraction = (done / total) if total else 0
    bar_len = 24
    filled = int(fraction * bar_len)
    bar = (
        "[green]" + "█" * filled + "[/green]"
        + "[dim]" + "░" * (bar_len - filled) + "[/dim]"
    )
    label = f"{bar}  {done}/{total} done ({fraction * 100:.0f}%)"
    return Panel(label, title="Progress", expand=False, border_style="cyan")


def info(message):
    console.print(f"[cyan]{message}[/cyan]")


def error(message):
    console.print(f"[bold red]Error:[/bold red] {message}")
