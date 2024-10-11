""""practice with lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float]  # constructor
my_numbers.append(5.0)
# my_name: str = ""


game_points: list[int] = [102, 86, 94]
print(game_points)

print(game_points[2])
game_points[1] = 72

len(game_points)

game_points.pop(1)


def display(list: list[int]) -> None:
    i: int = 0
    while i < len(list):
        print(list[i])
        i += 1


display(game_points)
