dz
import math
def pifagor():
    a = int(input('введите первый катет: '))
    b = int(input('введите второй катет: '))
    c = a**2 + b**2
    c1 = f'гипотенуза равна {math.sqrt(c)}'
    return c1
print(pifagor())

