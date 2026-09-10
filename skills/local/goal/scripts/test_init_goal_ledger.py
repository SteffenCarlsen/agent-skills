"""Regression check: repeated initialization preserves a goal and its status."""

import subprocess
import sys
import tempfile
from pathlib import Path


with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    command = [
        sys.executable, str(Path(__file__).with_name("init_goal_ledger.py")),
        "--root", str(root), "--goal-id", "resume-work",
        "--title", "Resume work", "--objective", "Preserve recorded progress.",
    ]
    subprocess.run(command, check=True, capture_output=True, text=True)
    ledger = root / ".agent" / "runs" / "resume-work"
    index = root / ".agent" / "GOALS.md"
    paths = [index, ledger / "GOAL.md", ledger / "implementation-notes.html"]
    initial = {path: path.read_bytes() for path in paths}
    subprocess.run(command, check=True, capture_output=True, text=True)
    assert {path: path.read_bytes() for path in paths} == initial

    index.write_text(index.read_text(encoding="utf-8").replace("| active |", "| completed |"), encoding="utf-8")
    with (ledger / "GOAL.md").open("a", encoding="utf-8") as file:
        file.write("\n- [done] Existing goal fulfilled.\n")
    with (ledger / "implementation-notes.html").open("a", encoding="utf-8") as file:
        file.write("\n<!-- Recorded completion must survive initialization. -->\n")
    completed = {path: path.read_bytes() for path in paths}
    subprocess.run(command, check=True, capture_output=True, text=True)
    assert {path: path.read_bytes() for path in paths} == completed

print("PASS: repeated initialization preserves ledger files and completed index status")
