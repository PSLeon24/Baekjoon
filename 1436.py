'''
666
1666, 2666, 3666, 4666, 5666,
6660, 6661, 6662, 6663, 6664, 6665
6666
6667, 6668, 6669
7666, 8666, 9666
10666

logic
Brute Force 무작위 대입을 사용하여, 먼저 hells 라는 변수에 666이라는 수를 선언
몇번째인지 저장할 cnt 변수를 초기화,
666 - 1번째, 1666 - 2번째 ...
만약 hells 안에 666이 포함되면 cnt +1
그리고 cnt와 처음 입력받은 n이 같다면 반복 탈출, hells 출력
while 문으로 계속 hells는 +1씩 반복
'''

n = int(input())
hells = 666
cnt = 0
while True:
    if '666' in str(hells):  # if '666' is included in hells, cnt + 1
        cnt += 1
    if cnt == n:
        print(hells)
        break
    hells += 1
