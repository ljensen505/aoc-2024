from pathlib import Path


def read_lines(day: str, testing=True):
    lines = []
    filename = "sample.txt" if testing else "input.txt"
    txt_file = Path(day).parent / "input" / day.split("/")[-1] / filename

    with open(txt_file, "rt") as f:
        for line in f.readlines():
            lines.append(line.strip())

    return lines
