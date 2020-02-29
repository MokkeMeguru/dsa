import sys
input = sys.stdin.readline


S = int(input())
second = S % 60
hour = int(S / (60 * 60))
minute = int(S / 60) - (hour * 60)
print("{}:{}:{}".format(hour, minute, second))
