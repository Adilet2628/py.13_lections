# ;
  # Создайте класс University. В конструкторе создайте переменную экземпляра name, куда записывается переданный аргумент university_name.


# class University:
#     def __init__(self,university_name):
#         self.university_name = university_name
#         print(self.university_name)
# a = University('adi')


    # Создайте переменную класса departments, у которого значение по умолчанию -- пустой словарь
    # Создайте метод add_department, у которого параметр название факультета. Метод должен записать в словарь departments название факультета, а в качестве значения -- пустой список
    


# class Departments:
#     def __init__(self,name):
#         self.name = name
#         self.departments = {}

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





















