import sys
n, x = map(int, sys.stdin.readline().split())
A = []
A = map(int, input().split())
# print(A)
answer = []
for i in A:
    if i < x:
        answer.append(i)

for i in answer:
    print(i, end=' ')
