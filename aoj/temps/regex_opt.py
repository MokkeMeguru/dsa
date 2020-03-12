import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline

import re

es = ("s", "sh", "ch", "o", "x")
remove_ves = ("f", "fe")


def main():
    N = int(input().rstrip())
    for _ in range(N):
        s = input().rstrip()
        if s.endswith(es):
            print(s + "es")
        elif s.endswith(remove_ves):
            if s.endswith("e"):
                s = s[:-1]
            print(s[:-1] + "ves")
        elif s[-1] == "y" and s[-2] not in ["a", "i", "u", "e", "o"]:
            print(s[:-1] + "ies")
        else:
            print(s + "s")

if __name__ == '__main__':
    main()
