# import re

# def check_password(password):
#     if len(password) < 8:
#         return 'Должен содержать не менее 8 символов'

#     if not any(char.isupper() for char in password):
#         return "Должен содержать одну заглавную букву"

#     if not any(char.islower() for char in password):
#         return"Должен содержать одну строчную букву " 
#     if not any(char.isdigit() for char in password):
#         return"Должен содержать одну цифру"

#     # special_characters = 
#     if not re.search(r"[-!@#$%^&*()_+=<>?/]", password):
#         return "Должен седержать  символ"
#     return'ееееессссс'    

# user_password = input("Введите пароль: ")

# result = check_password(user_password)
# print(result)

  


#2

# ls=[1,2,3,4,5,6,7,8,9,0]
# try :
#     a1=int(input('введите индекс а1: '))
#     a2 = int(input('введите индекс а2: '))
#     print(ls[a1]/ls[a2])
# except ZeroDivisionError:
#     print('на ноль делить нельзя !')    
# except ValueError:
#     print('ошибка ')
# except IndexError:
#     print('такова  индекс нет ')










#3
user= {'артем':16, 'адилет':17 ,'ильсур':15, 'вадим':14 }
try:
    key= (input('введите имя : '))
    print(user[key])
except KeyError:
    print(f'{key} не сушествует ')































































































































































