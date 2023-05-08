cnt = 0
while True:
    array = list(map(int, input().split()))
    if array[0] == 0 and array[1] == 0 and array[2] == 0:
        break
    maximum = max(array)
    array.remove(maximum)
    if maximum**2 == array[0]**2 + array[1]**2:
        print('right')
    else:
        print('wrong')
