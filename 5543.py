bugers = []
for _ in range(3):
    bugers.append(int(input()))

drinks = []
for _ in range(2):
    drinks.append(int(input()))

bugers.sort()
drinks.sort()

print(bugers[0] + drinks[0] - 50)
