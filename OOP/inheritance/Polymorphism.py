# к
#  Полиморфизм - способность метода (функции) использоваться в разных типах(классов) 
# Широко распространенное определение: 'один интерфейс - много реализации'

# class Cat:
#     def __init__(self,name,age)->None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'it\'s a cat.Cats name is{self.name},age: {self.age}')

#     def make_sound(self):
#         print('Meow, meow')


# class Dog:
#     def __init__(self,name,age)->None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'it\'s a dog.Dogs name is{self.name},age: {self.age}')

#     def make_sound(self):
#         print('bark,bark')

# obj1 = Cat('asdf',5)
# obj1.info()
# obj1.make_sound()
# print()
# obj = Dog('asc',3)
# obj.info()
# obj.make_sound()




# class Shape:
#     def __init__(self,name):
#         self.name = name 
#     def area(self):
#         pass
#     def info(self):
#         print('я геометрическая фигура')    
# class Square(Shape):
#     def __init__(self,length)->None:
#         super().__init__('kvadrat')
#         self.len = length
#     def area(self):
#         return self.len**2

#     def info(self):
#         super().info()
#         print('все стороны равны и углы все по 90 градусов')


# class Circele(Shape):
#     def __init__(self,radius):
#         super().__init__('okrujnost')
#         self.r = radius
#     def area(self):
#         from math import pi
#         return round(pi*self.r**2, 2)

#     def info(self):
#         super().info()
#         print('диаметр равен двум радиусам')


# a = Square(8)
# b = Circele(4)
# a.info()
# print(a.area())
# print()
# print()

# b.info()
# print(b.area())


"""
1) Объявите 3 переменных, запишите в них строку, список и словарь. Затем запишите их в список, и пройдитесь по нему циклом чтобы распечатать длину сразу каждого из объектов.
"""
#
"""
2) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", для кошек "Мяу".
Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()
"""
# class Dog:
#     def voice(self):
#         print('гав')

# class Cat:
#     def voice(self):
#         print('мяу') 
        
# Dog = Dog()
# Cat = Cat()  
# def to_pet(pet): 
#     pet.voice()

# to_pet(Cat)
# to_pet(Dog)

"""
3. Создайте 2 класса: MyInt и MyString, наследуйте MyInt от int, MyString от str. У обоих
классов переопределите метод, который отвечает за работу с оператором “+”.
Напишите функцию add_objects(), которая принимает объект одного из 2 типов.
При сложении объектов класса MyInt должно выдаваться сообщение “Это сложение”, а
потом идти логика сложения 2 чисел, и выдача результата.
При конкатенации объектов класса MyString() Должно выдаваться сообщение: “Это
конкатенация”, а затем логика конкатенации из базового класса и выдача результата.
"""
# jls_extract_var
# писать код здесь
"""
4) Создайте 3 класса: Person, Employee и Student, при этом Employee и Student должны наследоваться от Person. Определите во всех трёх классах метод get_info():
-для класса Person он должен принимать и возвращать следующее: “Привет, меня зовут Иван Петров”.
-для класса Employee он должен принимать и возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.
-для класса Student должно приниматься и возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.
Определите функцию get_human_info(), которая будет принимать объект одного из трёх классов, вызывать метод get_info и печатать результат.
"""
# class Person:
#     def get_info(self, name, last_name):
#         return f'Привет меня зовут {name} {last_name}'

# class Employee(Person):
#     def get_info(self, n, l, k, d):
#         return f'{super().get_info(n, l)},я работаю в компании "{k}" на должности "{d}"'

  
# class Student(Person):
#     def get_info(self, n, l, k, d):
#         return f'{super().get_info(n, l)},я учусь в "{k}" на  {d} курсе'

# a = Employee()
# print(a.get_info('asd', 'qwerty', 'ASDFGH', 'direktor'))
# a = Student()
# print(a.get_info('adi','rai','codify',2))

"""
5) Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.

Затем наследуйте от Shape три класса: Triangle, Square и Circle.
-треугольник создаётся с заданными основанием и высотой
-квадрат создаётся с заданной длиной стороны
-круг создаётся с заданным радиусом
Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.

Затем создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()

Подсказка: для создания абстрактных классов воспользуйтесь модулем abc
"""

# from abc import ABC, abstractmethod
# import math
# class Shape(ABC):
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#     def get_area(self):
#         return 0.5*self.base * self.height

# class Square(Shape):
#     def __init__(self,len):
#         self.len = len

#     def get_area(self):
#         return self.len**2

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def get_area(self):
#         return math.pi*self.radius**2    


# a= Triangle(2,3)
# print(a.get_area())
# b = Square(3)
# print(b.get_area())
# c = Circle(5)
# print(c.get_area())


