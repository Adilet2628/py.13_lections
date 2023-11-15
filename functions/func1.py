# найти квадрат, куб, результат деления на 100 любого числа \

# num1 = 5 
# -> {'num1':5 , '2':25, '3':125,'100' : 0.05}

# num1 = 5 
# res= {'num':num1 , '2':num1**2, '3':num1**3,'100' :num1/100}
# print(res)


# num2= 75
# res= {'num':num2 , '2':num2**2, '3':num2**3,'100' :num2/100}
# print(res)


# DRY - DON'T repeat yourself 

def do_operations(num: int):
    res= {'num':num , '2':num**2, '3':num**3,'100' :num/100}
    print(res)
do_operations(15)
do_operations(3)
do_operations(21)

# ==================
# Функция это именнованная часть программы ,
# которая содержит в себе определенный набор инструкций, 
# и может вызываться в других частях программы столько раз сколько угодно
# def name_of_funk(<a,b>)#параметры функции:
    # <body>#код какая то логика кторая будет давать конечный результат
#  <return># оператор который помогает сохранить результат 

# name_of_funk(5,6# аргументы 

# параметры функции - переменных в которых мы временно сохраняем данные
#  которые  передаем при вызове в функцию,доступны только внутри функции

# Aргументы функции - данные которые мы передаем при вызове функции,
   # они попадают в параметры по очередности 

# print (len('string'))
# from typing import Iterable
# def our_len ( obj: Iterable) -> int:
#     """возвращает длинну итерируемого объекта"""
#     print(obj)
#     i = 0 
#     for _ in obj:
#       i += 1 
#     return f"result: {i}"
# ls = [1,2,3,4,5]
# str1= 'hello world s vami john snow!'
# print(our_len(ls))
# print(our_len(str1))

# def isEven (num):
#         return True if num % 2 == 0 else False


# result = isEven(15)
# print(result) 

# def isEven( num: int) -> bool:

#     """return true or false while after checking number for ever """
#     return True if num % 2 == 0 else False


# result = isEven(15)
# print(result) 




# ===================

# default параметры 

# def sum_of_args(a:int ,b:int,c:int)-> int:
#     """returns sum of arguments"""
#     return a + b +c
# print(sum_of_args(12,3,4))    
# print(sum_of_args(12,32,45))

# ==================================
# позиционные и именованные аргументы 
# def printParams(a,b,c):
#     print(a,'is stored in param a')
#     print(b,'is stored in param b')
#     print(c,'is stored in param c')

# printParams(5,6,7)Позиционные аргументы 
# print()
# printParams(b=5,a=7,c=6)Именнованые аргументы 
# ==================================
# оператор *
# a=[1,2,3]
# b=[4,5,6]
# c=[*a,*b]
# print(c)
# ====================
# *args, **kwargs


# def get_some_data(a,b,*args,**kwargs):
    
#     print('parametry a и b :' , a,b)
#     print('аргументы :',args)
#     print('именнованые аргументы :',kwargs)

# get_some_data(1,2,3,4,5)

# def printScores(student: str , *scores):
#     print(f'name of student : {student}')
#     print(f'AVG:{sum(scores)/len(scores),1}')
#     print(scores,type (scores),'!!!')
# for x in scores:
#     print('score:',x)

# printScores('john snow ',5,5,5,5,4,4,2)

# def printPetNames (owner: str,**pets):
#     print(f'Owner name {owner}!')
#     print(pets,type (pets),'!!!')
#     for key in pets.items():
#         if type(name)==list:
#             print(f'{pet}',*name)
#         else:
#             print(f'{pet}',*name, sep=', ')    
#         print(f'{key}: {pets[key]}')

# printPetNames('john snow ',dog = 'pluto', cat = 'garfild ', fish = ['nemo', 'dori', ' golden'])


# ==================================
# from random import choice, shuffle
# from string import ascii_letters, digits,punctuation

# symbols=ascii_letters + digits
# print(symbols)

# def generate_pass(len_: int ) -> str:

#     '''Function  generates random string for password, 
#     parameters len needs to give lenghts of password.
#    if blank len_= 8'''
#     res = [choice(symbols) for _ in range(len_ -2 )]+[choice(punctuation)for _ in range(2)]
#     shuffle(res)
#     return ''.join(res)



# print(generate_pass(18))    
# print(generate_pass(9))  























































































