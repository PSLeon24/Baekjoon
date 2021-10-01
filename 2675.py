t = int(input())

for _ in range(t):
    num, string = input().split()
    text = ''
    for i in string:
        text += int(num) * i
    print(text)
