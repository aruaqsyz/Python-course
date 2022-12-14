import math
import random
import numpy as np
# task 1.1
def triangleArea(base,height):
    return (height * base) / 2
def rectangleArea(length,width):
    return length * width
def circleArea(radius):
    return math.pi * radius ** 2

shape = int(input("Choose the shape to calculate its area:\n1.Triange\n2.Rectangle\n3.Circle\n"))
if shape == 1:
    base = int(input("Base of triange: "))
    height = int(input("Height of triange: "))
    print(triangleArea(base,height))
elif shape == 2:
    length = int(input("Length of rectangle: "))
    width = int(input("Width of rectangle: "))
    print(rectangleArea(length,width))
else:
    radius = int(input("Radius of circle: "))
    print(circleArea(radius))   

# task 1.2
def sumArr(n):
    sum = 0
    for i in n:
        sum += i
    return sum

def meanArr(n,sum):
    return sum/len(n)

for i in range(3):
    a = random.sample(range(100), 15)
    print(a)
    print(sumArr(a))
    print(meanArr(a,sumArr(a)))

# task 2.1
def regTriangleArea(a):
    return (math.sqrt(3) / 4) * a ** 2
a = int(input("Side of regular hexagon: "))
print("Area of regular hexagon is:", regTriangleArea(a)*6)

# task 2.2
for i in range(3):
    a = int(input("first side: "))
    b = int(input("second side: "))
    print("area of recangle is:", rectangleArea(a,b))

# task 3.1
def hypotenuses(a,b):
    return math.sqrt(a**2 + b**2)

temp = []
for i in range(2):
        a = int(input("a: "))
        b = int(input("b: "))
        print("hypotenuses of triangle is:",hypotenuses(a,b))
        temp.append(hypotenuses(a,b))

if temp[0] > temp [1]:
    print("hypotrnuses of first triangle is bigger")
elif temp[1] > temp[0]:
    print("hypotrnuses of second triangle is bigger")
else:
    print("hypotrnuses of both triangles are same")

# task 3.2
def sortString(s):
    return ''.join(sorted(s))

# print(sortString("AITUMOMENTS"))

#task 4.1
def gcd(x,y):
    if (y == 0):
        return abs(x)
    else:
        return gcd(y, x % y)

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
print(math.trunc(a*d / gcd(a*d,b*c)), "/", math.trunc(b*c / gcd(a*d,b*c)))

# task 4.2
def isInCircle(r,x,y):
    if r > hypotenuses(x,y):
        return True
    else:
        return False

a = int(input("a: "))
b = int(input("b: "))
r = int(input("r: "))

p1 = int(input("p1: "))
p2 = int(input("p2: "))
print(isInCircle(r,abs(p1) - abs(a),abs(p2) - abs(b)))
f1 = int(input("f1: "))
f2 = int(input("f2: "))
print(isInCircle(r,abs(f1) - abs(a),abs(f2) - abs(b)))
l1 = int(input("l1: "))
l2 = int(input("l2: "))
print(isInCircle(r,abs(l1) - abs(a),abs(l2) - abs(b)))

# task 5.1
def lcm(x,y):
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

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
a /= gcd(a,b)
b /= gcd(a,b)
c /= gcd(c,d)
d /= gcd(c,d)
b2 = lcm(b,d)
d2 = b2
a *= b2 / b
c *= d2 / d
print(a - c, "/", b2)

# task 5.2
def allDivisors(n):
    ans = []
    for i in range(1,n+1):
        if n % i == 0:
            ans.append(i)
    return ans
    
n = int(input("n: "))
print(allDivisors(n))

# task 6.1
a = int(input("a: "))
b = int(input("b: "))

print("gcd of a and b:",gcd(a,b))
print("lcm of a and b:",lcm(a,b))

# task 6.2
def triangleAreaSemiP(a,b,c):
    s = (a + b + c) / 2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
h = int(input("diagoal (A,C): "))
print(triangleAreaSemiP(a,b,h) + triangleAreaSemiP(c,d,h))

# task 7.1
a = int(input("long base: "))
b = int(input("short base: "))
h = int(input("height: "))
t = int(input("leg: "))

print("Area:", triangleArea(a-b,h) + rectangleArea(b,h))

# task 7.2
def decToOct(n):
    return '{:010o}'.format(n)

a = int(input())
print(decToOct(a))

#task 8.1
def divByTheirD(n):
    ans = []
    for i in range(1,n+1):
        s = str(i)
        temp = True
        for j in s:
            if int(j) == 0:
                temp = False
            elif i % int(j) != 0:
                temp = False
        if temp:
            ans.append(i)
    return ans

n = int(input("n: "))
print(divByTheirD(n))

#task 8.2
def swapFirstLast(a):
    a[0],a[len(a)-1] = a[len(a)-1],a[0]
    return a

m = int(input("length of array: "))
A = []
for i in range(m):
    n = int(input("element of array: "))
    A.append(n)

print(A)
print(swapFirstLast(A))

# task 9.1
def sumOfDigits(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

n = int(input("N: "))
sub = sumOfDigits(n)
ans = 0
while n > 0:
    ans += 1
    n -= sub

print(ans)

# task 9.2
def prdArr(n):
    prd = 1
    for i in n:
        prd *= i
    return prd

for i in range(3):
    a = random.sample(range(100), 15)
    print(a)
    print(prdArr(a))
    print(meanArr(a,sumArr(a)))

# task 10.1
def digitsOfN(n):
    ans = []
    s = str(n)
    for i in s:
        ans.append(int(i))
    return ans

N = int(input("N: "))
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

ans = []
for i in range(100,N):
    dgts = digitsOfN(i)
    if a in dgts:
        dgts.remove(a)
    if b in dgts:
        dgts.remove(b)
    if c in dgts:
        dgts.remove(c)
    if len(dgts) == 0:
        ans.append(i)
print(ans)

#task 10.2
def reverceSeq(s):
    s = s.split()[::-1]
    ans = []
    for i in s:
        ans.append(i)
    return ' '.join(ans)

s = input("Enter str to reverse: ")
print(reverceSeq(s))

# task 11.1
def isPrime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

n = int(input("n: "))

for i in range(n,2*n):
    if isPrime(i) and isPrime(i+2):
        print(i,i+2)

# task 11.2
def findMax(arr, n):
    max = -1
    x = 0
    y = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max:
                max = arr[i][j]
                x = i
                y = j
    return x,y

arr1 = np.random.randint(100, size=(4, 4))
arr2 = np.random.randint(100, size=(4, 4))
print(arr1)
print(arr2)

max1 = findMax(arr1,4)
max2 = findMax(arr2,4)

arr1[max1[0]][max1[1]],arr2[max2[0]][max2[1]] =  arr2[max2[0]][max2[1]],arr1[max1[0]][max1[1]]
print(arr1)
print(arr2)

#task 12.1
def sumOFAllDivisors(n):
    ans = 0
    for i in range(1,n+1):
        if n % i == 0:
            ans+= i
    return ans

n = int(input("N: "))
for i in range(n):
    a = sumOFAllDivisors(i)
    for j in range (i+1,n):
        b = sumOFAllDivisors(j)
        if a == b:
            print(i,j)
            continue

#task 12.2

#task 13.1
k = int(input("k: "))
for i in range(2,k):
    for j in range(k):
        if sumOfDigits(i)**j == i:
            print(i,j)
        elif sumOfDigits(i)*j > i:
            break

    