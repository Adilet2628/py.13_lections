# декораторы- это функция которая позволяет без 
# изменения кода функции расширить ее функионал.

# def decorator(func):
#     print(f'{func.__name__} была вызвана!')
#     func()
# def printPetNames(owner:str= 'john', **pets):
#     print(f'owner name {owner}')
#     print(pets,type(pets),'!!!')
    # for pet, name in pets.items():

        # print(f'{pet}:',*name )





# pythonic way - @

# def decorator(func):
#     def wrapper():
#         print('decorator work')
#         print(f'{func.__name__} была вызвана!')
#         func()
#     return wrapper

# @decorator
# def get_name():
#     print(f'owner name john snow!')              

# get_name()

# import time
# def benchmark(func):

#     def wrapper(*args,**kwargs):
#         start = time.time()
#         func(*args,**kwargs)
#         finish = time.time()
#         print(f'время выполнения функции: {func.__name__}, заняло : {finish - start}')
#     return wrapper



# @benchmark
# def loop():
#     i = 0 
#     num =100_000_000
#     ls = []
#     while i <= num:
#         ls.append(i)
#         i+=1
# loop()

# @benchmark
# def add(numbers):
#     i = 0
#     ls=[]
#     while i <=numbers:
#         ls.append(i)
#         i+=1

# # loop()
# add(100000000)

# def bold(func):
#     def wrapper(*args,**kwargs):
#         res = '<bold>'+ func(*args,**kwargs) + '</bold>'
#         return res 
#     return wrapper

# def div (func):
#     def  wrapper(*args,**kwargs):
#         res = '<div>'+ func(*args,**kwargs) + '</div>'
#         return res 
#     return wrapper

# @div
# @bold
# @div
# def get_name():
#     name = input('введите имя: ')
#     return name 
# res = get_name()    

# print(res)


# =====================================================


def trace (func):
    def wrapper(*args,**kwargs):
        print(f'trase: вызвала {func.__name__}(\noна приняла args:{args}, kwargs{kwargs})')

        res = func(*args,**kwargs)
        print(f'trase: вызвала {func.__name__}(\noна вернула args:{args}, kwargs{kwargs})')


@trace
def hello (name, last_name, contry):
    return f'hello {name} {last_name} from {contry}'

hello (name= 'fsv', last_name='simpson', contry='canada' )













































































































































































