# 킹:1 , 퀸:1, 룩:2, 비숍:2, 나이트:2, 폰:8
king, queen, look, bishop, night, phone = map(int, input().split())
print(f'{1-king} {1-queen} {2-look} {2-bishop} {2-night} {8-phone}')
