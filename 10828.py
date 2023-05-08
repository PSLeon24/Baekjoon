import sys
input = sys.stdin.readline

n = int(input())

command = [] # 명령어 저장
result = [] # 답 저장

for _ in range(n):
    command.append(input().split())

for i in range(len(command)):
    if command[i][0] == 'push':
        result.append(command[i][1])

    elif command[i][0] == 'pop':
            if len(result) == 0:
                print(-1)

            else:
                print(result.pop())

    elif command[i][0] == 'size':
        print(len(result))

    elif command[i][0] == 'empty':
        if len(result): # 1 이상일 때
            print(0)
        else:
            print(1)

    elif command[i][0] == 'top':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])