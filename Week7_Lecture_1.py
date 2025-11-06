# Create a list called 'colors' with three color names

# Create a list called 'numbers' with the values 10, 20, 30

# Print both lists
colors = ['red', 'green', 'blue']
numbers = [10, 20, 30]
print("Colors:", colors)
print("Numbers:", numbers)
print("="*40)


# For each variable, predict if it's mutable or immutable:
a = 42 # Mutable or Immutable? Immutable
b = "Python" # Mutable or Immutable? Immutable
c = [1, 2, 3] # Mutable or Immutable? Mutable
d = 3.14 # Mutable or Immutable? Immutable
e = True # Mutable or Immutable? Immutable
# Test your predictions by trying to change them
#Your code here
print("Before change:")
print("a:", a) 
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
a = 100 # Immutable
b = "Java" # Immutable
c.append(4) # Mutable
d = 2.71 # Immutable
e = False # Immutable
print("After change:")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
print("="*40)


# Create a string variable called 'greeting' with value "Good"
# Try to add " Morning" to it two ways:
# 1. Using + (creating new string)
# 2. Try to modify the first character to 'F' (will fail)
# Create a list called 'temps' with values [72, 75, 78]
# 1. Change the first element to 70
# 2. Print to verify it changed
temps = [72, 75, 78]
temps[0] = 70
print("Temps:", temps)
greeting = "Good"
greeting = greeting + " Morning" # Using +
print("Greeting after +:", greeting)
try:
    greeting[0] = 'F' # Trying to modify first character (will fail)
except TypeError as e:
    print("Error:", e)
print("="*40)




# Without using loops:
# 1. Create a list of the first 10 even numbers (use range and list)
# 2. Create a checkerboard pattern: [0,1,0,1,0,1]
# 3. Create a list that contains three empty lists
# 4. Create a list from the string "1,2,3" that gives [1, 2, 3]
# Hint for #4: Use split() then convert strings to integers manually
even_numbers = list(range(0, 20, 2))
checkerboard = [0, 1] * 3
empty_lists = [[] for _ in range(3)]
string_list = "1,2,3".split(',')
int_list = [int(num) for num in string_list]
print("Even Numbers:", even_numbers)
print("Checkerboard:", checkerboard)
print("Empty Lists:", empty_lists)
print("Integer List from String:", int_list)
print("="*40)



# Given these lists:
list1 = [10, 20, 30, 40, 50]
list2 = []
list3 = [100]
# Write code to:
# 1. Safely print the first element of each list (handle empty)
# 2. Safely change the last element to 999 (if it exists)
# 3. Swap first and last elements of list1
# 4. Calculate the middle index of list1 and print that element
for lst in [list1, list2, list3]:
    if lst:
        print("First element:", lst[0])
    else:
        print("List is empty.")
for lst in [list1, list2, list3]:
    if lst:
        lst[-1] = 999
for lst in [list1, list2, list3]:
    print("List after changing last element if exists:", lst)
if len(list1) >= 2:
    list1[0], list1[-1] = list1[-1], list1[0]
    print("List1 after swapping first and last:", list1)
if list1:
    middle_index = len(list1) // 2
    print("Middle element of list1:", list1[middle_index])
print("="*40)