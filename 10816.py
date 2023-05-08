import sys

input = sys.stdin.readline

n = int(input()) # first line
arr = input().split() # second line
m = int(input()) # third line
searched = input().split()
dic = dict.fromkeys(searched, 0)

for i in arr:
    if i in dic.keys():
        dic[i] += 1

for i in searched:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end =' ')