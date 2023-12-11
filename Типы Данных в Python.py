a=15
b=3
print("Сумма:",a+b)
print("Разность:",a-b)
print("Умножение:",a*b)
print("Деление:",a/b)

name="Толагай"
city="Астана"
age="22"
print("Как вас зовут?"+" "+name)
print("Вы откуда?"+" "+city)
print("Сколько вам лет?"+" "+age)


import math
r=6
z=4
C=2*math.pi*r
S=math.pi*r*r
C=round(C,z)
S=round(S,z)
print('Длина окружности:',C)
print('Площадь окружности:' ,S)

yes='+'
no='-'
a=(input('Сегодня солнечно? +/-: ',))
if a==yes:
    is_sunny=True
    print('Сегодня солнечно!')
else:
    is_sunny=False
    print('Сегодня пасмурно')



