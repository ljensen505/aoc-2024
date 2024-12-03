from pathlib import Path

TESTING = False


def read_lines() -> list[str]:
    filename = "sample.txt" if TESTING else "input.txt"
    lines = []
    with open(Path(__file__).parent / filename, "rt") as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines
