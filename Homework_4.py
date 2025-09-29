print("=== Temperature Converter & Weather Advisor ===")
# Get temperature from user
temp = float(input("Enter temperature: "))
# Get the scale (C or F)
scale = input("Is this Celsius or Fahrenheit? (C/F): ").upper()
# YOUR CODE HERE
# 1. Check which scale was entered
# 2. Convert to the other scale
# 3. Display both temperatures
# 4. Give weather advice based on Fahrenheit

#Code Here:
if scale == 'C':
    fahrenheit = (temp * 9/5) + 32
    celsius = temp
    print(f"{temp}°C is {fahrenheit:.2f}°F")
elif scale == 'F':
    celsius = (temp - 32) * 5/9
    fahrenheit = temp
    print(f"{temp}°F is {celsius:.2f}°C")
else:
    print("Invalid scale entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    exit()
# Weather advice based on Fahrenheit
if fahrenheit < 32:
    advice = "It's freezing! Stay warm!"
elif 32 <= fahrenheit < 50:
    advice = "It's chilly. Wear a jacket!"
elif 50 <= fahrenheit < 70:
    advice = "It's cool. A light sweater should be fine."
elif 70 <= fahrenheit < 85:
    advice = "It's warm. Perfect weather!"
else:
    advice = "It's hot! Stay hydrated!"
print(advice)

print("="*40)




print("=== Movie Theater Ticket System ===")
# Get customer information
age = int(input("Enter customer age: "))
day = input("Enter day of week: ").lower()
# YOUR CODE HERE
# Remember:
# - Check for Tuesday special first
# - If not Tuesday, ask for show time
# - Apply age-based pricing
# - Apply matinee discount if applicable

#Code Here:
if day == 'tuesday':
    price = 7.00
    print("It's Tuesday! All tickets are $7.00.")
else:
    show_time = int(input("Enter show time (24-hour format, e.g., 13 for 1 PM): "))
    if age < 3:
        price = 0.00
        print("Free ticket for children under 3!")
    elif 3 <= age <= 12:
        price = 8.00
        print("Child ticket: $10.00")
    elif 13 <= age <= 64:
        price = 15.00
        print("Adult ticket: $15.00")
    else:  # age 65 and older
        price = 10.00
        print("Senior ticket: $10.00")
    print(f"Base ticket price: ${price:.2f}")
    # Apply matinee discount if applicable
    if show_time < 17:  # before 5 PM
        price -= 3.00
        print("Matinee discount applied: -$3.00")
print(f"Total ticket price: ${price:.2f}")
print("="*40)



print("=== Grade Calculator ===")
# Get three test scores
test1 = float(input("Enter Test 1 score (0-100): "))
test2 = float(input("Enter Test 2 score (0-100): "))
test3 = float(input("Enter Test 3 score (0-100): "))
# YOUR CODE HERE
# 1. Validate all scores are between 0 and 100
# 2. If invalid, print error and stop
# 3. Calculate average
# 4. Determine letter grade using elif
# 5. Check passing criteria (D or better AND at least one test >= 60)
# 6. Display results

if not all(0 <= score <= 100 for score in [test1, test2, test3]):
    print("Error: All test scores must be between 0 and 100.")
    exit()
average = (test1 + test2 + test3) / 3
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Average score: {average:.2f}")
print(f"Letter grade: {grade}")
if grade in ['A', 'B', 'C', 'D'] and any(score >= 60 for score in [test1, test2, test3]):
    print("Status: Passing")
else:
    print("Status: Failing")
print("="*40)




print("=== Password Strength Checker ===")
password = input("Enter a password to check: ")
# Initialize criteria counters
criteria_met = 0
feedback = []

# 1. Check each criterion
# 2. For each criterion met, increment criteria_met
# 3. For each criterion not met, add feedback message
# 4. Determine strength level
# 5. Display results and feedback
# Hint for checking digits:
#Length: At least 8 characters
#Contains at least one uppercase letter
#Contains at least one lowercase letter
#Contains at least one digit
#Not a common password ("password", "12345678", "qwerty")
#Weak: Meets 0-2 criteria
#Fair: Meets 3 criteria
#Good: Meets 4 criteria
#Strong: Meets all 5 criteria
#Code Here:
if len(password) >= 8:
    criteria_met += 1
else:
    feedback.append("Password should be at least 8 characters long.")
if any(c.isupper() for c in password):
    criteria_met += 1
else:
    feedback.append("Password should contain at least one uppercase letter.")
if any(c.islower() for c in password):
    criteria_met += 1
else:
    feedback.append("Password should contain at least one lowercase letter.")
if any(c.isdigit() for c in password):
    criteria_met += 1
else:
    feedback.append("Password should contain at least one digit.")
if any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in password):
    criteria_met += 1
else:
    feedback.append("Password should contain at least one special character (!@#$%^&*()-_=+[]{}|;:,.<>?/).")
# Determine strength level
if criteria_met == 5:
    strength = "Strong"
elif criteria_met == 4:
    strength = "Good"
elif criteria_met == 3:
    strength = "Moderate"
elif criteria_met == 2:
    strength = "Weak"
else:
    strength = "Very Weak"
# Display results
print(f"Password strength: {strength}")
if feedback:
    print("Feedback:")
    for item in feedback:
        print(f" - {item}")
print("="*40)


print("=== Restaurant Bill Calculator ===")
# Get initial information
food_total = float(input("Enter food total: $"))
is_holiday = input("Is today a holiday? (yes/no): ").lower()
party_size = int(input("How many people in your party? "))
# Follow the requirements and calculation order
# Remember to ask additional questions based on conditions
# Display a detailed breakdown of the bill
# Input the food total
# Ask if it's a holiday (15% surcharge on holidays)
# Ask for party size
# Ask if they have a membership (10% discount for members)
# Ask for day of week (10% senior discount on Wednesdays for parties with seniors)
# Calculate automatic gratuity for parties of 6 or more (18%)
# Calculate tax (8.5%)
#Display itemized bill
#If bill is 100 then the total should be 97.65
#Code Here:
tax_rate = 0.085
holiday_surcharge = 0.15 if is_holiday == 'yes' else 0.0
membership_discount = 0.10 if input("Do you have a membership? (yes/no): ").lower() == 'yes' else 0.0
#Party size with no seniors
gratuity = 0.18 if party_size >= 6 else 0.0
subtotal = food_total
if holiday_surcharge > 0:
    subtotal += food_total * holiday_surcharge
if membership_discount > 0:
    subtotal -= food_total * membership_discount
if gratuity > 0:
    subtotal += food_total * gratuity
tax = subtotal * tax_rate
total = subtotal + tax
print("=== Itemized Bill ===")
print(f"Food Total: ${food_total:.2f}")
print(f"Holiday Surcharge: ${food_total * holiday_surcharge:.2f}")
print(f"Membership Discount: -${food_total * membership_discount:.2f}")
print(f"Gratuity: +${food_total * gratuity:.2f}")
print(f"Tax: +${tax:.2f}")
print(f"Total: ${total:.2f}")
print("="*40)