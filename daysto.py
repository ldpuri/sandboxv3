from datetime import date

d0 = date.today()
d1 = date(2021, 8, 27)
delta = d1 - d0
days = delta.days

print(f"You got {days} days remaining to launch!")
