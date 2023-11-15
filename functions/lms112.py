"""
1) Умножение соответствующих элементов двух списков: Используйте map и lambda, чтобы умножить соответствующие элементы двух списков.
"""
# ls = [1,2,3]
# ls2 = [4,5,6]
# res= list(map(lambda x,y :x*y, ls,ls2 ))
# print(res) 


"""
2) Проверка, что в строке есть хотя бы одна гласная буква: Используйте any и lambda, чтобы проверить, что в строке есть хотя бы одна гласная буква.
"""
# ls = 'hello'
# res= any(map(lambda x : x in  'aeiouyAEIYOU',ls))
# print(res)
"""
3) Фильтрация слов с определенной длиной: Используйте filter и lambda для фильтрации слов в списке строк, имеющих заданную длину.
"""

# ls = ['hello','sdgfvsdf','sdfzxc','srgbefaegtrybht']
# res = list(filter(lambda x : len(x) >= 6, ls))
# print(res)
"""
4) Проверка, что все элементы списка больше нуля: Используйте all и map, чтобы проверить, что все элементы в списке больше нуля.
"""
# ls= [1,2,3,4,5]
# res= all(map(lambda x : x >0, ls))
# print(res)
"""
5) Сумма квадратов четных чисел: Напишите программу, которая с использованием map и reduce находит сумму квадратов четных чисел в списке.
"""
# from functools import reduce

# ls = [1,2,3,4,5]
# res = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, ls)))
# print(res)
 