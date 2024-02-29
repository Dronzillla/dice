def draw_dice(number: int) -> str:
    # Define building blocks of dices
    border = "+-------+"
    blank = "|       |"
    one_middle = "|   *   |"
    one_left = "| *     |"
    one_right = "|     * |"
    two_left_right = "| *   * |"

    # Define dices as strings as at them to a tuple
    one = "\n".join([border, blank, one_middle, blank, border])
    two = "\n".join([border, one_right, blank, one_left, border])
    three = "\n".join([border, one_right, one_middle, one_left, border])
    four = "\n".join([border, two_left_right, blank, two_left_right, border])
    five = "\n".join([border, two_left_right, one_middle, two_left_right, border])
    six = "\n".join([border, two_left_right, two_left_right, two_left_right, border])
    dices = (one, two, three, four, five, six)

    return dices[number - 1]


def main():
    print(draw_dice(2))


if __name__ == "__main__":
    main()
