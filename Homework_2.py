# CS 1300 - Homework 2
# Name: Logan Ghast
# Date: 9/15/2025
# Description: Variables, Input/Output, and Type Conversions


print("\n" + "=" * 40)
print("Problem 1: Personal Finance Calculator")
print("=" * 40)
# TODO: Your code here
# Get user inputs
income = float(input("Enter your monthly income: $"))
# Get expenses
rent = float(input("Enter your monthly rent/mortgage: $"))
#Enter food expenses
food = float(input("Enter your monthly food expenses: $"))
#Enter transportation expenses 
transportation = float(input("Enter your monthly transportation expenses: $"))
#Enter other expenses
other = float(input("Enter your other monthly expenses: $"))

print("="*40)
print("MONTHLY BUDGET REPORT")
print("="*40)

#print income and expenses
print("Monthly Income: $", format(income, '.2f'), sep='')
print("Rent/Mortgage: $", format(rent, '.2f'), sep='')
print("Food Expenses: $", format(food, '.2f'), sep='')
print("Transportation Expenses: $", format(transportation, '.2f'), sep='')
print("Other Expenses: $", format(other, '.2f'), sep='')

print("="*40)

# Calculate total expenses
total_expenses = rent + food + transportation + other
# Calculate savings
savings = income - total_expenses
#Calculate savings rate
savings_rate = (savings / income) * 100 if income != 0 else 0
# Display results
print("\nTotal Monthly Expenses: $", format(total_expenses, '.2f'), sep='')
print("Monthly Savings: $", format(savings, '.2f'), sep='')
print("Savings Rate: ", format(savings_rate, '.2f'), "%", sep='')
print("\n" + "=" * 40)


print("\n" + "=" * 40)
print("Problem 2: Grade Statistics Calculator")
print("=" * 40)
# TODO: Your code here
# Get user inputs
grade1 = float(input("Enter the first grade (0-100): "))
grade2= float(input("Enter the second grade (0-100): "))
grade3 = float(input("Enter the third grade (0-100): "))
grade4 = float(input("Enter the fourth grade (0-100): "))
grade5 = float(input("Enter the fifth grade (0-100): "))

#Grade report
print("="*40)
print("GRADE REPORT")
print("="*40)
# Print each grade out of 100
print("Grade 1: ", format(grade1, '.2f'), "/100", sep='')
print("Grade 2: ", format(grade2, '.2f'), "/100", sep='')
print("Grade 3: ", format(grade3, '.2f'), "/100", sep='')
print("Grade 4: ", format(grade4, '.2f'), "/100", sep='')
print("Grade 5: ", format(grade5, '.2f'), "/100", sep='')

print("="*40)
# Calculate statistics
#Total points out of 500
total_points = grade1 + grade2 + grade3 + grade4 + grade5
# Average grade
average_grade = total_points / 5
# Overall grade out of 500
overall_grade = (total_points / 500) * 100

#Points needed for 90%
points_needed_90 = max(0, 450 - total_points)



#Total points out of 500
print("\nTotal Points: ", format(total_points, '.2f'), "/500", sep='')
print("Average Grade: ", format(average_grade, '.2f'), sep='')
print("Points needed for 90% overall: ", format(points_needed_90, '.2f'), sep='')
print("="*40)


