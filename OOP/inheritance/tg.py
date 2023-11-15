"""

)1 Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.

"""

# class Machina:
#     def nami(self):
#         print(f'Avto  {self.name}')
#     def years(self):
#         print(f'Год выпуска {self.year}')
# class Auto(Machina):
#     name ='Audi'
#     year = 2017
    
#     def nami(self):
#         super().nami()
#         print('go')
#     def years(self):
#         super().years()
#         print('gogo')
# auto = Auto()
# auto.nami()
# auto.years()

"""

)2 Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.

"""

# class A:
#     def method1(self):
#         return("Основной функционал")

# class B(A):
#     def method1(self):
        
#         return(f'{super().method1()}\nДополнительный функционал')        

# sl = B()
# print(sl.method1())
"""

)3 Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:

append, который будет принимать строку и добавлять её в конец исходной

pop, который удаляет из строки последний элемент и возвращает его.

Пример:

# example = MyString('String')

# example.append('hello')

# print(example) -> 'Stringhello'

# print(example.pop()) -> 'o'

# print(example) -> 'Stringhell'

"""

# писать код здесь
# class MyString(str):
#     def __init__(self, str1):
#         self.str1 = str1

#     def append(self, st):
#         self.str1 += st
#         return self.str1
   
#     def __str__(self):
#         return self.str1



# example = MyString('String')
# # print(example)
# example.append('hello')

# print(example)


"""

4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.

"""


"""

)5 Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.

Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.

Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.

"""

# class Person:
#     def display(self):
#         return ('adilet 17 лет')


# class Student(Person):
#     def display_student(self,opis):
#         self.opis = opis
    
#         print(f'{super().display()}\nДанные:{self.opis}')

# student = Student()

# student.display_student('pfyznjq')

"""

6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.

"""

# class ContactList(list):
#   all_contacts = ['adi','kani','anvar']
#   def __init__(self):
#     pass
#   def search_by_name(self,name):
#     if self.name == all_contacts:
#       return self.name
# a = ContactList()
# a.search_by_name('adi','kani')


"""

7. Создайте класс Smartphone, экземпляры класса должны иметь такие свойства - name, color, memory, battery. battery по умолчанию

должно быть 0. Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона.

У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.

 

Создайте два дочерних класса от Smartphone - Iphone и Samsung.

У Iphone должен быть дополнительный аттрибут - ios и метод send_imessage - возвращает строку с сообщением и от какого телефона оно было выслано.

А у Samsung должен быть дополнительный аттрибут android и метод show_time, который показывает текущее время.

Создайте объекты от данных классов и примените все методы.

"""
# from datetime import time
# print(time())
# class Smartphone:
#     def phone(self,name,color,memory,battery = 0):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery  = battery
#     def charge(self,a):
#         self.battery += a 
#     def __str__(self) -> str:
#         return f'Название:{self.name},память {self.memory},цвет:{self.color} ,батареея:{self.battery}'
# class Iphone(Smartphone):
    # def phone(self,name,color,memory,ios,):

    #     self.ios = ios
    # def send_imessage(self,strr):
    #     self.strr = strr
    #     print(f'{self.strr} :{self.name}')

# class Samsung(Smartphone):
#     def phone(self,name,color,memory,android):
#         self.android = android
      
#     def show_time(self):
#         print(datetime())   
# samsung = Samsung()
# samsung.__str__()
"""

8. Создайте класс Spell для магических заклинаний, экземпляры класса имеют два аттрибута - name - название и formula - полное произношение заклинания.

 

У класса есть два метода: get_description() - дает полное описание заклинания и execute() - совершает заклинание.

 

Переопределите у класса метод str, чтобы он выдавал вам название, формулу и описание вместе, к примеру:

 

Открытие замков: Alohomora

позволяет магу попасть в любую комнату,

способно открыть любую закрытую замочную скважину.

 

Наследуя от класса Spell создайте три заклинания,переопределяя в них родительские методы. Создайте объекты этих трех заклинаний. Вызовите все методы

"""

 

