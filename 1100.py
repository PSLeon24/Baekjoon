'''
Chess : 8 X 8

((0,0) ~ (8,8))
(0,0) - white (0,1) - black (0,2) - white (0,3) - black (0,4) - white (0,5) - black (0,6) - white (0,7) - black
(1,0) - black (1,1) - white (1,2) - black (1,3) - white (1,4) - black (1,5) - white (1,6) - black (1,7) - white
...
...
(7,0) - black (7,1) - white (7,2) - black (7,3) - white (7,4) - black (7,5) - white (7,6) - black (7,7) - white

(i, j) - i+j 가 0,0 을 제외하고 짝수이면 white

.F.F...F
F...F.F.
...F.F.F
F.F...F.
.F...F..
F...F.F.
.F.F.F.F
..FF..F.

'''

chess = []
cnt = 0
for i in range(8):
    chess.append(list(input()))
    for j in range(8):
        if (i + j) % 2 == 0:
            if chess[i][j] == 'F':
                cnt += 1

print(cnt)
