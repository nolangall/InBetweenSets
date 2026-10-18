"""Data models for InBetween Sets.

Uses dataclasses and type hints, two of the Python features this project
is meant to practice.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class Exercise:
    """An exercise the user can log, e.g. Bench Press (chest)."""

    name: str
    muscle_group: str


@dataclass
class WorkoutSet:
    """One logged set: an exercise, the weight lifted and the reps done."""

    exercise: Exercise
    weight: float  # pounds
    reps: int
    logged_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        if self.weight < 0:
            raise ValueError("weight cannot be negative")
        if self.reps <= 0:
            raise ValueError("reps must be at least 1")

    @property
    def volume(self) -> float:
        """Training volume for the set (weight x reps)."""
        return self.weight * self.reps
