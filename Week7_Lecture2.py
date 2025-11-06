# Start with:
fruits = ["apple", "banana"]
# Use extend() to add:
# - ["orange", "grape"]
# Print the result
# Now create a new list 'numbers' with [1, 2]
# Use extend to add [3, 4, 5]
# Print the result
fruits = ["apple", "banana"]
fruits.extend(["orange", "grape"])
print(fruits)
# Now create a new list 'numbers' with [1, 2]
numbers = [1, 2]
# Use extend to add [3, 4, 5]
numbers.extend([3, 4, 5])
# Print the result
print(numbers)

print("="*40)


# Predict the output, then test:
# Case 1:
list1 = [1, 2]
list1.append([3, 4])
# What is list1 now?
# Case 2:
list2 = [1, 2]
list2.extend([3, 4])
# What is list2 now?
# Case 3:
list3 = ['a']
list3.extend('bc')
# What is list3 now?
#Your Code Here
print("Case 1:", list1) # Expecting [1, 2, [3, 4]]
print("Case 2:", list2) # Expecting [1, 2, 3, 4]
print("Case 3:", list3) # Expecting ['a', 'b', 'c']
print("="*40)



# You have three sources of data:
morning_temps = [65, 68, 70]
afternoon_temps = [75, 78]
evening_temps = [72, 70, 68]
# Create 'all_temps' list that combines all three
# Try three approaches:
# 1. Using extend() multiple times
# 2. Using + operator
# 3. Using += operator
# Which modified the original? Which created new lists?

all_temps1 = []
all_temps1.extend(morning_temps)
all_temps1.extend(afternoon_temps)
all_temps1.extend(evening_temps)
print("All Temps (extend):", all_temps1)

all_temps2 = morning_temps + afternoon_temps + evening_temps
print("All Temps (+):", all_temps2)

all_temps3 = []
all_temps3 += morning_temps
all_temps3 += afternoon_temps
all_temps3 += evening_temps
print("All Temps (+=):", all_temps3)
print("="*40)