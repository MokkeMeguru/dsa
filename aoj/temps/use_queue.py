import sys
from queue import Queue
input = sys.stdin.readline


def solve(table, N, M):
    def draw(i, j, li):
        places = Queue()
        places.put([i, j])
        while not places.empty():
            place = places.get()
            if table[place[0]][place[1]] == 1:
                table[place[0]][place[1]] = li
                places.put([place[0] + 1, place[1]])
                places.put([place[0] - 1, place[1]])
                places.put([place[0], place[1] + 1])
                places.put([place[0], place[1] - 1])

    land_idx = 2
    for i in range(M):
        for j in range(N):
            if (table[i][j] == 1):
                land_idx += 1
                draw(i, j, land_idx)

    return land_idx - 2


def main():
    N, M = map(int, input().rstrip().split())
    table = []
    table.append([0] * (N + 2))
    for _ in range(M):
        table.append([0] + list(map(int, input().rstrip().split())) + [0])
    table.append([0] * (N + 2))
    print(solve(table, N + 2, M + 2))

if __name__ == "__main__":
    main()
