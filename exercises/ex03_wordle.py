"""EX03 - Creating Wordle."""

__author__: str = "730749982"

# assigns values of emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(num_characters: int) -> str:

    word: str = input(f"Enter a {num_characters} character word: ")
    # asks the user to input a guess

    while len(word) != num_characters:
        # asks user to reinput word with correct num of characters

        word = input(f"That wasn't {num_characters} chars! Try Again: ")

    return word


def contains_char(word: str, character: str) -> bool:
    """Checks to see if the guess contains a character also part of the correct word"""
    assert len(character) == 1
    i: int = 0

    while i < len(word):
        # searches through the letters of the guess word
        if word[i] == character:
            # returns true if the guess word contains the character
            return True
        i += 1

    return False
    # returns false if the guess word does not contain the character


def emojified(guess: str, secret_word: str) -> str:
    """adds colored boxes based on the letter/letter position in the word"""
    assert len(guess) == len(secret_word)
    emoji_string: str = ""
    # creates empty string to add the colored boxes to
    i: int = 0
    while i < len(guess):

        if guess[i] == secret_word[i]:
            # adds green box to the string if letter in the secret word/correct position

            emoji_string += GREEN_BOX

        elif contains_char(secret_word, guess[i]):
            emoji_string += YELLOW_BOX
            # adds yellow box to string if letter in secret word/not correct position

        else:
            emoji_string += WHITE_BOX
            # adds white box to the string if letter isnt in the secret word
        i += 1

    return emoji_string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    n: int = 1

    while n <= 6:
        boxes: str = emojified(input_guess(len(secret)), secret)
        # assigns the string of boxes to the variable
        print(f"=== Turn {n}/6 ===")
        print(boxes)

        if boxes == GREEN_BOX * len(secret):
            print(f"You won in {n}/6 turns!")
            return None
            # if the word is correct with all green boxes it tells the user they won
        n += 1
        # turn number increases if the user's guess is wrong and they can try again

    print("X/6 - Sorry, try again tomorrow!")
    # user ran out of attempts


if __name__ == "__main__":
    main(secret="codes")
