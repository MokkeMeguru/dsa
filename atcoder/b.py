import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip().split())
    As = list(map(int, input().rstrip().split()))
    bound = sum(As) / (4 * M)
    res = 0
    for a in As:
        if a >= bound:
            res += 1
    if res >= M:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
