T = int(input())

for _ in range(T):
    cnt = 0
    lst = list(input())
    if len(lst) == 0:
        print('YES')
        break
    if lst.count('(') != lst.count(')'):
        print('NO')
    elif lst[0] == ')':
        print('NO')
    elif lst[-1] == '(':
        print('NO')
    else:
        for i in lst:
            if cnt < 0:
                print('NO')
                break
            elif i == '(':
                cnt += 1
            elif i == ')':
                cnt -= 1
        if cnt == 0:
            print('YES')