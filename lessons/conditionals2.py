"""Practice with conditionals"""

# def check_first_letter(word: str, letter: str) -> str:
# """Tell me if the first character of the word is  letter"""

# if word[0] == letter:
# return "match"

# else:
# return "no match"


# print(check_first_letter(word="happy", letter="h"))


def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    else:
        price: int = 10
    return price
