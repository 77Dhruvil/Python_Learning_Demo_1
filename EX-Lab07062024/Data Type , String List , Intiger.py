print("Helllo World")

print(2 + 2)
print(2 * 2)
print(2 / 2)
print(2 - 2)

print("Hello", "Dhruvil", "Patel")
print("Hello Dhruvil", "Patel", sep="-")
print("Hello", "Dhruvi patel", end="\n")
print(123)

print(max(11,11.34,11.35,2345,-2345,-99999))

first_name = input("Enter your first name :")
last_name = input("Enter Your last name :")
print("My first name is" , first_name , "My last name is" , last_name)

name="Dhruvil"
print(name)
print(type(name))

age = 25
print(age)
print(type(age))

pi=3.24
print(pi)
print(type(pi))

isMale = True
print(isMale)
print(type(isMale))


# Advance Data Tyoes in the python
# List , Tuple , Set , Dictionary

num1 = input("Enter the first number :")
num2 = input("Enter the second number :")

print(num1 + num2)
print(int(num1) + int(num2))
print(type(num1))


pi=3.14
print(pi)
print(type(pi))

i=10
i1=12
print(i1/i)
print(type(i1/i))


# Strings - There are three types of the strings '',"",""" """,
name = 'Dhruvil'
print(name)

name = "Dhruvil"
print(name)

name = """Hello My name is Devlil
i am the good boy and also very
hardworking person ...

..
.

.
.
..
"""
print(name)

dir = "c:\nomdir\dhruvil\dir"
dir1 = r'c:\nomdir\dhruvil\dir'
print(dir)
print(dir1)


first_name = "Dhruvil"
last_name = "Patel"
print(first_name + " " + last_name)
print(first_name,last_name)
#f is used for formatting
#{} placeholder
print(f'Your full name is {first_name} {last_name}')

print(2*1)
num = 90
print(f'The number is {num*1}')
print(f'The number is {num*2}')
print(f'The number is {num*3}')

num=5
print(f'The number is {num}*1={num}')
print(f'The number is {num}*2={num*2}')
print(f'The number is {num}*3={num*3}')
print(f'The number is {num}*4={num*4}')
print(f'Then number is {num}*5={num*5}')

B=1
print(f'The number is {B}*1={B}')
print("2*{}={},{}".format(B,B*2,3))

#Strings
#Functions - Repeat a task - You can use a function.
# print() , input , type() , format() , max , min , id() , sum () , avg ()

name = "Dhruvil"
print(name)
print(type(name))
print(len(name))
print(id(name))
print(name.upper())
D= name.count('D')
print(D)
print(name[1])


name = "Dhruvil patel is not a good person"
print(len(name))
print(type(name))
print(name[-1])


val = None
print(val)

name=""
print(name)
name = None
print(name)
name = "Dhruvil"
print(name)
print(id(name))
print(type(name))

#Lists

shopping_list = ["Bread" , "Butter" , "Pani-puri"]
print(shopping_list)
print(type(shopping_list))
print(len(shopping_list))
print(id(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])
shopping_list.append("curd")
print(shopping_list)
shopping_list.insert(1,"jam")
print(shopping_list)
shopping_list.extend(["Chips" , "Salt"])
print(shopping_list)
shopping_list.remove("Bread")
print(shopping_list.pop())
print(shopping_list.index("Butter"))
shopping_list.reverse()
shopping_list.sort()
print(shopping_list)
shopping_list[0]="Devil"
print(shopping_list)

my_list = [1,3.14,True,"Devil"]
print(my_list)
print(type(my_list))

#Escap Sequence
print("HEllo \"World\"")
print("Hello \nWorld")
print("Hello \tworld")
print("Hello \bworld")