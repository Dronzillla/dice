from functools import wraps
from random import randint, shuffle


# Data validation to get integers as arguments
def positive_int(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check if arguments are of type int
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError
        for value in kwargs.values():
            if not isinstance(value, int):
                raise ValueError

        result = func(*args, **kwargs)
        return result

    return wrapper


def int_1_to_6(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check if areguments are between 1 and 6
        for arg in args:
            if arg < 0 or arg > 6:
                raise ValueError
        for value in kwargs.values():
            if value < 0 or arg > 6:
                raise ValueError

        result = func(*args, **kwargs)
        return result

    return wrapper


@int_1_to_6
def draw_dice() -> list:
    # Define building blocks of dices
    border = "+-------+"
    blank = "|       |"
    one_middle = "|   *   |"
    one_left = "| *     |"
    one_right = "|     * |"
    two_left_right = "| *   * |"

    # Define dices as strings as at them to a tuple
    # one = "\n".join([border, blank, one_middle, blank, border])
    # two = "\n".join([border, one_right, blank, one_left, border])
    # three = "\n".join([border, one_right, one_middle, one_left, border])
    # four = "\n".join([border, two_left_right, blank, two_left_right, border])
    # five = "\n".join([border, two_left_right, one_middle, two_left_right, border])
    # six = "\n".join([border, two_left_right, two_left_right, two_left_right, border])

    one = (border, blank, one_middle, blank, border)
    two = (border, one_right, blank, one_left, border)
    three = (border, one_right, one_middle, one_left, border)
    four = (border, two_left_right, blank, two_left_right, border)
    five = (border, two_left_right, one_middle, two_left_right, border)
    six = (border, two_left_right, two_left_right, two_left_right, border)
    dices = [one, two, three, four, five, six]

    return dices


def join_strings(*args):
    return " ".join(args)


def draw_dices(number: int) -> int:
    # Get dices and shuffle the list
    dice_list = draw_dice()
    shuffle(dice_list)

    # Delete number of dices we dont need
    for _ in range(6 - number):
        dice_list.pop()

    # Print random dices
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    fifth_line = ""
    for dice in dice_list:
        for i in range(len(dice)):
            if i == 0:
                first_line = first_line + " " + dice[i]
            elif i == 1:
                second_line = second_line + " " + dice[i]
            elif i == 2:
                third_line = third_line + " " + dice[i]
            elif i == 3:
                fourth_line = fourth_line + " " + dice[i]
            elif i == 4:
                fifth_line = fifth_line + " " + dice[i]

    print(first_line)
    print(second_line)
    print(third_line)
    print(fourth_line)
    print(fifth_line)

    # for dice in dice_list:
    #     print(dice)

    # print(dice_list[0])

    # for dice in map(join_strings, dice_list[0]):
    #     print(dice)


def dices_rolled():
    while True:
        try:
            user = int(input("How many dice do you want to roll? [1 - 6]"))
        except ValueError:
            print("Enter an integer")
        return user


def main():
    ...
    # dices_to_roll = dices_rolled()
    draw_dices(3)


if __name__ == "__main__":
    main()
