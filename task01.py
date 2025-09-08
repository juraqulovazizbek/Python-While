from random import randint

son = randint(1, 20)
topildi = False
while not topildi:
    tavakkal =  int(input("son kiriting: "))
    if tavakkal < son:
        print("kattaroq son kiriting ")
    elif tavakkal > son:
        print("kichikroq son kiriting")
    else:
        print("   OOO taxmin TOPILDI..!")
