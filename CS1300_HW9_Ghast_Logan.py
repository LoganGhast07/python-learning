#Problem 1: Temperature Converter

def celsius_to_fahrenheit(celsius):

# Your code here:
    return celsius * 9/5 + 32
def fahrenheit_to_celsius(fahrenheit):

# Formula: C = (F - 32) * 5/9
# Your code here
    return (fahrenheit - 32) * 5/9

def temperature_report(temp, scale="C"):

# Your code here
# If scale is "C", show temp in C and converted to F
# If scale is "F", show temp in F and converted to C
    if scale == "C":
        fahrenheit = celsius_to_fahrenheit(temp)
        print(f"{temp:.2f}°C is {fahrenheit:.2f}°F")
    elif scale == "F":
        celsius = fahrenheit_to_celsius(temp)
        print(f"{temp:.2f}°F is {celsius:.2f}°C")
    else:
        print("Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit.")


# Test 1
print(celsius_to_fahrenheit(0)) 
print(celsius_to_fahrenheit(100)) 
# Test 2
print(fahrenheit_to_celsius(32)) 
print(fahrenheit_to_celsius(68)) 


# Test 2
print(fahrenheit_to_celsius(32)) 
print(fahrenheit_to_celsius(68)) 


# Test 3
temperature_report(25) 
temperature_report(77, "F") 
print("="*40)

#Problem 2: Grade Calculator with Multiple Parameters

def calculate_weighted_grade(homework, midterm, final, hw_weight=0.3,
mid_weight=0.3, final_weight=0.4):
    # Your code here
    weighted_grade = (homework * hw_weight) + (midterm * mid_weight) + (final * final_weight)
    return weighted_grade
def get_letter_grade(score):
#Convert numeric score to letter grade
# A: >= 90, B: >= 80, C: >= 70, D: >= 60, F: < 60
# Your code here
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def print_grade_report(name, hw, mid, final):
#Print complete grade report for a student
# Use the other functions to calculate and display:
# - Student name
# - Individual scores
# - Weighted average
# - Letter grade
# Your code here:
    weighted_score = calculate_weighted_grade(hw, mid, final)
    letter_grade = get_letter_grade(weighted_score)
    print(f"Grade Report for {name}:")
    print(f"  Homework: {hw}")
    print(f"  Midterm: {mid}")
    print(f"  Final: {final}")
    print(f"  Weighted Average: {weighted_score:.2f}")
    print(f"  Letter Grade: {letter_grade}")
    
# Test 1: Default weights
grade1 = calculate_weighted_grade(85, 78, 92)
print(f"Grade 1: {grade1}")
 
# Test 2: Custom weights
grade2 = calculate_weighted_grade(90, 85, 80, hw_weight=0.4, mid_weight=0.2,
final_weight=0.4)
print(f"Grade 2: {grade2}") 

# Test 3: Complete report
print_grade_report("Alice Smith", 88, 91, 85)
# Should display formatted report with all information
print("="*40)





#Problem 3: Scope Challenge
# BROKEN CODE - FIX THE SCOPE ISSUES
total_points = 0
bonus_multiplier = 1.1
def add_score(points):
    """Add points to total score"""
    global total_points
    total_points = total_points + points 
    return total_points
def apply_bonus():
    """Apply bonus multiplier to total"""
    global total_points
    total_points = total_points * bonus_multiplier 
def get_final_score():
    #Get the final score
    final = total_points # Is this accessing the right variable?
    return final
# Test your fixes:
add_score(100)
add_score(50)
apply_bonus()
print(f"Final score: {get_final_score()}") # Should print 165.0