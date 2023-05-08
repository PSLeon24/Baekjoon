def solution(array, v):
    v_count = array.count(v)
    return v_count


N = int(input())
v_array = list(map(int, input().split()))
v = int(input())
print(solution(v_array, v))
