"""Creating a tea party"""

__author__: str = "730749982"


def main_planner(guests: int) -> None:
    """Creates a variable for the number of guests at the tea party"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # needed to put string before function call for it to work
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Creates a variable for the number of people at the tea party"""
    return people * 2  # adds 2 teacups per person to the total tea needed
    # I thought I needed to create a new variable at first but realized I didn't need to


def treats(people: int) -> int:
    """Creates a variable for the number of people at the tea party"""

    return int(
        (tea_bags(people=people)) * 1.5
    )  # had issues at first with calling function and getting integer form
    # I was able to properly change float to integer to suffice tea_bags


def cost(tea_count: int, treat_count: int) -> float:
    """Creates a variable for the amount of tea and treats needed for the tea party"""
    return (
        tea_count * 0.5 + treat_count * 0.75
    )  # wasn't sure if I should add parentheses but this sufficed


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
