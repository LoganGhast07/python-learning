#Logan Ghast
#9/4/2025
#Excersise 1.1
print("=== Memory Investigation ===")
# Create variables with small integers
a = 100
b = 100
print(f"a = {a}, memory address = {id(a)}")
print(f"b = {b}, memory address = {id(b)}")
print(f"a and b same object? {id(a) == id(b)}")
print()
# Create variables with large integers
c = 1000
d = 1000
print(f"c = {c}, memory address = {id(c)}")
print(f"d = {d}, memory address = {id(d)}")
print(f"c and d same object? {id(c) == id(d)}")
print()
# Create variables with strings
e = "Python"
f = "Python"
print(f"e = '{e}', memory address = {id(e)}")
print(f"f = '{f}', memory address = {id(f)}")
print(f"e and f same object? {id(e) == id(f)}")

# Q1: Why do a and b share the same memory address?
# Your answer: Python caches small integers for efficiency, so a and b point to the same object.
# Q2: Why might c and d have different memory addresses?
# Your answer: Larger integers are not cached, so c and d are separate objects.
# Q3: What happens with string variables e and f?
# Your answer: Strings with the same content may share memory due to interning.


print("=" * 40)



print("\n=== Variable References ===")
# Create a variable
original = 500
print(f"original = {original}, id = {id(original)}")
# Create a reference to the same object
reference = original
print(f"reference = original")
print(f"reference = {reference}, id = {id(reference)}")
print(f"Same object? {id(original) == id(reference)}")
print()
# Now modify original
original = original + 100
print("After: original = original + 100")
print(f"original = {original}, id = {id(original)}")
print(f"reference = {reference}, id = {id(reference)}")
print(f"Still same object? {id(original) == id(reference)}")
# YOUR TURN: Create your own example with strings
# Create a string variable:
text = "Hello"
print(f"text = '{text}', id = {id(text)}")
# Create a reference to it:
alias = text
print(f"alias = text")
# Modify the original using concatenation:
text = text + " World"
print("After: text = text + ' World'")
print(f"text = '{text}', id = {id(text)}")
# Check if they still point to the same object:
print(f"alias = '{alias}', id = {id(alias)}")
print(f"Same object? {id(text) == id(alias)}")


print("\n=== Memory Changes with Operations ===")
# Track memory changes with different operations
x = 200
print(f"Initial: x = {x}, id = {id(x)}")
# Save the original id
original_id = id(x)
# Try different operations and check if id changes
x = x + 50
print(f"After x = x + 50: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")
# YOUR TURN: Test these operations (one at a time, reset x=200 between each)
# Test 1: x = x * 2:
x = 200  # reset
original_id = id(x)
x = x * 2
print(f"After x = x * 2: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")


# Test 2: x = x - 100
x = 200  # reset
original_id = id(x)
x = x - 100
print(f"After x = x - 100: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")
# Test 3: x = x / 2
x = 200  # reset
original_id = id(x)
x = x / 2
print(f"After x = x / 2: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")

# Test 4: x = x // 3
x = 200  # reset
original_id = id(x)
x = x // 3
print(f"After x = x // 3: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")

# Test 5: x = x % 7
x = 200  # reset
original_id = id(x)
x = x % 7
print(f"After x = x % 7: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")
# What pattern do you notice about memory addresses after operations?
# Your observation: Most operations create a new object, changing the memory address.
print("=" * 40)



print("\n=== Compound vs Regular Assignment ===")
# Compare regular and compound assignment
print("Regular assignment:")
a = 10
print(f"Start: a = {a}")
a = a + 5
print(f"After a = a + 5: a = {a}")
a = a * 2
print(f"After a = a * 2: a = {a}")
a = a - 3
print(f"After a = a - 3: a = {a}")
print()
print("Compound assignment:")
b = 10
print(f"Start: b = {b}")
b += 5
print(f"After b += 5: b = {b}")
b *= 2
print(f"After b *= 2: b = {b}")
b -= 3
print(f"After b -= 3: b = {b}")
# YOUR TURN: Complete using compound operators
print("\nYour turn - use compound operators:")
c = 100
print(f"Start: c = {c}")
# Add 25 to c using compound operator
# Your code here:
c += 25

print(f"After adding 25: c = {c}")
# Divide c by 5 using compound operator
# Your code here:
c /= 5
print(f"After dividing by 5: c = {c}")
# Get remainder when c is divided by 7 using compound operator
# Your code here:
c %= 7
print(f"After modulo 7: c = {c}")
print("=" * 40)




