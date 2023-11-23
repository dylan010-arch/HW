#2
def count_words(text):
    words = text.split()
    return len(words)

def usage():
    text = "Я говорю, отчего люди не летают так, как птицы? Знаешь, мне иногда кажется, что я птица. Когда стоишь на горе, так тебя и тянет лететь. Вот так бы разбежалась, подняла руки и полетела."
    
    word_count = count_words(text)
    print(f"Количество слов в тексте: {word_count}")
if __name__ == "__main__":
    usage()

#3
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}")

student1 = Student("Ivar", 20)

student1.display_info()

#4
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == "__main__":
    radius = float(input("Введите радиус круга: "))
    circle = Circle(radius)
    print(f"Площадь круга: {circle.area()}")

    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    rectangle = Rectangle(length, width)
    print(f"Площадь прямоугольника: {rectangle.area()}")
