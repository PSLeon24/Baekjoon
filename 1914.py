def move(no, x, y): # 옮겨 놓아야 할 원반 no개를 시작 기둥(x)에서 목표 기둥(y)으로 옮기는 함수 move()
    if no > 1: # 원반이 1개를 초과할 경우
        move(no - 1, x, 6 - x - y) # 가장 아래의 원반을 제외한 나머지 원반들을 시작 기둥(x)에서 중간 기둥(6-x-y)으로 이동시킨다.
        # 중간 기둥을 6-x-y로 표현한 이유는 시작 기둥의 번호가 1, 중간 기둥의 번호는 2, 목표 기둥의 번호가 3이므로 기둥 번호의 합은 6이다.
        # 이때, 시작 기둥과 목표 기둥이 어느 위치에 있든 항상 6 - 1(x) - 3(y) = 2(중간 기둥)이 나오기 때문에 위와 같이 구하였다.
    print(f'{x} {y}') # 시작 기둥(x)에서 목표 기둥(y)으로 옮겼다는 것을 출력한다.
        
    if no > 1:
        move(no - 1, 6 - x - y, y) # 중간 기둥(6-x-y)으로 옮긴 원반들을 목표 기둥(y) 위에 다시 얹는다.

N = int(input())
print((2**N) - 1)
if N <= 20:
    move(N, 1, 3) # 원반의 개수가 1개 일때