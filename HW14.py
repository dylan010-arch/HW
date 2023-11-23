#1
class Calendar:
    def __init__(self):
        self.events = {}

    def add_event(self, date, event):
        if date not in self.events:
            self.events[date] = []
        self.events[date].append(event)
        print(f"Event '{event}' added on {date}.")

    def display_events_on_date(self, date):
        if date in self.events:
            print(f"Events on {date}: {', '.join(self.events[date])}")
        else:
            print(f"No events on {date}.")

    def remove_event(self, date, event):
        if date in self.events and event in self.events[date]:
            self.events[date].remove(event)
            print(f"Event '{event}' removed from {date}.")
        else:
            print(f"Event '{event}' not found on {date}.")

    def display_events_next_n_days(self, n):
        for i in range(n):
            date = f"Day {i + 1}"
            if date in self.events:
                print(f"Events on {date}: {', '.join(self.events[date])}")
            else:
                print(f"No events on {date}.")


def main():
    calendar = Calendar()

    while True:
        print("\n1. Add Event")
        print("2. Display Events on Date")
        print("3. Remove Event")
        print("4. Display Events for Next N Days")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            date = input("Enter the date for the event: ")
            event = input("Enter the event: ")
            calendar.add_event(date, event)
        elif choice == "2":
            date = input("Enter the date to display events: ")
            calendar.display_events_on_date(date)
        elif choice == "3":
            date = input("Enter the date for the event: ")
            event = input("Enter the event to remove: ")
            calendar.remove_event(date, event)
        elif choice == "4":
            n = int(input("Enter the number of days to display events for: "))
            calendar.display_events_next_n_days(n)
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


#2

class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def increase_quantity(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"Quantity of {self.name} increased by {amount}.")
        else:
            print("Please enter a positive quantity")

    def decrease_quantity(self, amount):
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            print(f"Quantity of {self.name} decreased by {amount}.")
        elif amount > self.quantity:
            print(f"Error: Quantity of {self.name} is less than {amount}.")
        else:
            print("Please enter a positive quantity")

    def calculate_total_value(self):
        total_value = self.quantity * self.price
        return total_value

item1 = InventoryItem("Laptop", 3, 250000)
print(f"{item1.name} - Quantity: {item1.quantity}, Price: T{item1.price}, Total Value: ${item1.calculate_total_value()}")
item1.increase_quantity(int(input("Enter a number:")))
print(f"Updated Quantity: {item1.quantity}, Updated Total Value: T{item1.calculate_total_value()}")
item1.decrease_quantity(int(input("Enter a number:")))
print(f"Updated Quantity: {item1.quantity}, Updated Total Value: T{item1.calculate_total_value()}")

#3
class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}
    
    def add_subject(self, subject):
        self.subjects[subject] = []
    
    def add_grade(self, subject, grade):
        if subject in self.subjects:
            self.subjects[subject].append(grade)
        else:
            print(f"Предмет {subject} не найден для студента {self.name}")
    
    def calculate_average(self):
        if not self.subjects:
            return 0 
        total_grade = 0
        total_subjects = 0
        for grades in self.subjects.values():
            total_grade += sum(grades)
            total_subjects += len(grades)
        return total_grade / total_subjects

student1 = Student(input("Имя студента: "))

while True:
    subject = input("Предмет (или 0 для завершения): ")
    if subject.lower() == "0":
        break
    student1.add_subject(subject)
    grade = int(input(f"Оценка по предмету {subject}: "))
    student1.add_grade(subject, grade)

average_grade = student1.calculate_average()
print(f"Средний балл студента {student1.name}: {average_grade}")

