# exercise3.py
# Arithmetic Operations Lab
# Logan Ghast
# 8/25/2025
# Test numbers
a = 17
b = 5
c = 2.5
print("Test Values:")
print(f"a = {a}, b = {b}, c = {c}")
print("-" * 30)
# TODO: Perform each operation and observe results
# Addition

add_result = a + b
print(f"{a} + {b} = {add_result}")
# Subtraction
sub_result = a - b
print(f"{a} - {b} = {sub_result}")

# Multiplication
mul_result = a * b
print(f"{a} * {b} = {mul_result}")

# Division (/) - note the type!
div_result = a / b
print(f"{a} / {b} = {div_result} (Type: {type(div_result)})")
# Integer Division (//)
int_div_result = a // b
print(f"{a} // {b} = {int_div_result} (Type: {type(int_div_result)})")

# Modulo (%)
mod_result = a % b
print(f"{a} % {b} = {mod_result}")

# Exponentiation (**)
exp_result = a ** b
print(f"{a} ** {b} = {exp_result}")

print("-" * 30)
# TODO: Mixed type operations
print("Mixed Type Operations:")
# What happens with int + float? 
# It results in a float.
mixed1 = a + c
#Observations to Note:
#• What's the difference between / and // ? The / operator performs regular division and returns a float, while // performs integer (floor) division and returns an integer if both operands are integers.
#• What type does regular division ( / ) always return? It always returns a float.
#• How does Python handle very large numbers? Using arbitrary-precision arithmetic
#• What happens with negative integer division? It rounds down to the nearest integer.

