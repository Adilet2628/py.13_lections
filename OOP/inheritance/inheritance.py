# принцыпа ООР
# 1. Наследование 
# 2. инкапсуляция 
# 3.






# ---------------------------------------------
# Наследовани 
# Позволяет принимать родительские метод и атрибуты дочернему классу

# Родительский класс
# Дочерний класс
# -----------------------------------------


# class Animal:
#     def print_info(self):
#         print('I\'m an Animal!')


# class Lion(Animal):
#     pass

# class Dog(Animal):
#     pass

# simba = Lion()
# simba.print_info()

# aktosh = Dog()
# aktosh.print_info()
# print(dir(simba))


# ----------------------------------------------------------------------------
# class Animal:
#     def say(self):
#         print(f'this  Animal name is: {self.name}:{self.golos}')
#     def eat(self):
#         print(f'{self.name} eats: {self.meat}')

# class Lion(Animal):
#     name = 'Lion'
#     golos = 'bark'
#     meat = 'meat'


# class Dog(Animal):
#     name = 'dog'
#     golos = 'brak'
#     meat = 'home meat'
# class Koala(Animal):
#     name = 'Koala'
#     golos = 'roar'
#     meat = 'efkalit'


# rex = Dog()
# simba = Lion()
# maris = Koala()
# rex.say()
# rex.eat()
# print()
# simba.say()
# simba.eat()
# print()
# maris.say()
# maris.eat()        
# ---------------------------------------------------------------------------

# class Person:
#     def info(self):
#         print('I\'m a person from Bishkek!')
# class Student(Person):
#     def info(sale):
#         super().info()
#         print('I\'m study in Manas University')
# class Adult(Person):
#     def info(self):
#         super().info()
#         print('I\'m older 18 years! I work 5 days in the week')


# obj1 = Student()
# obj2 = Adult()
# obj1.info()
# print()
# obj2.info()
# -------------------------------------------------------------------------
class Laptop:
    def __init__(self)->None:
        self.brand = brand
        self.model = model 
        self.price = price

    def get_info(self):
        return { 'brand' : self.brand, 'model': self.model, 'price': self.price }

class Acer(Laptop):
    def __init__(self,model,price,cpu,display):
        super().__init__('Acer',model,price)
        self.spu = spu
        self.display = display


    def get_info(self):
        repr = super().get_info()
        repr ['spu'] = self.spu
        repr ['display'] = self.display
        return repr


acer = Acer('svift',700,2022,'nvidia')
print(acer.get_info())
print()
mac = Apple('Air',1200,'M2',13.6)
print(mac.get_info())

















































