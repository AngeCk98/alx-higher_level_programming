#!/usr/bin/python3
"""
A function hat finds a peakin a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds peak integer
    """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
