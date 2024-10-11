"""Practice with while loops"""

__author__ = "7370749982"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    i: int = 0
    while i < len(phrase):
        if phrase[i] == search_char:
            count += 1
        i += 1
    return count
