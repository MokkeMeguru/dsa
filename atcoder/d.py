import sys
input = sys.stdin.readline
from collections import deque
import heapq

def solve(K: int):
    first = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    heapq.heapify(first)
    res = 1
    while K > 0:
        res = heapq.heappop(first)
        if res % 10 != 0:
            heapq.heappush(first, res * 10 + res % 10 - 1)
        heapq.heappush(first, res * 10 + res % 10)
        if res % 10 != 9:
            heapq.heappush(first, res * 10 + res % 10 + 1)
        K -= 1
    return res


def main():
    K = int(input().rstrip())
    res = solve(K)
    print(res)


if __name__ == "__main__":
    main()
