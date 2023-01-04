#!/usr/bin/python3


def print_last_digit(number):

    number = str(number)
    last_digit = int(number[-1])
    number = int(number)
    if number < 0:
        last_digit = last_digit
    else:
        last_digit = abs(last_digit)
    print("{}".format(last_digit), end="")
    return last_digit
