''' # Runtime error
a, b, n = map(int, input().split())

lst = list(str(a/b))
del lst[1]
print(lst[n])
'''

'''
a, b, n = map(int, input().split())
a /= b
# 25 // 7 = 3
# 25 % 7 = 4
#print(a, int(a*100000))
result = a
result = int(result * (10 ** n))
result = list(str(result))
print(result[-1])

#Overflow
'''

a, b, n = map(int, input().split())
a %= b
for i in range(n-1):
    a = (a*10) % b

print((a*10) // b)
