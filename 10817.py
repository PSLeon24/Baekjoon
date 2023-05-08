import sys

def med3(a, b, c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    else:
        return c
    
input = sys.stdin.readline
a, b, c = map(int, input().split())
print(med3(a, b, c))