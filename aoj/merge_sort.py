import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline


def merge(left, right):
    result = []
    compare = 0
    while len(left) > 0 and len(right) > 0:
        compare += 1
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    if len(left) < 1:
        compare += len(right)
        result += right
    elif len(right) < 1:
        compare += len(left)
        result += left
    return result, compare

def merge_sort(A):
    if len(A) < 2:
        return A, 0
    else:
        mid = int(len(A) / 2)
        left, c1 = merge_sort(A[mid:])
        right, c2 = merge_sort(A[:mid])
        Aa, c = merge(left, right)
        return Aa, c1 + c2 + c


def main():
    n = int(input())
    S = list(map(int, input().split()))
    Ss, count =  merge_sort(S)
    print(" ".join (list(map(str, Ss))))
    print(count)

if __name__ == '__main__':
    main()
