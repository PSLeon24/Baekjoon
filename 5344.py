def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


try:
    while True:
        a, b = map(int, input().split())
        print(gcd(factorial(a), b))
except EOFError:
    exit()
