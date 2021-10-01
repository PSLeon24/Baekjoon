home_to_school = int(input())
school_to_pc = int(input())
pc_to_academy = int(input())
academy_to_home = int(input())

sums = home_to_school + school_to_pc + pc_to_academy + academy_to_home
x = 0
y = 0
if sums >= 60:
    x = sums // 60
    y = sums % 60

print(x)
print(y)
