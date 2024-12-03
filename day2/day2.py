from pathlib import Path

TESTING = False

SAFE = range(1, 4)


def read_lines() -> list[str]:
    filename = "sample.txt" if TESTING else "input.txt"
    lines = []
    with open(Path(__file__).parent / filename, "rt") as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines


def is_safe(level: list[int]) -> bool:
    is_increasing = level[0] < level[1]

    for idx in range(len(level) - 1):
        curr, _next = level[idx], level[idx + 1]
        diff = curr - _next

        if diff == 0:
            return False
        elif is_increasing and (diff * -1) not in SAFE:
            return False
        elif not is_increasing and diff not in SAFE:
            return False

    return True


def part_1(levels: list[list[int]]):
    safe_count = 0
    for level in levels:
        if is_safe(level):
            safe_count += 1

    print("Part 1:", safe_count)


def is_extra_safe(level: list[int]) -> bool:
    for idx in range(len(level)):
        level_copy = list(level)
        level_copy.pop(idx)

        if is_safe(level_copy):
            return True

    return False


def part_2(levels: list[list[int]]):
    safe_count = 0
    for level in levels:
        if is_safe(level) or is_extra_safe(level):
            safe_count += 1

    print("Part 2:", safe_count)


def day2():
    lines: list[str] = read_lines()
    levels: list[list[int]] = []
    for level in lines:
        level = [int(c) for c in level.split(" ")]
        levels.append(level)

    part_1(levels)
    part_2(levels)


day2()
