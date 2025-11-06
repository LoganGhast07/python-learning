"""
Problem 1: String Processing
"""

full_name = "John Michael Smith"
email = "john.smith@university.edu"
phone = "555-123-4567"

print("="*40)

#Task 1.1: Extract and print first name only
first_name = full_name.split()[0]
print("First Name:", first_name)

#Task 1.2: Extract and print the last name only
last_name = full_name.split()[-1]
print("Last Name:", last_name)

#Task 1.3: Create and print initials
initials = ''.join([name[0] for name in full_name.split()])
print("Initials:", initials)

#Task 1.4: Check if the email contains "university"
contains_university = "university" in email
print("Email contains 'university':", contains_university)

#Task 1.5: Replace all dashes in phone with spaces and print
formatted_phone = phone.replace('-', ' ')
print("Formatted Phone:", formatted_phone)
print("="*40)


"""
Problem 3: Movie review number management
Manage a list of movie review numbers
"""

#Task 3.1: Create a list with these movie review numbers
numbers = [3, 5, 4, 3, 2, 1, 3]

#Task 3.2: Add a new review number of 4 to the end
numbers.append(4)
print("After appending 4:", numbers)

#Task 3.3: The third review was enterd wrong, change it to 3
numbers[2] = 3
print("After correcting third review to 3:", numbers)

#Task 3.4: Remove the review number 1 from the list
numbers.remove(1)
print("After removing review number 1:", numbers)

#Task 3.5: Insert a review number of 3 at position 2
numbers.insert(2, 3)
print("After inserting 3 at position 2:", numbers)

#Task 3.6: Create and print a sublist of the first 3 numbers
sublist_first_3 = numbers[:3]
print("Sublist of first 3 numbers:", sublist_first_3)

#Task 3.7: Print:
# - How many movie review numbers
# - The first review number
# - The last review number
print("Total number of reviews:", len(numbers))
print("First review number:", numbers[0])
print("Last review number:", numbers[-1])




