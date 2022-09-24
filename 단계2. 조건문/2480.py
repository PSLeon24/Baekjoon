def dice(a, b, c):
    if a == b and b == c:
        return 10000 + a*1000
    elif (a == b and b != c) or (a == c and a != b):
        return 1000 + a*100
    elif b == c and a != c:
        return 1000 + b*100
    else:
        return max(a, b, c) * 100


a, b, c = map(int, input().split())
print(dice(a, b, c))
