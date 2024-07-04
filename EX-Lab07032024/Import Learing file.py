# from ExceptionHandling import main,f1,f2,f3
# f1()
# f2()
# f3()
# main()
#
# if __name__ == "__main__":
#  main()

##############################################
# import os
# print(os.getcwd())
# cwd = os.getcwd()
# file = open("../Own Learning/data.txt", "r")
# content = file.read()
# print(content)
# file.close()
#
# #############################################################

try:
    file = open("Dhruvi.txt","r")
    content = file.read()
    print(content)

except Exception as e:
    print("I am not able to find the file")

finally:
    try:

        file.close()
        print("Close the file")

    except NameError as Devil:

        print("Devil")
