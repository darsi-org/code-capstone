"""Marks and attendance. Write the test first (tests/test_core.py), watch it fail, then make it pass."""
import csv


def load(path):
    """Read the CSV into a list of dicts. Milestone 2: report bad rows (blank ID, mark over 100) instead of crashing."""
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


# TODO milestone 2: averages(rows), at_risk(rows, days), clean_id(text)
