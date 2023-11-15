# a=int (input(':===='))
# if a == "6":
#     print('угадал')
# elif a >= '6':
#     print('ты был далек ')   
# elif a <= '6 ':
#     print('ты был близок ')


# a =(input('угадай число от 1 до 10 :'))
# if a == 6:
#     print('угадал ')
# elif a >= 6:
#    print('Далеко')
# elif a >= 6:
#     print('близко')
    
# else:
#     print('Воопше титон! ')



# Вот пример программы, которая реализует игру "Угадай число" с использованием указанных условий:


blacklist = ["Нурсултан", "Вероника", "Айкена"]
num = 42

def game():
    user_name = input("Как вас зовут? ")
    if user_name in blacklist:
        print(user_name + ", ты не являешься студентом, тебе данной программой-игрой пользоваться нельзя!")
    else:
        guess = int(input("Угадай число!: "))
        if guess - num < 10 and guess - num > -10:
            print("Ты был очень близок")
        elif guess > num + 10 or guess < num - 10:
            print("Ты был далек")
        else:
            print("Ты угадал!")

game()




































































