print("\n=== Building a Total ===")
# Calculate a restaurant bill
bill = 0.0
print(f"Starting bill: ${bill:.2f}")
# Add items using compound operators
appetizer = 12.99
bill += appetizer
print(f"Added appetizer (${appetizer}): ${bill:.2f}")
entree = 24.50
bill += entree
print(f"Added entree (${entree}): ${bill:.2f}")
dessert = 8.99
bill += dessert
print(f"Added dessert (${dessert}): ${bill:.2f}")
# YOUR TURN: Complete the bill calculation
# Calculate 20% tip (multiply bill by 0.20)
tip = 0 # Replace with calculation
tip = bill * 0.20
print(f"Tip (20%): ${tip:.2f}")
# Add tip to bill using compound operator
# Your code here:
bill += tip
print(f"Total with tip: ${bill:.2f}")
# Calculate 8.5% tax on the original bill (before tip)
# Note: You'll need to recalculate the original bill amount
original_bill = appetizer + entree + dessert
tax = 0 # Replace with calculation
tax = original_bill * 0.085
print(f"Tax (8.5%): ${tax:.2f}")
# Add tax to bill using compound operator
# Your code here:
bill += tax
print(f"Final total: ${bill:.2f}")
print("=" * 40)



print("\n=== String Building ===")
# Build a message using compound operators
message = "Shopping list"
print(f"1. message = '{message}'")
message += ":"
print(f"2. After += ':' -> '{message}'")
message += " apples"
print(f"3. After += ' apples' -> '{message}'")
# YOUR TURN: Continue building the shopping list
# Add ", bananas" to message
# Your code here:
message += ", bananas"
print(f"4. After adding bananas -> '{message}'")
# Add ", milk" to message
# Your code here:
message += ", milk"
print(f"5. After adding milk -> '{message}'")
# Add ", bread" to message
# Your code here:
message += ", bread"
print(f"6. Final list -> '{message}'")
# Check memory - does += create a new string? 
original_message = "Test"
original_id = id(original_message)
original_message += " String"
new_id = id(original_message)
print(f"\nString memory test:")
print(f"Original id: {original_id}")
print(f"After += id: {new_id}")
print(f"Same object? {original_id == new_id}")
print("=" * 40)




print("\n=== Operator Precedence - Predict First! ===")
# For each expression:
# 1. Write your prediction
# 2. Run the code
# 3. Explain why you got that result
# Example:
# Prediction: 14
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")
print("Explanation: Multiplication happens before addition\n")
# YOUR TURN - Predict before running:
# Prediction: 4
result1 = 10 - 2 * 3
print(f"10 - 2 * 3 = {result1}")
# Explanation: Multiplication happens before subtraction


# Prediction: 24
result2 = (10 - 2) * 3
print(f"(10 - 2) * 3 = {result2}")
# Explanation: Parentheses change the order, so subtraction happens first.



# Prediction: 32
result3 = 2 ** 3 * 4
print(f"2 ** 3 * 4 = {result3}")
# Explanation: Exponentiation happens before multiplication.


# Prediction: 4096
result4 = 2 ** (3 * 4)
print(f"2 ** (3 * 4) = {result4}")
# Explanation: Parentheses change the order, so multiplication happens first.


# Prediction: 50.0
result5 = 100 / 10 * 5
print(f"100 / 10 * 5 = {result5}")
# Explanation: Division and multiplication have the same precedence, so they are evaluated left to right.


# Prediction: 2.0
result6 = 100 / (10 * 5)
print(f"100 / (10 * 5) = {result6}")
# Explanation: Parentheses change the order, so multiplication happens first.

print("=" * 40)


print("\n=== Fix the Expression with Parentheses ===")
# Each calculation is wrong. Add parentheses to fix it.
# Goal: Calculate the average of 10 and 20:
wrong_avg = 10 + 20 / 2

print(f"Wrong average: {wrong_avg}")
# YOUR FIX:
fixed_avg = (10 + 20) / 2  
print(f"Fixed average: {fixed_avg}")
# Goal: Calculate 5% of 200
wrong_percent = 5 / 100 * 200
print(f"Wrong calculation: {wrong_percent}")
# YOUR FIX:
fixed_percent = (5 / 100) * 200
print(f"Fixed calculation: {fixed_percent}")
# Goal: Convert 75 minutes to hours (divide by 60)
wrong_hours = 75 / 60 * 60
print(f"Wrong hours: {wrong_hours}")
# YOUR FIX:
fixed_hours = 75 / 60
print(f"Fixed hours: {fixed_hours}")
print("=" * 40)


print("\n=== Understanding Division Operations ===")
# Regular division (/)
print("Regular division (/):")
print(f"17 / 5 = {17 / 5}")
print(f"20 / 4 = {20 / 4}")
print(f"Type of 20 / 4: {type(20 / 4)}")
print()
# Floor division (//)
print("Floor division (//):")
print(f"17 // 5 = {17 // 5}")
print(f"20 // 4 = {20 // 4}")
print(f"Type of 20 // 4: {type(20 // 4)}")
print()
# Modulo (%)
print("Modulo (%):")
print(f"17 % 5 = {17 % 5}")
print(f"20 % 4 = {20 % 4}")
print()

