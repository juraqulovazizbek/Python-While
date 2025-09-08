from getpass import getpass
 
parol = ("python123")

while True:
    new = input("parol kiriting: ")
    if new == parol:
        print ("xush kelibsiz")
        break
    else:
     print("Xato! Qayta urinib ko‘ring.")