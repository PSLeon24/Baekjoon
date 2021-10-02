hours, minutes = map(int, input().split())
adds = int(input())

'''
14:30
50을 더하면
15:20
'''
hours += adds // 60
minutes += adds % 60

if minutes >= 60:
    hours += 1
    minutes -= 60
if hours >= 24:
    hours -= 24

print(hours, minutes, end=' ')
