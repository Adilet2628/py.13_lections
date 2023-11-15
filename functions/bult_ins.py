# zip(iterable) - она соединяет каждый элемент итерируемый объектов между 
# собой в тип данных tuple  и возврашает итератор

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]

# res = dict(zip(ls1, ls2))
# print(res)

# =================================================================================
# all(), any()


# all(Iterable)- Возвращает True,если все элементы итерируемого обьекта истина, иначе false

# ls = [[1,2], 5 , 'stroka', True, 1 ]
# print(all(ls))



# ip = '10.255.12.155'
# ip2 = '10.255.1y.155'


# resalt= all(x.isdigit() for x in ip1.split('.'))
# print(resalt)


# any - возврашает true, если хотябы один элемент истина 

# ls = [0,2,0,0]
# print(any(ls))



# ignore = ['rm-rf', 'sudo','reset', 'poweroff']

# command = input('введите команду :')
# if any(x in command for x in ignore):
#     raise Exception ('you do not have permission!')

# print('OK')



# анонимные функции - lambda(также функции только без названия)
# lambda функции могут принимать сколько угодно аргументов одно выражение 


# def sum_of_args(a,b) :
#     res = a+b 
# \    return res
# print(sum_of_args(5,15))

# lambda a,b,:a+b

# def myfunk(n):
#     retirn lambda a :a*n

# mydoubler = myfunk(2)
# mydoubler = myfunk(3)

# mydoubler = myfunk(50)

# mydoubler = myfunk(2123)
# mydoubler = myfunk(27)


# dict_= {'john': 50000, 'jamie': 100000,'aibek': 1000000,'aigerim':150000
# }

# res = dict(sorted(dict_.items(), key=lambda x : x[1]))
# print(res)




# map(function, iterable)-> применяет ко всем элементам iterable функцию которую мы передаем 


# ls=['one', 'two', 'three', 'four', 'five']
# res= list(map(str.upper, ls))
# print(res)



# for i in range(len(ls)):
#     ls[i] = ls[i].upper()
# print(ls)


# names = ['john', 'sultan', 'jamie', 'raychel', 'aibek']
# res = list(map(lambda name:f'hello mr/mrs {name}!',names ))
# print(res)





# res = []
# for name in names:
#     res.append(func(name))

# def func(name):
#     return f'hello mr/mrs {name}!'
# print(names)
# printres


# dict_ = {1:2,3:4,5:6}

# res = dict(map(lambda x: (x[0],str(x[1])), dict_.items()))

# print(res)

# filter(function, iterable)-> применяет ко всем элементам iterable функцию которую мы передали и возвращает итератор с теми элементами для которых функция вернула True 







# ls = ['one', 'two' , '', 'list', '100', '1', 'john']

# # res = []
# # for x in ls:
# #     if x.isdigit():
# #         res.append(x)

# # print(res)


# res = list(filter(str.isdigit,ls))
# print(res)


# ls = ['john', 'codify', 'aibek', 'ono', 'bootcamp', 'Kyrgyzstan', 'mountains']
# res = list(filter(lambda x: len(x)>5,ls))
# print(res)


# ls = [{'name': 'python','point':10},
#  {'name': 'c++', 'point': 6},
#  {'name':'JS','point': 8},
#  {'name': 'JAVA', 'point': 3},
#  {'name': 'c#', 'point':9}]
# res = list(filter(lambda dic: dic
# ['point']>7, ls))
# print(res)
                                                                                     
                                                                                                                                                                                                             

# users = [{'username': "john",'coments':['i love you , really good']},
# {'username': 'reychel','coments':[]},
# {'usrename': 'steven','comments':['bishkek', 'python']},
# {'username':'hello','coments':[]}]

# active_users= list(filter(lambda obj: obj['coments'],users))
# inactive_users= list(filter(lambda obj:not obj['coments'],users))

# print(active_users)
# print()
# print(inactive_users)


# =============================================================

# enumerate- она пронумеровывает каждый элемент внутри iterable,ее собственным индексом


# ls = ['one', 'two', 'three', 'four', 'five']
# res =list( enumerate(ls ,1))
# print(res)
# for i ,x in enumerate(ls):
#     print(f'index: {i}, element: {x}')

# from functools import reduce

# ls = [1,2,3,4,5]

# sun_= reduce(lambda a,b:a+b,ls)
# res = reduce(lambda a,b: a*b,ls)
# print(sun_)
# print(res)

# from itertools impor t repeat

# for x in repeat(lambda x: x * 5,5):

#     print(x)



# TODO filter, reduce, enumarate,repeat
# from itertools import repeat
# from random import choices, shuffle
# from string import ascii_letters,digits
# from statistics import mean


# symbols = '_()$!%+-@#'

# q_pass = int(input('vvedite kolichestvo paroley:'))



