import sys
input = sys.stdin.readline

def solve(init: int, K: int, acc: int):
    while abs(init - K) < init:
        init = abs(init - K)
    return init

    # temp = abs(init - K)
    # if temp > acc:
    #     return init
    # else:
    #     return solve(temp, K, temp)



def main():
    N, K = map(int, input().rstrip().split())
    N -= K * (N  // K)
    res = solve(N, K, N)
    print(res)


if __name__ == "__main__":
    main()
