lst = list(input())
for i in range(len(lst)):
    lst[i] = lst[i].upper()
lst.sort()
new = set(lst)

max = 0
rank = 0
for i in new:
    if max < lst.count(i):
        max = lst.count(i)
        rank = i
    elif max == lst.count(i):
        rank = '?'
    elif len(lst) == 1:
        rank = i
    else:
        continue

print(rank)
