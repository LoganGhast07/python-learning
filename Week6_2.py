# TODO: Create a store system with these features:
# 1. Display a menu of 5 items with prices
# 2. Let user select one item
# 3. Ask for quantity
# 4. Apply discounts:
# - 10+ items: 10% off
# - Member: additional 5% off
# 5. Calculate tax (8%)
# 6. Show final receipt
print("=== CORNER STORE ===")
# Your code here:
items = {
    1: ("Apple", 1.00),
    2: ("Banana", 0.50),
    3: ("Orange", 0.75),
    4: ("Grapes", 2.00),
    5: ("Mango", 1.50)
}
for key, (name, price) in items.items():
    print(f"{key}. {name} - ${price:.2f}")
choice = int(input("Select an item by number: "))
if choice not in items:
    print("Invalid choice.")
    exit() 
item_name, item_price = items[choice]
quantity = int(input(f"How many {item_name}s would you like to buy? "))
is_member = input("Are you a member? (yes/no): ").strip().lower() == 'yes'
subtotal = item_price * quantity
discount = 0
if quantity >= 10:
    discount += 0.10
if is_member:
    discount += 0.05
discount_amount = subtotal * discount
subtotal -= discount_amount
tax = subtotal * 0.08
total = subtotal + tax
print("\n=== RECEIPT ===")
print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal + discount_amount:.2f}")
if discount > 0:
    print(f"Discount: -${discount_amount:.2f}")
print(f"Tax: +${tax:.2f}")
print(f"Total: ${total:.2f}")

print("="*40)


# TODO: Create a health advisor with these features:
# 1. Ask for age, weight, height
# 2. Ask about exercise (none/light/moderate/heavy)
# 3. Ask about sleep hours
# 4. Ask about water intake (glasses per day)
# 5. Calculate BMI
# 6. Provide personalized recommendations based on all inputs
# 7. Give an overall health score (0-100)
print("=== HEALTH ADVISOR ===")
# Your code here
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (lb): "))
height = float(input("Enter your height (inches): "))
exercise = input("How often do you exercise? (none/light/moderate/heavy): ").strip().lower()
sleep = float(input("How many hours do you sleep per night? "))
water = int(input("How many glasses of water do you drink per day? "))
bmi = (weight / (height ** 2)) * 703
print(f"Your BMI is: {bmi:.2f}")
score = 100
if age < 18 or age > 65:
    score -= 10
if bmi < 18.5 or bmi > 24.9:
    score -= 20
if exercise == 'none':
    score -= 20
elif exercise == 'light':
    score -= 10
elif exercise == 'moderate':
    score -= 5
if sleep < 6:
    score -= 15
elif sleep > 9:
    score -= 5 
if water < 5:
    score -= 10
elif water > 10:
    score -= 5 
print("\n=== HEALTH RECOMMENDATIONS ===")
if bmi < 18.5:
    print("You are underweight. Consider a balanced diet to gain weight.")
elif bmi > 24.9:
    print("You are overweight. Consider a healthy diet and regular exercise.")
else:
    print("Your weight is normal. Maintain your current lifestyle.")
if exercise == 'none':
    print("Try to incorporate at least light exercise into your routine.")
elif exercise == 'light':
    print("Consider increasing your exercise to moderate levels.")
elif exercise == 'moderate':
    print("Great job! Keep up the good work.")
elif exercise == 'heavy':
    print("Excellent! Just ensure you are not overtraining.")
if sleep < 7:
    print("Try to get at least 7-8 hours of sleep per night.")
elif sleep > 9:
    print("Too much sleep can be detrimental. Aim for 7-8 hours.")
if water < 8:
    print("Increase your water intake to at least 8 glasses per day.")
elif water > 12:
    print("You might be drinking too much water. Aim for 8-12 glasses per day.")
print(f"\nYour overall health score is: {score}/100")
print("="*40)



# TODO: Create a contact form with validation for:
# 1. Name (required, 2-50 chars)
# 2. Email (must contain @ and .)
# 3. Subject (required, max 100 chars)
# 4. Message (required, 10-500 chars)
# 5. Show all errors at once with helpful messages
print("=== CONTACT FORM ===")
# Your code here:
def validate_name(name):
    if not name:
        return "Name is required."
    if len(name) < 2 or len(name) > 50:
        return "Name must be between 2 and 50 characters."
    return None
def validate_email(email):
    if "@" not in email or "." not in email:
        return "Email must contain '@' and '.'."
    return None
def validate_subject(subject):
    if not subject:
        return "Subject is required."
    if len(subject) > 100:
        return "Subject must be less than 100 characters."
    return None
def validate_message(message):
    if not message:
        return "Message is required."
    if len(message) < 10 or len(message) > 500:
        return "Message must be between 10 and 500 characters."
    return None
name = input("Enter your name: ").strip()
email = input("Enter your email: ").strip()
subject = input("Enter the subject: ").strip()
message = input("Enter your message: ").strip()
errors = []
name_error = validate_name(name)
if name_error:
    errors.append(name_error)
email_error = validate_email(email)
if email_error:
    errors.append(email_error)
subject_error = validate_subject(subject)
if subject_error:
    errors.append(subject_error)
message_error = validate_message(message)
if message_error:
    errors.append(message_error)
if errors:
    print("\n=== ERRORS ===")
    for error in errors:
        print(f"- {error}")
else:
    print("\nThank you for contacting us! We will get back to you soon.")
print("="*40)
