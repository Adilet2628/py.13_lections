

    # Создайте класс Notebook
    #     Создайте метод __init__() и определите внутри него три динамических атрибута: ram (размер оперативной памяти, целочисленное значение), memory (Размер внутренней памяти, целочисленное значение) и cpu (количество ядер в процессоре, целочисленное значение) . Свои начальные значения они получают из параметров метода __init__ ()


# class Notebook:
#     def __init__(self,ram,memory,cup):
#         self.ram = ram
#         self.cup = cup
#         self.memory = memory
#     def info(self):
#         return (f'«Ноутбук с {self.ram} ГБ оперативной памяти, {self.memory} ГБ внутренней памяти и с {self.cup} ядрами процессора»')

#     def add_notebook(self):
#         return {f'ram : {self.ram},memory : {self.memory},cup : {self.cup}'}
# a = Notebook(12,128,8)
# print(a.add_notebook())
# b = Notebook(16,516,10)
# print(b.add_notebook())

# print(a.info())
# print(b.info())


    #     Напишите метод info () в котором будет возвращаться через return информация о ноутбуке формата: «Ноутбук с 16 ГБ оперативной памяти, 500 ГБ внутренней памяти и с 4 ядрами процессора».
    #     Создайте класс-метод add_notebook который будет принимать в себя словарь и на основе словаря будет создавать экземпляр класса.

# Пример словаря = {

#     'ram': 12,

#     'memory': 500,

#     'cpu': 4

# }.