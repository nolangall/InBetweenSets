"""SQLite storage for workout sets.

Only the table setup and two basic queries exist so far; the full logger
is planned for Weeks 3-4.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime

from models import Exercise, WorkoutSet

DEFAULT_DB_PATH = "inbetween_sets.db"


def connect(path: str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """Open the database and make sure the tables exist."""
    conn = sqlite3.connect(path)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS workout_sets (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise     TEXT    NOT NULL,
            muscle_group TEXT    NOT NULL,
            weight       REAL    NOT NULL,
            reps         INTEGER NOT NULL,
            logged_at    TEXT    NOT NULL
        )
        """
    )
    conn.commit()
    return conn


def save_set(conn: sqlite3.Connection, workout_set: WorkoutSet) -> int:
    """Insert one set and return its new row id."""
    cur = conn.execute(
        "INSERT INTO workout_sets (exercise, muscle_group, weight, reps, logged_at) "
        "VALUES (?, ?, ?, ?, ?)",
        (
            workout_set.exercise.name,
            workout_set.exercise.muscle_group,
            workout_set.weight,
            workout_set.reps,
            workout_set.logged_at.isoformat(),
        ),
    )
    conn.commit()
    return cur.lastrowid


def get_sets(conn: sqlite3.Connection, exercise_name: str) -> list[WorkoutSet]:
    """Return every logged set for one exercise, oldest first."""
    rows = conn.execute(
        "SELECT exercise, muscle_group, weight, reps, logged_at FROM workout_sets "
        "WHERE exercise = ? ORDER BY logged_at",
        (exercise_name,),
    ).fetchall()
    return [
        WorkoutSet(Exercise(name, group), weight, reps, datetime.fromisoformat(ts))
        for name, group, weight, reps, ts in rows
    ]
