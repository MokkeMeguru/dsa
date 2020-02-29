import sys
import math
input = sys.stdin.readline

# def prime_table(m: int) -> list:
#     prime = [False] * (m + 1)
#     prime[0] = False
#     prime[1] = False
#     for i in range(2, (m + 1)):
#         if prime[i]:
#             continue
#         for j in range(i, (m + 1)):
#             if i * j > m:
#                 break
#             prime[i * j] = True
#     return prime

n = int(input())
def is_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    res = 0
    for i in range(n):
        if is_prime(int(input())):
            res += 1
    print(res)
