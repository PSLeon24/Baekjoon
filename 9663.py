# N-Queen

N = int(input())

# (j, i)의 2 dimensional-matrix라 생각
pos = [0] * N # 각 열에 배치한 퀸의 위치
flag_a = [False] * N # 각 행에 퀸을 배치했는지 체크 (False: 배치 X, True: 배치 O)
flag_b = [False] * ((2*N)-1) # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크 (False: 배치 X, True: 배치 O)
# 4x4 table을 그리면, 좌측 상단부터 대각선 번호 0 ~ (2N-1)로 나타낼 수 있음
flag_c = [False] * ((2*N)-1) # 대각선 방향(↖↘)으로 퀸을 배치했는지 체크 (False: 배치 X, True: 배치 O)
# 4x4 table을 그리면, 좌측 하단부터 대각선 번호 0 ~ (2N-1)로 나타낼 수 있음
cnt = 0  # N개의 퀸을 조건에 맞게 모두 배치시키는 경우의 수

def put():
    global cnt # N개의 퀸을 조건에 맞게 모두 배치시키는 경우의 수를 전역변수로 생성
    cnt += 1 # put()함수가 호출될 때마다 경우의 수는 1씩 증가

def set(i):
    for j in range(N): # N개의 행을 검색
        if(not flag_a[j] # j행에 퀸이 배치되지 않았다면
          and not flag_b[i + j] # 대각선 방향(↙↗)으로 퀸이 배치되지 않았다면 - j행 i열의 값은 i+j로 구할 수 있음
          and not flag_c[i - j + (N-1)]): # 대각선 방향(↖↘)으로 퀸이 배치되지 않았다면 - j행 i열의 값은 i - j + (N-1)으로 구할 수 있음
            pos[i] = j # 퀸을 j행에 배치
            if i == (N-1): # 모든 열에 퀸을 배치 완료 (0열 ~ (N-1)열까지 총 N개의 열)
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (N-1)] = True
                # 위 코드는 (j, i) 위치에 퀸을 배치할 때, 해당 행, 대각선 (↙↗), 대각선 (↖↘)에 퀸이 배치되었다는 표시
                set(i + 1) # 다음 열(i + 1)에 대해 재귀적으로 퀸을 배치하기 위한 함수를 호출
                # 위 코드는 열이 한 칸씩 증가하며 가능한 모든 퀸의 배치를 찾는 과정
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (N-1)] = False # 퀸이 배치되었던 행, 대각선 (↙↗), 대각선 (↖↘)의 표시를 다시 False로 변경
                # 위 코드는 해당 위치에서 다른 가능한 퀸의 배치를 찾기 위해 다시 되돌리는 역할
                
set(0)
print(f'{cnt}')