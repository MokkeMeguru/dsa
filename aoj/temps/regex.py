import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline

import re

def main():
    pattern = '[a-z]'
    repattern = re.compile(pattern)
    result = lambda x: repattern.match(x)
    S =  str(input().rstrip())
    for token in S:
        if result(token) is not None:
            print(token.upper(), end="")
    print()

if __name__ == '__main__':
    main()

    # memo
    # match 先頭
    # search contain
    # fullmatch 全体一致
    # ref: https://note.nkmk.me/python-re-match-search-findall-etc/
