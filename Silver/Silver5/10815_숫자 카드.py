import sys

N = int(sys.stdin.readline())
cards = [int(x) for x in sys.stdin.readline().split()]
M = int(sys.stdin.readline())
find_card = [int(x) for x in sys.stdin.readline().split()]
cards.sort()


def binary_search(x):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == x:
            return 1
        elif cards[mid] > x:
            end = mid - 1
        else:
            start = mid + 1

    return 0


for i in find_card:
    print(binary_search(i), end=" ")
