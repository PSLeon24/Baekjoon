# I
N, M = map(int, input().split())

# create arrangement
n_list = []
m_list = []
result_list = []
for _ in range(N):
    n_list.append(list(map(int, input().split())))

print(n_list)

for _ in range(M):
    m_list.append(list(map(int, input().split())))
print(m_list)

for i in m_list:
    print(n_list[i[0]-1:i[1]-1])
    # P

    # O
