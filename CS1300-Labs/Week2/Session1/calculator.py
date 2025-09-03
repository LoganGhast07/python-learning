# calculator.py
# Simple Calculator with Type Handling
# Logan Ghast
# 8/25/2025
print("=" * 40)
print(" ARITHMETIC CALCULATOR")
print("=" * 40)
# TODO: Create variables for two numbers 
# Use meaningful variable names

first_number = 10 # Change to your values
second_number = 3 # Change to your values
# TODO: Display the numbers and their types

print(f"First number: {first_number} (Type: {type(first_number).__name__})")
print(f"Second number: {second_number} (Type: {type(second_number).__name__})")
print("-" * 40)
# TODO: Perform all arithmetic operations
print("CALCULATIONS:")

# Addition
sum_result = first_number + second_number 
print(f"Addition: {first_number} + {second_number} = {sum_result}")

# Subtraction
diff_result = first_number - second_number
print(f"Subtraction: {first_number} - {second_number} = {diff_result}")

# Multiplication
product_result = first_number * second_number
print(f"Multiplication: {first_number} * {second_number} = {product_result}")



# Division (regular)

div_result = first_number / second_number
print(f"Division: {first_number} / {second_number} = {div_result}")

# Integer Division

int_div_result = first_number // second_number
print(f"Integer Division: {first_number} // {second_number} = {int_div_result}")
# Modulo

mod_result = first_number % second_number
print(f"Modulo: {first_number} % {second_number} = {mod_result}")

# Exponentiation
exp_result = first_number ** second_number
print(f"Exponentiation: {first_number} ** {second_number} = {exp_result}")
#Testing Values: Try your calculator with these combinations:
#1. first_number = 10, second_number = 3
#2. first_number = 7, second_number = 2
#3. first_number = 15.5, second_number = 4
#Final Commit: git commit -m "Complete calculator with all operations"
# Your code
print("-" * 40)
# TODO: Type analysis section
print("TYPE ANALYSIS:")
# Check and display the type of each result
# Show which operations always return floats
# Show which preserve integer type
print("-" * 40)
# TODO: Fun calculations section
print("FUN CALCULATIONS:")
# Calculate the area of a circle with radius = first_number
pi = 3.14159
area = pi * (first_number ** 2)
print(f"Area of circle with radius {first_number}: {area:.2f}")
# Calculate compound interest
# Principal = first_number * 100, Rate = second_number%, Time = 5 years
principal = first_number * 100
rate = second_number / 100
time = 5
amount = principal * (1 + rate) ** time
print(f"${principal} at {second_number}% for {time} years = ${amount:.2f}")
# Calculate how many whole pizzas and slices
# If first_number is people and each pizza has 8 slices
# Each person gets second_number slices
total_slices_needed = first_number * second_number
slices_per_pizza = 8
whole_pizzas = total_slices_needed // slices_per_pizza
extra_slices = total_slices_needed % slices_per_pizza
print(f"{first_number} people × {second_number} slices each =")
print(f" Need {whole_pizzas} pizzas with {extra_slices} slices left over")
print("=" * 40)