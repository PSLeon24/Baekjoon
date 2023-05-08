n = int(input())
array_n = list(map(int, input().split()))
m = int(input())
array_m = list(map(int, input().split()))

array_n.sort()
def binary_search(i):
    start = 0
    end = n-1
    
    while start <= end: # 시작값이 end보다 커지면 종료
        midIndex = (start + end) // 2
        if array_n[midIndex] == i:
            return True
        elif i < array_n[midIndex]:
            end = midIndex - 1
        elif i > array_n[midIndex]:
            start = midIndex + 1


for i in range(m):
    if binary_search(array_m[i]) == True:
        print(1)
    else:
        print(0)