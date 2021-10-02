a, b, c = map(int, input().split())
# Remind
'''
c*i = a + b*i
(c-b)*i = a
i = a / (c-b)
'''
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)


# 1000 70 170
# 1.
# expense = 1000 + 70
# income = 170
# 2.
# expense = 1070 70
# income = 170 + 170
'''
i = 1
while True:
    if b >= c:
        print(-1)
        break
    income = c * i
    expense += b*i
    if income > expense:
        print(i)
        break
    else:
        i += 1
'''
