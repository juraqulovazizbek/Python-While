ball = 0

while True:
    print("(+) yoki (stop) lardan birini kiriting!")
    answer = input("Tanlovni kiriting: ")

    if answer == "+":
        ball += 10
        print("Sizga ball qo`shildi! ")

    elif answer == "stop":
        print("Ball yigi`sh to`xtatildi! ")
        print(f"To`plangan ball {ball}")
        break
    else:
        print("Faqat `+` yoki `stop` yozing!")
        break
