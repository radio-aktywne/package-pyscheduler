from typing import TypedDict

from pyscheduler.models import types as t


class Specification(TypedDict):
    """Generic specification for type-based implementation."""

    type: str
    parameters: dict[str, t.JSON]


class Task(TypedDict):
    """Core task data."""

    operation: Specification
    condition: Specification
    dependencies: dict[str, str]


class QueuedTask(TypedDict):
    """Data of a queued task."""

    task: Task
    enqueued: str


class WaitingTask(TypedDict):
    """Data of a waiting task."""

    task: Task
    enqueued: str
    dequeued: str


class SleepingTask(TypedDict):
    """Data of a sleeping task."""

    task: Task
    enqueued: str
    dequeued: str | None
    slept: str


class RunningTask(TypedDict):
    """Data of a running task."""

    task: Task
    enqueued: str
    dequeued: str
    started: str


class CancelledTask(TypedDict):
    """Data of a cancelled task."""

    task: Task
    enqueued: str
    dequeued: str
    started: str | None
    cancelled: str


class FailedTask(TypedDict):
    """Data of a failed task."""

    task: Task
    enqueued: str
    dequeued: str
    started: str | None
    failed: str
    error: str


class CompletedTask(TypedDict):
    """Data of a completed task."""

    task: Task
    enqueued: str
    dequeued: str
    started: str
    completed: str
    result: t.JSON


class Tasks(TypedDict):
    """Tasks data organized by status."""

    queued: dict[str, QueuedTask]
    waiting: dict[str, WaitingTask]
    sleeping: dict[str, SleepingTask]
    running: dict[str, RunningTask]
    cancelled: dict[str, CancelledTask]
    failed: dict[str, FailedTask]
    completed: dict[str, CompletedTask]


class Relationships(TypedDict):
    """Relationships between tasks."""

    dependents: dict[str, list[str]]
    dependencies: dict[str, list[str]]


class State(TypedDict):
    """State of the scheduler."""

    tasks: Tasks
    statuses: dict[str, t.Status]
    relationships: Relationships
