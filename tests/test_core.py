import subprocess
import sys


def test_revan_core_runs():
    result = subprocess.run(
        [sys.executable, "core/revan_core.py"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0