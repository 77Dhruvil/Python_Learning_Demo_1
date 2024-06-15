# Condition and Loops

# age > 18  #Then allow to go to club
# age < 18  # Not allow to go to club

# If,else

# if condition:
#    code to be executed
# else:
#    code to be executed when condition is false

# Wrinte a program to take a user age and let him know if he can go to club or not

# age = int(input("Enter your age: "))
#
# if age > 18:
#     print("you can go to club")
# else:
#     print("you can not go to club")
#
# a1 = 8
# if a1 == 5:
#     print("Abc")
# else:
#     print("xyz")
#
# a = 10
# b = 45
# x = 10
# y = 67
#
# result1 = (a > b)
# result2 = (x < y)
# result3 = result1 and result2
# print(result3)
#
# a1 = int(input("Enter a number1: "))
# b1 = int(input("Enter a number2: "))
#
# # max
# # result = max(a,b)
# # print(result)
#
# if a > b:
#
#     print("a is greater")
#
# else:
#
#     print("b is greater")
#
# # multi condition
#
# num1 = int(input("Enter a number1: "))
# num2 = int(input("Enter a number2: "))
# num3 = int(input("Enter a number3: "))
#
# if num1 > num2 and num1 > num3:
#     print("num1 is greater")
#
# elif num2 > num1 and num2 > num3:
#     print("num2 is greater")
# else:
#     print("num3 is greater")


# Loops
# Repeat a block of code multiple times

# print a hello world  10 times

# for loop
# for i in range(10):
#     print(i)
#
# for i in range(1,5):
#     print(i)
#
# for i in range(3,10):
#     print(i)

# for i in range(1,10,1):
#     print(i)
#
# for i in range(1,10,2):
#     print(i)
#
# for i in range(1,10,3):
#     print(i)
#
# for i in range(3,9,3):
#     print(i)

# for i in range(1,11):
#     print("Hello -> ",  i)


# While

# i = 0
# while i<5:
#     print(i)
#     i=i+1


# score = int(input("Enter your score: "))
#
# if score >= 90 and score <= 100:
#     print("Grade A")
# elif score >= 80 and score <= 89:
#     print("Grade B")
# elif score >= 70 and score <= 79:
#     print("Grade C")
# elif score >= 60 and score <= 69:
#     print("Grade D")
# elif score >= 0 and score <= 59:
#     print("Grade E")
# else:
#     print("Grade F")
#
# For Loops
# for counter in range (0,100,2): #Even Numbers
#     print(counter)
#
# for counter in range (1, 100, 2): #Odd Numbers
#     print(counter)

# for counter in range (1,100):
#     print(counter)
#     if counter == 5:
#         break
# print("outside of the program")

# Range can be negative also

# for i in range (10,0,-1):
#     print(i)
#
# for i in reversed (range (0,10,1)):
#     print(i)

# Break : Based on the condition it will kick you out of the loop

# for i in range(10):
#     if i == 5 or i ==6 :
#         pass
#     else:
#         print(i)
#
# for i in range (1,10):
#      if i%3 == 0:
#          print (i)
#
#      else:
#          print(i*2)
#

# Multiple condition

# numbers = int(input("Enter a number: "))
# #3.10
# match numbers:
#     case 1:
#         print("one")
#         #break
#     case 2:
#         print("two")
#         #break
#     case 3:
#         print("three")
#         #break
#     case _:
#         print("Not a valid number")
#

# browser = str(input("Enter your browser: "))
# browser = browser.lower()
# match browser:
#     case "chrome":
#         print("Chrome")
#         # break
#     case "firefox":
#         print("Firefox")
#
#     case _:
#         print("Not a valid browser")


#function

# def greet():
#     print("Hello")
#
# greet()

    # def greet():
    #     print("code is executed")
    #     print("Hello")
    #     print("bye")
    # greet()
    # greet()
    # greet()

#pass some info into func

def greet(name):
    print("Hello",name)

greet("Devil")
