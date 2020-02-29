import sys
input = sys.stdin.readline

def print_vec(vec):
    print(" ".join(map(str, vec)))

N = int(input())
A = list(map(int, input().split()))
for i in range (len (A)):
    key = A [i]
    j = i - 1
    while j >= 0 and A [j] > key:
        A [j + 1] = A [j]
        j -= 1
    A [j + 1] = key
    print_vec(A)
