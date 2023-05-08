# I(input)
N = int(input())
lst = []
for _ in range(N):
    lst.append(input())

# P(process:logic)
lst = list(set(lst))
lst.sort(key=lambda x: (len(x), x))

# O(output)
for i in lst:
    print(i)
