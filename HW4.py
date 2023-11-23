#1
x=int(input("Enter x = "))
y=int(input("Enter y = "))
if x>y:
    print("X is bigger than Y")
if x<y:
    print("Y is bigger than X")
if x==y:
    print("X is equal Y")

#2
x=int(input("Enter x = "))
if x>10:
    print("Yes")
elif x==20:
    print("Yes")
else:
    print("No")

#3
Age=int(input("Enter your age "))
if Age>18:
    print("Yes")
elif Age==18:
    print("Yes")
else:
    print("No")

#4
Grade=int(input("Enter your Grade "))
if Grade==5:
    print("Your mark 'Otlichno'")
elif Grade==4:
    print("Your mark 'Horosho'")
elif Grade==3:
    print("Your mark 'Udovletvoritelno'")
else:
    print("Your mark 'Neudoletvoritelno'")

#5
Age=int(input("Enter your Age "))
if Age>=2:
    print("You are Mladenets")
if Age<=12:
    if Age >= 2:
        print("Your are 'Rebenok'")
if Age>=12:
    if Age <= 18:
        print("Your are 'Podrostok'")
if Age>=18:
    if Age <= 60:
        print("Your are 'Vzrosliy chelovek'")
if Age>=60:
        print("Your are 'Pozhiloy chelovek'")

#6 
x=int(input("Enter x = "))
if x==1:
    print("first quarter")
elif x==2:
    print("second quarter")
elif x==3:
    print("third quarter")
elif x==4:
    print("fourth quarter")
else:
    print("uncorrect")

#7
x=int(input("Enter a number:"))
y=x%2
if y==0:
    z=x%4
    print("even number")
    if z==0:
        print("delitsya na 4 bez ostatka ")
    else:
        print("ne delitsya na 4")
else:
    print("odd number")

#8
x=int(input("Enter (1-10):"))
if x==10 or x==9:
    print("Otlichno")
elif x==8 or x==7:
    print("Horosho")
elif x==6:
    print("Udovletvoritelno")
elif x==5:
    print("Neudovletvoritelno")
elif x<=4:
    input("Есть ли у ученика дополнительные работы?")
else:
   print("Error #444") 

#9
x=int(input("Enter a number"))
y=x%2
if x>0:
    if y==0:
        print(f" {x} - positive and even number ")
    else:
        print(f"{x} - positive and odd numver")
elif x<0:
    if y==0:
        print(f"{x} - negative and even number" )
    else:
        print(f"{x} - negative and odd number" )
else:
    print("Error")

#10 
year=int(input("Enter year:"))
x=year%4
y=year%100
if x==0 and y!=0:
    print(f"{year} visokosny god")
else:
    print(f"{year} ne visokosny god")

#11
age=int(input("Enter your age:"))
med=(input("Medical issues choose (yes/no):"))
if age>=18 and age<=45:
    if med=="yes":
        print("Pass")
else:
    print("Deny")

#12
price1=int(20)
price2=int(35)
w=float(input("Enter weight:"))
d=int(input("Enter the distance:"))
cost1=price1*(w/100)
cost=(price2*d)*cost1
print(f"Cost: {cost} tg")

#13
pas="erkgsn"
name=input("Enter login:")
pastr=input("Enter password:")
if pastr==pas:
    print("Access")
else:
    print("Denied")

#14
print("Quiz:General Knowledge")
print("Choose only one option")
print("Question 1:")
print("What is the capital of France?")
print("a) London")
print("b) Rome")
print("c) Paris")
t=int(0)
otv=input("Answer:")
if otv=="c":
    print("True")
    t=t+1
else:
    print("False")
print("Question 2:")
print("Who wrote the play Romeo and Juliet?")
print("a) William Shakespeare")
print("b) Jane Austen")
print("c) Charles Dickens")
otv=input("Answer:")
if otv=="a":
    print("True")
    t=t+1
else:
    print("False")
print("Question 3:")
print("Which gas do plants absorb from the atmosphere during photosynthesis?")
print("a) Carbon Dioxide")
print("b) Hydrogen")
print("c) Oxygen")
otv=input("Answer:")
if otv=="a":
    print("True")
    t=t+1
else:
    print("False")
print(f" Correct: {t}")


