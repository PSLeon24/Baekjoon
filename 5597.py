students = []
for _ in range(28):
    students.append(int(input()))

absent = []
for i in range(1, 31):
    if i not in students:
        absent.append(i)

print(absent[0])
print(absent[1])
