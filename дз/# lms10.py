# lms10
ls=[1,2,3,4,5,6,7,8,9,0]
try :
    a1=int(input('введите индекс а1: '))
    a2 = int(input('введите индекс а2: '))
    print(ls[a1]/ls[a2])
except ZeroDivisionError:
    print('на ноль делить нельзя !')    
except ValueError:
    print('ошибка ')
except IndexError:
    print('такова  индекс нет ')










#3
# user= {'артем':16, 'адилет':17 ,'ильсур':15, 'вадим':14 }
# try:
#     key= int (input('введите имя : '))
#     print(user[key])
# except KeyError:
#     print(f'{key} не сушествует ')


















