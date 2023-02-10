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




