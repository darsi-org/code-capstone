from pathlib import Path

from marks.core import load

ROOT = Path(__file__).resolve().parents[1]


def test_load_reads_every_row():
    assert len(load(ROOT / "sample.csv")) == 30
