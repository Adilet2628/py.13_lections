# dz 10.10
"""
1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
"""
# def sum(a:int ,b: int):
#     return a+b
# print(sum(2,3))


'2) Создайте функцию, которая будет принимать строку. Функция должна выводить длину этой строки(не использовать функцию len).'

# def our_len ( obj: Interable) -> int:
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

"""
3) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
"""

"""
4) Создайте функцию, которая должна принимать 2 числа и возвращать результат их деления.
"""
# def sum(a:int ,b: int):
#     return a/b
# print(sum(6,2))
"""
5) Создайте функцию, которая принимает словарь. Пройдитесь по словарю циклом и распечатайте все его ключи
"""

"""
6) Создайте функцию, которая принимает и выводит "It's odd number" если это число не кратно двум и "It's even number" в противном случае.
"""
# def vivod(n:int):
#     if n%2==0:
#         print("It's even number")
#     else:
#         print( "It's odd number")
#vivod(4)       
"""
7) Напишите функцию, которая будет принимать строку и проверять является ли она палиндромом. Пробелы и регистр учитывать не нужно.
(Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 101; слова "кок", "топот", "комок" и т.д.)
"""
def zer(a:str):
    if a == a[::-1]:
        return ' true'
    else:
        return'не палиндромом '
print(zer('201'))        



"""
😍 Создайте функцию которая принимает от пользователя два числа. Она должна сравнить эти числа между собой и вывести максимальное значение.
"""
# def maxi(a:int,b:int):
#     if a>b:
#         print(a)
#     else:
#         print(b)    
# maxi(45,3) 
"""
9) Напишите функцию, которая принимает список чисел и возвращает их произведение.
"""
# def sum(a:int ,b: int):
#     return a*b
# print(sum(2,3))
"""
10) Напишите функцию, которая принимает целое число и возвращает сумму всех его цифр. Например, число 123 --> 6
"""
# def sum_(a: str):
#     n = 0
#     for i in a:
#         n += int(i)
#     return n
# print(sum_('126'))