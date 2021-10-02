from math import ceil

a, b, v = map(int, input().split())

days = ceil((v-a) / (a-b)) + 1

print(days)
