"""
Задания по исключениям.
"""

"""
1) Опишите полный синтаксис конструкции try-except:
"""
try-если нету ошибки в коде то пропускает 
except если в коде есть ошибка он сообщает об ошибке 
finally выводит в любом случае 



"""
2) Дан следующий код:
b = 10
c = 11
print(a)
Обработайте ошибку, которая может возникнуть.
"""
# try:
#     b = 10
#     c = 11
#     print(a)
# except NameError:
#     print ('oshipka')    
"""
3) Напишите программу которая будет получать два числа через input и делить одно на другое. Обработайте ошибку, которая возникнет в случае, если второе число окажется 0 и выведите сообщение.
"""

# try:
#     num1 = int (input('enter the num1 : '))
#     num2 = int (input('enter the num2 : '))
#     print(num1/num2)   
# except ZeroDivisionError:
#     print('cant divide by zero!') 


"""
4) Напишите программу, которая будет получать через инпут 2 числа и будет печатать их сумму. Обработайте ошибку, которая возникнет, если пользователь введёт не числовое значение и выведите сообщение.
"""
# try:
#     num1=int (input('введите num1 : '))
#     num2= int(input('введите num2 :'))
#     print(num1+num2)
# except ValueError:
#     print('вы ввели число не корректно ')
    

"""
5) Дан словарь. Попытайтесь получить значение по ключу. Обработайте ошибку, возникающую в том случае, если запрашиваемый ключ не существует.
"""
# a= {1:'one',2:'two',3:'three'}
# print(a)
# try:
#     k= int (input('vvedite key : '))
#     print(a[k])
# except KeyError:
#     print('net takogo key ')    



"""
6)  Дан список. Обработайте исключение при попытке обращения к несуществующему элементу.
"""
# a= [2,33,55,64,4,6]
# print(a)
# try:
#      index= int (input('wvedite index :'))
#      print(a[index])
# except IndexError:
#     print('такого индекса не существует')     



"""
7) Попытайтесь в блоке try принять 2 числа и разделить одно на другое. В блоке except обработайте сразу 2 возможных исключения.
"""
# try:
#     num1 = int (input('enter the num1 : '))
#     num2 = int (input('enter the num2 : '))
#     print(num1/num2)   
# except ZeroDivisionError:
#     print('cant divide by zero!') 
# except ValueError:
#     print('введите число корректно!')
"""
# 😍 Запросите у пользователя сумму, которая у него сейчас есть в бумажнике. Если он введёт сумму, меньшую чем 0, то выбросите исключение с текстом "Сумма не может быть отрицательной!"
"""

# a=input('сколько у вас денег в бумажнике ? ')
# if a < '0':
#     print("Сумма не может быть отрицательной!")    
# else:
#     print(a)    

"""
# 9)  В блоке try запросите у пользователя ввод его возраста. Затем в том же блоке проверьте его возраст на совершеннолетие. Если пользователь несовершеннолетний, выбросите исключение с текстом "Доступ запрещён". Обработайте также исключение если пользователь вводит текст вместо числа с сообщением 'Введен некорректный возраст'. Если ошибок не возникло, то распечатайте сообщение "Спасибо!", а затем "До свидания", вне зависимости от того, произошла ошибка или нет.
# """
# try:
#     a= int(input('введите ваш возраст:'))
#     if a < 18:
#         print('доступ запрещен ')
#     if a > 18:
#         print('спасибо')

# except ValueError:
#     print('Введен некорректный возраст')        

# finally:
#     print('досвидание ')  


