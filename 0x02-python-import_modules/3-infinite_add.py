#!/usr/bin/python3

if __name__ == "__main__":
    import math
    from sys import argv

    num_list = [int(i) for i in argv[1:]]
    print(sum(num_list))
