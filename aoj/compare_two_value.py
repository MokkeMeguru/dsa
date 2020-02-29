import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a == b")
