import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline

import re

def main():
    N, X = map(int, input().rstrip().split())
    for _ in range(N):
        x = X
        a = int(input().rstrip())
        for _ in range(a - 1):
            x = int(x / 2)
        if x % 2 == 1:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    main()
