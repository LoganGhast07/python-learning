# Week 2 Session 2 Lab
# Logan Ghast
#9/3/2025
print("=" * 50)
print("WEEK 2 SESSION 2 LAB")
print("=" * 50)
# Problem 1: Age Calculator
print("\n--- Problem 1: Age Calculator ---")

current_year = 2025 
birth_year = 2006    
age = current_year - birth_year
print(f"You are {age} years old.")

# Problem 2: Temperature Converter
print("\n--- Problem 2: Temperature Converter ---")
celsius = 25.0  
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F.")

#Problem 3: Rectangle Measurements
print("\n--- Problem 3: Rectangle Measurements ---")

length = 5.5
width = 3.2
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area:.2f}, Perimeter: {perimeter:.2f}")

#Problem 4: Bill Calculator
print("\n--- Problem 4: Bill Calculator ---")

meal_cost = 50.0
tip_percentage = 20
tip_amount = meal_cost * (tip_percentage / 100)
total_cost = meal_cost + tip_amount
print(f"Meal: ${meal_cost:.2f}, Tip: ${tip_amount:.2f}, Total: ${total_cost:.2f}")

#Problem 5: Student Info Display
print("\n--- Problem 5: Student Info Display ---")

name = "Alice"
age = 20
major = "Computer Science"
print(name, age, major)  # Default spacing
print(name, age, major, sep=", ")  # Comma separation
print(name, age, major, sep=" | ")  # Pipe separation

#Problem 6: Progress Indicator
print("\n--- Problem 6: Progress Indicator ---")

print("Processing", end="")
for _ in range(5):
    print(".", end="")
print(" Complete!")


#Problem 7: Data Table Header
print("\n--- Problem 7: Data Table Header ---")

print("=" * 40)
print("Name\tScore\tGrade")
print("=" * 40)
student_name = "Bob"
student_score = 88
student_grade = "B+"
print(f"{student_name}\t{student_score}\t{student_grade}")

#Problem 8: Message Box
print("\n--- Problem 8: Message Box ---")

message = "Hello World"
border = "+" + "-" * 30 + "+"
print(border)
print(f"| {message:<28} |")
print(border)


#Problem 9: Price Display
print("\n--- Problem 9: Price Display ---")

item_name = "Apple"
item_price = 1.5
print(f"Item: {item_name} Price: ${item_price:>8.2f}")
print("=" * 50)

#Problem 10: Percentage Calculator
print("\n--- Problem 10: Percentage Calculator ---")

earned_points = 85
total_points = 100
percentage = (earned_points / total_points) * 100
print(f"Score: {earned_points}/{total_points} = {percentage:.1f}%")
print("=" * 50)


#Problem 11: Receipt Line Item
print("\n--- Problem 11: Receipt Line Item ---")

product = "Notebook"
quantity = 3
unit_price = 2.50
total_price = quantity * unit_price
print(f"{product:<20}{quantity:^10}{total_price:>10.2f}")
print("=" * 50)


#Problem 12: ID Formatter
print("\n--- Problem 12: ID Formatter ---")

user_id = 42  # Example input
print(f"4-digit ID: {user_id:04d}")
print(f"6-digit ID: {user_id:06d}")
print(f"8-digit ID: {user_id:08d}")
print("=" * 50)


print("\n" + "=" * 50)
print("LAB COMPLETED!")
print("=" * 50)

