n = int(input())
num_arr = input().split()
for i in range(len(num_arr)):
    num_arr[i] = int(num_arr[i])
num_arr.sort()

new_arr = []
for i in range(n):
    new_arr.append(num_arr[0]+num_arr[-1])
    del num_arr[-1]
    del num_arr[0]

new_arr.sort()
print(new_arr[0])
