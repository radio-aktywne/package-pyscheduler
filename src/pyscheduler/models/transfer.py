from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from pyscheduler.models.enums import Status
from pyscheduler.models.types import JSON


@dataclass(kw_only=True)
class Specification:
    """Generic specification for type-based implementation."""

    type: str
    parameters: dict[str, JSON]


@dataclass(kw_only=True)
class ScheduleRequest:
    """Request to schedule a task."""

    operation: Specification
    condition: Specification
    dependencies: dict[str, UUID]


@dataclass(kw_only=True)
class CancelRequest:
    """Request to cancel a task."""

    id: UUID


@dataclass(kw_only=True)
class CleanRequest:
    """Request to clean tasks."""

    strategy: Specification


@dataclass(kw_only=True)
class Task:
    """Core task data."""

    id: UUID
    operation: Specification
    condition: Specification
    dependencies: dict[str, UUID]


@dataclass(kw_only=True)
class TaskIndex:
    """Index of tasks by status."""

    queued: set[UUID]
    waiting: set[UUID]
    sleeping: set[UUID]
    running: set[UUID]
    cancelled: set[UUID]
    failed: set[UUID]
    completed: set[UUID]


@dataclass(kw_only=True)
class GenericTask:
    """Data of a task of any status."""

    task: Task
    status: Status


@dataclass(kw_only=True)
class QueuedTask:
    """Data of a queued task."""

    task: Task
    enqueued: datetime


@dataclass(kw_only=True)
class WaitingTask:
    """Data of a waiting task."""

    task: Task
    enqueued: datetime
    dequeued: datetime


@dataclass(kw_only=True)
class SleepingTask:
    """Data of a sleeping task."""

    task: Task
    enqueued: datetime
    dequeued: datetime | None
    slept: datetime


@dataclass(kw_only=True)
class RunningTask:
    """Data of a running task."""

    task: Task
    enqueued: datetime
    dequeued: datetime
    started: datetime


@dataclass(kw_only=True)
class CancelledTask:
    """Data of a cancelled task."""

    task: Task
    enqueued: datetime
    dequeued: datetime
    started: datetime | None
    cancelled: datetime


@dataclass(kw_only=True)
class FailedTask:
    """Data of a failed task."""

    task: Task
    enqueued: datetime
    dequeued: datetime
    started: datetime | None
    failed: datetime
    error: str


@dataclass(kw_only=True)
class CompletedTask:
    """Data of a completed task."""

    task: Task
    enqueued: datetime
    dequeued: datetime
    started: datetime
    completed: datetime
    result: JSON


FinishedTask = CancelledTask | FailedTask | CompletedTask


@dataclass(kw_only=True)
class CleaningResult:
    """Result of cleaning."""

    removed: set[UUID]
