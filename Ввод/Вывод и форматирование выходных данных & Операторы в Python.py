#1
name= input("Your name:")
print(f"Hello,{name}!")

#2
a1= int(input("Grade 1:"))
a2= int(input("Grade 2:"))
a3= int(input("Grade 3:"))
print("Average mean:", (a1+a2+a3)/3)

#3
physics_1=int(input('Grade 1:'))
physics_2=int(input('Grade 2:'))
maths_1=int(input('Grade 1:'))
maths_2=int(input('Grade 2:'))
history_1=int(input('Grade 1:'))
history_2=int(input('Grade 2:'))
physics_mean=(physics_1 + physics_2)/2
maths_mean=(maths_1 + maths_2)/2
history_mean=(history_1 + history_2)/2
average=(physics_mean + maths_mean + history_mean)/3
print(f'Physics mean: {physics_mean:.2f}')
print(f'Maths mean: {maths_mean:.2f}')
print(f'History mean: {history_mean:.2f}')
print(f'Average mean: {average:.2f}')

#4
name=input("What's your name?")
age=input("How old are you?")
city=input("Where are you from?")
print(f"Personal info of {name}")
print("Name:",name)
print("Age:",age)
print("City:",city)



