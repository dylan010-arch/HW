#1
x=int(input("Enter a grade from 1 to 10:"))

if x>=1 and x<=3:
    print("Plocho")
elif x>=4 and x<=6:
    print("Udovletvoritelno")
elif x>=7 and x<=9:
    print("Horosho")
elif x==10:
    print("Otlichno")
else:
    print("Error")

#2
time=int(input("Enter an hour:"))
if time>=0 and time<=6:
    print("Good night")
elif time>=6 and time<=12:
    print("Good morning")
elif time>12 and time<=18:
    print("Good afternoon")
elif time>18 and time<=24:
    print("Good evening")
else:
    print("Error")

#3
x=int(input("Enter a number:"))
for i in range(1,x+1):
    rez=i%3
    if rez==0:
        Numbers_3=i
print (Numbers_3, "\n")

#4
count = 0
num_list_1 = []
num_list_2 = []
sum_positive = 0
while True:
    x = int(input("Enter a number (enter 0 to finish):"))
    if x == 0:
        break
    if x < 0:
        num_list_1.append(x)
    else:
        count += 1
        num_list_2.append(x)
        sum_positive += x
if num_list_2 and num_list_2[-1] == 0:
    num_list_2.pop()
if count > 1:
    sr = sum_positive / count
    print("Positive numbers in the entered sequence:", num_list_2)
    print("Arithmetic mean of positive numbers in the sequence is equal to:", sr)
else:
    print("Less than two positive numbers entered")

#5
size = int(input("Enter the size of fir tree: "))
br = 0
while br != 2:
    num = 2 * size
    for i in range(size):
        for j in range(num - i):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print("")
    br += 1

#6
size = int(input("Enter the size of bowtie: "))
for i in range(1, size + 1):
    for j in range(1, 2 * size + 1):
        if j <= i or j > 2 * size - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(size, 0, -1):
    for j in range(1, 2 * size + 1):
        if j <= i or j > 2 * size - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#7
chess = []  
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            chess.append("|_|")
        else:
            chess.append("|w|")
    
for i in range(0, len(chess)):
    for j in range(0, len(chess[i])):
        print(chess[i][j], end="")
        if i == 7 and j == 6:
            print("К", end="")  
    else:
        print(" ", end=" ")
    print()

#8
num_list = []
n = int(input("Enter the digit of numbers to compare:"))
for i in range(n):
    x = int(input("Enter a number:"))  
    num_list.append(x)
print("List of unsorted numbers: \n", num_list)

for i in range(n-1):
    for j in range(n-i-1):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
print("Numbers in ascending order: \n", num_list)

for i in range(n-1):
    for j in range(n-i-1):
        if num_list[j] < num_list[j+1]:
            num_list[j], num[j+1] = num_list[j+1], num_list[j]
print("Numbers in descending order: \n", num_list)
