from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

def describe_color(color):
    match color:
        case Color.RED:
            print("Color is red")
        case Color.GREEN:
            print("Color is green")
        case Color.BLUE:
            print("Color is blue")
        case _:
            print("Unknown color")

# Пример использования
describe_color(Color.RED)
describe_color(Color.GREEN)
describe_color(Color.BLUE)

# А что если передать что-то другое?
describe_color("RED")  # попадёт в case _
