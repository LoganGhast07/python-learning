colors = ["red", "blue", "green"]
# Write your for loop here
for color in colors:
    print(color)

print("="*40)

numbers = [3, 7, 2, 9, 1]
# Your code here
# Expected output: 6, 14, 4, 18, 2
for number in numbers:
    print(number * 2)
    
print("="*40)


words = ["cat", "elephant", "dog", "rhinoceros"]
total_chars = 0
# Your code here to calculate total_chars
# Expected output: total_chars = 26
for word in words:
    total_chars += len(word)
print("Total characters:", total_chars)
print("="*40)