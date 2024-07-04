#Exception Handling
import __main__


# print("Start!")
#
# try:
#     a = int(input("Enter the num1"))
#     b= int(input("Enter the num2"))
#     c = a/b
#     print("Result Div is ",c)
#
# except Exception as e:
#     print(e)
#     print("please enter Intiger value")
#
# print("End!")

#########################################################################################################

#Try , except and finally
#
# try:
#     num1 = int(input("Enter the num1: "))
#     num2 = int(input("Enter the num2: "))
#     result = num1 / num2
#     print(result)
# #
# # except Exception as e:
# #     print(e)
#
# except ValueError as e1:
#     print(e1)
# except ZeroDivisionError as e2:
#     print(e2)
#
# else:
#     print(f'Result is {result}')
#
# finally:
#     print("Dhruvil patel")

##############################################################################################

#FILE IO
#
# with open('Dhruvil.txt','r' )as  file:
#     print(file.read())
#     file.close()
#
# #
# import os.path
# try:
#
#     file = open('Dhruvill.txt','r')
#     print(file.read())
#
# except FileNotFoundError as e:
#
#         print(" I am not able to find file ")
#
#
#
# finally:
#     print("Close the file")
#
#     try:
#         file.close()
#     except NameError as e1:
#         # print(e1)

######################################################################################################
#
# class XYZ:
#
#     def f1(self):
#         try:
#             a = int(input("Enter a number\n"))
#         except Exception as e:
#             print("Enter int only value a ")
#         else:
#             print(a)
#         finally:
#             print("Any how i will be printed")
#
# x = XYZ()
# x.f1()


####################
#
# class my_custom_exception(Exception):
#     def __init__(self,message):
#         self.message = message
#         super().__init__(self.message)
#
# balance = 100
# withdraw = int(input("Enter the amount to withdraw: "))
# if withdraw > balance:
#     raise my_custom_exception("Insufficient balance")
# else:
#     print(f"Remain balance  {balance- withdraw} ")

#################################################################
#
# def main():
#     print("Start!")
# main()

###################################################################
#
# def this_is_my_main_function():
#     print("I am main function")
#
# if __name__ == "__main__":
#     this_is_my_main_function()

##########################################################################

def f1():
    print("f1")

def f2():
    print("f2")

def f3():
    print("f3")

def f4():
    print("f4")

def f5():
    print(f5)

def main():
    print("main")

if __name__ == "__main__":
    main()
    f1()
    f2()
    f3()
    f4()
    f5()