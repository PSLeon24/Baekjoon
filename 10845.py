from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    queue = deque([])
    for _ in range(n):
        command = input().split()
        if command[0] == 'push':
            queue.append(command[1])
        elif command[0] == 'pop':
            print(queue.popleft()) if len(queue) != 0 else print(-1)
        elif command[0] == 'size':
            print(len(queue)) # size
        elif command[0] == 'empty':
            print(0) if len(queue) != 0 else print(1) # empty
        elif command[0] == 'front':
            print(queue[0]) if len(queue) != 0 else print(-1)
        elif command[0] == 'back':
            print(queue[-1]) if len(queue) != 0 else print(-1)

    # queue.append(1)
    # print(queue)
    # queue.append(2)
    # print(queue)
    # print(queue[0]) # front
    # print(queue[-1]) # back
    # print(len(queue)) # size
    # print(0) if len(queue) != 0 else print(1) # empty
    # print(queue.popleft()) if len(queue) != 0 else print(-1) # pop - popleft
    # print(queue.popleft()) if len(queue) != 0 else print(-1) # pop - popleft
    # print(queue.popleft()) if len(queue) != 0 else print(-1) # pop - popleft
    # print(len(queue)) # size
    # print(0) if len(queue) != 0 else print(1) # empty
    # print(queue.popleft()) if len(queue) != 0 else print(-1) # pop - popleft
    # queue.append(3)
    # print(0) if len(queue) != 0 else print(1) # empty
    # print(queue[0]) # front