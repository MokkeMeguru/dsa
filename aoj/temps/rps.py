import sys
input = sys.stdin.readline

def main():
    rock = 0
    paper = 0
    scissors = 0
    N, M = map(int, input().rstrip().split())
    hands = input().rstrip()
    for hand in hands:
        if hand == "G":
            rock += 1
        elif hand == "P":
            paper += 1
        elif hand == "C":
            scissors += 1
        else:
            raise NotImplementedError()
    max_win = 0
    c = 0
    for p in range(M // 5 + 1):
        for c in range(N - p + 1):
            if 5 * p + 2 * c == M:
                max_win = max(
                    max_win,
                    min(p, rock) + min(c, paper) + min(N - p - c, scissors))
    print(max_win)

if __name__ == "__main__":
    main()
