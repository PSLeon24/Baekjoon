a, b = input().split()
a = int(a, 2)
b = int(b, 2)
#print(a, b)
result = str(bin(a+b))
result = list(result)
del result[0]
del result[0]
for i in result:
    print(i, end='')

#print('%b' % result)
