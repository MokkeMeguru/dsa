import sys
import math
import copy
from typing import Tuple, List
input = sys.stdin.readline

expressions = ["+", "-", "*"]
def calc_reverse_polish(formula: List) -> int:
    stack = []
    for icon in formula:
        if icon in expressions:
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(str(eval(v1 + icon + v2)))
        else:
            stack.append(icon)
    return stack

if __name__ == "__main__":
    A = input().split()
    stack = calc_reverse_polish(A)
    print(stack[0])
