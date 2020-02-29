import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline


def binary_search(t, S):
    left = 0
    right = len (S)
    while left < right:
        mid = int ((left + right) / 2)
        if S [mid] == t:
            return True
        elif t < S[mid]:
            right = mid
        else:
            left = mid + 1
    return False


def main():
    n = int(input())
    S = tuple(map(int, input().split()))
    q = int(input())
    T = tuple(map(int, input().split()))
    return [binary_search(t, S) for t in T]



if __name__ == '__main__':
    print(sum(main()))
