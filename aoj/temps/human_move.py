import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline


def human_move(Ms: List[int]):
    speech_man = int(input())
    temp = 0
    for i in range(len(Ms)):
        if i == speech_man:
            pass
        if Ms[i] > 0:
             Ms[i] -= 1
             temp += 1
    Ms[speech_man] += temp


def main():
    M, N, K = map(int, input().split())
    Ms = []
    Ms.append(N)
    for i in range(M):
        Ms.append(0)
    for i in range(K):
        human_move(Ms)
    m = 0
    for human in Ms[1:]:
        if m < human:
            m = human
    for idx, human in enumerate(Ms[1:]):
        if m == human:
            print(idx + 1)

if __name__ == '__main__':
    main()
