#1
import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

radius = float(input("Введите радиус круга: "))
area = calculate_circle_area(radius)
print(f"Площадь круга с радиусом {radius} равна {area:.2f}")

#2
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

prime_number = int(input("Enter a number: "))

if is_prime(prime_number):
    print(f"{prime_number} is a prime number.")
else:
    print(f"{prime_number} is not a prime number.")

#3
def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

base_length = float(input("Введите длину основания треугольника: "))
height = float(input("Введите высоту треугольника: "))
triangle_area = calculate_triangle_area(base_length, height)
print(f"Площадь треугольника: {triangle_area}")

#4
import time

current_time = time.time()  
seven_days = 7 * 24 
new_time = current_time + seven_days
current_date = time.strftime("%Y-%m-%d", time.localtime(current_time))
new_date = time.strftime("%Y-%m-%d", time.localtime(new_time))

print("Текущая дата:", current_date)
print("Дата через 7 дней:", new_date)



#5
import datetime

def days_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d" 
    date1 = datetime.datetime.strptime(date_str1, date_format)
    date2 = datetime.datetime.strptime(date_str2, date_format)
    delta = date2 - date1
    return abs(delta.days)

date1 = "2023-11-01"
date2 = "2023-11-11"
result = days_between_dates(date1, date2)
print(f"Number of days between {date1} and {date2}: {result} days")

#6
import datetime

def get_day_of_week(date_string):
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        day_of_week = date_object.weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(f"The day of the week for {date_string} is {days[day_of_week]}.")

date_input = input("Enter a date (YYYY-MM-DD): ")


#7
import random

def play():
    wish_digit = random.randint(0, 6)
    play = int(input("Угадайте число от 0 до 6: "))
    
    if play == wish_digit:
        print("Поздравляю! Вы угадали число.")
    else:
        print(f"К сожалению, правильное число было {wish_digit}. Попробуйте еще раз.")


#8
import random, string

def generate_random_username(length=8):
    characters = string.ascii_letters + string.digits
    username = ''.join(random.choice(characters) for _ in range(length))
    return username

random_username = generate_random_username(10)
print("Random Username:", random_username)

#9
import random

participants_list = ["Ali", "ALisa", "David", "Damir", "Eva"]

def choose_winner(participants):
    if participants:
        winner_index = random.randint(0, len(participants) - 1)
        winner = participants[winner_index]
        
        print(f"The winner is: {winner}")
    else:
        print("No participants in the list.")



#10
import datetime
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
print("Current Time:", formatted_time)

#11
import datetime

def get_current_time():
    current_time = datetime.now().time()
    time_12_hour_format = current_time.strftime("%I:%M:%S %p")
    time_24_hour_format = current_time.strftime("%H:%M:%S")

    print("Current Time (12-hour format):", time_12_hour_format)
    print("Current Time (24-hour format):", time_24_hour_format)

#12 
import random

def generate_random_time():
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    return formatted_time  

random_time = generate_random_time()
print(f"Random Time: {random_time}")








