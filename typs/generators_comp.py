# generators
# print(x for x in (range(1,10)))
# x,a,b=(x for x in range(1,4))
# print(x,a,b)
# list comprehensions - генератоны списков
# list comprehensions - упрощеный подход к созданию списков , который задействует в себе цикл for, а так же конструкцию if для определения того,что в итоге попадает в наш список 
# list -> 0 -> 200
# ls =[]
# for x in range(0,200):
#     if x % 2 ==0:
#         ls.append(x)

# print(ls)


# ls=[x for x in range(0,200) if x%2==0]
# print(ls)
# ls=[x for x in range(0,300) if x%2==0 and x %4 ==0]
# print(ls)
# set {}- множество
# ===
# list - 0 ,100 ->x 2 ->x**2,x3 -> x**3


# ls= [ x for x in  range(1,101)if x%2 == 0 or x%3]
# print(ls)
# ls = [ x**2 if x %2==0 else xx**3 for x in range(0,101)]
# if x%2 == 0 or x%3



# # ls = [[1,2,3,],[4,5,6,][7,8,9]]

# res=[items for x in ls for items in ]
# #       #[1,2,3,4,5,6,7,8,9]

# from datetime import datetime

# start = datetime.now()
# ls = []
# for x in range(1,100000000):
#     ls.append(x)
# finish = datetime.now()
# print(finish - start)


# dict_= {x:x**2 for x in range(1,11)}
# print(dict_)

# names = ['john', 'tirion', 'sasna', 'eygan', 'ramsi']
# res = {name: len(name ) for name in  names }
# print(names )
# print(res)






































































































