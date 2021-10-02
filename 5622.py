dial = [2, 3, 4, 5, 6, 7, 8, 9, 10]
dict = ["0", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]


# print("A" in dict[0]) False
# print("A" in dict[0]) True
alpha = list(input())
# print(alpha)
cnt = 0
for i in range(len(alpha)):
    for j in dial:
        if alpha[i] in dict[j-2]:
            cnt += j

print(cnt)
