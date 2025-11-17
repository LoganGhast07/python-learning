#Problem 1: Multiplication Table Ge




while True:
    try:
        size = int(input("Enter table size (1-12): "))
        if 1 <= size <= 12:
            break
        else:
            print("Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Generate and print the multiplication table
print("    ", end="")
for i in range(1, size + 1):
    print(f"{i:4}", end="")
print("\n" + "----" * (size + 1))

for i in range(1, size + 1):
    print(f"{i:2} |", end="")
    for j in range(1, size + 1):
        print(f"{i*j:4}", end="")
    print()
    
print("="*40)


#Problem 2: Pattern Detective

#Your Task: Given a list of numbers, implement ALL these patterns in one program:
numbers = [23, 8, 45, 12, 78, 34, 67, 91, 15, 52, 41, 3]
#Patterns to Implement:
#1. Search Pattern: Find first number greater than 75
#2. Filter Pattern: Get all even numbers
#3. Counter Pattern: Count numbers in different ranges (0-25, 26-50, 51-75, 76-100)
#4. Accumulator Pattern: Print numbers divisible by 3 and then their sum
#5. Sentinel Pattern: Allow user to add numbers until they enter -1 and add them to the numbers list

# 1. Search Pattern

first_greater_than_75 = next((num for num in numbers if num > 75), None)
print(f"First number greater than 75: {first_greater_than_75}")
print("="*40)

# 2. Filter Pattern

even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Even numbers: {even_numbers}")
print("="*40)

# 3. Counter Pattern

range_counts = {"0-25": 0, "26-50": 0, "51-75": 0, "76-100": 0}
for num in numbers:
    if 0 <= num <= 25:
        range_counts["0-25"] += 1
    elif 26 <= num <= 50:
        range_counts["26-50"] += 1
    elif 51 <= num <= 75:
        range_counts["51-75"] += 1
    elif 76 <= num <= 100:
        range_counts["76-100"] += 1
print(f"Number counts in ranges: {range_counts}")
print("="*40)

# 4. Accumulator Pattern

div_by_3 = [num for num in numbers if num % 3 == 0]
print(f"Numbers divisible by 3: {div_by_3}")
print(f"Sum of numbers divisible by 3: {sum(div_by_3)}")
print("="*40)

# 5. Sentinel Pattern

while True:
    try:
        user_input = int(input("Enter a number to add to the list (-1 to stop): "))
        if user_input == -1:
            break
        numbers.append(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
print(f"Updated numbers list: {numbers}")
print("="*40)

#Problem 3: Grade Report Generator


#Your Task: Build a gradebook system that processes multiple students and assignments.
#Given Data:
students = ["Alice", "Bob", "Carol", "David", "Emma"]
assignments = ["HW1", "HW2", "Quiz1", "Exam1", "Quiz2"]
# Grades: each row is one student's grades for all assignments
grades = [
[92, 88, 95, 87, 90], # Alice
[78, 82, 73, 85, 80], # Bob
[95, 91, 98, 92, 94], # Carol
[65, 70, 68, 72, 75], # David
[88, 85, 82, 90, 87] # Emma
]


#Requirements:
#1. Display full grade table with formatting
#2. Calculate each student's average
#3. Find class average for each assignment
#4. Identify highest and lowest grade for each assignment
#5. Determine honor roll (average >= 90)
#6. Warning list (average < 70)
#Use These Patterns:
#Nested loops for table
#Accumulator for averages
#Search for min/max
#Filter for honor/warning lists
#Counter for statistics

# 1. Display full grade table with formatting
print(f"{'Student':<10}", end="")
for assignment in assignments:
    print(f"{assignment:<10}", end="")
print("\n" + "-"*60)

for student, student_grades in zip(students, grades):
    print(f"{student:<10}", end="")
    for grade in student_grades:
        print(f"{grade:<10}", end="")
    print()
print("="*60)

# 2. Calculate each student's average
student_averages = []
for student_grades in grades:
    average = sum(student_grades) / len(student_grades)
    student_averages.append(average)
    print(f"{students[grades.index(student_grades)]}'s average: {average:.2f}")
print("="*60)

# 3. Find class average for each assignment
for i in range(len(assignments)):
    assignment_grades = [grades[j][i] for j in range(len(students))]
    average = sum(assignment_grades) / len(students)
    print(f"Average for {assignments[i]}: {average:.2f}")
print("="*60)
# 4. Identify highest and lowest grade for each assignment
for i in range(len(assignments)):
    assignment_grades = [grades[j][i] for j in range(len(students))]
    highest = max(assignment_grades)
    lowest = min(assignment_grades)
    print(f"{assignments[i]} - Highest: {highest}, Lowest: {lowest}")
print("="*60)
# 5. Determine honor roll (average >= 90)
honor_roll = [student for student, avg in zip(students, student_averages) if avg >= 90]
print(f"Honor Roll: {honor_roll}")
print("="*60)
# 6. Warning list (average < 70)
warning_list = [student for student, avg in zip(students, student_averages) if avg < 70]
print(f"Warning List: {warning_list}")
print("="*60)

#Grade distribution statistics
grade_distribution = {"90-100": 0, "80-89": 0, "70-79": 0, "60-69": 0, "0-59": 0}
for avg in student_averages:
    if 90 <= avg <= 100:
        grade_distribution["90-100"] += 1
    elif 80 <= avg < 90:
        grade_distribution["80-89"] += 1
    elif 70 <= avg < 80:
        grade_distribution["70-79"] += 1
    elif 60 <= avg < 70:
        grade_distribution["60-69"] += 1
    else:
        grade_distribution["0-59"] += 1
print(f"Grade Distribution: {grade_distribution}")
print("="*60)
