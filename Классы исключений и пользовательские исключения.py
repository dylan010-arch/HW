#1
def main():
    try:
        x = float(input("Введите первое число (делимое): "))
        y = float(input("Введите второе число (делитель): "))

        result = x / y

        print(f"Результат деления: {result}")

    except ZeroDivisionError:
        print("Ошибка: деление на ноль недопустимо.")

    except ValueError:
        print("Ошибка: введены некорректные данные. Пожалуйста, введите числа.")

if __name__ == "__main__":
    main()

#2
class ValidationError(Exception):
    pass

def valid_username(username):
    if not username:
        raise ValidationError("Имя пользователя не должно быть пустым")
    if any(char.isdigit() or not char.isalnum() for char in username):
        raise ValidationError("Имя пользователя не должно содержать специальные символы или цифры")

def main():
    try:
        username = input("Введите имя пользователя: ")
        valid_username(username)
        print(f"Имя пользователя '{username}' допустимо.")
    except ValidationError as ve:
        print(f"Ошибка валидации: {ve}")

if __name__ == "__main__":
    main()

#3
import time

class TimerContextManager:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = (self.end_time - self.start_time)*1000
        
        print(f"Время выполнения:  {elapsed_time} миллисекунд")

with TimerContextManager():
    user_input = input("Введите 'wq': ")
    if user_input == "wq":
        print("Операция ввода-вывода выполнена")



