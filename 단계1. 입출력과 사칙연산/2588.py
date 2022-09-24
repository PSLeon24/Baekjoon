a = int(input())
b = int(input())

hundreds = b // 100
tens = b % 100 // 10
ones = b % 10

print(a*ones)
print(a*tens)
print(a*hundreds)
print(a*b)
