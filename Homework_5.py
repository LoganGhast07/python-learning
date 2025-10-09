"""
CS1300 - Homework #5: Advanced Control Structures
Name: Logan Ghast
Date: 10/6/2025
Description: Advanced conditional logic and validation
"""

print("=== SMART THERMOSTAT SYSTEM ===")
# Get inputs
current_temp = float(input("Current temperature (F): "))
desired_temp = float(input("Desired temperature (F): "))
hour = int(input("Current hour (0-23): "))
season = input("Season (summer/winter/spring/fall): ").lower()
# YOUR CODE HERE
# 1. Check if current temp is in comfortable range using chained comparison
# 2. Determine if it's night time (22-6)
# 3. Apply seasonal restrictions
# 4. Calculate actual target temperature after adjustments
# 5. Calculate time to reach target
# 6. Determine energy efficiency (Excellent/Good/Fair/Poor)
# Hint: Use chained comparisons like: 68 <= current_temp <= 76
# Hint: Night check needs: hour >= 22 or hour <= 6
#1. Get current temperature, desired temperature, time of day (0-23), and season
#2. Use chained comparisons to check temperature ranges
#3. Apply these rules:
#Comfortable range: 68-76°F
#Night hours: 22-6 (reduce by 3 degrees for energy saving)
#Summer: Never below 72°F
#Winter: Never above 70°F
#4. Calculate adjustment needed and estimated time to reach target (2 degrees per hour)
#5. Show energy efficiency rating
#Your Code Here
# 1. Check if current temp is in comfortable range using chained comparison
is_comfortable = 68 <= current_temp <= 76
# 2. Determine if it's night time (22-6)
is_night = hour >= 22 or hour <= 6
# 3. Apply seasonal restrictions
if season == "summer" and desired_temp < 72:
    desired_temp = 72
elif season == "winter" and desired_temp > 70:
    desired_temp = 70
# 4. Calculate actual target temperature after adjustments
if is_night:
    desired_temp -= 3
    if desired_temp < 65:
        desired_temp = 65
adjustment = desired_temp - current_temp
# 5. Calculate time to reach target
if adjustment == 0:
    time_to_target = 0
elif adjustment > 0:
    time_to_target = adjustment * 30
else:
    time_to_target = abs(adjustment) * 15
# 6. Determine energy efficiency (Excellent/Good/Fair/Poor)
if abs(adjustment) <= 2:
    efficiency = "Excellent"
elif abs(adjustment) <= 5:
    efficiency = "Good"
elif abs(adjustment) <= 10:
    efficiency = "Fair"
else:
    efficiency = "Poor"
# Output results
print(f"Adjusted Target Temperature: {desired_temp}°F")
print(f"Time to Reach Target: {time_to_target} minutes")
print(f"Energy Efficiency: {efficiency}")
print("="*40)




print("=== PASSWORD SECURITY ANALYZER ===")
password = input("Enter password to analyze: ")
# Initialize score
score = 0
# YOUR CODE HERE
# Use conditional expressions for each check
# Example: length_points = 30 if len(password) >= 16 else 20 if len(password) >= 12 else 10 if len(password) >= 8 else 0
# Check length (use conditional expression)
#Length: 8+ chars (10 points), 12+ chars (20 points), 16+ chars (30 points)
#Uppercase letters (15 points)
#Lowercase letters (15 points)
#Numbers (15 points)
#Special characters (15 points)
#No common patterns like "123", "abc", "qwerty" (10 points)
#If common pattern minus 10 points
#Sum up total score
length_points = 30 if len(password) >= 16 else 20 if len(password) >= 12 else 10 if len(password) >= 8 else 0
uppercase_points = 15 if any(c.isupper() for c in password) else 0
lowercase_points = 15 if any(c.islower() for c in password) else 0
digit_points = 15 if any(c.isdigit() for c in password) else 0
special_points = 15 if not password.isalnum() else 0
common_patterns = ["123", "abc", "qwerty", "password", "letmein"]
pattern_points = -10 if any(pat in password.lower() for pat in common_patterns) else 10
# Sum up total score
total_score = (length_points + uppercase_points + lowercase_points + digit_points + special_points + pattern_points)
# Determine strength level
if total_score >= 80:
    strength = "Very Strong"
elif total_score >= 60:
    strength = "Strong"
elif total_score >= 40:
    strength = "Moderate"
else:
    strength = "Weak"
# Output results
print(f"Password Strength: {strength}")
print(f"Total Score: {total_score}/100")
#Provide recommendations
if length_points < 30:
    print("Consider using a longer password (16+ characters).")
if uppercase_points == 0:
    print("Add uppercase letters to your password.")
    
if lowercase_points == 0:
    print("Add lowercase letters to your password.")
if digit_points == 0:
    print("Add numbers to your password.")
if special_points == 0:
    print("Add special characters to your password.")
print("="*40)

print("=== GRADE VALIDATION SYSTEM ===")
# Get four test scores
test1 = float(input("Test 1 score: "))
test2 = float(input("Test 2 score: "))
test3 = float(input("Test 3 score: "))
test4 = float(input("Test 4 score: "))
# YOUR CODE HERE
# 1. Validate each score is 0-100 using chained comparisons
# 2. Check for suspicious patterns
# 3. Use truth table logic:
# valid_range AND not_suspicious AND not_identical
# 4. If valid, calculate average, highest, lowest, improvement
# 5. Provide appropriate feedback
# Example validation:
all_valid_range = (0 <= test1 <= 100) and (0 <= test2 <= 100) and (0 <= test3 <= 100) and (0 <= test4 <= 100)
# Check if all identical
all_identical = (test1 == test2 == test3 == test4)
# Check for huge jumps
huge_jump = (abs(test2 - test1) > 30) or (abs(test3 - test2) > 30) or (abs(test4 - test3) > 30)
# Combine validations using truth table logic
#Your Code Here
is_valid = all_valid_range and not all_identical and not huge_jump
if is_valid:
    average = (test1 + test2 + test3 + test4) / 4
    highest = max(test1, test2, test3, test4)
    lowest = min(test1, test2, test3, test4)
    improvement = test4 - test1
    print(f"Average Score: {average}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Improvement from Test 1 to Test 4: {improvement}")
    if improvement > 0:
        print("Great job improving!")
    elif improvement < 0:
        print("Scores declined. Consider reviewing material.")
    else:
        print("No change in scores.")
else:
    print("Invalid scores detected.")
    if not all_valid_range:
        print("Scores must be between 0 and 100.")
    if all_identical:
        print("All test scores are identical, which is suspicious.")
    if huge_jump:
        print("There are suspiciously large jumps between test scores.")
        
