import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip().split())
    As = list(map(int, input().rstrip().split()))
    Q  = int(input().rstrip())
    for _ in range(Q):
        s, e = map(int, input().rstrip().split())
        while sum(As[s-1:e]) / (e - s + 1) < M:
            for i in range(s-1, e):
                As[i] += 1
    print(" ".join(map(str, As)))



if __name__ == '__main__':
    main()
