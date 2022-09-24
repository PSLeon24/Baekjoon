H, M = map(int, input().split())

if H <= 0:
    if M >= 45:
        M -= 45
    elif M < 45:
        H = 23
        M += 15
else:
    if M >= 45:
        M -= 45
    elif M < 45:
        H -= 1
        M += 15


print(H, M)
