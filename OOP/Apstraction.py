# Apstraction.py
# from abc import ABC, abstractclassmethod





# class Animal(ABC):
#     @abstractclassmethod
#     def eat(self):
#         pass



#     @abstractclassmethod
#     def breathe(self):
#         pass





# class Lion(Animal):
#     def eat(self):
#         print('Meal')

#     def breathe(self):
#         print('Lungs')    

# obj = Lion()
# obj.eat()

# Абстракция (Абстрактный класс) - его можно рассматривать как набор методов,которые должны быть созданы и реализованы во всех дочерних классах, которые были унаследованы от абстракного класса


# Абстрактный метод - это метод, у которого есть обьявление но нет реализации




# from abc import ABC, abstractclassmethod
# from math import pi


# class Shape(ABC):
#     def __init__(self,name)->None:
#         self.name = name 


#     @abstractclassmethod
#     def area(self):
#         pass    


# class Square(Shape):
#     def __init__(self,lenght)->None:
#         super().__init__('kvadrat')
#         self.lenght = lenght

#     def area(self):
#         return self.lenght**2


# class Circle(Shape):
#     def __init__(self,radius)->None:
#         super().__init__('krug')
#         self.radius = radius

#     def area(self):
#         return round(pi*self.radius**2,2)


# a = Square(4)
# print(a.area())

# b = Circle(3)
# print(b.area())

# ==========================================================
# from abc import ABC,abstractclassmethod

# class ChessPiece(ABC):
#     # общий метод который будет использовать все наслежники этого класса 
#     def draw(self):
#         print('Drew a chess piece')

#     # абстракный метод еоторый необходимо переопределить для каждого дочернего класса

#     @abstractclassmethod
#     def move(self):
#         pass 

# class Queen(ChessPiece):
#     def move(self):
#         print('The Queen can move everywhere she wants  diagonally,vertically,horisontally')


# class Pawn(ChessPiece):
#     def move(self):
#         print('The Pawn can move directly to one or two cells!')


# q = Queen()
# q.draw()
# q.move()

# p = Pawn()
# p.draw() 
# p.move()