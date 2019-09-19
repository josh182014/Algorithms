import sys


def rock_paper_scissors(n):
    if n > 0:
        for i in range(n):
            helper(n)
            rock_paper_scissors(n - 1)


def helper(a):
    possible = [['rock'], ['paper'], ['scissors']]

    possible.append(possible[a])
    print(possible)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
