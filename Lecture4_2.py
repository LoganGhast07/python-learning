# Problem 1

user_input = " Hello123 "
# Clean the input: user_input.________() = _______
cleaned_input = user_input.strip()
print("Cleaned input:", cleaned_input)
# Check if alphanumeric: ____________.isalnum() = _______
is_alnum = cleaned_input.isalnum()
print("Is alphanumeric:", is_alnum)
# Convert to uppercase: ____________.upper() = _______
upper_input = cleaned_input.upper()
print("Uppercase input:", upper_input)







#Problem 2
name = " jOHn DOE "
# Format as "John Doe"

# Step 1: Strip spaces: _____________
name = name.strip()
# Step 2: Convert to title: _____________
name = name.title()
# One line: name.________().________()
name = name.strip().title()
print("Formatted name:", name)  
print("="*40)


# Problem 3
password = "Pass123"
# Has uppercase? not password.islower() = _____

has_upper = not password.islower()
print("Has uppercase:", has_upper)

# Has lowercase? not password.isupper() = _____
has_lower = not password.isupper()
print("Has lowercase:", has_lower)
# Has digit? (check each character - we'll learn loops later)
has_digit = any(char.isdigit() for char in password)
print("Has digit:", has_digit)
print("="*40)


# Problem 4
url = "https://www.example.com"
# Is secure? url.startswith("https") = _____
is_secure = url.startswith("https")
print("Is secure:", is_secure)
# Get domain: url.replace("https://", "").replace("www.", "") = _____
domain = url.replace("https://", "").replace("www.", "")
print("Domain:", domain)
# Is .com site? url.endswith(".com") = _____
is_com = url.endswith(".com")
print("Is .com site:", is_com)
print("="*40)



#To be or not to be
sentence = "To be or not to be"
# Find "be": sentence.find("be") = _____
first_be = sentence.find("be")
print("First 'be' at index:", first_be)

# Count "to": sentence.count("to") = _____
to_count = sentence.lower().count("to")
print("Count of 'to':", to_count)

# Find "or": sentence.find("or") = _____
or_index = sentence.find("or")
print("First 'or' at index:", or_index)

# Count "o": sentence.count("o") = _____
o_count = sentence.lower().count("o")
print("Count of 'o':", o_count)
print("="*40)


text = "Hello, World! How are you?"
# Remove extra spaces (hint: split and join):
# Step 1: text.split() = _____________
result = text.split()

# Step 2: " ".join(result) = _____________
result = " ".join(result)
print("Cleaned text:", result)
