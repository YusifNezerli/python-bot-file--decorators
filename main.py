# Write a bot:

# 	bot functions:
		
# 		tarixi de => Indiki tariff qaytarmalidi
# 		ili de => Indiki ili qaytarmalidi
# 		Ayi de => Indiki Ayi qaytarmalidi
# 		saati de => Indiki saati qaytarmalidi
		
# 		"Flan" adli folder yarat => olduğumuz qovluqda verilen adla Folder yaratsın
# 		"Flan" adli folderi sil => olduğumuz qovluqda verilen adla Folderi silsin

# 		Hesabla (misal) => cavab

from datetime import date,datetime
import sys
import os

datetime
now = datetime.now()
time = now.strftime("%H:%M:%S")

today = date.today()


# qovluq yarat

cwd = os.getcwd()



if sys.argv[1] == "tarixi" and sys.argv[2] == "de":
    print("Bu gun:",today )
elif sys.argv[1] == "il":
    print("Il:", today.year)
elif sys.argv[1] == "ay":
    print("Il:", today.month)
elif sys.argv[1] == "saat":
    print("saat:", time)
elif sys.argv[1] == "gun":
    print("Week:",now.strftime("%A"))
elif sys.argv[1] == "qovluq" and sys.argv[2] == "yarat":
    directory = input()
    location = 'D:\my-lesson\python'
    path = os.path.join(location, directory)
    os.mkdir(path)
elif sys.argv[1] == "qovluq" and sys.argv[2] == "sil":
    directory = input()
    location = 'D:\my-lesson\python'
    path = os.path.join(location, directory)
    os.rmdir(path)
elif sys.argv[1] == "hardadi":
    print("Qovluq",cwd)
elif sys.argv[1] =="+":
    X = int(input('Ilk Reqem: '))
    Y = int(input('Ikinci Reqem: '))
    print(X, "+", Y, "=", X + Y)
elif sys.argv[1] == "-":
    X = int(input('Ilk Reqem: '))
    Y = int(input('Ikinci Reqem: '))
    print(X, "-", Y, "=", X - Y)
elif sys.argv[1] == "*":
    X = int(input('Ilk Reqem: '))
    Y = int(input('Ikinci Reqem: '))
    print(X, "*", Y, "=", X * Y)
elif sys.argv[1] == "/":
    X = int(input('Ilk Reqem: '))
    Y = int(input('Ikinci Reqem: '))
    print(X, "/", Y,"=", X / Y)

# update File yaratma

elif sys.argv[1] == "file" and sys.argv[2] == "new":
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



