import sys
# from collections import deque
input = sys.stdin.readline 
n = int(input())
queue = []
# queue = deque()

def check(command):
    if command.startswith("push"):
        _, value = command.split()
        queue.append(value)
    elif command == "pop":
        if queue:
            print(queue[0])
            del queue[0]
        else :
            print(-1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if queue:
            print(0)
        else :
            print(1)
    elif command == "front":
        if queue:
            print(queue[0])
        else :
            print(-1)
    elif command == "back":
        if queue:
            print(queue[len(queue)-1])
        else :
            print(-1)


for _ in range(n):
    command = input().strip()
    check(command)
