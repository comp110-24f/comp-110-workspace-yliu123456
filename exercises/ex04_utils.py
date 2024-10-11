"""EX04 - creating list utility functions"""

__author__: str = "730749982"


def all(vals: list[int], num: int) -> bool:
    if len(vals) == 0:
        return False
    for x in vals:  # runs through list values
        if x != num:
            return (
                False  # returns false if list value doesnt equal the number or if empty
            )
    return True


def max(vals: list[int]) -> int:
    max: int = vals[0]  # sets the initial max value to the first value in the lext
    for x in vals:  # runs through list values
        if x > max:
            max = (
                x  # sets max to the value at the list index if larger than previous max
            )
    return max


def is_equal(vals: list[int], vals2: list[int]) -> bool:
    if len(vals) != len(vals2):
        return False
    for idx in range(0, len(vals)):  # runs through list values
        if vals[idx] != vals2[idx]:
            return (
                False  # returns false if list values not same at same index or length
            )
    return True


def extend(vals: list[int], vals2: list[int]) -> None:
    for y in vals2:  # runs through list
        vals.append(y)  # adds second list values to first list
