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
#
#
#  # Create object for the person class
# # ObjectRef = Object - it is className()
# surya = person()
# surya.name = "Surya Kumar"
# surya.talk()
#
# Ritika = person()
# Ritika.name = "Ritika"
# Ritika.walk()

class Dog:
    name = None
    id = None

    #Constructor
    # USe the initialize the values for the attributes

    def sleep(self):
        print("I am sleeping")

dog1 = Dog()
print(dog1.name)
dog1.name = "Tom"
print(dog1.name)
dog1.sleep()

dog2 = Dog()
print(dog2.name)
dog2.name = "Scooby"
dog2.sleep()
