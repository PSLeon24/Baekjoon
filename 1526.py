import sys

num = int(sys.stdin.readline())

while True:
    if len(str(num)) == str(num).count('4') + str(num).count('7'):
        print(num)
        break
        # lst[i+1] = str(int(lst[i+1]) - 1)
    num -= 1
