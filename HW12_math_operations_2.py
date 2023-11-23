import math_operations

num1=float(input("Enter number 1 ="))
num2=float(input("Enter number 2 ="))

ans = input("Choose an operation:")

if ans=="add":
    result_add = math_operations.add(num1, num2)
    print(f"{num1} + {num2} = {result_add}")
elif ans=="substract":
    result_subtract = math_operations.subtract(num1, num2)
    print(f"{num1} - {num2} = {result_subtract}")
elif ans=="multiply":
    result_multiply = math_operations.multiply(num1, num2)
    print(f"{num1} * {num2} = {result_multiply}")
elif ans=="divide":
    result_divide = math_operations.divide(num1, num2)
    print(f"{num1} / {num2} = {result_divide}")
