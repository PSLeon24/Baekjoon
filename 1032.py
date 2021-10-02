t = int(input())
command = list(input())
# print(command)
for _ in range(t-1):
    prompt = list(input())
    for i in range(len(command)):
        if command[i] != prompt[i]:
            command[i] = '?'

for j in command:
    print(j, end='')