"""

)9. Напишите класс CustomError который наследуется от встроенного класса исключений Exception. Переопределите init таким образом

чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений.

Создайте исключение от этого класса с сообщением:

"ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ"

 

Напишите функцию проверяющую строки на регистр и если строка не написана в верхнем регистре выбросите исключение созданное классом CustomError:

 

Traceback (most recent call last):

  File "inheritance.py", line 121, in <module>

    check_letters(a)

  File "inheritance.py", line 117, in check_letters

    raise capitals_error

main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ

 

"""
# class CustomError(Exception):
#     def init(self, *args: object) -> None:
#         super().init(*args)

# b = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def error(s):
#     if s != s.upper():
#         raise b
    
# error('ASDFGHJKLh')

"""

)10. Создайте класс Character с помощью которого можно создавать героев для игры. Экземпляры класса должны иметь аттрибут name. У класса должна быть переменная power_list, в которой хранится словарь:

power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }

 

Класс должен иметь методы:

give_weapon - выбирает случайное оружие из списка

 

give_role - выбирает случайную роль из списка, к примеру:

["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]

 

give_powers, передавая силу и значение можно менять power_list для определенного героя, к примеру:

char1.give_powers('ловкость', 5)

увеличит ловкость вашего героя.

 

Создайте три разных дочерьних класса от класса Character - Elf, Orc, DragonBorn,

дайте каждому из классов уникальный метод и добавьте уникальные аттрибуты экземпляра класса,наследуя init от Character. Создайте несколько героев от этих классов и вызовите их методы и методы родительского класса Character.

"""
 


# from random import choice
# class Character:
#     role_list = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#     weapon_list = ['Пистолет', 'Автомат', 'Меч', 'Гранотамет', 'Граната', 'Бита', 'Танк', 'Копье', 'Снайпер', 'Лук', 'Базука - РПГ']
#     power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }
#     def __init__(self, name):
#         self.name = name
#     def give_weapon(self):
#         weapon = choice(self.weapon_list)
#         return weapon
#     def give_role(self):
#         role = choice(self.role_list)
#         return role
#     def give_powers(self, power, val):
#         self.power_list[power] = val



# class Elf(Character):
#     magic_skill = ['Бессмертие', 'Читать мысли', 'Регенерация', 'Управление чужим разумом', 'Управление воздухом', 'Управление водой', 'Управление огнем', 'Целительство']
#     def __init__(self, name):
#         super().__init__(name)

#     def skill_(self):
#         skill = choice(self.magic_skill)
#         return skill
#     def __str__(self):
#         return f'Имя: {self.name}\nОружие: {self.give_weapon()}\nПрофессия: {self.give_role()}\nХарактеристика: {self.power_list}\nУникальный скилл: {self.skill_()}'
    
    
# elf = Elf('Legolas')
# elf.give_powers('мудрость', 200)
# elf.give_powers('харизма', 90)
# elf.give_powers('интеллект', 2)
# elf.give_powers('сила', 100)
# elf.give_powers('ловкость', 5)
# print(elf)
# print("""  """)

# class Orc(Character):
#     location = ['Средиземье', 'Мордор', 'Шир', 'Драндуил', 'Темный лес', 'Гондор', 'Мериадок', 'Вонючий носок']
#     def __init__(self, name):
#         super().__init__(name)

#     def local(self):
#         local_ = choice(self.location)
#         return local_

#     def __str__(self):
#             return f'Имя: {self.name}\nОружие: {self.give_weapon()}\nПрофессия: {self.give_role()}\nХарактеристика: {self.power_list}\nМесто жительства: {self.local()}'
    
# orc = Orc('АзокОсквернитель')
# orc.give_powers('мудрость', 40)
# orc.give_powers('харизма', 90)
# orc.give_powers('интеллект', 2)
# orc.give_powers('сила', 100)
# orc.give_powers('ловкость', 5)
# print(orc)
    


# class DragonBorn(Character):
#     duty = ['Мыть посуду', 'Смотреть за детьми', 'Пылесосить', 'Жена на час', 'Боди массаж']
#     def init(self, name):
#         super().__init__(name)
#     def choice_duty(self):
#         duty_ = choice(self.duty)
#         return duty_
#     def __str__(self):
#         return f'Имя: {self.name}\nОружие: {self.give_weapon()}\nПрофессия: {self.give_role()}\nХарактеристика: {self.power_list}\nОбязанность: {self.choice_duty()}'

# gohan = DragonBorn('Гохан')
# print(gohan)


















































