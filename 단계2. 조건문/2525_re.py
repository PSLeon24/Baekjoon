H, M = map(int, input().split())
needs_time = int(input())

H += needs_time // 60
M += needs_time % 60

if M >= 60:
    M -= 60
    H += 1

if H >= 24:
    H -= 24

print(H, M)
