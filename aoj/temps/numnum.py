import sys
input = sys.stdin.readline


def main():
    P_1, P_2, P_3, num = map(int, input().rstrip().split())
    res = [1]
    for i in range(num):
        temp = res[i]
        res = res + [temp * P_1, temp * P_2, temp * P_3]
        res = sorted(set(res))
    print(res[num - 1])

if __name__ == "__main__":
    main()
