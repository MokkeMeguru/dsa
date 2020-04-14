
import sys
input = sys.stdin.readline

def swap(A, B):
    temp = A
    A = B
    B = temp
    return A, B

def main():
    X, Y, Z = map(int, input().rstrip().split())
    A = X
    B = Y
    C = Z
    A, B = swap(A, B)
    A, C = swap(A, C)
    print(" ".join(map(str, [A, B, C])))


if __name__ == "__main__":
    main()
