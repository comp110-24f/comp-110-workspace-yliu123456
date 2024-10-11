"""creates coordinates"""

__author__: str = "730749982"


def get_coords(xs: str, ys: str) -> None:

    i1: int = 0
    while i1 < len(xs):
        i2: int = 0
        while i2 < len(ys):
            print(f"({xs[i1]}, {ys[i2]})")
            i2 += 1
        i1 += 1


get_coords("hello", "hello")
