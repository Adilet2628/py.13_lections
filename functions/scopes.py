# области видимости и пространство имен (scopes)
# техналогия которая определяет контекст имени, в рамках которого мы можем уу использовать

# built-ins (встроеная область видимости )->print,len.__global(глобальная )-область одного файла enclosed(не локальная (замкнутая )),nonlocal
# local (локальная ) -> 

# x=200
# def myfanc():
#     print(x)
#     a=300
#     print(a)
#     return a 
# myfanc()

# a = 10 #global
# print# built_in

# def hello():#global
#     a = 'hello'
#     print(a,'local inside in func')
# hello()
# print(a,'global')

# =====================================

# enclosed 
# змкнутое пространство имен - локальное пространство , у которого есть внутренее (вложение )локальное пространство 
# x = 'global'
# print(x,'1')
# def enclosed():#global
#     x = 'enclosed'
#     def local():
#         x= 'local'
#         print(x,'3')
#     print(x,'2')
#     local()
#     print(x,'4')
# enclosed()
# print(x,'5')



# global-> позволяет изменять значениу глобальной переменной 
# nonlocal-> позволяет изменять значение не локальной (замкнутой ) переменной находясь внутри локальной области 
# var = 0 

# def increment():# LEGB
#     global var
#     var+=1
#     print(var)
# increment()

# increment()
# increment()







# def  counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num+=1 
#         return num
#     return increment    
# c_steps = counter()
# c_squats=counter()
# print(c_steps())
# print(c_steps())
# print(c_steps())
# print(c_steps())
# print(c_steps())
# print(c_squats())
# print(c_squats())
# print(c_squats())
# print(c_steps())
# print(c_steps())
# print(c_steps())


# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num+=1 
#         return num
#     return increment    
# def showStats(heroes,walkers):
#     print()
#     print(f'john snow ты убил : \n\tгероев:{heroes}\n\tбелых ходоков:{walkers}')
#     print()
# c_heroes = counter()
# c_walkers = counter()
# heroes=0
# walkers=0
# print('приветствую вас, король севера john snow,в игре престолов ')
# while True:
#     print('тебе доступны следующие действия:')
#     print('1-убить героя, 2- убить ходока , 3-статистика,4-выйти из игры')
#     choice = input ('введите что хотите сделать: ').strip()
#     if choice == '1':
#         heroes = c_heroes()
#         print('вы обезглавили Ланистера !')
#     elif choice == '2':
#         walkers = c_walkers()
#         print('вы убили белого ходока ')
#     elif choice == '3':
#         showStats(heroes,walkers)
#     elif choice == '4':
#         print('bye bye')
#         break
"""
 У Ирины футболки 2 цветов. Ирина одевает красную футболку в чётные числа месяца, а синюю в нечётные. Напишите программу, которая по введённому числу месяца определяет какую футболку нужно одеть Ирине сегодня.
"""

# a = int(input('введите число: '))
# def ul(a):
#     if a <= 30:
#         if a % 2 == 0:
#             return 'красная'
#         elif a % 2 != 0:
#             return 'синяя'   
#         else:
#             return 'ошибка'
#     else:
#         return 'ошибка'

# print(ul(a))
"""
Пользователь должен ввести 2 целых числа, Вам необходимо проверить делится ли первое число на второе. Вывести результат, а также остаток от деления (если есть)
"""
# a=int(input('введите число:'))
# b=int (input('введите второе число:')) 
# if a % b == 0:   
#     print(a/b)
# elif a % b != 0:
#     print(f'целое ')
# else:
#     print('ошибка!!!')











# lms task7


def pi():
    what = input ("Что будем делать? (+,-,*,/,%):")
    a = float(input("Ведите первое число:"))
    b = float(input("Ведите второе число:"))
    if what == "+":
        c = a  + b
        return("Результат:" + str(c))
    if what == "-":
        c = a - b
        return("Результат:" + str(c))   
    if what == "*":
        c = a * b
        return("Результат:" + str(c))
    elif what == "/":
        c = a / b
        return("Результат:" + str(c))
    else:
        return('oshibka')
print(pi())






# №1
# while True:
   
#     def summa_n(a):
#         b = int(input('введите число:'))
#         a=range(1,b+1)
#         a=sum(a)
#         return a
# print(summa_n(a))   


# №4
# while True:
#     a = input('введите число: ')
   
#     if a != '0':
#         print(a[::-1])
#     elif a == '0':
#         print('bye bye')
#         break       
#     else:
#         print('ошибка')  
# 
# №5  
# a= int(input('монет по 1 копейке :'))
# b= int(input('монет по 5 копеек: '))
# c = int(input('монет по 10 копеек:'))
# d = int(input('монет по 50 копеек:'))
# b1 = b * 5
# c1= c * 10
# d1= d * 50
# a1= (a+b1+c1+d1) / 100
# print(f'всего у нас {a1} руб')





































































































































