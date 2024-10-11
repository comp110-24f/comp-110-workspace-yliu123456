"""Summing the elements of a list using different loops"""

__author__: str = "730749982"


def w_sum(vals: list[float]) -> float:
    i: int = 0
    sum: float = 0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0
    for x in vals:
        sum += x
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum
