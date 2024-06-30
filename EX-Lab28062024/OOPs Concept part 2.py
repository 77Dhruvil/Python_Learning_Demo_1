# class person:
#
#         #Variables
#         name = "Devil"
#         age = None
#
#         #Function define
#         def walk(self):
#             a= 10
#             print("Hi i am method")
#             print("Hi" , self.age)
#
# #Object
# Dhruvil = person()
# Dhruvil.walk()


# class car:
#
#     name = None
#     make = None
#     model = None
#
#
#     def __init__(self , o_name , o_model):
#         self.name = o_name
#         self.model = o_model
#
#     def start_engine(self):
#         print("Starting a car with the name " + self.name)
#         print("Starting a model with the nmae " + self.model)
#
#
# Devil = car(o_name="BMW",o_model="s5")
# Devil.start_engine()


#Web automation Example

# class FoveroLoginpage:
#
#     email = None
#     password = None
#
#     def __init__(self , email , password):
#         self.email = email
#         self.password = password
#
#     def Login_confirm(self):
#         if self.password ==  "Test@123":
#             print("ALlow to Login")
#         else :
#             print("Not allow to login")
#
#
# email = input("Enter the email \n")
# password = input("Enter the password \n")
# Concetto = FoveroLoginpage(email="Devil@gmail.com" , password="Test@123")
# Concetto.Login_confirm()


#Encapsulation

#
# class FoveroLogin:
#
#     def __init__(self,email,password):
#         self.__email = email
#         self.__password = password
#
#
#     def login_confirm(self):
#         if self.__email == "Devil@gmail.com" and self.__password =="123":
#             print("Allow to Enter")
#         else:
#             print("Not Allow")
#
# Dhruvil = FoveroLogin(email="Devil@gmail.com" , password= "123")
# Dhruvil.login_confirm()

#Practical Example
# class BankAccount:
#
#     def __init__(self):
#         self.balance = 0
#         self.__private_var = 100
#
#
#     def public_fn(self):
#         print(self.__private_var)
#
#     def deposite(self,amount):
#         self.balance += amount
#
#     def __withdraw(self,amount):
#         self.balance -= amount
#
#     def __show_balance(self):
#         print("Your balance is " , self.balance)
#
#     def if_you_are_auth(self,flag):
#         if flag:
#             self.__show_balance()
#         else:
#             print("Not Allowed")
#
#     def if_you_are_auth1(self,auth,amount):
#         if auth:
#             self.__withdraw(amount=amount)
#         else:
#             print("Not Allowed")
#
# jp_chase = BankAccount()
# jp_chase.deposite(1000)
# secret_pass = input("Enter Your PIN")
# if secret_pass == "1234":
#     jp_chase.if_you_are_auth(True)
# else:
#     jp_chase.if_you_are_auth(False)
# jp_chase.if_you_are_auth1(True,999)
# jp_chase.if_you_are_auth(True)


#

class password:
    def __init__(self,password):
        self.__password = password
        self.public_var = 10

    def get_password(self,is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Wrong password")
    def set_password(self,password):
        if len(password) > 10:
            self.__password = password
            print("set to corrent", self.__password)
        else:
            print("Not allowed , Week password")

pwd = password("Hacker123")
pwd.get_password(True)
pwd.set_password("dfdsfdsfdsfdsfdsfdsfdsf")
