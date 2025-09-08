while True:
    son1 = float(input("Birinchi sonni kiriting: "))
    son2 = float(input("Ikkinchi sonni kiriting: "))
    amal = input("Amalni tanlang (+, -, *, /): ")

    if amal == '+':
        print("Natija:", son1 + son2)
    elif amal == '-':
        print("Natija:", son1 - son2)
    elif amal == '*':
        print("Natija:", son1 * son2)
    elif amal == '/':
        if son2 != 0:
            print("Natija:", son1 / son2)
        else:
            print("0 ga bo'lish mumkin emas!")
    else:
        print("Noto'g'ri amal tanlandi!")

    davom = input("Davom etasizmi? (ha/yo‘q): ")
    if davom.lower() != "ha":
        print("Dastur tugadi.")
        break
