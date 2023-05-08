def solution(n):
    str = ''
    for _ in range(n):
        str += 'long '
    str += 'int'
    return str


N = int(int(input())/4)
print(solution(N))