# resalt = {f(choices(ascii_letters, k = 10),
# choices(digits,k= 5),
# choices(symbols,k= 2))
# for f in repeat(lambda a,d,s: ''.join(set(a+d+s)), q_pass)
# }
# print(resalt)

# 1)
'''Магическими называются даты, в которых произведение дня и месяца
составляет последние две цифры года. Например, 10 июня 1960 года –
магическая дата, поскольку 10 ´ 6 = 60. Напишите функцию, определя-
ющую, является ли введенная дата магической. Используйте написан-
ную функцию в главной программе для отображения всех магических
дат в XX ве­ке.'''






#2) 
'''Напишите функцию для определения количества дней в конкретном ме-
сяце. Ваша функция должна принимать два параметра: номер месяца
в виде целого числа в диапазоне от 1 до 12 и год, состоящий из четырех
цифр. Убедитесь, что функция корректно обрабатывает февраль високос-
ного года. В основной программе запросите у пользователя номер месяца
и год и отобразите на экране количество дней в указанном месяце.'''



# 3) 
'''Напишите две функции с именами hex2int и int2hex для конвертации
значений из шестнадцатеричной системы счисления (0, 1, 2, 3, 4, 5, 6, 7,
8, 9, A, B, C, D, E и F) в десятичную (по основанию 10) и обратно. Функ-
ция hex2int должна принимать на вход строку с единственным символом
в шестнадцатеричной системе и преобразовывать его в число от нуля
до 15 в десятичной системе, тогда как функция int2hex будет выполнять
обратное действие – принимать десятичное число из диапазона от 0 до
15 и возвращать шестнадцатеричный эквивалент. Обе функции должны
принимать единственный параметр со входным значением и возвращать
преобразованное число. Удостоверьтесь, что функция hex2int корректно
обрабатывает буквы в верхнем и нижнем регистрах. Если введенное поль-
зователем значение выходит за допустимые границы, вы должны вывести
сообщение об ошибке.'''



#4
'''Представьте, что в вашем регионе устаревшим является формат номер-
ных автомобильных знаков из трех букв, следом за которыми идут три
цифры. Когда все номера такого шаблона закончились, было решено об-
новить формат, поставив в начало четыре цифры, а за ними три буквы.
Напишите функцию, которая будет генерировать случайный номерной
знак. При этом номера в старом и новом форматах должны создаваться
примерно с одинаковой вероятностью. В основной программе нужно сге-
нерировать и вывести на экран случайный номерной знак.'''


















































































































16.10
"""
1) Дан список list_ = [1, 2, 3, 4]. Выведите сумму всех этих чисел.
"""
# list_ = [1,2,3,4]
# res = sum(list_)
# print(res)

"""
2) Дан списка из чисел. Проверьте, что все числа больше трёх.
"""
# ls = [4,5,6,7]
# re = all(x > 3 for  x in ls )
# print(re)



"""
3) Даны список из чисел. Проверьте, что в нём есть отрицательные числа.
"""
# ls= [-1,2,3,4]

# re = all(x>0 for x in ls)
# print(re)

"""
4) Дан список, состоящий из числами. Создайте новый список, состоящий из квадратов этих чисел.
"""
# ls = [2,3,4,5]
# re = [x ** 2 for x in ls]
# print(re)
"""
5) Дан список с числами. Отфильтруйте этот список, оставив только чётные числа.
"""

# ls= [1,2,3,4,5]
# res =[x for x in ls if x % 2 == 0]
# print(res)

"""
6) Дан список, со строками. Отфильтруйте этот список, оставив только те строки, длина которых больше 7 символов.
"""
# ls = ['dfasdgvawrg','adsg','agerggrr']
# res = [x for x in ls if len(x)>7]
# print(res)

"""
7) Дан список list_ = [5, 6, 7, 8]. Выведите произведение всех этих чисел.
# """
# ls = [5,6,7,8]
# num = 1
# for x in ls : num *=x
# print(num)
"""
8) Дан список, с числами. Посчитате количество чётных и нечётных чисел в этом списке.
"""
# ls = [1,2,3,4,5,6,7,8,9]
# res = [x for x in ls if x % 2 ==0]
# res1 = [x for x in ls if x %2 != 0 ]
# print(res)
# print(res1)

"""
 9 Дан список list_ = [-1, 2, 3, 0, 5, -3, 7,]. Если число в списке меньше 0, замените его на False, если больше, то на True
"""
# ls = [-1,2,3,4,5,0,5,-2,-4]

# res= all(x<0 for x in ls)
# res1= any(x>0 for x in ls)
# print(res)
# print(res1)

"""
10) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
# """
# from functools import reduce

# ls = ['artem','ilsur', 'vadim', 'adilet']
# res=  reduce(lambda a, b: a if len(a) > len(b) else b, ls )

# print(res)










































