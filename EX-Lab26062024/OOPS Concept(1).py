# class person:
#
#     # Attributes
#     name = None
#     ID = None
#     Age = None
#     Address = None
#     phone_number = None
#
#
#     # Behaviours
#     def talk(self):
#         print("I am talking")
#
#     def another(self):
#         print("I am doing something else")
#
#
#     def sleep(self, name):
#         print("I am method")
#         print("Sleep", name)
#
#
#     def walk(self):
#         print("I am walking")
#
#
#  # Create object for the person class
#
# surya = person()
# surya.name = "Surya Kumar"
# surya.talk()
#
# Ritika = person()
# Ritika.name = "Ritika"
# Ritika.walk()

# class person:
#
#     # Attributes
#     name = None
#     ID = None
#     Age = None
#     Address = None
#     phone_number = None
#
#
#     # Behaviours
#     def talk(self):# No Argument No Return type
#         print("I am talking")
#
#     def sleep(self, name): #1 Arg but No Return type
#         print("I am method")
#         print("Sleep", name)
#
#     def sleep2(self, name):  # Arg with return type
#         print("I am method")
#         return  None
#
#
#
#     def walk(self):
#         print ("I am walking")
#
#     def walk_return(self): #No Argument but Return type
#         return "I am walking"
#


 # Create object for the person class
# ObjectRef = Object - it is className()
# surya = person()
# surya.name = "Surya Kumar"
# surya.talk()
#
# Ritika = person()
# Ritika.name = "Ritika"
# Ritika.walk()
#
# class Dog:
#     name = None
#     id = None
#
#     def __init__(self, name,id):
#             self.name = name
#             self.id = id
#
#
#     #Constructor
#     # USe the initialize the values for the attributes
#
#     def sleep(self):
#         print("I am sleeping"+self.name)
#
# dog1 = Dog("Chow","1")
# dog2 = Dog("Puppy", "2")
#
# print(f'{dog1.name} has ID {dog1.id}')
# print(f'{dog2.name} has ID {dog2.id}')
#
# dog1.sleep()
# dog2.sleep()
#
# class Calc:
#
#     def sum(self, a, b):
#         return a + b
#     def sub(self, a, b):
#         return a - b
#     def mul(self, a, b):
#         return a * b
#     def div(self, a, b):
#         return a / b
#
# object_ref = Calc()
# output = object_ref.sum(10, 20)
# print(output)

class Student:

    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def display(self):
        print(f"Name is {self.name}, Age is {self.age}")


student = Student()
student.display()
