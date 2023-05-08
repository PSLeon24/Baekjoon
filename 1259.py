while True:
    n = int(input())
    if n==0:
        break
    if n>9:
        if str(n) == str(n)[::-1]:
            print('yes')
        elif str(n)[0] == '0':
            print('no')
        else:
            print('no')
    else:
        print('yes')
