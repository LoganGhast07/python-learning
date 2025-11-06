#Problem 1:


temperatures = [72, 68, 75, 71, 69, 77, 74, 70, 73, 76]


total_temp = 0
highest_temp = temperatures[0]
lowest_temp = temperatures[0]
days_above_72 = 0

for temp in temperatures:
    total_temp += temp
    if temp > highest_temp:
        highest_temp = temp
    if temp < lowest_temp:
        lowest_temp = temp
    if temp > 72:
        days_above_72 += 1

average_temp = total_temp / len(temperatures)

print("Average Temperature:", average_temp)
print("Highest Temperature:", highest_temp)
print("Lowest Temperature:", lowest_temp)
print("Days Above 72°F:", days_above_72)

for temp in temperatures:
    celsius = (temp - 32) * 5.0/9.0
    print(f"{temp}°F is {celsius:.2f}°C")
print("="*40)



#Problem 2:

import random

secret_number = random.randint(1, 20)
guesses = []

for attempt in range(5):
    guess = int(input("Guess a number between 1 and 20: "))
    guesses.append(guess)
    if guess == secret_number:
        print("Correct!")
        break
    elif guess < secret_number:
        print("Higher")
    else:
        print("Lower")

if guess == secret_number:
    if attempt == 0:
        print("Amazing! You're a mind reader!")
    elif attempt < 3:
        print("Great job!")
    else:
        print("Good work!")
else:
    print("Sorry, you ran out of guesses. The number was", secret_number)

print("Your guesses were:", guesses)
print("="*40)


#Problem 3:




grades = [85, -10, 92, 150, 78, 0, 95, 88, -5, 100, 73, 200]
total_valid = 0
count_valid = 0
invalid_count = 0
grade_distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

for grade in grades:
    if grade < 0 or grade > 100:
        invalid_count += 1
        continue
    count_valid += 1
    total_valid += grade
    if grade >= 90:
        grade_distribution['A'] += 1
    elif grade >= 80:
        grade_distribution['B'] += 1
    elif grade >= 70:
        grade_distribution['C'] += 1
    elif grade >= 60:
        grade_distribution['D'] += 1
    else:
        grade_distribution['F'] += 1

if count_valid > 0:
    average_grade = total_valid / count_valid
else:
    average_grade = 0

print("Summary Report")
print("="*15)
print(f"Total grades processed: {count_valid}")
print(f"Invalid grades skipped: {invalid_count}")
print("Grade Distribution:")
for letter, count in grade_distribution.items():
    print(f" {letter}: {count}")
print(f"Class Average: {average_grade:.1f}")
print("="*40)