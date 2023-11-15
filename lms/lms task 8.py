

# 2
# def describe_sandwich(size, components):
#     size_description = ""
#     if size == "Большой":
#         size_description = "Большой сэндвич"
#     elif size == "Средний":
#         size_description = "Средний сэндвич"
#     elif size == "Маленький":
#         size_description = "Маленький сэндвич"
#     else:
#         print("Неверный размер сэндвича")
#         return
    
#     components_description = "со следующими ингредиентами: " + ", ".join(components)
#     print(size_description + " " + components_description)

# # Вызов функции с разными аргументами
# describe_sandwich("Большой", ["огурец", "колбаса", "сыр"])
# describe_sandwich("Средний", ["котлета", "помидор", "лук"])
# describe_sandwich("Маленький", ["тунец", "майонез"])




# 3
# def make_car(manufacturer, model, **kwargs):
#     car_info = {'manufacturer': manufacturer,
#         'model': model,}
#     car_info.update(kwargs)
    
#     info_str = f"{car_info['manufacturer'].title()} {car_info['model']}"

#     for key, value in car_info.items():
#         if key not in ['manufacturer', 'model']:
#             info_str += f", {key} is {value}"
    
#     return info_str

# car = make_car('subaru', 'outback', colour='blue', engine='V8')
# cas = make_car('lexsus', 'is200', colour= 'white', engine= '2.3'  )
# print(car)
# print(cas)

# 4
# while True:
#     def count_letters(s, k, n): 
#         return s.count(k), s.count(n)
#     t = input('Введите текст: ')
#     if t == 'выход':
#         break
#     k = input('Какую цифру ищем? ')[0]
#     n = input('Какую букву ищем? ')[0]
#     r = count_letters(t, k, n)
#     print(f"Количество цифр {k}: {r[0]}\nКоличество букв {n}: {r[1]}")

# 5
# def doljnosti(a: dict) -> str:
#     for k, v in a.items():
#         print(f'Работник {k}, занимает должность {v}')
# ls={"Asan":'директор', 'Osmon':'Texpoderjka','Sanjar': 'Menter'}
# doljnosti(ls)

# 6
while True:
    what = input ("Что будем делать? (+,-,*,/,%):")
    a = float(input("Ведите первое число:"))
    b = float(input("Ведите второе число:"))
    if what == "+":
        c = a  + b
        print("Результат:" + str(c))
    if what == "-":
        c = a - b
        print("Результат:" + str(c))   
    if what == "*":
        c = a * b
        print("Результат:" + str(c))
    elif what == "/":
        c = a / b
        print("Результат:" + str(c))
    else:
        print('Результат неверный')

















