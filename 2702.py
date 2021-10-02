from math import gcd, lcm

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b), gcd(a, b))
