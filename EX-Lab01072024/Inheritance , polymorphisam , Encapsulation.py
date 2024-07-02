# Inheritance
# Acquireing the attributes and behaviour
#Data mammbers and Methods
###########################################################################################################
#Types of inheritance
#SIngle
#Multiple
#multi-level
#Hybrid
#Hierarchical
####################################################################################################################
#Single Inheritance program

# class grandfather:
#     Key = "TEst@123"
#
#     def grandfather_method(self):
#         return "I am grandfather"
#
# class my_father(grandfather):
#
#     def parent_method(self):
#         return "Parent's method"
#
# parent = my_father()
# print(parent.parent_method())
# print(parent.grandfather_method())
# print(parent.Key)

class Parent:

    gold = "5kg"

    def BHK2(self):
        print("2 BHK flat")
#
# class Child(Parent):
#
#     def BHK3(self):
#         print("3 BHK flat")
#
# Child = Child()
# Child.BHK2()
# Child.BHK3()
# print(Child.gold)
#
# father = Parent()
# father.BHK2()
# #father.BHK3()
# print(father.gold)

####################################################################################################################
#Hierarchical
#
# class father:
#
#     def BHK1(self):
#         print("1 BHK flat")
#
# class Dhruvil(father):
#
#     def BHK2(self):
#         print("2 BHK flat")
#
# class Khush(father):
#     def BHK3(self):
#         print("3 BHK flat")
#
# class Shlok(father):
#     def BHK4(self):
#         print("4 BHK flat")
#
#
# Dhruvil = Dhruvil()
# Dhruvil.BHK1()
# Dhruvil.BHK2()
#
# Khush = Khush()
# Khush.BHK1()
# Khush.BHK3()
#
# Shlok = Shlok()
# Shlok.BHK1()
# Shlok.BHK4()

#####################################################################################################
#multilevel Inheritance
#
# class grandfather:
#
#     key_gold = "TEst@123"
#
#     def BHK1(self):
#         return "1 BHK flat"
#
# class father(grandfather):
#
#     def BHK2(self):
#         return "2 BHK flat"
#
# class son(father):
#
#     mac = "M3pro"
#     def BHK3(self):
#         return "3 BHK flat"
#
#
# son = son()
# print(son.BHK1())
# print(son.BHK2())
# print(son.BHK3())
# print(son.key_gold)
# print(son.mac)
#
# father = father()
# print(father.BHK1())
# print(father.BHK2())
# print(father.key_gold)
#
# grandfather = grandfather()
# print(grandfather.BHK1())
# print(grandfather.key_gold)

################################################################################################

#Multiple Inheritance
#
# class father:
#     def father_money(self):
#         return "Father has 10 lakhs"
#
#     def house(self):
#         return "Father has a house"
#
# class mother:
#     def mother_money(self):
#         return "Mother has 5 lakhs"
#
#     def house(self):
#         return "Mother has a house"
#
# class son(father,mother):
#
#     #Son class with function
#
#     # def house(self):
#     #     return "Son has a house"
#
#     # Son class without function
#
#     pass
#
# son = son()
# print(son.father_money())
# print(son.mother_money())
# print(son.house())

#
# class A:
#
#     def method(self):
#         return "Method A"
#
# class B:
#
#     def method(self):
#         return "Method B"
#
#
# class C(A,B):
#
#     pass
#
#
# C = C()
# print(C.method())


#####################################################################################################

#Hybride Inheritance
#
# class A:
#
#     def methodA(self):
#         return "Method A"
#
# class B(A):
#
#     def methodB(self):
#         return "Method B"
#
# class C(A):
#
#     def methodC(self):
#         return "Method C"
#
# class D(B, C):
#
#     def methodD(self):
#         return "Method D"
#
# d = D()
# print(d.methodA())
# print(d.methodB())
# print(d.methodC())
# print(d.methodD())

################################################################################################

#Polymorphisam

#Method Overriding
#
# class Shape:
#
#     def area(self):
#         print("Area of shape")
#
# class Rectangle(Shape):
#
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# shape1 = Rectangle(3,4)
# print(shape1.area())
#
# shape2 = Circle(10)
# print(shape2.area())
#
# shape3 = Shape()
# print(shape3.area())

#
#
# class Father:
#
#     def home(self):
#         print("1 BHK")
#
# class son (Father):
#
#     def home(self):
#         super().home()
#         print("2 BHK")
#
# Dhruvil = son()
# Dhruvil.home()

##################################################################

#Abstraction
#
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     def __init__(self,name):
#         self.name = name
#
#     @abstractmethod
#     def sound(self):
#         pass
#
#
# class Dog(Animal):
#     def sound(self):
#
#         return "Barking"
#
# class cat(Animal):
#     def sound(self):
#
#         return "Meow"
#
# dog = Dog("Buddy")
# print(dog.sound())
#
# cat = cat("Whiskers")
# print(cat.sound())


#

from abc import ABC, abstractmethod

class ATB(ABC):
    @abstractmethod
    def perfrom_task(self):
        pass
    @abstractmethod
    def perform_task1(self):
        pass

class Dhruvil(ATB):

    def perfrom_task(self):
        return "Performing task"

    def perform_task1(self):
        return "Performing task1"

Devil = Dhruvil()
print(Devil.perfrom_task())
print(Devil.perform_task1())
