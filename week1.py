import math
#task 1.1
name = input("Your last name, first name? ")
age = input("How old are you " + name + "? ")
phone_number = input("Your phone number?? ")
print("Your name is " + name + ".")
print("You are " + age + " years old.")
print("Your phone number " + phone_number + ".")
print("")

#task 1.2
shape = int(input("Choose the shape to calculate its area:\n1.Triange\n2.Rectangle\n3.Circle\n"))
if shape == 1:
    base = int(input("Base of triange: "))
    height = int(input("Height of triange: "))
    print((height * base) / 2)
elif shape == 2:
    length = int(input("Length of rectangle: "))
    width = int(input("Width of rectangle: "))
    print(length * width)
else:
    radius = int(input("Radius of circle: "))
    print(math.pi * radius ** 2)
print("")
#just copied from 2nd practice :)

# task 1.3
print("changing the integer and fractional parts")
a = float(input("A: "))
integer_part = math.trunc(a)
fractional_part = math.trunc((a * 100) % 100)
print(integer_part / 100 + fractional_part)
print("")

# task 1.4
print("calculating the expression")
A = int(input("A: "))
Y = math.pow(A,2)/3 + (math.pow(A,2)+4)/6 + math.sqrt(math.pow(A,2)+4)/4 + math.sqrt(math.pow((math.pow(A,2)+4),3))/4
print("answer: ",Y)
print("")

# task 1.5
print("choose one random number and let guess it")
print("a) multiply the planned number by 5\nb) add 8\nc) multiply the sum by 2")
print("print your result")
n = int(input())
n = ((n / 2) - 8) / 5
print("your choosen number is: ", n)
print("")

# task 2.1 2.2
print("Smart Calculator")
first_number = int(input("First number: "))
operation = input("Operation: ")
second_number = int(input("Second number: "))

if operation == "+":
    print("%2d + %2d = %2d" % (first_number,second_number,first_number+second_number))
if operation == "-":
    print("%2d - %2d = %2d" % (first_number,second_number,first_number-second_number))
if operation == "*":
    print("%2d * %2d = %2d" % (first_number,second_number,first_number*second_number))
if operation == "/":
    if second_number == 0:
        print("can not divide by 0")
    else:
        print("%2d / %2d = %2d" % (first_number,second_number,first_number/second_number))
print("")

# task 2.3
a = int(input("triple check number: "))
if(a>10 and a!=12 and a<=15 or a==18):
    print("True")
print("")

# task 2.4
print("even numbers from 34 to 67")
n = 34
while n < 67:
    print(n)
    n += 2
print("")

# task 2.5
print("print numbers from 1 to 10 using do while")
n = 1
while True:
    print(n)
    if n == 10:
        break
    n += 1
print("")

# task 2.6
for i in range(1, 101, 1):
    while(i != 50 or i != 99):
        continue
    print(i)
print("")


# task 2.7
word = input("enter a word: ")
number = int(input("enter a number: "))
for i in range(len(word)):
    temp = 0
    while temp < number:
        print(word[i], end = "")
        temp += 1
    print('')