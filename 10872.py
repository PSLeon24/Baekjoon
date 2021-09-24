# define the factorial function.
def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


# input the number.
whatnum = int(input())
print(fact(whatnum))
