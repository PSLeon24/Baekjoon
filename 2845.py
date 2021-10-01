import sys

l, p = map(int, sys.stdin.readline().split())
participants = list(map(int, sys.stdin.readline().split()))

#print(l, p, participants)

result = []
for i in range(5):
    result.append(participants[i]-(l*p))

for i in range(5):
    print(result[i], end=' ')
