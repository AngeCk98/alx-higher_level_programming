#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    x = len(argv) - 1
    if x == 0:
        print("0 arguments.")
        if x == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(x))

        for i in range(x):
            print("{:d}: {:s}".format(i + 1, argv[i + 1]))
