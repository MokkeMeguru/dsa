import sys
import math
input = sys.stdin.readline
import itertools
import copy

def play(orig, replace):
    result = [0] * len(orig)
    for idx, order in enumerate(replace):
        result[order - 1] = orig[idx]
    return result

def solve(_P, orig):
    if len(_P) == 0:
        return [orig]
    else:
        return solve(_P[1:], orig) + solve(_P[1:], play(orig, _P[0]))


def main():
    N = int(input().rstrip())
    S = list(map(int, input().rstrip().split()))
    M = int(input().rstrip())
    P = []
    for _ in range(M):
        P.append(list(map(int, input().rstrip().split())))
    Ps = itertools.permutations(P, len(P))
    candidates = []
    for _P in Ps:
        candidates += solve(_P, S)
    candidates = list(map(lambda x: ''.join(map(lambda i: str(i - 1),x)), candidates))
    print(' '.join(map(str, [int(x) + 1 for x in sorted(candidates)[0]])))

if __name__ == "__main__":
    main()
