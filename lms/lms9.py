# lms8


from random import randint
x  = randint(1,10)
print(x)
user_num = 0
attemt = 0 

while True:
    print('Я загадал число от 1 до 10, угадай его:')
    user_num = int(input("Ваша догодка :"))
    attemt +=1 
    if user_num == x:
        print("Молодец, ты угадал число!\nКоличество твоих попыток:" + str(attemt) + "Спасибо за игры:")
        break
    elif user_num > x:
        print("Мое число меньше.")
    elif user_num < x :
        print("мое число больше.")
# 2
 
# number = 50

# blacklist = ["Нурсултан", "Вероника", "Айкена"]

# user_name = input("Введите имя пользователя: ")


# while True:
#     if user_name in blacklist:
#         print("Вы в черном списке.")
#         break

#     chislo = int(input())

#     if chislo == number:
#         print('Ты угадал!')
#         break
#     elif chislo < 50:
#         print('Ты был очень близок!')
#     elif  chislo >50:
#         print('ты был далеко ')