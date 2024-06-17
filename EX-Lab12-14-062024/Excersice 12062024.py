import math
  # Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

def is_leap_year(year):
    if year % 4 == 0:  # year is divisible by 4
        if year % 100 == 0:  # year is divisible by 100
            if year % 400 == 0:  # year is divisible by 400
                return True  # year is a leap year
            else:
                return False  # year is not a leap year
        else:
            return True  # year is a leap year
    else:
        return False  # year is not a leap year


# Test the function
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Write a program that classifies a triangle based on its side lengths.


# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
#
#
#
# Use an if-else statement to classify the triangle.
#
# 3 Input
#
# side 1, side 2 and side 3
#
# output - Eq, Iso, Scalene -
#
# Eq. = side 1 == side 2 = side 3

def classify_triangle(a, b, c):
    if a == b == c:
        return "Eq"
    elif a == b or a == c or b == c:
        return "Iso"
    else:
        return "Scalene"


# Get input from user
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Classify the triangle
classification = classify_triangle(a, b, c)

print(f"The triangle is {classification}.")


# Task - Fibonacci series and Factorial


# 3. Factorial

# n = 5

# 5! -->5*4*3*2*1 -> 120

# 3! -> 3*2*1 -> 6

# 4! -> 4*3*2*1 -> 24

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series


n = int(input("Enter the number of terms: "))
print(fibonacci(n))


# Fibonaci series
# 0,0+1, 0+1+1,

# n = 7

# 0, 1, 2, 3, 5, 8, 13

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series


n = int(input("Enter the number of terms: "))
print(fibonacci(n))

# Leap Year

year = 2024

(year % 4 == 0)
(year % 100 != 0)
(year % 400 == 0)

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")

# tringle

side1 = 3
side2 = 3
side3 = 3

if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

#factorial

n=5

factorial =1
result = math.factorial(n)
print(result)

