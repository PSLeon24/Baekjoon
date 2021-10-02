import sys

for i in range(3):
    n = int(sys.stdin.readline())
    nums = [int(sys.stdin.readline()) for _ in range(n)]

    if sum(nums) > 0:
        print('+')
    elif sum(nums) < 0:
        print('-')
    elif sum(nums) == 0:
        print(0)
