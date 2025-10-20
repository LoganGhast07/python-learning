import calendar
# Scenario 1: Print all months of the year
print("Scenario 1: Print all months of the year")
for month in calendar.month_name[1:]:
    print(month)
# Your answer: for or while? Why?
# Scenario 2: Keep rolling dice until you get a 6
print("Scenario 2: Keep rolling dice until you get a 6")
import random
roll = 0
while roll != 6:
    roll = random.randint(1, 6)
    print("Rolled:", roll)
# Your answer: for or while? Why?