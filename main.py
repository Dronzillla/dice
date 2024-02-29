from random import shuffle


def draw_dice() -> list:
    # Define building blocks of dices
    border = "+-------+"
    blank = "|       |"
    one_middle = "|   *   |"
    one_left = "| *     |"
    one_right = "|     * |"
    two_left_right = "| *   * |"

    # Make dices and at them to a list of dices
    one = (border, blank, one_middle, blank, border)
    two = (border, one_right, blank, one_left, border)
    three = (border, one_right, one_middle, one_left, border)
    four = (border, two_left_right, blank, two_left_right, border)
    five = (border, two_left_right, one_middle, two_left_right, border)
    six = (border, two_left_right, two_left_right, two_left_right, border)
    dices = [one, two, three, four, five, six]

    return dices


def draw_dices(number: int) -> None:
    # Get dices and shuffle the list
    dice_list = draw_dice()
    shuffle(dice_list)

    # Delete number of dices we dont need
    for _ in range(6 - number):
        dice_list.pop()

    # Create lines for printing required amount of dices
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

    # Print dices
    row_len = len(first_line)
    print("RESULT".center(row_len, "~"))
    print(first_line)
    print(second_line)
    print(third_line)
    print(fourth_line)
    print(fifth_line)


def dices_rolled():
    # Loop until user writes an integer, which is between 1 and 6
    while True:
        try:
            number = int(input("How many dice do you want to roll? [1 - 6]: "))
            # Check if number is between 1 and 6
            if number < 1 or number > 6:
                print("Error. Pick a number between 1 - 6. ")
                continue
        except ValueError:
            print("Error. Enter an integer.")
            continue
        return number


def main():
    # Get number of dices to draw
    no_dices = dices_rolled()
    # Draw dices
    draw_dices(no_dices)


if __name__ == "__main__":
    main()
