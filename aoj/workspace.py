import sys
import math
input = sys.stdin.readline
import itertools


def solve(i, last):
    res = 0
    print(i)
    while len(last) > 7:
        print(last[0:7])
        if sum(last[0:7]) > 5:
            break
        else:
            res += 7
            last = last[7:]

    if len(last) == 1:
        if last[0] == 1:
            res += 0
        # else:
        #     res += 1
    elif len(last) > 7:
        pass
    else:
        if sum(last) == len(last):
            res += 0
        else:
            res += len(last)
    for j in reversed(last):
        if j == 0:
            res -= 1
    return res - i

def main():
    N  = int(input().rstrip())
    days = list(map(int, input().rstrip().split()))
    candidates = [(i, [0] * i + days) for i in range(7)]
    print(max(map(lambda candidate: solve(*candidate), candidates)))

if __name__ == "__main__":
    main()

# / / / / 1 1 1
# 1 0 1 1 0 1 1
# 1 / / / / / /



# 1 1 1 0 1 1 1 0 1 1 0

11
1 1 1 0 1 1 1 0 1 1 0
-> 10

/ / / / / / 1
1 1 0 1 1 1 0
1 1 0 _ _ _ _
