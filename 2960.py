import sys
input = sys.stdin.readline

n, k = map(int, input().split())

prime = [True] * (n+1)
num = 1

for i in range(2, n+1):
    if prime[i] == True: # 소수가 아니라면
        for j in range(i, n+1, i): # 배수 확인
            # ex) i=2, n=15라면, 2, 4, 6, 8, 10, 12, 14까지 확인
            if prime[j] == False: # 소수일 때는 건너뛰기
                continue

            if num == k: # 세고 있는 num과 입력받은 k가 같으면 j 출력
                print(j)
            
            prime[j] = False # 소수일 경우 j번째에 False 처리(소수로 지정)
            num += 1 # 걸러지는 숫자 나올 때마다 +1 씩 해줌