# YOUR TURN: Calculate these
numerator = 23
denominator = 7
regular_div = numerator / denominator
floor_div = numerator // denominator
remainder = numerator % denominator
print(f"Calculations for {numerator} and {denominator}:")
print(f"{numerator} / {denominator} = {regular_div}")
print(f"{numerator} // {denominator} = {floor_div}")
print(f"{numerator} % {denominator} = {remainder}")
# Verify: numerator should equal (floor_div * denominator) + remainder
verification = (floor_div * denominator) + remainder
print(f"Verification: {floor_div} * {denominator} + {remainder} = {verification}")

print("=" * 40)

print("\n=== Time Conversion ===")
# Convert total seconds to hours, minutes, seconds
total_seconds = 7325
print(f"Converting {total_seconds} seconds:")
# Calculate hours
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
print(f"Hours: {hours}")
print(f"Remaining seconds: {remaining_seconds}")
# Calculate minutes from remaining seconds
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
print(f"Result: {hours} hours, {minutes} minutes, {seconds} seconds")
# YOUR TURN: Convert 9876 seconds
total_seconds_2 = 9876
print(f"\nConverting {total_seconds_2} seconds:")
# Calculate hours
hours_2 = total_seconds_2 // 3600
remaining_2 = total_seconds_2 % 3600
print(f"Hours: {hours_2}")
# Calculate minutes
minutes_2 = remaining_2 // 60
seconds_2 = remaining_2 % 60
print(f"Minutes: {minutes_2}")
print(f"Result : {hours_2} hours, {minutes_2} minutes, {seconds_2} seconds")
print("=" * 40)

print("\n=== Making Change ===")
# Calculate coins needed for given cents
cents = 287
print(f"Making change for {cents} cents:")
# Calculate quarters (25 cents)
quarters = cents // 25
remaining = cents % 25
print(f"Quarters: {quarters}, Remaining: {remaining} cents")
# Calculate dimes (10 cents)
dimes = remaining // 10
remaining = remaining % 10
print(f"Dimes: {dimes}, Remaining: {remaining} cents")
# Calculate nickels (5 cents)
nickels = remaining // 5
pennies = remaining % 5
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")

# YOUR TURN: Calculate change for 193 cents
cents_2 = 193
print(f"\nMaking change for {cents_2} cents:")
quarters_2 = cents_2 // 25
remaining_2 = cents_2 % 25
print(f"Quarters: {quarters_2}, Remaining: {remaining_2} cents")
dimes_2 = remaining_2 // 10
remaining_2 = remaining_2 % 10
# Update remaining_2
nickels_2 = remaining_2 // 5
pennies_2 = remaining_2 % 5
print(f"Quarters: {quarters_2}")
print(f"Dimes: {dimes_2}")
print(f"Nickels: {nickels_2}")
print(f"Pennies: {pennies_2}")
# Verify your answer
total_check = (quarters_2 * 25) + (dimes_2 * 10) + (nickels_2 * 5) + pennies_2
print(f"Verification: {total_check} cents")
print("=" * 40)

print("\n=== Unit Conversion Calculator ===")
# Convert miles to various units
miles = 5.5
print(f"Starting with: {miles} miles")
# Convert to feet (1 mile = 5280 feet)
feet = miles * 5280
print(f"In feet: {feet:.1f} feet")
# Convert to yards (1 mile = 1760 yards)
yards = miles * 1760
print(f"In yards: {yards:.1f} yards")
# Convert to kilometers (1 mile = 1.60934 km)
kilometers = miles * 1.60934
print(f"In kilometers: {kilometers:.2f} km")
# Convert to meters (using the km value)
meters = kilometers
meters *= 1000
print(f"In meters: {meters:.2f} meters")


# YOUR TURN: Data Storage Units
# Convert 2.5 GB to other units
gigabytes = 2.5
print(f"\n=== Data Storage Conversion ===")
print(f"Starting with: {gigabytes} GB")
#CttMB(1GB1024MB)
# Convert to MB (1 GB = 1024 MB)
megabytes = gigabytes
megabytes *= 1024
print(f"In Megabytes: {megabytes:.0f} MB")
# Convert to KB (use MB value, 1 MB = 1024 KB)
kilobytes = megabytes
# Multiply by 1024 using compound operator
kilobytes *= 1024
print(f"In Kilobytes: {kilobytes:.0f} KB")
# Convert to bytes (use KB value, 1 KB = 1024 bytes)
bytes_total = kilobytes
# Multiply by 1024 using compound operator
bytes_total *= 1024
print(f"In Bytes: {bytes_total:.0f} bytes")
# Convert to bits (1 byte = 8 bits)
bits = bytes_total
# Multiply by 8 using compound operator
bits *= 8
print(f"In Bits: {bits:.0f} bits")
print("=" * 40)


