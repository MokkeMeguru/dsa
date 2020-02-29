import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

flag = True
if a < b and b < c:
    print("Yes")
else:
    print("No")
