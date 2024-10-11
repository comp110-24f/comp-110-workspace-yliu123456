"""Mutating functions."""

__author__: str = "730749982"


def manual_append(number: int, a: list[int]) -> None:
    a.append(number)


def double(b: list[int]) -> None:
    i: int = 0
    while i < len(b):
        b[i] *= 2
        i += 1


list_1: list[int] = [1, 2, 3]

list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
