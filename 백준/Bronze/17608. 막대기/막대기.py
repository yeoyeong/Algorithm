import sys
input = sys.stdin.readline

n = int(input())
sticks = [int(input().strip()) for _ in range(n)]

def compareHeights():
    cnt = 0
    current = 0
    for stick in reversed(sticks):
        if stick > current:
            cnt += 1
            current = stick
    return cnt


result = compareHeights()
print(result)