# #Function Scope
#
# def my_function():
#     a=10
#     print("HELLO")
#     print(a)
#
# my_function()
#
#
# global_a1 = 10
#
# def f1():
#     print (global_a1)
#
# f1()

# #
# def outer():
#     var1 = 30
#     def inner_function():
#         print(var1)
#
#     inner_function()
# outer()

#
#
# numbers = [1,2,3]
#
# def do_something(numbers):
#     numbers.append(4)
#     numbers[2] = 100
#     return numbers
#
# l = do_something(numbers)
# print(l)

# Lambda expression
#To Do the task in one line.

# # This is the 1st way to do
# def double_my_salary(salary):
#     return salary * 2
#
# new_salary = double_my_salary(100)
# print(new_salary)
#
# #This is the 2nd way to do
# double_my_salary = lambda salary: salary * 2
# print(double_my_salary(80))

#
# def sum_two_numbers(a,b):
#     return a+b
#
# o = sum_two_numbers(10, 20)
# print(o)
#
# o_f = lambda a, b: a+b
# print(o_f(10, 20))  # 30_f(10, 20))

# #
# def find_odd_even(number):
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("odd")
#
# find_odd_even(4)
#
# Check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
# print(Check_even_odd(2))

#
#Power**2
#
# pow_function = lambda : int(input("Enter a number: "))**2
# print(pow_function())

# my_list = [1, 2, 3, 4, 5]
#
# #Indexing
# print("Element at index 0:", my_list[0])
# print("Element at index 2:", my_list[2])
#
# #Changing an element
# my_list[2] = 10
# print("List after changing an element at index 1 :",my_list)
#
# #append
# my_list.append(6)
# print("List after appending :",my_list)
#
# #extend
# my_list.extend([7, 8, 9])
# print("List after extending :",my_list)
#
# #
# # #insert
# my_list.insert(3, 11)
# print("List of Inserting ", my_list)
#
# my_copy = my_list.copy()
# print(my_copy)
#
# my_list.clear()
# print("Intial list:",my_list)
# print(my_copy)
#
# #print("Index of 3 in the list:",my_list.index(3))
#
# my_copy.sort()
# print(my_copy)
#
# my_copy.reverse()
# print(my_copy)
#
# print(my_copy[1])
# print(my_copy[2])
#
# my_list = [1, 2, 3, 4, 5]
# my_list.sort()
# print(my_list)
#
# square = [1,4,9,16,25]
#
# if not False:
#     print("Not a square")
# else:
#         print("Square")
#
# # 1st way
# list = [1,2,3,4,5,6,7,8,9,10]
# temp_list=[]
# for i in list:
#     temp = i*2
#     temp_list.append(temp)
# print(temp_list)
#
#
# # 2nd way
# list = [1,2,3,4,5,6,7,8,9,10]
# temp_list=[]
# for i in list:
#     temp_list.append( i*2)
# print(temp_list)

#
# # 1st way
# my_list = [1, 2, 3, 4, 5]
#
# def double_item(num):
#     return num**2
#
# double_list = list(map(double_item, my_list))
# print(double_list)
#
# #2nd way
# my_list = [1, 2, 3, 4, 5]
#
# double_item = lambda num: num**2
#
# double_list = list(map(double_item, my_list))
# print(double_list)
#
# #3rd way
# my_list = [1, 2, 3, 4, 5]
#
# double_list = list(map(lambda num: num**2, my_list))
# print(double_list)


# Tuple : Collection of items

my_Tuple = (1,2,3,4,5,6,7,8,9,10)
my_Tuple[0] = 11
print(my_Tuple)
