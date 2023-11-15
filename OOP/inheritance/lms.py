"""это старое 
# Напишите класс Subscriber, у которого есть переменные экземпляра:
#         firstname
#         lastname
#         Сделайте так, чтобы метод __repr__ возвращал firstname + lastname

# class Subscriber:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#     def __repr__(self):
#         print (f'{self.firstname} {self.lastname}')


# obj = Subscriber('adilet', 'raimbekov')
# obj.__repr__()

# # 2,3
# class Provider:
#     def __init__(self, name):
#         self.name = name

#     def register_payment(self, subscriber, amount):
       
#         return True

# class Subscriber:
#     def __init__(self, name):
#         self.name = name


# # ========================
# class Terminal:
#     def __init__(self):
#         self.amount = 0
#         self.providers = []

#     def register(self, provider):
#         if isinstance(provider, Provider):
#             self.providers.append(provider)
#         else:
#             raise ValueError("oshipka shoto tam povider")

#     def pay(self, provider, subscriber, amount):
#         if provider in self.providers:
#             if provider.register_payment(subscriber, amount):
#                 self.amount += amount
#                 print(f"Payment of {amount} accepted for provider {provider.name}.")
#             else:
#                 print(f"Payment of {amount} for provider {provider.name} failed.")
#         else:
#             print(f"Provider {provider.name} is not registered with this terminal.")



# provider1 = Provider("Provider A")
# provider2 = Provider("Provider B")
# terminal = Terminal()

# terminal.register(provider1)
# terminal.register(provider2)

# subscriber = Subscriber("vcbbce")

# payment_amount = 500.0
# p = 200
# terminal.pay(provider1, subscriber, payment_amount)
# terminal.pay(provider2, subscriber, p)

# print(f"Provider A balance: {payment_amount}")
# print(f"Terminal amount: {terminal.amount}")

# =======================================================================================================

    # Создайте класс University. В конструкторе создайте переменную экземпляра name, куда записывается переданный аргумент university_name.


# class University:
#     def __init__(self,university_name):
#         self.university_name = university_name
#         print(self.university_name)
# a = University('adi')


    # Создайте переменную класса departments, у которого значение по умолчанию -- пустой словарь
    # Создайте метод add_department, у которого параметр название факультета. Метод должен записать в словарь departments название факультета, а в качестве значения -- пустой список
    


# class Departments:
#     def __init__(self,name,departments = {}):
#         self.name = name
#         self.departments = departments

#     def add_department(self, fakultet):
#         self.departments[fakultet] = []
#         return self.departments
# a = Departments('auca')
# a.add_department('info')
# a.add_department('it')
# print(a.add_department('math'))
    # Создайте класс Student, в конструкторе которого записывается firstname, lastname студента. Т.е. при создании экземпляра должны быть переданы имя и фамилия студента.
    # Создайте метод add_student с параметрами название факультета и объект студент -- экземпляр класса Student. Метод должен записать в словарь departments студента в соответствующий факультет.
    # Создайте экземпляр университета. Создайте нескольких студентов. Добавьте факультеты. Добавьте студентов в факультеты.
# class Student:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname        
        

# class Departments:
#     def __init__(self,name):
#         self.name = name
#         self.departments = {}

#     def add_department(self, fakultet):
#         self.departments[fakultet] = []

#     def add_student(self, fakultet, student):
#         if fakultet in self.departments:
#             self.departments[fakultet].append(student)
#         else:
#             print(f"Факультет '{fakultet}' не существует в университете {self.name}.")

# my = Departments("Мой университет")

# my.add_department("Факультет информатики")
# my.add_department("Факультет иностранных языков")

# s1 = Student("Иван", "Иванов")
# s2 = Student("Петр", "Петров")
# s3 = Student("Мария", "Сидорова")

# my.add_student("Факультет информатики", s1)
# my.add_student("Факультет иностранных языков", s2)
# my.add_student("Факультет информатики", s3)

# for department, students in my.departments.items():
#     print(f"Факультет: {department}")
#     for student in students:
#         print(f"Студент: {student.firstname} {student.lastname}")
"""





# Создайте класс Person

# Создайте метод __init__ () и определите внутри него два динамических атрибута: name и birth_year (год рождения). Свои начальные значения они получают из параметров метода __init__ ()

# Создайте класс Student (студент), который наследуется от класса Person

# Добавьте ему 3 динамических поля (атрибут)

# Первое поле course (курс на котором он обучается) должно быть public так как такая информация как должность сотрудника она открытая и не является тайной,

# Второе поле notebook (его ноутбук) должно быть экземпляром класса Notebook

# Третье поле private называется payments (сумма оплат студента за курсы) и по умолчанию при создании равен пустому списку.

# Создать метод do_payment, которое принимает в качестве параметра сумму платежа и добавляет его в payments

# Создать метод get_all_payments, которое возвращает сумму всех платежей, сделанных студентом.

# Создать метод check_pc которая проверяет ноутбук на соответствие требованиям к программированию. Минимальные требования к ноутбуку должны быть:

# Оперативная память 4ГБ и более

# Память 120 ГБ и более

# Процессор 2 ядра и более

# Если ноутбук не подходит хотя бы по одному параметру, то метод должен выдать False, если все три параметра сходятся, то True

class Person:
    def __init__(self,name,birth_year):
        self.name = name 
        self.birth_year = birth_year

class Student(Person):
    def __init__(self,course,notebook,__payments=[]):
        self.course = course
        self.notebook = notebook
        self.__payments = __payments
    def do_payment(self,a):
        self.a+=self.__payments
    def get_all_payments(self):
        print(self.__payments)
    def check_pc(self):
                i





