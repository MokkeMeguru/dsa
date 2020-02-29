import sys
N = int(input())
while (N > 0):
    N -= 1
    years = sys.stdin.read().splitlines()
    for year in years:
        year = int(year)
        if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
            print('{} is a leap year'.format(year))
        else:
            print('{} is not a leap year'.format(year))
