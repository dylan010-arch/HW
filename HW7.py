#1
number = int(input("Enter a number: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
result = factorial(number)
print("Factorial of", number, "is", result)

#2
# Celsius to Fahrenheit conversion
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Fahrenheit to Celsius conversion
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

number_1 = int(input("Enter Celsius:"))
fahrenheit_temperature = celsius_to_fahrenheit(number_1)
print(f"{number_1} Celsius is {fahrenheit_temperature} Fahrenheit.")

number_2 = int(input("Enter Fahrenheit:"))
celsius_temperature = fahrenheit_to_celsius(number_2)
print(f"{number_2} Fahrenheit is {celsius_temperature} Celsius.")

#3
def find_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("Enter first digit: "))
num2 = int(input("Enter second digit: "))

lcm = find_lcm(num1, num2)
print(f"The Least Common Multiple of {num1} and {num2} is {lcm}")

#4
def cal_month_payment(principal, annual_interest_rate, num_years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_months = num_years * 12
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**num_months) / ((1 + monthly_interest_rate)**num_months - 1)
    return monthly_payment

principal = int(input("Enter a debt amount: "))
annual_interest_rate = 5.0
print("Annual interest rate is 5% ")
num_years = int(input("Enter a period of years:"))

monthly_payment = cal_month_payment(principal, annual_interest_rate, num_years)
print(f"Monthly payment:{monthly_payment:.2f} T")

#5
def is_palindrome(number):
    num_str = str(number)
    if num_str == num_str[::-1]:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
