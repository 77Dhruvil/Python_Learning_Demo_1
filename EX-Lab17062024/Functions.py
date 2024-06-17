# Function
# Block of code- That can be excute or reused.
# Define
# Call

# Built in functions
# Which are created by python guys.
# result = max(2,3)
#
# #
#
# def say_hello(): #No return type and no parameter
#     print("Hello")
#
# say_hello()
#
# #1st way
# def say_hello_arg(name): #No return type with argument
#     print("Hello",name)
#
# say_hello_arg("Dhruvil")
#
# #2nd way
# def say_hello_arg_default(name="Devil"): #No return type with default argument
#     print("Hello",name)
#
# say_hello_arg_default()
#
# #3rd way
# def say_hello_arg_default(name="Dhru"): #No return type with default argument
#     print("Hello",name)
#
# say_hello_arg_default("Khush")
#
# #4th way
#
# def say_hello_arg_default(name="Dhruvil"): #No return type with default argument
#     print("Hello",name)
#
# say_hello_arg_default(name="Shloku")

#
# def sum_num_arg_returns(a, b):  # arguments with return type
#     return a + b
#
#
# result = sum_num_arg_returns(3,4) #1st way to pass
# result1 = sum_num_arg_returns(a=3 , b=4) #2nd way to pass
# print(result)
# print(result1)

#
# def f1(a,b,c):
#     return a+b+c
# result = f1(3,4,5)
# print(result)


#args
#
# print("abc","def","ghi")
#
# def sum3(a,b,c): #1st way to use
#     return a+b+c
#
# result = sum3(2,4,5)
# print(result )
#
# def sum3(a=1,b=2,c=2): #2nd way to use
#     return a+b+c
#
# result= sum3()
# print(result)

# def sum3(a=10,b=10,c=10): #3rd way to use , in that A VALUE 2 and other value 10 10 taken
#     return a+b+c
#
# result = sum3(a=2)
# print(result)
#
# def sum3(a=10,b=10,c=10): #3rd way to use , in that A VALUE 2 and other value 10 10 taken
#     return a+b+c
#
# result = sum3(3) #4th way to use , in that DEFAULT 1st value taken 2 other are 10 10
# print(result)


#
# def print_args(*args):
#     for i in args:
#         print(i ,end="-")
#
# print_args("Devil","Sunny")
#
# #*args is a list
# a= [1,2,3,4,5]
# for i in a:
#         print(i)
#

#
# def make_pizza(*brands):
#     for brand in brands:
#         print(brand)
#
# Dhruvil = make_pizza("Cheezy")
# Khush = make_pizza("margerita" , "garlic bread")

#Dictonary
d = {"Dhruvil" : "patel"}
print(d)

#
def make_pizza(*brands,base):
    print(brands,base)

Dhruvil = make_pizza("Dhru" , "Sunny" , base = "Khush")