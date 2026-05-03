from enum import StrEnum


class Status(StrEnum):
    """Status of a task."""

    QUEUED = "queued"
    WAITING = "waiting"
    SLEEPING = "sleeping"
    RUNNING = "running"
    CANCELLED = "cancelled"
    FAILED = "failed"
    COMPLETED = "completed"
