# Автомобиль: создайте класс с именем Car. Метод __init__ () класса Car должен содержать три атрибута: brand, year и color. Создайте метод get_auto(), который выводит информацию об автомобиле, и метод get_year, который выводит возраст авто .
# Добавьте атрибут horsepower, который равен 85.
# Напишите метод add_horsepower, который всем машинам будет добавлять по 20 л/с, а машинам Mers, Bmw, Poshe по 40 л/с
# class Car:
#     horsepower = 85
#     def __init__(self,brand,year,color,):
#         self.brand = brand
#         self.year = year
#         self.color = color 
        
#     def get_auto(self):
#         print(f'{self.brand} {self.year} года {self.color} цвета')
#     def get_year(self):
#         print(f'Возраст авто {2023 - self.year} лет')

#     def add_horsepower(self):
#         if self.brand == 'Mers':
#              self.horsepower += 40
#         elif self.brand == 'Bmw': 
#             self.horsepower += 40 
#         elif self.brand == 'Poshe':
#             self.horsepower += 40 
#         else: 
#            self.horsepower += 20
#         return f'У {self.brand} {self.horsepower} л/c'

# obj = Car('Bmw',2017,'black')
# obj1 = Car('Audi',2018,'white')
# obj.get_auto()
# obj.get_year()
# obj1.get_auto()
# obj1.get_year()
# print(obj.add_horsepower())
# print(obj1.add_horsepower())



# Создайте на основе своего класса экземпляр с именем bmw . Выведите три атрибута по отдельности, затем вызовите все методы.

# Два авто: начните с класса из вышеописанного упражнения. Создайте 2 разных экземпляра, вызовите для каждого экземпляра метод get_auto

# Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. Напишите метод get_student(), который выводит сводку с информацией о студенте . Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.

# class Student:
#     def __init__(self,name,age,course):
#         self.name = name 
#         self.age = age
#         self.course = course
#     def get_student(self):
#         print(f'Студента зовут {self.name} ему {self.age} лет и он на {self.course} курсе ')    
#     def get_birth_year(self):
#         print(f'Студент {2023-self.age} года рождения')

# obj = Student('Adilet',17,1)
# obj.get_student()
# obj.get_birth_year()


#Создайте класс Soda принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».
# class Soda:
#     def __init__(self, dobavka=''):
#         self.dobavka = dobavka
#     def show_my_drink(self):
#         if self.dobavka !='':
#               print(f'«Газировка и {self.dobavka}»')
#         else:
#              print('«Обычная газировка»')
# sl = Soda('jkhj')
# sl.show_my_drink()
# Создайте класс Student. При создании его экземпляра, мы должны записать имя и фамилию студента в соответствующие переменные объекта. В классе должны быть:
#  1 переменная объекта books = [ ]
#  2 переменная объекта “knowledge” со значением по умолчанию 0
#  3 метод read_book, который принимает название книги, добавляет книгу в books, добавляет 100 баллов в knowledge
#  4 метод do_homework, который при вызове добавляет 10 баллов в knowledge
#  5 Создайте экземпляры, вызовите методы.

# class Student:
    
   
#     def __init__(self,name, last_name):
#         self.name = name
#         self.last_name = last_name
#         self.knowledge = 0
#         self.books = []
    
#     def read_book(self,book):
#         self.knowledge+=100
#         self.books.append(book)
    
#     def do_homework(self):
#      self.knowledge+=10

# wd = Student('хехех','хахаха')
# wd.read_book('Горе от ума')
# wd.do_homework()
# print(wd.books)

# print(wd.knowledge)