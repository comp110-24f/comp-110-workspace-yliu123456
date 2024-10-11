"""CQ00 mimic exercise"""

_author_ = "730749982"


def mimic(message: str) -> str:
    """returns my input message back to me"""
    return message


def main() -> None:
    """print mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
