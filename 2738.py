import sys

'''
n, m = map(int, input().split())

matrix_A = []
matrix_B = []

for i in range(n):
    matrix_A.append(list(map(int, sys.stdin.readline().split())))

for j in range(m):
    matrix_B.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        matrix_A[i][j] += matrix_B[i][j]
    print(*matrix_A[i])

'''
n, m = map(int, input().split())

matrix_A = []
matrix_B = []
for i in [matrix_A, matrix_B]:
    for j in range(n):
        i.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        matrix_A[i][j] += matrix_B[i][j]
    print(*matrix_A[i])
