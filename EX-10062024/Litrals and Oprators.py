# Litrels :
# variable_name = Variable_value
import math

name = "Dhruvil"  # Dhruvil is the literal
# variable_name is Know as identifier
# Variable_value is know as literal
# Literals are numeric or non-numeric values
age = 12
pi = 3.14
is_married = False
have_lambo = None
my_list = [1, 2, 3, 4, 5]
my_set = {1, 2, 3, 4, 5, 5}  # Set is collection of unique values
print(my_set)

# Litreals (Escap sequence)
newline_char = '\n'
newline_char = '\t'
newline_char = '\\'
newline_char = '\''
newline_char = '\b'

# Escap Sequence
print("HEllo \"World\"")
print("Hello \nWorld")
print("Hello \tworld")
print("Hello \bworld")

# More different types of Literals

# Boolean Literals
is_married = True
is_Dhruvil_married = False

age = 65 #Decimal

# Binary
age = 0b1101 #Binary

#oct
a = 0o12 #octal

#Hex
a = 0x12 #Hexadecimal

#string
name = 'Dhruvil'

name2 = "patel"

name3 = """Dhruvil Patel is the most 
good person in the history of the 
world ........
...........
..........
..........

........
..........
"""

#Boolean Literals
x = True
Y = False

#Operators

#Assignment Operator
# = - Assign value from right to left
name = "Dhruvil"

# == -> Compare Operator (boolean )

v1 = (1==True)
v2 = (0==False)
print(v1)
print(v2)

age = 65
print(age)

age1 = -1
print(age1)

r = age + age1
print(r)

#Not Operator (boolean)
is_married = True
print(not is_married)

#Is Operator  - Identity operator
a= 5
b= 6
c= False

print(a is b)

my_list  = [1,2,3,4,5]
my_list2 = [1,2,3,4,5]
print(my_list is my_list2)

#is - How? - Conditions


#Arithmetic operators
# - + / * %

a = 180
b = 90
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#Modulus Operator
print(a%b)

print(87 % 10)
#print(a**b)
r = pow(10,2)
print(r)

print(87//10)

#Logical Operator
# and , or , not

x = 10
y = 20

print(x>y)
print(x<y)

a = 10
b = 10

print (a<=b)
print(a==b)

#or Gate
f = False
t = True
print(f and t)
print(f or t)

x = 10
y = 20
result = (x!=y)
print(result)

#Ternary Operator
# condition_if_true if condition else condition_if_false

Dhruvil_marks = 10
Devil_marks = 20

print("Dhruvil is the winner" if Dhruvil_marks > Devil_marks else "Devil is the winner")

if  Dhruvil_marks > Devil_marks:
    print("Dhruvil is the king")

else:
    print("Devil is the king")


#Program - calculate the area  of circle
#input > Radius
#output > area

#data types
# input   > float
# output > float


#core logic > pi*r*r = 3.14
radius = float(input("Enter the radius \n"))
print(math.pi)
area = math.pi*(radius**2)
print(area)


print(math.pi*(float(input("Enter the radius \n"))))
