# Tuples

# # Real case , Where we tuples
# API_URLSs = ("https://api.example.com", "https://api2.example.com")
# print(API_URLSs[0])
#
# t = tuple()
# print(t)
#
# t1 = tuple(["Hello" , "Dhruvil" , "Patel"])
# print(t1)
#
# del t1
# print(t1)
#
# hero1 = ("Batman", "Bruce Wayne")
# hero2 = ("Spiderman", "Peter Parker")
# main_hero = (hero1, hero2)
# print(main_hero)
# print(main_hero[1])
# print(main_hero[1][0])
#
# x = 10
# q,w,e = (8,9,10)
# print(x)
# print(q)
# print(w)
# print(e)
#
# #Search in tuples
#
# cities = ("London", "New York", "Paris", "Tokyo", "Mumbai")
# print("New York" in cities) # Output: True
# print("Toronto" in cities) # Output: False

# #SET
# a,b,c = (1,2,3)
# t = (1, 2, 3, 1, 2, 3)
# #t.append()
# new_t = t + (1,)
# print(new_t)
#
# my_list = list(t)
# print(my_list)
# my_list.append(4)
# new_t2 = tuple(my_list)
# print(new_t2)

# SET
# Collection of iteams
#
# list_of_unique_items = {1,2,3,4,4,5,5,6,6,7}
# print(list_of_unique_items)
#
# list1 = [45.33,33,45,21]
# set1 = set(list1)
# print(set1)
# print(len(set1))

# t = ("a", "b", "a")
# print(set(t))
#
# set1 = {1, 2, 3}
# set2 = {1,4,5}
# my_set = set1.union(set2)
# my_set1 = set1.intersection(set2)
# my_set2 = set1.difference(set2)
# my_set3 = set2.union(set1)
# my_set4 = set2.intersection(set1)
# my_set5 = set2.difference(set1)
# print(my_set)
# print(my_set1)
# print(my_set2)
# print(my_set3)
# print(my_set4)
# print(my_set5)
#
# set1 = {1,2,3,4,5,6,}
# set2 = {2,3,8}
# subset = set2.issubset(set1)
# print(subset)
#
# set1 = (["Dhruvil" , "Patel" , "Dhruvil."])
# print(len(set1))
#
# for i in set1:
#     print(i)

# set1 = set([1,2,3,4,5,6,
#          7,8,9,10,11,12])
# print(set1)
# print(len(set1))
# set1.remove(5)
# print(set1)
# print(len(set1))
#
# set1.add(15)
# print((set1))
# set1.pop()
# print(set1)
#
#
# def say_hello(name):
#     print("Hello", name)

# Pass

# def something_in_future():
#     # Do something in the future
#     pass
#
# something_in_future()

# Decorators

# def my_decorator(func):
#
#     def wrapper():
#         print("Starting........")
#         print("*************")
#         func()
#         print("**************")
#         print("Ending........")
#
#     return wrapper()
#
# @my_decorator
# def say_hello():
#     print("Hello")
#

# Real example

# import time
# def note_time_decorator (func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print("Time taken " + str(end_time - start_time))
#     return wrapper()
#
# @note_time_decorator
# def logs_function():
#     time.sleep(5)
#     print("print the logs of time taken")
# @note_time_decorator
# def reporting_function():
#     time.sleep(2)
#     print("print the logs of time taken")
#
# def decorator1(func):
#     def wrapper():
#         print("Decorator 1")
#         func()
#     return wrapper
#
#
# def decorator2(func):
#     def wrapper():
#         print("Decorator 2")
#         func()
#     return wrapper
#
#
# @decorator1
# @decorator2
# def say_hello():
#     print("Hello")
#
#
# say_hello()


# Dict
# Key and value
# name : "Dhruvil"
# my_dict1 = {
#     "name": "Dhruvil",
#     "age": 21,
#     "gender": "Male"
#
# }
#
# print(len(my_dict1))
# print(my_dict1["name"])
# print(my_dict1["age"])
# print(my_dict1["gender"])
#
# phone_book = dict(name="Dhruvil", age=21, gender="Male")
# print(phone_book)
# print(phone_book["name"])
# my_dict1["name"] = "Devil"
# print(my_dict1)

#
# my_dict2 = {
#      "name": "Dhruvil",
#      "age": 21,
#      "gender": "Male"
#
# }
#
# print(my_dict2.get("name"))
# print(my_dict2.values())
# print(my_dict2.keys())


my_dict3 = {"a":1 , "b":2 , "c":3 , "a" : 95}
print(my_dict3)
print(len(my_dict3))
print(list(my_dict3))
print(my_dict3.values())
for i in list(my_dict3):
    print(i)

for k,v in my_dict3.items():
    print(k,v)