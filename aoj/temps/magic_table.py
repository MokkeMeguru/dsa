import sys
import math
input = sys.stdin.readline
from typing import List
# N  = int(input().rstrip())
# inputs = map(int, input().rstrip().split())

def print_table(table: List[List[int]]):
    for row in table:
        print(' '.join(map(str, row)))

def solve_table(N, table, axis, row_sum):
    for i in range(N):
        for j in range(N):
            if table[i][j] == 0:
                if axis == 0:
                    table[i][j] = row_sum - sum(table[i])
                else:
                    table[i][j] = row_sum - sum([table[k][j] for k in range(N)])
    return table

def main():
    N  = int(input().rstrip())
    row_sum = sum([i + 1 for i in range(N * N)]) // N
    table = [list(map(int, input().rstrip().split())) for _ in range(N)]
    axis = 0
    for row in table:
        temp = 0
        for e in row:
            if e == 0:
                temp += 1
        if temp == 2:
            axis = 1
            break
    table = solve_table(N, table, axis, row_sum)
    print_table(table)

if __name__ == "__main__":
    main()
