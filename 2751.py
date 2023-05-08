import sys

n = int(input())
array = []
for _ in range(n):
    i = int(sys.stdin.readline())
    array.append(i)

array.sort()
for i in array:
    print(i)