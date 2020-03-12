import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline

class Process:
    def __init__(self, name: str, value: Union[int, str]):
        self.name = name
        self.value = int(value)
    def takes(self, quontum:int) -> Tuple[int, bool]:
        if self.value > quontum:
            self.value -= quontum
            return (quontum, True)
        else:
            return (self.value, False)

    def __repr__(self):
        return "{}-{}".format(self.name, self.value)


if __name__ == "__main__":
    queue = []
    n, q = map(int , input().split())
    for i in range(n):
        queue.append(Process(*input().split()))
    time = 0
    j = 0
    while len(queue):
        process = queue.pop(0)
        val, rest = process.takes(q)
        time += val
        if rest:
            queue.append(process)
        else:
            print(process.name,time)
