import sys
import math
input = sys.stdin.readline
from typing import List
# N  = int(input().rstrip())
# inputs = map(int, input().rstrip().split())

class Frame:
    def __init__(self, balls, rest, b):
        self.b = b
        self.balls = balls
        if len(rest) == 0:
            self.solve_last (rest)
        else:
            self.solve (rest)
    def solve (self, rest):
        self.score = sum (self.balls)
        if len (self.balls) == 1:
            self.score += sum (rest [:2])
        elif self.score == self.b:
            self.score += sum (rest [:1])

    def solve_last (self, rest):
        self.score = sum (self.balls)
        if self.balls [0] == self.b:
            self.score += self.balls [1]
            self.score += self.balls [2]
            if self.balls [1] == self.b:
                self.score += self.balls [2]
            else:
                pass
        elif self.balls[0] + self.balls [1] == self.b:
            self.score += self.balls [2]
        else:
            pass
    def __repr__ (self):
        return ' '.join(list(map(str, self.balls)))


def main():
    a, b, n = map(int, input().rstrip().split())
    temp = [int(i) if i != 'G' else 0 for i in input().rstrip().split()]
    frames = []
    i = 0
    while i < n:
        a -= 1
        if a == 0:
            frames.append (Frame(temp [i:], [], b))
            break
        elif temp [i] == b:
            frames.append (Frame([temp [i]],temp [i+1:], b))
            i += 1
        else:
            frames.append(Frame (temp[i:i+2], temp [i+2:], b))
            i += 2
    # for frame in frames:
        # print(frame)
    print (sum ([frame.score for frame in frames]))
if  __name__ == "__main__":
    main()
