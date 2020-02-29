import sys
import math
input = sys.stdin.readline

def get_max(vec: list) -> int:
    reference = vec[0]
    diffs = -1 * 1e+9
    for x in vec[1:]:
        _diffs = reference - x
        if diffs < _diffs:
            diffs = _diffs
        if reference < x:
            reference = x
    return diffs

if __name__ == "__main__":
    n = int(input())
    res = 0
    vec = []
    for _ in range(n):
        vec.append(int(input()))
    print(get_max(list(reversed(vec))))
