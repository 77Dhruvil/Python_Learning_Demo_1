# OS Module
#
# import os
# import math
#
# print(os.name)
# print(os.getcwd())
# # print(math.pi)
# print (os.listdir("C:\\Users\\PATEL\\PycharmProjects\\Python Learning Demo 1\\EX-05072024"))
#
# size = os.path.getsize('Test.txt')
# print(size)
#
# if size != 0:
#     print (" file is present")
# else:
#     print("file does not exist")
#
# mttime = os.path.getmtime('Test.txt')
# print(mttime)
#
# import time
# print(time.gmtime(mttime))
#
# all_dir = os.listdir("C:\\Users\\PATEL\\PycharmProjects\\Python Learning Demo 1\\EX-05072024")
# print(all_dir)

####################################################
#
# import os
#
# for root,dir, files in os.walk("C:\\Users\\PATEL\\PycharmProjects\\Python Learning Demo 1\\EX-05072024"):
#     print("current Dir")

###############################################################

import os

for root ,dir ,files in os.walk("C:\\Users\\PATEL\\PycharmProjects\\Python Learning Demo 1\\EX-05072024"):
        print("Current Dir {root}")
        print("sub Dir Dir {dir}")
        print(f"files Dir Dir {files}")
        print(len(files))