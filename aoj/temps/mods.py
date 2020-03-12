import sys
from queue import Queue
input = sys.stdin.readline


def solve(mod7):
    total = 0
    for i in range(7):
        for j in range(7):
            for k in range(7):
                if (i + j + k) % 7 == 0:
                    resi =mod7[i]
                    resj =mod7[j]
                    resk =mod7[k]
                    if i == j: resi-=1
                    if j == k: resk-=1
                    if k == i: resk-=1
                    total += resi * resj * resk
    return total // (7 - 1)


def main():
    N = int(input().rstrip())
    mod7 = [0, 0, 0, 0, 0, 0, 0]
    for i in range(N):
        mod7[int(input().rstrip()) % 7] += 1
    print(solve(mod7))

if __name__ == "__main__":
    main()
