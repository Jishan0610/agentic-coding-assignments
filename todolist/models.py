"""Data model for a Task."""
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone

VALID_PRIORITIES = ("low", "medium", "high")


@dataclass
class Task:
    """A single task/to-do item."""

    id: int
    title: str
    priority: str = "medium"
    done: bool = False
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self):
        """Return a plain-dict version (used when saving to JSON)."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        """Rebuild a Task from a dict (used when loading from JSON)."""
        return cls(**data)
