from calendar import isleap


def leaf(year):
    bool_year = isleap(year)
    if bool_year == False:
        return 0
    else:
        return 1


years = int(input())
print(leaf(years))

'''
# Step 1. Input Year
year = int(input())

# Step 2. Judge multiples
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)
'''
