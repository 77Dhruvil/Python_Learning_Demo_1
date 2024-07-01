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

class A:

    def methodA(self):
        return "Method A"

class B(A):

    def methodB(self):
        return "Method B"

class C(A):

    def methodC(self):
        return "Method C"

class D(B, C):

    def methodD(self):
        return "Method D"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())
