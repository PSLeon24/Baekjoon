from math import sqrt
d, h, w = map(int, input().split())
# D : 대각선의 길이, H : 높이의 비율, W : 너비의 비율
# height : 높이, width : 너비

# (r*w)^2 + (r*h)^2 = d^2
# r = d^2 / (w^2 + h^2)
# width = r * w
# height = r * h
result = sqrt(d**2 / (w**2 + h**2))
width = result * w
height = result * h
print(int(height), int(width), end=" ")
