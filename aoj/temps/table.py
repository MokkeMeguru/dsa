import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline

def main():
    H, W = map(int, input().rstrip().split())
    a_1_1, a_1_2 = map(int, input().rstrip().split())
    a_2_1, a_2_2 = map(int, input().rstrip().split())
    A = []
    for i in range(H):
        A.append([0 for j in range(W)])
    A[0][0] = a_1_1
    A[0][1] = a_1_2
    A[1][0] = a_2_1
    A[1][1] = a_2_2
    for i in range(2):
        for j in range(2, W):
            A[i][j] = A[i][j - 1] + A[i][1] - A[i][0]
    for i in range(2, H):
        A[i][0] = A[i - 1][0] + A[1][0] - A[0][0]
        A[i][1] = A[i - 1][1] + A[1][1] - A[0][1]
        for j in range(2, W):
            A[i][j] = A[i - 1][j] + A[1][j] - A[0][j]
            # A[i][j] = A[i][j - 1] + A[i][1] - A[i][0]

    for i in range(H):
        print(' '.join(list(map(str, A[i]))))



if __name__ == '__main__':
    main()

# testcase
# 5 5
# 1 2
# 3 4
# answer
# 1 2 3 4 5
# 3 4 5 6 7
# 5 6 7 8 9
# 7 8 9 10 11
# 9 10 11 12 13
