import sys
import math
input = sys.stdin.readline

def search(pos, start, end):
    # assert (end - start + 1) % 3 == 0, "except {} {}".format(start, end)
    mid = (start + end) // 2
    # print(pos, start, mid, end)
    if pos == start: return "A"
    elif pos == end: return "C"
    elif pos == mid: return "B"
    elif pos < mid: return search(pos, start + 1, mid - 1)
    else: return search(pos, mid + 1, end - 1)

def main():
    K,S,T = map(int,input().split())
    end = 0
    for i in range(K):
        end += 3 * (2 ** i)

    for x in range(end):
        print(search(x, 0, end - 1), end="")
    print()

if __name__ == "__main__":
    main()
