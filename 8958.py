t = int(input())

score = 0
cnt = 1
result = []
for _ in range(t):
    o_x = input()
    o_x = list(o_x)
    for i in range(len(o_x)):
        if o_x[i] == 'O':
            score += cnt
            cnt += 1
        elif o_x[i] == 'X':
            cnt = 1
    result.append(score)
    score = 0
    cnt = 1

for i in result:
    print(i)
