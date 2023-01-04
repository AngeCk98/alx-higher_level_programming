#!/usr/bin/python3
def decToHexa(i):
    return hex(i)


for i in range(0, 99):
    print("{0} = {1}".format(i, decToHexa(i)))
