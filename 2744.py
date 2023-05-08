a = input()
b = []
for i in range(len(a)):
    b.append(a[i])

for i in range(len(b)):
    if b[i].isupper() == True:
        b[i] = b[i].lower()
    else:
        b[i] = b[i].upper()

for i in b:
    print(i, end='')
