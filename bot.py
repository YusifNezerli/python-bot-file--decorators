# Write a bot:

# 	bot updates:
		
# 		bot istediyimiz adda  text file I yaradmalidi
# 		bot file a istediyimiz texti yazmalidi
# 		bot file a istediyimiz tecti ilave elemelidir
# 		bot file in  dahilindeki texti sile bilmelidir


# bot file yaratmaq

import sys
import os


if sys.argv[1] == "file" and sys.argv[2] == "new":
    f = open(input("file name:"),"x")
elif sys.argv[1] == "file" and sys.argv[2] == "clear":
    os.remove(input("file name:"))
elif sys.argv[1] == "file" and sys.argv[2] == "write":
    f = open(input("file name:"), "w")
    f.write(input())
elif sys.argv[1] == "file" and sys.argv[2] == "read":
    f = open(input("file name:"), "r")
    content = f.read()
    print(content)
    f.close()
elif sys.argv[1] == "file" and sys.argv[2] == "add":
    f = open(input("file name:"), "a")
    f.write(input())
elif sys.argv[1] == "file" and sys.argv[2] == "textsil":
    f = open(input("file name:"), "r+")
    f.seek(0)
    f.truncate()






# number duzelme

# l = []
# l.append(input("Mobil number:"))

# def decor(fn):
#     def inner(l):
#         fn("+994" +" "+ c[1]+ c[2] +" " + c[3]+ c[4] + c[5]  +" "+c[6]+c[7] +" "+c[-2:] for c in l)
#     return inner

# @decor
# def number(l):
#     print(*(l))

# number(l)


