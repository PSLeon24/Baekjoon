def fibo(num):
    fibos, next = 0, 1
    for _ in range(num):
        fibos, next = next, fibos + next

    return fibos


n = int(input())
print(fibo(n))
