import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline

def main():
    a, b, c = map(int, input().rstrip().split())
    N = int(input().rstrip())
    latest = 8 * 60 + 59
    min_train_at_gino = latest - c
    min_train_at_paiza = min_train_at_gino - b
    prev_t = 0
    for _ in range(N):
        h, m = map(int, input().rstrip().split())
        t = h * 60 + m
        if t > min_train_at_paiza:
            break
        else:
            prev_t = t
    min_go_home = prev_t - a
    h = int(min_go_home / 60)
    m = min_go_home % 60
    print("{:02d}:{:02d}".format(h, m))


if __name__ == '__main__':
    main()

    # memo
    # python format
    # "{:02d}:{:02d}".format(h, m)
    # -------------------------------
    # print('sign: {: 06}'.format(100))
    # print('sign: {: 06}'.format(-100))
    # sign:  00100
    # sign: -00100
    # -------------------------------
    # print('sign: {:_>6}'.format(100))
    # print('sign: {:_>6}'.format(-100))
    # sign: ___100
    # sign: __-100
    # print('{:,}'.format(100000000))
    # 100,000,000
    # print('{:_}'.format(100000000))
    # 100_000_000
    # --------------------------------------
    # print('bin: {:08b}'.format(255))
    # print('oct: {:08o}'.format(255))
    # print('dec: {:08d}'.format(255))
    # print('hex: {:08x}'.format(255))
    # print('HEX: {:08X}'.format(255))
    # bin: 11111111
    # oct: 00000377
    # dec: 00000255
    # hex: 000000ff
    # HEX: 000000FF
    # https://note.nkmk.me/python-format-zero-hex/
