import sys
import math
input = sys.stdin.readline

def check(cameras, place):
    for i, camera in enumerate(cameras):
        if (place[0] - camera[0]) ** 2 + (place[1] - camera[1]) ** 2 <= camera[-1] ** 2:
            rad = math.atan2(place[1] - camera[1], place[0] - camera[0]) * 180 / math.pi
            circle_start = camera[2] - (camera[3] / 2)
            circle_end = camera[2] + (camera[3] / 2)
            if rad < 0:
                rad += 360
            if circle_start <= 0:
                if circle_start + 360 <= rad and rad <= 360 or rad <= circle_end:
                    return True
            elif 360 <= circle_end:
                if circle_start <= rad and rad <= 360 or rad <= circle_end - 360:
                    return True
            elif circle_start <= rad and rad <= circle_end:
                return True
    return False

def main():
    H, W, M, N = map(int, input().rstrip().split())
    cameras = []
    for _ in range(M):
        cameras.append(list(map(int, input().rstrip().split())))
    for _ in range(N):
        print("yes" if check(cameras, list(map(int, input().rstrip().split()))) else "no")


if __name__ == "__main__":
    main()
