def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char
    removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        # if <something>
        # <do something>
        if not msg[index] == char:

            copy += msg[index]
        index += 1

    return copy


word: str = "yoyo"

print(remove_chars(msg=word, char="y"))

print(remove_chars(word, "o"))
