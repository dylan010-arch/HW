#1
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def arithmetic_operation(operation, x, y):
    if operation == "сложение":
        return add(x, y)
    elif operation == "вычитание":
        return subtract(x, y)
    elif operation == "умножение":
        return multiply(x, y)
    else:
        return "Произошла ошибка"

def main():
    x = input("Введите первое число: ")
    y = input("Введите второе число: ")

    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        
        result = arithmetic_operation("сложение", x, y)
        print(f"Результат сложения: {result}")

        result = arithmetic_operation("вычитание", x, y)
        print(f"Результат вычитания: {result}")

        result = arithmetic_operation("умножение", x, y)
        print(f"Результат умножения: {result}")
    else:
        print("Ошибка ввода. Введите корректные числа.")

if __name__ == "__main__":
    main()


#2
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == "__main__":
    choice = input("Выберите фигуру (Круг, Прямоугольник, Треугольник): ").capitalize()

    if choice == "Круг":
        radius = float(input("Введите радиус круга: "))
        shape = Circle(radius)
    elif choice == "Прямоугольник":
        width = float(input("Введите ширину прямоугольника: "))
        height = float(input("Введите высоту прямоугольника: "))
        shape = Rectangle(width, height)
    elif choice == "Треугольник":
        base = float(input("Введите основание треугольника: "))
        height = float(input("Введите высоту треугольника: "))
        shape = Triangle(base, height)
    else:
        print("Неправильный выбор фигуры")

    area = shape.area()
    print(f"Площадь выбранной фигуры ({choice}) равна {area}.")

#3
from abc import ABC

class Drawable(ABC):
    def draw(self):
        pass

class Circle(Drawable):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Рисуем круг с радиусом {self.radius}.")

class Rectangle(Drawable):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Рисуем прямоугольник с шириной {self.width} и высотой {self.height}.")

def main():
    circle_radius = float(input("Введите радиус круга: "))
    rectangle_width = float(input("Введите ширину прямоугольника: "))
    rectangle_height = float(input("Введите высоту прямоугольника: "))

    # Создание объектов
    circle = Circle(circle_radius)
    rectangle = Rectangle(rectangle_width, rectangle_height)

    # Вызов метода draw 
    circle.draw()
    rectangle.draw()

if __name__ == "__main__":
    main()

