#1
students = {
    'Анна': {'возраст': 20, 'курс': 3, 'предмет': 'Информатика'},
    'Арман': {'возраст': 22, 'курс': 4, 'предмет': 'Математика'},
    'Даниел': {'возраст': 21, 'курс': 2, 'предмет': 'Физика'}
}
print("Информация о студентах:")
for student, info in students.items():
    print(f"Имя: {student}, Возраст: {info['возраст']}, Курс: {info['курс']}, Предмет: {info['предмет']}")

имя_студента = input("Введите имя студента, которого нужно удалить: ")
if имя_студента in students:
    del students[имя_студента]
    print(f"Студент {имя_студента} удален из словаря.")
else:
    print(f"Студент с именем {имя_студента} не найден в словаре.")

#2
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
set_a = set(a)
set_b = set(b)

intersection = set_a.intersection(set_b)
print("Пересечение множеств:", intersection)
union = set_a.union(set_b)
print("Объединение множеств:", union)

#3
country_cities = {}  
while True:
    country = input("Введите название страны (esc):")
    if country.lower() == 'esc':
        break
    city = input("Введите название города:")

    if country in country_cities:
        country_cities[country].append(city)
    else:
        country_cities[country] = [city]

for country, cities in country_cities.items():
    print(f"{country}: {', '.join(cities)}")

#4
Inventar = {}
Inventar[1] = {"название": "Золотая монетка", "количество": 50, "цена":2000}
Inventar[2] = {"название": "Ложка", "количество": 30, "цена":4000}
Inventar[3] = {"название": "Ваза", "количество": 20, "цена": 5000}

for id, item in Inventar.items():
    print(f"Идентификатор: {id}")
    print(f"Название: {item['название']}")
    print(f"Количество: {item['количество']}")
    print(f"Цена: {item['цена']}")

#5
products = {
    1: {"название": "Iphone 15", "цена": 750000, "количество": 10},
    2: {"название": "Samsung Note S23", "цена": 540000, "количество": 15},
    3: {"название": "Iphone 15 Max", "цена": 850000, "количество": 5},
}

def поиск_товар(id):
    товар = products.get(id)
    if товар is not None:
        return товар
    else:
        return "Товар не найден"

id = 2 
результат_поиска = поиск_товар(id)

if результат_поиска != "Товар не найден":
    print(f"Информация о товаре с идентификатором {id}:")
    print(f"Название: {результат_поиска['название']}")
    print(f"Цена: {результат_поиска['цена']}")
    print(f"Количество: {результат_поиска['количество']}")
else:
    print(результат_поиска)

#6
товары = [
    {"название": "Молоко", "цена": 350},
    {"название": "Хлеб", "цена": 170},
    {"название": "Яблоки", "цена": 650},
]

def подсчет_стоимости(список_товаров):
    общая_стоимость = 0
    for товар in список_товаров:
        цена = товар.get("цена", 0) 
        общая_стоимость += цена

    return общая_стоимость

общая_стоимость = подсчет_стоимости(товары)
print(f"Общая стоимость товаров: {общая_стоимость}")

#7
a_1 = {1, 2, 3, 4, 5}
a_2 = {3, 4, 5, 6, 7}
union=a_1.union(a_2)
intersection=a_1.intersection(a_2)
print("Множество 1:", a_1)
print("Множество 2:", a_2)
print("Объедение множеств:{intersection}")
print("Объедение множеств:{union}")

