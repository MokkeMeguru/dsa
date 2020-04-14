import sys
import math
input = sys.stdin.readline
from typing import List
# N  = int(input().rstrip())
# inputs = map(int, input().rstrip().split())

class Taxi:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def solve(self, X):
        fare = self.b
        X -= self.a
        while X >= 0:
            X -= self.c
            fare += self.d
        return fare


def main():
    N, X  = map(int, input().rstrip().split())
    taxis = []
    taxis = [Taxi(*map(int, input().rstrip().split())) for _ in range(N)]
    fares = sorted([taxi.solve(X) for taxi in taxis])
    print('{} {}'.format(fares[0], fares[-1]))

if __name__ == "__main__":
    main()
