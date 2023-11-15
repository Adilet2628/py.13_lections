# Инкапсуляция 
# 1. языковая конструкция которая помогает связать данные с методами для их обработки и их управления (связь между данным и методами которые пользуются ими )(класс это капсула)
# 2. механизм сокрытия , при помощи которого можно ограничить доступ одного компонента программы к друному компоненту 


# инкапсуляция как мех анизм сокрытия
# 3 уровня сокрытия данных:
        # 1. Публичный (public)- number, print_number
        # 2. защищенный (_protectid)- _number
        # 3. приватный(_private)- __number




# class Car:
#     _country = 'Germany'
#     __moror = 'Turbo diesel'
#     def __init__(self)->None:
#         self.marka = "Mersedes_Benz"#public
#         self._model = 'W140'#protected
#         self.__color = 'grey'#private
# obj = Car()
# print(dir(obj))
# print(obj._country)
# print(obj._model)
# print(obj._Car__motor)


# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_calls = 15
#     def call(self):
#         print(f'{self._caller} звонит вам!')
#         choice = input('взять трубку(yes/no): ').lower().strip()
#         self._trun_on() if choice =='yes' else print('сбросили трубку')

#     def __incriment_calls(self):
#         self.__count_of_calls +=1



#     def _trun_on(self):
#         self.__incriment_calls()
#         print('Alo')
#         print(f'Count of calls with{self._caller}:{self.__count_of_calls}')


# phone = Phone()
# print(phone.username)
# phone.call()
# phone.call()
# phone.call()
# phone.call()
# ---------------------------------------------------------------------------------------------------------
# class Person:
#     def __init__(self,name,age)->None:
#         self.set_name(name) 
#         self.set_age (age)

#     def display_info(self):
#         print(f'my name is {self.name} and i\'m {self.age} years old!')


#     def set_name(self,name):
#         if isinstance(name,str):
#             self._name = name 
#         else:
#             print('oshibka') 

#     def set_age(self,age):
#         if isinstance(age,int) and 0 < age< 200:
#             self._age = age
#         else:
#             print('age must be int obj')    










# obj = Person('John',24)
# obj.display_info()
# obj.name = 'jamie'
# obj.age = '28'
# obj.display_info()
# obj.name = 24
# obj.age = -14
# obj.age = None
# obj.display_info()



# -------------------------------
# getter/ setter/

# они нужны чтобы избкжать прямого обращения к скрытым атрибутам при этом можно добавить логику валидация(проверки) данных которые будут установленны в атрибут и тд

# Анотация свойств(@property(getter setter))

# class Person:
#     def __init__(self)->None:
#         self.__name = None
#         self.__age = None
#     @property#getter
#     def name (self):
#         return self.__name

#     @property#getter
#     def age(self):
#         return self.__age 

#     @name.setter
#     def name(self,other):
#         if isinstance(other,str): self.__name = other

#         else:
#             print('name oshibka')
#     @age.setter
#     def age (self,other):
#         if isinstance(other,int) and 0 < other <200:
#             self.__age = other

#         else:
#             print('age oshibka')




# obj = Person()
# print(obj.name,obj.age)
# obj.name = 'john'
# obj.age=24
# print(obj.name,obj.age)

# =========================================================================================

"""
1)Создайте класс и объявите в нём 3 метода: публичный, защищённый и приватный. Затем создайте экземпляр данного класса и вызовите по очереди каждый из методов.
"""
# class Person:
#         def __init__(self,name, age,last_name):
#                 self.name = name 
#                 self.age = age
#                 self.last_name = last_name
#         def name_(self,name):
#                 if isinstance(name, str):
#                         self.name = name
#                         return self.name
#                 else:
#                         return f'{name} не является строкой '
                
#         def _age(self,age):
#                 if isinstance(age,int) and 0 < age < 120:
#                         self.age = age
#                         return self.age
#                 else:
#                          return  f'{age} не явлется int или чел умер уже хехехе'      
#         def _last_name(self,last_name):
#                 if isinstance(last_name,str):
#                         self.last_name = last_name
#                         return self.last_name
#                 else:
#                         return f'{last_name} не является строкой'
        

# obj = Person('k', 5, 'o')
# print(obj.name_('adi'))
# print(obj._age(347))
# print(obj._last_name('ghj'))










"""
2)Определите класс A, в нём объявите метод method1, который печатает строку "Hello World". Затем создайте класс B, который будет наследоваться от класса A. Создайте экземпляр от класса B, и через него вызовите метод method1.
"""
# class A:
#         def method1(self):
#                 print('hello World')
# class B(A):
#         def met(self):
#                 self.method1()
# obj = B()
# obj.met()              


"""
3)Объявите класс Car, в котором будет приватный атрибут экземпляра speed. Затем определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, с помощью которого Вы будете получать значение скорости.
"""
# class Car:
#         def __init__(self,speed=0):
#                 self.__speed = speed
                
#         def set_speed(self,a):
#                 if isinstance(a,int) and 0 < a <221:
#                         self.__speed += a
#                 else: 
#                         print('OSHIBKA')        
#         def show_speed(self):
#               print (f'{self.__speed} км/ч')


# a = Car()
# a.set_speed(12)
# a.show_speed()
"""
4)Перепишите класс Car из предыдущего задания.
Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора @property, для того чтобы можно было работать с данным классом следующим образом:

car = Car()
car.speed = 120
print(car.speed)
"""
# class Car:                             
#         def __init__(self,speed=0):
#                 self.__speed = speed
                
#         def set_speed(self,a):
#                 if isinstance(a,int) and 0 < a <221:
#                         self.__speed += a
#                 else: 
#                         print('OSHIBKA')        
#         def show_speed(self):
#               print (f'{self.__speed} км/ч')
              
"""
5. Создайте класс Car. Пропишите в init параметры make, model, year, odometer, fuel.
Пусть у показателя odometer будет первоначальное значение 0, а у fuel 70.
Добавьте метод drive, который будет принимать расстояние в км. В самом начале проверьте,
хватит ли вам бензина из расчета того, что машина расходует 10 л / 100 км (1л - 10 км) . Если
его хватит на введенное расстояние, то пусть этот метод добавляет эти километры к значению
одометра, но не напрямую, а с помощью приватного метода __add_distance. Помимо этого
пусть метод drive также отнимет потраченное количество бензина с помощью приватного
метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. Если же бензина не Let’s drive!”. Если же бензина не
хватит, то распечатайте “Let’s drive!”. Если же бензина не Need more fuel, please, fill more!”
"""
# писать код здесь
"""
6)# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.
"""













