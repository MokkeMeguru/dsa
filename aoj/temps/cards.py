import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline

import re

def main():
    N = int(input().rstrip())
    for _ in range(N):
        hands = list(map(int, input().rstrip()))
        candidate = len(list(set(hands)))
        if candidate == 4:
            print("No Pair")
        elif candidate == 3:
            print("One Pair")
        elif candidate == 2:
            x = list(set(hands))[0]
            c = 0
            for i in hands:
                if x == i:
                    c += 1
            if c == 1 or c == 3:
                print("Three Card")
            else:
                print("Two Pair")
        else:
            print("Four Card")


if __name__ == '__main__':
    main()
