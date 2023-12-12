#1
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def description(self):
        return f" {self.brand} {self.model}, {self.year} "
    
Choice = input("Choose Toyota or Ford: ")

if "Toyota":
    car1 = Car("Toyota", "Camry", 2022)
    print(car1.description())  
elif "Ford":
    car2 = Car("Ford", "Mustang", 2021)
    print(car2.description()) 

#2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

person1 = Person("Amelia", 25)
print(f"Person 1 - Name: {person1.name}, Age: {person1.age}")

employee1 = Employee("Ali", 30, 250000)
print(employee1.get_info())

employee2 = Employee("Dylan", 28, 260000)
print(employee2.get_info())

#3
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "WOOF!"

class Cat(Animal):
    def speak(self):
        return "MEAOW!"

dog_instance = Dog()
cat_instance = Cat()

print(dog_instance.speak()) 
print(cat_instance.speak())  

#4
class BankAccount:
    def __init__(self, account_number):
        self.balance = 0
        self.account_number = account_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозит в размере {amount} тенге выполнен. Новый баланс: {self.balance} тенге.")
        else:
            print("Ошибка: Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Снятие средств в размере {amount} тенге выполнено. Новый баланс: {self.balance} тенге.")
        else:
            print("Ошибка: Недостаточно средств на счете или сумма для снятия должна быть положительной.")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, interest_rate):
        super().__init__(account_number)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
        print(f"Начислены проценты в размере {interest_amount} тенге. Новый баланс: {self.balance} тенге.")

# Сберегательный счет
account_number = input("Введите номер счета: ")
interest_rate = float(input("Введите процентную ставку для сберегательного счета: "))
savings_account = SavingsAccount(account_number, interest_rate)

# Внесение депозита
deposit_amount = float(input("Введите сумму для депозита: "))
savings_account.deposit(deposit_amount)

# Снятие средств
withdraw_amount = float(input("Введите сумму для снятия: "))
savings_account.withdraw(withdraw_amount)

# Начисление процентов
savings_account.add_interest()

