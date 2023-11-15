"""
lms task7
"""
# №6
# def pi():
#     what = input ("Что будем делать? (+,-,*,/,%):")
#     a = float(input("Ведите первое число:"))
#     b = float(input("Ведите второе число:"))
#     if what == "+":
#         c = a  + b
#         return("Результат:" + str(c))
#     if what == "-":
#         c = a - b
#         return("Результат:" + str(c))   
#     if what == "*":
#         c = a * b
#         return("Результат:" + str(c))
#     elif what == "/":
#         c = a / b
#         return("Результат:" + str(c))
#     else:
#         return('oshibka')
# print(pi())






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

# #6
# while True:
#     what = input ("Что будем делать? (+,-,*,/,%):")
# a = float(input("Ведите первое число:"))
# b = float(input("Ведите второе число:"))
# if what == "+":
#     c = a  + b
#     print("Результат:" + str(c))
# if what == "-":
#     c = a - b
#     print("Результат:" + str(c))   
# if what == "*":
#     c = a * b
#     print("Результат:" + str(c))
# elif what == "/":
#     c = a / b
#     print("Результат:" + str(c))
# else:
#     print('Результат неверный')














dict_= {'john': 50000, 'jamie': 100000,'aibek': 1000000,'aigerim':15
}

res = sorted(dict_)
