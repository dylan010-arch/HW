#1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")
# Персона 1
person1 = Person("Иван", 25)
person1.introduce()
# Персона 2
person2 = Person("Мария", 30)
person2.introduce()

#2
class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def set_description(self, new_description):
        self.description = new_description

    def set_price(self, new_price):
        if new_price >= 0:
            self.price = new_price
        else:
            print("Цена не может быть отрицательной.")

    def display_product_info(self):
        print(f"Название: {self.name}")
        print(f"Описание: {self.description}")
        print(f"Цена: {self.price} тг.")

if __name__ == "__main__":
    # Создаем экземпляр класса Product
    product1 = Product("Ноутбук", "Мощный ноутбук с высокой производительностью", 250000)

    # Выводит информацию о продукте
    product1.display_product_info()

    # Изменяет описание продукта
    product1.set_description("Ноутбук с процессором Intel Core i7 и 16 ГБ RAM")

    # Изменяет цену продукта
    product1.set_price(250000)

    # Выводит обновленную информацию о продукте
    product1.display_product_info()

#3
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def checkout(self):
        if self.is_available:
            print(f"Книга '{self.title}' выдана читателю.")
            self.is_available = False
        else:
            print(f"Извините, книга '{self.title}' уже выдана.")

    def checkin(self):
        if not self.is_available:
            print(f"Книга '{self.title}' возвращена в библиотеку.")
            self.is_available = True
        else:
            print(f"Ошибка: книга '{self.title}' уже находится в библиотеке.")

    def display_info(self):
        status = "доступна" if self.is_available else "недоступна"
        print(f"Название: {self.title}\nАвтор: {self.author}\nГод публикации: {self.publication_year}\nСтатус: {status}\n")

book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("Преступление и наказание", "Федор Достоевский", 1866)

book1.display_info()
book1.checkout()
book1.display_info()
book1.checkin()
book1.display_info()

book2.display_info()
book2.checkout()
book2.display_info()
