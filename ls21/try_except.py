# обработка исключений 
# операторов try.....except 
# ощибки errors ->связаны с кодом 
    # syntaxerrory
    # TabError
    # IndentationError
# a = 5 
# b = 6


# исключения exceptions -> связаны с неправильным вводом данных которые передаются в код 
# ValueError
# TypeError
# NameError
# ZeroDivisionError
# IndexError
# KeyError
# ImportError
# # BaseException
# try:
#     num1 = int (input('enter the num1 : '))
#     num2 = int (input('enter the num2 : '))
#     print(num1/num2)
# except ValueError:
#     print ('idi na')    
# except ZeroDivisionError:
#     print('cant divide by zero!') 

# try:
    # <body> #код с вероятным исключением 
# except:
# <body except>сработает только если ошибка в try 
# <else>:
#<body >сработает только если нет ошибки в try
# <finally>:
# <body> сработает в любом случае  

# dict_={1:"one", 2 :'two ',3:'three'}
# print(dict_)
# try:
#     key = int (input('wvdite key : '))
#     print(dict_[key])
# except ValueError:
#     print ('invalid value for key ')
# except KeyError:
#     print('key does not exsists ')  
# else:
#     print('no errors ')
# finally:
#     print('the end ')

# =====================================


# отображение ощибки 
# 1. import sys
# ls = [1,2,3,4,5]
# try:
#     index= int (input('wvedite index :'))
#     print(ls[index])
# except:
#     import sys 
#     print(f'oops, we catched {sys.exc_info()[0]} errors')
# 2. exception as e 
# ls = [1,2,3,4,5]
# while True:
#     try:
#         index = int(input('vvedite index: '))
#         print(ls[index])
#     except Exception as e:
#         print(f'oops, we catched {e.__class__}errors ')    

# ===============================================================================================
# flag = True
# symbols = '0123456789' + '-' + '.'

# while flag:
#     print()
#     num1 = input('Введите первое число: ')
#     num2 = input('Введите второе число: ')
        
#     try:    
#          num1 = float(num1) if '.' in num1 else int(num1)
#          num2 = float(num2) if '.' in num2 else int(num2)
#     except ValueError:
#         print('вы ввели некоректное число ')     
#         continue


#     operator = input('Введите операцию(+,-,*,/): ').strip()
#     if operator == '+': 
#         print(f'Результат: {num1 + num2}')
#     elif operator == '-':
#         print(f'Результат: {num1 - num2}')
#     elif operator == '*':
#         print(f'Результат: {num1 * num2}')
#     elif operator == '/':
#         print(f'Результат: {num1 / num2}' if num2 != 0 else 'На ноль делить нельзя!')
#     else:
#         print('Вы ввели неверный оператор!')
    
#     choice = input('Хотите продолжить?(уes/no): ')
#     if choice.lower().strip() != 'yes':
#         flag = False
#         print('Пока пока!')






























