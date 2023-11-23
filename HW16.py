#1
class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, model, year, fuel_type):
        super().__init__(model, year)
        self.fuel_type = fuel_type

vehicle1 = Vehicle("Generic Model", 2020)
print(f"Vehicle: {vehicle1.model}, Year: {vehicle1.year}")

car1 = Car("Toyota Camry", 2022, "Gasoline")
print(f"Car: {car1.model}, Year: {car1.year}, Fuel Type: {car1.fuel_type}")

car2 = Car("Tesla Model S", 2023, "Electric")
print(f"Car: {car2.model}, Year: {car2.year}, Fuel Type: {car2.fuel_type}")

#2
class Animal:
    def make_sound(self):
        pass

class Flyable:
    def fly(self):
        pass

class Bird(Animal, Flyable):
    def make_sound(self):
        return "Tweet Tweet"

    def fly(self):
        return "Bird Is Flying"

bird_instance = Bird()
print(bird_instance.make_sound()) 
print(bird_instance.fly())         

#3
class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make}")

class Car(Vehicle):
    def __init__(self, make, year, model_name, fuel_efficiency):
        super().__init__(make, year)
        self.model_name = model_name
        self.fuel_efficiency = fuel_efficiency

    def display_info(self):
        super().display_info()
        print(f"Model: {self.model_name}")
        print(f"Fuel Efficiency: {self.fuel_efficiency} mpg")

class Toyota(Car):
    def __init__(self, year, model_name, fuel_efficiency):
        super().__init__("Toyota", year, model_name, fuel_efficiency)

    def display_info(self):
        print("Toyota:")
        super().display_info()

class Ford(Car):
    def __init__(self, year, model_name, fuel_efficiency):
        super().__init__("Ford", year, model_name, fuel_efficiency)

    def display_info(self):
        print("Ford:")
        super().display_info()

class Tesla(Car):
    def __init__(self, year, model_name, fuel_efficiency):
        super().__init__("Tesla", year, model_name, fuel_efficiency)

    def display_info(self):
        print("Tesla:")
        super().display_info()

toyota_camry = Toyota(2023, "Camry", 30)
ford_focus = Ford(2023, "Focus", 25)
tesla_model_s = Tesla(2023, "Model S", 60)

toyota_camry.display_info()
print("\n")
ford_focus.display_info()
print("\n")
tesla_model_s.display_info()
