import math
import queue
import sys
from typing import List

input = sys.stdin.readline

class Point:
    def __init__(self, x, y):
        
        
    


def solve():
    pass

def main():
    ok = 0
    N = int(input().rstrip())
    for idx in range(N):
        t, e, m, s, j, g = input().rstrip().split()
        e, m, s, j, g = map(int, [e, m, s, j, g])
        if t == "s":
            if s_solve(e, m, s, j, g):
                ok += 1
        else:
            if l_solve(e, m, s, j, g):
                ok += 1

    print(ok)


if __name__ == '__main__':
    main()
