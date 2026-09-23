"""Validation for new tasks."""
from .models import VALID_PRIORITIES


class ValidationError(Exception):
    """Raised when a task fails validation."""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


def validate_new_task(title, priority):
    """Validate a new task's fields.

    Returns:
        A dict with ``title`` and ``priority``.
    Raises:
        ValidationError: if the input is invalid.
    """
    if not title:
        raise ValidationError("title is required")

    if priority not in VALID_PRIORITIES:
        raise ValidationError(
            "priority must be one of " + ", ".join(VALID_PRIORITIES)
        )

    return {"title": title, "priority": priority}
