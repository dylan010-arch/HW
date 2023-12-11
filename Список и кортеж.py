#1
numbers = [56,42,85,52,53,78,96,52,42,6,57,96,63,41,12,36]
sum = sum(numbers)
av = sum / len(numbers)

print("Numbers:", numbers)
print("Sum of Numbers:", sum)
print("Average:", av)

#2
employee1 = ("Athos", "Royal Musketeer", 25,)
employee2 = ("Partos", "Musketeer", 23)
employee3 = ("Aramis", "General of the Jesuit order", 22)

for employee in (employee1, employee2, employee3):
    print("Name:", employee[0])
    print("Position:", employee[1])
    print("Age:", employee[2])
    print()   

#3
list = ["Astana","Almaty","Shymkent"]
new_list = ["Akmola","Almaty","Turkestan"]
condition = new_list
list = new_list
print(list)

#4
fruits_1 = ["apple","pear", "banana", "kiwi", "orange","lemon"]
fruits_2 = [fruit for fruit in fruits_1 if len(fruit) >= 5]
print(fruits_2)

#5
student1 = ("Iman", 90)
student2 = ("Maria", 85)
student3 = ("Pete", 78)
student4 = ("Ann", 92)
student5 = ("Mira", 88)

print(f"{student1[0]},{student1[1]}")
print(f"{student2[0]},{student2[1]}")
print(f"{student3[0]},{student3[1]}")
print(f"{student4[0]},{student4[1]}")
print(f"{student5[0]},{student5[1]}")

#6
even_num = []
for i in range(1, 21):
    if i % 2 == 0:
        even_num.append(i)
print(even_num)

#7
list_new = [1, 2, 3, 4, 5]
square = [x ** 2 for x in list_new]
sum_square = sum(square)

print("Sum of squares of numbers from the new list:", sum_square)





