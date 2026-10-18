import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import db  # noqa: E402
from models import Exercise, WorkoutSet  # noqa: E402

BENCH = Exercise("Bench Press", "chest")


def test_volume_is_weight_times_reps():
    assert WorkoutSet(BENCH, weight=135, reps=10).volume == 1350


def test_negative_weight_is_rejected():
    with pytest.raises(ValueError):
        WorkoutSet(BENCH, weight=-5, reps=10)


def test_zero_reps_is_rejected():
    with pytest.raises(ValueError):
        WorkoutSet(BENCH, weight=135, reps=0)


def test_saved_set_can_be_read_back():
    conn = db.connect(":memory:")
    db.save_set(conn, WorkoutSet(BENCH, weight=185, reps=5))
    sets = db.get_sets(conn, "Bench Press")
    assert len(sets) == 1
    assert sets[0].weight == 185
    assert sets[0].reps == 5
    assert sets[0].exercise == BENCH
