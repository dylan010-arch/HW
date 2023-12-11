#1
x=int(input("Enter a number: "))
for x in range (1,x+1):
    rez=x%2
    if rez==0:
        print(f'{x}')

#2
count=int(1)
rez=int(0)
s=int(input("Enter a number:"))
while count<=s:
    rez+=count
    count+=1
print(f"Sum of all numbers from {s} is {rez}")

#3
for x in range(21):
    rez=x%2
    if rez==0:
        print(x)

#4
n=int(input("Enter a digit:"))
for i in range (11):
    print(f"{i}*{n}={i*n}")

#5
name=("Python")
for x in name:
    print(x)

#6
count=int(1)
x=int(0)
while count<=100:
    rez=count%2
    if rez!=0:
        x=x+count
    count+=1
print(f"Sum of all odd numbers from 1 to 100 is {x}")

#7
x='*'
for i in range (5):
    for j in range (1):
        print(x)
        x+='*'

#8
for x in range (6):
    for y in range(6):
        if x!=0 and y!=0:
            print(f"{x}*{y}={x*y}", "\n")

#9
x=int(input("Enter a number: "))
rez_x=int(0)
rez_y=int(0)
print(f"The following prime numbers in the range from 2 to {x}:")
for i in range (2,n+1):
    if x%i==0:
        rez_x+=1  
    for j in range (1,x+1):
            if i%j==0: 
                rez_y+=1
    if rez_y==2:
         print(i)
         rez_y=0
if rez_x==2:
    print(f"prime number {x}")
else:
    print(f"non-prime number {x}")

