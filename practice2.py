import math
# exercise
x = 10; t = 1
ans = (9*math.pi*t+10*math.cos(x)) / (math.sqrt(t)-math.fabs(math.sin(t))) * math.pow(math.e, x)

# task 1.1
a = int(input("a: "))
b = int(input("b: "))
h = int(input("h: "))

S = ((a ** 2 + b) * h) / (2 * (a - b) + 4)

print('%.2f' % S + "\n")


# task 1.2
x = float(input("x: "))
y = float(input("y: "))

H =  math.sqrt(math.cos(2 * y) + math.sin(4 * y) + math.sqrt(math.exp(x) + math.exp(-x))) / (math.pow((math.exp(-x) + math.exp(x)),3) * math.pow((math.sin(4 * y) + math.cos(2 * y) - 2),2))

print('%.4f' % H + "\n")


# task 1.3.1
x = 2; y = 1
ans = math.pow(math.pow(x,y),x) + math.pow(math.pow(x,x),y) - math.pow(x,4)
print('%.2f' % ans)


# task 1.3.2
x = 1; y = 4; z = 3
ans = math.pow((abs(1 / math.tan(y) + 6)), 1/3)+ math.sqrt((x+1)**3/(4*y-2*z))
print('%.2f' % ans)


# task 1.3.3
x = 3; y = 0.2
ans = 5*x*y/(x**3-4) + math.exp(x**2) + math.sqrt(math.cos(y)**2-y**2)
print('%.2f' % ans)


# task 1.3.4
x = 4; y = 5
ans = math.sqrt(abs(y)) + math.atan(math.log10(x)/math.log10(math.e))**3/(x**y-y+1)
print('%.2f' % ans)


# task 1.3.5
x = 3; y = 1; z = 2
ans = math.pow(4,x*y) - math.pow(x,y*z) + math.pow((x*y),z)
print('%.2f' % ans)


# task 1.3.6
x = 2; y = 2; z = 1
ans = (4*abs(x) - (x*y*z)**2)/(x + math.exp(y*x) - 2*y*z)
print('%.2f' % ans)

# task 1.3.7
x = 0,8; y = 0,1; z = 4
ans = math.pow((1-x+math.atan(x-7*y))/(4*x*z-math.pow(math.log10(y),2)),1/5)
print('%.2f' % ans)

# task 1.3.8
x = 3; y = 1; z = 3
ans = 2*3*4/(math.sin(x)**3 + math.tan(y)**3) - math.sqrt(z(x-y))
print('%.2f' % ans)

# task 1.3.9
x = 4
ans = (math.log(x - 3) ** 4 + 2 ** x * math.sin(3 * x) ** 2) / (4 * x - 5.2)
print('%.2f' % ans)


# task 1.3.10
x = 2; y = 2; z = 1
ans = math.sqrt(0.6 * x * y * z) + (y ** x) ** 2 - math.exp(math.sin(2 * x ** 2))
print('%.2f' % ans)


# task 1.3.11
x= 0.5; y = 2
ans = math.asinh(math.pow(x,3)-6)/(8*(math.cos(4*y)-math.sin(4*x)))
print('%.2f' % ans)


# task 1.3.12
x= 2; y = 1; z = 3
ans = abs(math.log10(x**3)/math.log10(math.e)) + math.exp(2*x)/(x+3.4) - 1 / math.tan(3/x*y*z)**3
print('%.2f' % ans)


# task 2
a = int(input("a: "))
b = int(input("b: "))
c = math.sqrt(math.pow(a,2) + math.pow(b,2))

S = a + b + c
A = (a * b) / 2

print('Area of triangle:', '%.2f' % A)
print('Perimeter of triangle:', '%.2f' % S + "\n")


# task 3
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

d = (b**2) - (4*a*c)

if d > 0:
    ans1 = (-b-math.sqrt(d))/(2*a)
    ans2 = (-b+math.sqrt(d))/(2*a)

    print('The answers are {0} and {1}'.format(ans1,ans2))
    print("\n")
elif d == 0:
    print('The answer is' + "\n", (-b)/(2*a))
else:
    print("No answer :(\n")


# task 4
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
