import sys
input = sys.stdin.readline
from collections import deque
import heapq
from pprint import pprint
import copy

def solve(K, S, acc, C):
    # end place
    if K == 0:
        return [S]
    elif K > S[acc + C:].count('o'):
        return []
    result = []
    for i in range(acc + C, len(S)):
        if S[i] == 'o':
            temp = copy.copy(S)
            temp[i] = 'c'
            result += solve(K - 1, temp, i, C)
    return result


def main():
    N, K, C = map(int, input().rstrip().split())
    S = input()
    S = S.replace('x', ' ').rstrip().replace(' ', 'x')
    if len(S.replace('x', '')) < K:
        return
    S = list(S)
    first = 0 - C
    res = solve(K, ['x'] + S, first, C)
    # pprint(res)
    result = [0 for _ in range(N + 1)]
    for r in res:
        for i, x in enumerate(r):
            if x == 'c':
                result[i] += 1
    for idx, r in enumerate(result):
        if r == len(res):
            print(idx)


if __name__ == "__main__":
    main()
