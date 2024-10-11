"""practice with conditonials"""


def less_than_10(num: int) -> bool:
    """Tell me if num<10"""

    if num < 10:
        print("Small  number!")

    else:
        print("Big number1")
    print("Have a nice day")


def should_i_eat(hungry: bool) -> None:
    """ "Tells me whether or not to eat based on hunger"""
    if hungry:  # conditional boolean expression
        print("Eat some food silly goose!")  # "then" block
    else:
        print("Do your COMP 110 homework instead")
    print("I'm proud of you <3")


print(less_than_10(num=2))
