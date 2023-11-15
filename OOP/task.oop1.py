"""
1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
"""
# class Circle:
#     pi = 3.14
#     color = 'blue'
#     def __init__(self,radius,color=color):
#         self.radius = radius
#         self.color = color
#     def pl(self):
#         print(f'площадь круга = {self.radius**2*self.pi}\nцвет {self.color}')    

# obj = Circle(5)
# obj.pl()




"""
2) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
"""
# class Song:
#     def __init__(self,name,author,year)->None:
#         self.name = name 
#         self.author = author
#         self.year = year 
#     def show_author(self):
#         print(f"Автор песни {self.author}")

#     def show_title(self):
#         print(f"Название песни {self.name}") 

#     def show_year(self):
#         print(f'Эта песня вышла в {self.year} году')    

# obj = Song('Привет','Bakr','2023')
# obj.show_author()
# obj.show_title()
# obj.show_year()



"""
3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
"""
# class Taxi:
#     def __init__(self,name,price,raing_price)->None:
#         self.name = name 
#         self.price = price
#         self.raing_price = raing_price
    
#     def go(self,km):
     
#         print(f'{self.name} стоимость поездки {self.price + self.raing_price*km}')


# obj = Taxi('Jorgo', 50, 20)  
# obj1 = Taxi('Yandex',60,15) 
# obj2 = Taxi('Namba',50,13)     
# obj.go(3)
# obj1.go(3)
# obj2.go(3)





"""
4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
Затем объявите экземляр класса и вызовите метод.
"""
# class Aparat:
#     def __init__(self,name,last_name,num)->None:
#         self.name = name 
#         self.last_name = last_name
#         self.num = num 

#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон:{self.num}')    
   
   

# obj = Aparat('Ivan','Petrov','+996708324692')
# obj.get_info()




"""
5) Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
# """
# class Salary:
#     def __init__(self,zarplata,stash):
#         self.nalog = 0.08
#         self.zarplata = zarplata
#         self.stash = stash
#     def summa(self):
          
       
#          print(f'summa naloga = {self.zarplata*self.nalog*self.stash}') 
# obj = Salary(10000,12)   
# obj.summa()












