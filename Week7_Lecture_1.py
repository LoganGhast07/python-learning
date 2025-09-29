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