print("\n" + "=" * 40)
print("Problem 3: Time Zone Converter")
print("=" * 40)
# TODO: Your code here
#Ask for current hour in 24 hour format in EST
current_hour = int(input("Enter the current hour (0-23) in EST: "))
#Ask for current minute
current_minute = int(input("Enter the current minute (0-59): "))
#Calculate time zones in 4 different zones
#EST    
est_hour = current_hour
est_minute = current_minute
#CST
cst_hour = (current_hour - 1) % 24
cst_minute = current_minute
#MST
mst_hour = (current_hour - 2) % 24
mst_minute = current_minute
#PST
pst_hour = (current_hour - 3) % 24
pst_minute = current_minute
#Display time zone report
print("="*40)
print("TIME ZONE REPORT")
print("="*40)
#Print each time zone
print("Eastern Standard Time (EST): ", format(est_hour, '02d'), ":", format(est_minute, '02d'), sep='')
print("Central Standard Time (CST): ", format(cst_hour, '02d'), ":", format(cst_minute, '02d'), sep='')
print("Mountain Standard Time (MST): ", format(mst_hour, '02d'), ":", format(mst_minute, '02d'), sep='')
print("Pacific Standard Time (PST): ", format(pst_hour, '02d'), ":", format(pst_minute, '02d'), sep='')
print("="*40)
#Print times in 12 hour format with AM/PM
def convert_to_12_hour_format(hour, minute):
    period = "AM"
    if hour == 0:
        hour_12 = 12
    elif hour == 12:
        hour_12 = 12
        period = "PM"
    elif hour > 12:
        hour_12 = hour - 12
        period = "PM"
    else:
        hour_12 = hour
    return f"{hour_12:02d}:{minute:02d} {period}"
print("\n12-Hour Format:")
print("Eastern Standard Time (EST): ", convert_to_12_hour_format(est_hour, est_minute), sep='')
print("Central Standard Time (CST): ", convert_to_12_hour_format(cst_hour, cst_minute), sep='')
print("Mountain Standard Time (MST): ", convert_to_12_hour_format(mst_hour, mst_minute), sep='')
print("Pacific Standard Time (PST): ", convert_to_12_hour_format(pst_hour   , pst_minute), sep='')
print("\n" + "=" * 40)


print("\n" + "=" * 40)
print("\n" + "=" * 40)
print("Problem 4: Recipe Scaler")
print("=" * 40)
# TODO: Your code here
#Get original servings
original_servings = int(input("Enter the original number of servings: "))
#Get desired servings
desired_servings = int(input("Enter the desired number of servings: "))
#Get 5 ingeredients with amounts and units:
ingredient1 = input("Enter the name of ingredient 1: ")
amount1 = float(input(f"Enter the amount of {ingredient1} (in cups): "))
ingredient2 = input("Enter the name of ingredient 2: ")
amount2 = float(input(f"Enter the amount of {ingredient2} (in cups): "))
ingredient3 = input("Enter the name of ingredient 3: ")
amount3 = float(input(f"Enter the amount of {ingredient3} (in tbsp): "))
ingredient4 = input("Enter the name of ingredient 4: ")
amount4 = float(input(f"Enter the amount of {ingredient4} (in whole): "))
ingredient5 = input("Enter the name of ingredient 5: ")
amount5 = float(input(f"Enter the amount of {ingredient5} (in tsp): "))




#Calculate Scaling Factor
scaling_factor = desired_servings / original_servings if original_servings != 0 else 0

#Scale all ingredients
scaled_amount1 = amount1 * scaling_factor
scaled_amount2 = amount2 * scaling_factor
scaled_amount3 = amount3 * scaling_factor
scaled_amount4 = amount4 * scaling_factor
scaled_amount5 = amount5 * scaling_factor

#Display original and scaled recipe
print("="*40)
print("RECIPE SCALER")
print("="*40)
print("Original Servings: ", original_servings, sep='')
print("Desired Servings: ", desired_servings, sep='')
print("="*40)
#Print each ingredient with original and scaled amounts
print(f"{ingredient1}: {format(amount1, '.2f')} -> {format(scaled_amount1, '.2f')}")
print(f"{ingredient2}: {format(amount2, '.2f')} -> {format(scaled_amount2, '.2f')}")
print(f"{ingredient3}: {format(amount3, '.2f')} -> {format(scaled_amount3, '.2f')}")
print(f"{ingredient4}: {format(amount4, '.2f')} -> {format(scaled_amount4, '.2f')}")
print(f"{ingredient5}: {format(amount5, '.2f')} -> {format(scaled_amount5, '.2f')}")
print("="*40)  
print("\n" + "=" * 40)

