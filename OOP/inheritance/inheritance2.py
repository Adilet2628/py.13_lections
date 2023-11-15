# KRad 

# множественное наследование - это когда класс наследуется от двух или более классов, порядок наследования определяется при помощи MRO 


# class Plane:
#     def play_music(self):
#         print('music i plaing')
#     def fly(self):
#         print('we\'re flying')

# class Auto:
#     def play_music(self):
#         print('music i plaing on radio')    
#     def ride(self):
#         print('We\'re riding on the ground')

# class Boat:
#     def play_music(self):
#         print('music i plaing karaoki') 

#     def swim(self):
#         print('we\'re swiming on the sea')

# class Future_Auto(Auto,Boat,Plane):
#     pass


# obj = Future_Auto()
# obj.fly()
# obj.ride()
# obj.swim()
# obj.play_music()
# obj.play_music()

# --------------------------------------------------------------------------------------------

# object
# print(object)
# print(dir(object))

# class A:
#     pass

# print(A.mro)


# ---------------------------------------------------------------------------------------------------------
# проблема ромба - когда поиск шел в родительский класс прежде че
# м искать у соседнего потомка (решена при помощи MRO)

# MRO(Metod resolution order)- механизм для кореккного поиска родительских методовю Поиск идет таким образом что если у родительского класса есть общий предок, то поиск идет в ширину, другими словами сначала у потомков, а потом у общего предка 


# class Zero:
#     def say(self):
#         print('Zero')

# class First():
#     def say(self):
#         print('first')

# class Second():
#     def say(self):
#         print('second')

# class Myclass(First,Second):
#     pass



# obj = Myclass()
# obj.say()
# print(Myclass.mro())

# ---------------------------------------------------------------------------------

# Проблема перекрестного наследования 

# class X :
#     pass

# class Y:
#     pass

# class A(X,Y):
#     pass
# class B(X,Y):
#     pass

# class MyMRO(type):
#     def mro(cls):
#         return [cls,A,B,X,object]
# class Myclass(A,B,metaclass=MyMRO):
#     pass

# print(Myclass.mro())