import sys
input = sys.stdin.readline

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, x=0, y=0):
        self.x += x
        self.y += y
        return self
    def out(self, o):
        return not (0 <= self.x
                    and self.x <= o.x
                    and 0 <= self.y
                    and self.y <= o.y)

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

def walk(table, _to, _from, direct, acc):
    if _from.out(_to):
        print(acc)
    else:
        if table[_from.y][_from.x] == "_":
            if direct == ">":
                walk(table, _to, _from.move(x = 1), direct, acc + 1)
            elif direct == "<":
                walk(table, _to, _from.move(x = -1), direct, acc + 1)
            elif direct == "^":
                walk(table, _to, _from.move(y = -1), direct, acc + 1)
            elif direct == "v":
                walk(table, _to, _from.move(y = 1), direct, acc + 1)
            else:
                raise Exception()
        elif table[_from.y][_from.x] == "/":
            if direct == ">":
                walk(table, _to, _from.move(y = -1), "^", acc + 1)
            elif direct == "<":
                walk(table, _to, _from.move(y = 1), "v", acc + 1)
            elif direct == "^":
                walk(table, _to, _from.move(x = 1), ">", acc + 1)
            elif direct == "v":
                walk(table, _to, _from.move(x = -1), "<", acc + 1)
            else:
                raise Exception()
        elif table[_from.y][_from.x] == "\\":
            if direct == ">":
                walk(table, _to, _from.move(y = 1), "v", acc + 1)
            elif direct == "<":
                walk(table, _to, _from.move(y = -1), "^", acc + 1)
            elif direct == "^":
                walk(table, _to, _from.move(x = -1), "<", acc + 1)
            elif direct == "v":
                walk(table, _to, _from.move(x = 1), ">", acc + 1)
            else:
                raise Exception()

def main():
    H, W = map(int, input().rstrip().split())
    table = []
    
    for i in range(H):
        table.append(input().rstrip())

    walk(table, Position(W - 1, H - 1), Position(0, 0), ">", 0)

if __name__ == "__main__":
    main()
