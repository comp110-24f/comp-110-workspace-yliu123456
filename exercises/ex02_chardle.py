"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730749982"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    # asks user to input word which is stored in the variable word
    if len(word) == 5:
        return word
        # returns word if it is 5 characters long
    print("Error: Word must contain 5 characters.")
    exit()
    # exits program if word doesnt satisfy the 5 character requirement


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    # asks user to input a letter which is stored in the variable letter
    if len(letter) == 1:
        return letter
        # returns letter if it 1 character long
    print("Error: Character must be a single character.")
    exit()
    # exits program if letter doesnt satisfy the 1 character requirement


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    i: int = 0
    # creates index for the word
    count: int = 0
    # creates a counter for amount of specific letters in a word
    while i < len(word):

        if word[i] == letter:
            print(letter + " found " + "at index " + str(i))
            # prints where the specific letter is found in the word
            count += 1
            # adds one to count if the specific letter appears in the word
        i += 1
        # allows the program to go through each letter of the word

    if count == 0:
        print("No instances of " + letter + " found in " + word)
        # prints message if the specific letter isnt present in the word

    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)

    else:
        print(str(count) + " instances" + " of " + letter + " found in " + word)
        # prints the amount of times a specific letter is found in the word


def main() -> None:
    word: str = input_word()
    letter: str = input_letter()
    contains_char(word, letter)
    # calls function with embedded functions in one central area


if __name__ == "__main__":
    main()
