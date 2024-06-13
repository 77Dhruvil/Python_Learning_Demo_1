# Condition and Loops

# age > 18  #Then allow to go to club
# age < 18  # Not allow to go to club

# If,else

# if condition:
#    code to be executed
# else:
#    code to be executed when condition is false

# Wrinte a program to take a user age and let him know if he can go to club or not

age = int(input("Enter your age: "))

if age > 18:
    print("you can go to club")
else:
    print("you can not go to club")

a1 = 8
if a1 == 5:
    print("Abc")
else:
    print("xyz")

a=10
b=45
x=10
y=67

result1 = (a>b)
result2 = (x<y)
result3 = result1 and result2
print(result3)



a1= int(input("Enter a number1: "))
b1= int(input("Enter a number2: "))

#max
# result = max(a,b)
# print(result)

if a>b:

    print("a is greater")

else:


    print("b is greater")