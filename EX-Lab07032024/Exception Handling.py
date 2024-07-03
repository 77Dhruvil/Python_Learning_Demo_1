#Exception Handling

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

try:

    file = open('Dhruvi.txt','r')
    print(file.read())

except FileNotFoundError as e:

    print(" I am not able to find file ")

finally:
    file.close()