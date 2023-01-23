#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
        count = 0
        for i in range(0, x):
                try:
                    if isinstance(i, int):
                            print("{:d}".format(my_list[i]), end=""
                            count = count + 1
                except (TypeError, ValueError):
                    pass
                except IndexError:
                    raise
        print()
        return count
