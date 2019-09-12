#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):

    count = 0

    if n < 1:
        count = 0
        return count

    if n == 1:
        count = 1
        return count

    if n == 2:
        count = 2
        return count

    if n == 3:
        count = 4
        return count

    if n > 3:
        count = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        return count


if __name__ == "__main__":
    if len(sys.argv) >= 0:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
