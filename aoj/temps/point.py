import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline


def main():
    N, M =  map(int, input().rstrip().split())
    fs = []
    for m in range(M):
        fs.append(int(input().rstrip()))
    point = 0
    for f in fs:
        if point >= f:
            point -= f
        else:
            N -= f
            point += int(f * 0.1)
        print("{} {}".format(N, point))


if __name__ == '__main__':
    main()
