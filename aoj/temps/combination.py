import sys
import math
input = sys.stdin.readline
import itertools


def search(candidate, N, K):
    prev_0 = 0
    prev_1 = 0
    diff = N
    for i in range(N):
        if (prev_0 > candidate[i]
            or prev_1 > candidate[i + N]
            or diff > K):
            return 0
        diff += abs(candidate[i] - candidate[i + N]) - 1
        prev_0 = candidate[i]
        prev_1 = candidate[i + N]
    if diff > K:
        return 0
    return 1


def main():
    N, K  = map(int, input().rstrip().split())
    result = 0

    if N > K:
        print(0)
        return

    candidates = itertools.combinations(range(1, 2 * N + 1), N)
    for candidate in candidates:
        c = set(range(1, 2 * N + 1)) - set(candidate)
        result += search(list(c) + list(candidate), N, K)
    print(result)



if __name__ == "__main__":
    main()
