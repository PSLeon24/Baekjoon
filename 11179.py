n = int(input())

n = bin(n)
# print(n[2:])
n = list(n)
del n[:2]
tmp = []
for i in range(1, len(n)+1):
    tmp.append(n[-i])

#tmp.insert(0, '0')
#tmp.insert(1, 'b')
#tmp = list(map(int, tmp))
j = "".join(tmp)
j = int(j, 2)
print(j)
