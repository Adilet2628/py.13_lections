# Mixins

# Миксинсы - класса которые используются для наследования и передачи дочерним классам определенных методов, но от них не создаются обьекты 

# 1 вы хотите представить множество доп методов для классов
# 2 вы хотите использовать один конкретный метод 

# class EngineMixin:
#     def start_engine(self):
#         print('started endine')


# class RadioMixin:
#     def play_radio(self):
#         print('music is playing')


# class Auto(EngineMixin,RadioMixin):
#     pass



# class Plane(EngineMixin):
#     pass


# class Smartphone(RadioMixin):
#     pass


# class Traing(EngineMixin,RadioMixin):
#     pass


# class FlyMixin:
#     def fly(self):
#         print('I can fly')


# class WalkMixin:
#     def walk(self):
#         print('I can walk')

# class SwimMixin:
#     def swim(self):
#         print('I can swim')



# class Human(WalkMixin,SwimMixin):
#     name = 'human'

#     def talk(self):
#         print('I can talk')

# class Fish(SwimMixin):
#     name = 'fish'

# class Volans(SwimMixin,FlyMixin):
#     name = 'volan'



# class Duck(SwimMixin,FlyMixin):    
#     name = 'duck'





# obj = Human()
# obj.walk()
# obj.swim()







