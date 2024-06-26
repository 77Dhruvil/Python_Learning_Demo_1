# my_dict = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

#for loop
# 1st step
# for k,v in my_dict.items():
#     print(k,v)

#2nd Step
# for k,v in  my_dict.items():
#     if k == 'name':
#         print("Key b name found")
#
#
# op = 'name' in my_dict
# print(op)

#Filters in python

numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
#Filters on the above even
# new_list = list(filter(lambda x: x%2 == 0, numbers))
# print(new_list)

def is_even(num):
    return num%2 == 0
def is_odd(num):
    return num%2 != 0

new_numbers_even = list(filter(is_even, numbers))
print(list(new_numbers_even))

new_numbers_odd = list(filter(is_odd, numbers))
print(list(new_numbers_odd))