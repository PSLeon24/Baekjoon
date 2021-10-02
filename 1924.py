from datetime import date

x, y = map(int, input().split())
dates = date(2007, x, y)

dates = dates.strftime("%a")

print(dates.upper())
