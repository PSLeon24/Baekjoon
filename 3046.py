import sys

r1, s = map(int, sys.stdin.readline().split())

# I have to print R2
# S = (R1 + R2) / 2
# 2S = R1 + R2
# R2 = 2S - R1
print((s*2) - r1)
