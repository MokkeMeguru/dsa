import sys
input = sys.stdin.readline

def main():
    H, W, N = map(int, input().rstrip().split())
    table = []
    for i in range(H):
        table.append([0 for w in range(W)])
    for _ in range(N):
        h, w, x = map(int, input().rstrip().split())
        min_h = 0
        for _h in range(H - 1, -1, -1):
            if sum([table[_h][x + j] for j in range(w)])== 0:
                min_h = _h
            else:
                break
        for i in range(h):
            for j in range(w):
                table[min_h + i][x + j] = 1
    for row in reversed(table):
        for i in row:
            if i == 0:
                print(".", end="")
            else:
                print("#", end="")
        print()


if __name__ == "__main__":
    main()
