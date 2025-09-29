print("=== Business Card Generator ===")
# Get user information
name = input("Enter your full name: ")
title = input("Enter your job title: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
# Create the business card
border = "*" * 40 # This creates a line of 40 asterisks
# YOUR CODE HERE
# 1. Print the top border
# 2. Print the name (centered if possible)
# 3. Print the title
# 4. Print the email
# 5. Print the phone
# 6. Print the bottom border
# Hint: You can center text using:
# text.center(40) # Centers text in 40 characters
print(border)
print(name.center(40))
print(title.center(40))
print(email.center(40))
print(phone.center(40))
print(border)
#Make Side borders
print("="*40)
# 1. Print the top border
print(border   )
# 2. Print the name (centered if possible)
print(f"* {name.ljust(36)} *")
# 3. Print the title
print(f"* {title.ljust(36)} *")
# 4. Print the email
print(f"* {email.ljust(36)} *")
# 5. Print the phone
print(f"* {phone.ljust(36)} *")
# 6. Print the bottom border
print(border)
print("="*40)




print("=== Username Generator ===")
# Get user's name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
# Generate usernames
# YOUR CODE HERE
# Remember:
# - Use .lower() to make lowercase
# - Use [0:3] to get first 3 characters
# - Use [0] to get first character
# - Use str() to convert numbers to strings
print("\nYour username options:")
username1 = (first_name[0:3] + last_name[0:3]).lower()
print("1:", username1)
username2 = (first_name[0] + last_name).lower()
print("2:", username2)
import random
random_number = random.randint(10, 99)
username3 = (first_name + str(random_number)).lower()
print("3:", username3)
print("="*40)



print("=== Text Message Formatter ===")
# Get the message
message = input("Enter your message: ")
# Calculate length
length = len(message)
# YOUR CODE HERE
# Display all the required transformations
# For the first half: use message[0:length//2]
# For the last half: use message[length//2:]
# For reversed: use message[::-1]
print(f"\nOriginal: {message}")
print(f"Length: {length} characters")
# Continue with other transformations...
print(f"Uppercase: {message.upper()}")
print(f"Lowercase: {message.lower()}")
print(f"Snake Case: {message.replace(' ', '_').lower()}")
print(f"First half: {message[0:length//2]}")
print(f"Second half: {message[length//2:]}")
print(f"Reversed: {message[::-1]}")
print("="*40)


print("=== Password Validator ===")
# Get password
password = input("Create a password: ")
# Check length
length = len(password)
has_minimum_length = length >= 8
# Check for uppercase and lowercase
has_uppercase = password != password.lower()
has_lowercase = password != password.upper()
# YOUR CODE HERE
# 1. Create masked version (first char + asterisks + last char)
# Example: "password" becomes "p******d"

# 3. Display results
# For masking:
# First character: password[0]
# Last character: password[-1]
# Middle asterisks: "*" * (length - 2)
masked_password = password[0] + "*" * (length - 2) + password[-1] if length > 2 else password
criteria_met = 0
feedback = []
if has_minimum_length:
    criteria_met += 1
if has_uppercase:
    criteria_met += 1
if has_lowercase:
    criteria_met += 1
if any(c.isdigit() for c in password):
    criteria_met += 1
if any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in password):
    criteria_met += 1
print(f"\nMasked Password: {masked_password}")
print(f"Criteria met: {criteria_met} out of 5")
# 3. For each criterion not met, add feedback message
if not has_minimum_length:
    feedback.append("Password should be at least 8 characters long.")
if not has_uppercase:
    feedback.append("Password should contain at least one uppercase letter.")
if not has_lowercase:
    feedback.append("Password should contain at least one lowercase letter.") 
if not any(c.isdigit() for c in password):
    feedback.append("Password should contain at least one digit.")
if not any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in password):
    feedback.append("Password should contain at least one special character.")
if feedback:
    print("Feedback:")
    for msg in feedback:
        print("-", msg)
print("="*40)



print("=== Mad Libs Story Generator ===")
print("I need some words to create your story!\n")
# Collect inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a type of food: ")
adjective1 = input("Enter an adjective (describing word): ")
adjective2 = input("Enter another adjective: ")
verb1 = input("Enter a verb ending in -ing: ")
verb2 = input("Enter another verb ending in -ing: ")
number = input("Enter a number: ")
color = input("Enter a color: ")
# YOUR CODE HERE
# Create your story using the inputs
# You can use + to concatenate or use f-strings
# Make the user inputs uppercase for highlighting
name_upper = name.upper()
place_upper = place.upper()
# ... continue for all inputs
# Create the story
story = f"""
Once upon a time, {name_upper} was {verb1.upper()} through {place_upper}
when they discovered a {adjective1.upper()} {animal.upper()}.
The {animal.upper()} was eating {number} pieces of {food.upper()}
and wearing a {color.upper()} hat.
"How {adjective2.upper()}!" exclaimed {name_upper}.
They spent the rest of the day {verb2.upper()} together.
THE END
"""
# Count words (split by spaces and count)
word_count = len(story.split())
print("\n" + "="*50)
print("YOUR STORY")
print("="*50)
print(story)
print(f"\nYour story has {word_count} words!")
