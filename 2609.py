'''
from math import gcd, lcm

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))
'''


def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def lcm(num1, num2):
    return num1 * num2 // gcd(num1, num2)


a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))
