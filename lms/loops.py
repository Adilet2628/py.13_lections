# while <expression:
#  <body>


# i=0
# while 'string':
#     print(f'Srabotalo :{i} raz!')
#     i += 1 # i = + 1 increment 
# ====================



# i = 0 
# while i < 10:
#     i += 1
#     print(f'цикл сработал {i} раз')

# ====================

# ls = list(range(1,51))
# ls.reverse()
# print(ls)

# while ls:
#     print (ls.pop())

# user = { " username" :'johnsnow ',
#        'password':'ilovepython123'}
# print(user)
# i = 3
# password = None
# while  password != user['password']:
#     password = input(f'{user["username"]}vvedite parole: ')
#     i -= 1
#     if i == 0:
#         print('vy zablokirovany!')
#         break
# else :
#     print(f'vvy uspeshno zasli na sait {user["username"]}')    
    
    

# print(user)
# i = 3
# password = None
# while  password != user['password']:
#     input(f'{user["username"]}vvedite parole: ')!={user['password']}:

#     i -= 1
#     if i < 0:
#         print('vy zablokirovany!')
#         break
# else :
#     print(f'vvy uspeshno zasli na sait {user["username"]}')    

# ==================================

# i = 0 
# while i <15:
#     i+=1
#     print(i)

# for <variable> in < iterable object>:
#  body
# range(1,5)->1,2,3,4,5
# 'string'-> s  t r i n g 
# [1 , None, 15, False]->1 None 15 False
# 15->-------
# True->-----------
# i=iter('string')

# print(next(i))#s
# print(next(i))#t
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# str1= 'string '
# for x in str1:

#     if x == 'r':
#         continue
#     print (x)
# else :
#         print('end')

# ls= ['tirion', 'john',' san', 'eddgar', 'jamie']
# for x in ls:
#     if x =='san':
#         continue
#     print(f'hello mr/mrs  {x}')

# число 100
# надо найти все делители 

# num = 1000
# root  = int (num**0.5)
# res=[]

# for x in range(1,root+1):
#     print(x)
#     if num%x==0:
#         res.extend({x, num// x })
# res.sort()
# print(res)
# =======================
# import random

# ls= [ 'plov', 'manty', 'kuurdak', 'lagman', 'besh']
# p=m=k=l=b= 0
# # print(p,m,k,l,b)
# for x in range(1_000_000):
#     meal=random.choice(ls)
#     if meal=='plov':p+=1
#     elif meal=='manty':m+=1
#     elif meal=='kuurdak':k+=1
#     elif meal=='lagman':l+=1
#     else: b +=1

# dict_={'plov':p,'beash':b,'lagman': l,'kuurdak': k,'manty':m }
# print(dict_)
# =====================================================================
"""
1) Создайте список изпользуя циклы.
"""

# i = 0 
# while i < 32:
#     i += 1
#     print(f'цикл сработал {i} раз')
"""
2) Дан список из чисел, запишите чётные числа в один лист а нечётные в другой лист и выведите результат.
"""
# ls=list(range(1,15))
# a=[]
# b=[]
# for i in ls:
#     if i % 2 ==0:
#         a.append(i)
#     else:
#          b.append(i)
# print('чеьтные',  a)
# print('нечетные',b)


"""
3) Напишите программу, которая найдет факториал введенного числа.
"""

# ls = int(input('введите число : '))
# factorial = 1
# while ls > 1:
#     factorial *= ls
#     ls -= 1
 
# print(factorial)


"""
4) Напишите программу, которая будет находить наибольшую цифру натурального
числа. Натуральное число вводится с клавиатуры. Найти его наибольшую цифру.

"""
# a = int(input())
# m = a%10
# a = a//10
# while a > 0:
#     if a%10 > m:
#         m = a%10
#     a = a//10
# print(m)
"""
5) Вам дан список из чисел. Напишите программу в котором вам необходимо найти факториал каждого
числа и записать в новый список.
"""


# import math
 
# x= int(input('введите число :'))

# # returning the factorial
# print ("факториал вашего числа =  ", math.factorial(x))


 

"""
6) Вам дан список из чисел. Напишите скрипт в котором она запишет в новый список.
"""
   
a=()





"""
7) Создайте пустой список. Напишите программу которая должна 
записывать в ваш список числа от 0 до 10 включительно.
"""
# a=[]
# i = 0 
# while i <10:
#     i+=1

#     print(i)



"""
😍 Вам дан список целых чисел. Напишите программу
которая выводит все элементы которые меньше 7.
"""
a=input('введите число :  ')

for x in a >7:
    print(x)


#     print(i)




















































































