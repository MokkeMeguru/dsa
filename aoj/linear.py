import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline


def main():
    n = int(input())
    S = tuple(map(int,input().split()))
    q = int(input())
    T = tuple(map(int,input().split()))
    res = 0
    for t in T:
        for s in S:
            if s == t:
                res += 1
                break
    return res


if __name__ == '__main__':
    print(main())
