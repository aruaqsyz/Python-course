#task 1
a = [1,2,3,4,5,6,7,8,9,10]
print(max(a))
print(a[::-1])

a = [1,0,3,0,5,0,7,0,9,0]
sum = 0
for i in a:
    sum += i
mean = sum / len(a)
for i in range(len(a)):
    if a[i] == 0:
        a[i] = mean
print(a)

#task 2
n = int(input())
a = [ int(input()) for i in range(n)]
min = a[0]
min_index = 0
for i in range(len(a)):
    if a[i] < min:
        min = a[i]
        min_index = i
print(min_index)

a = [-1,2,-3,4,-5,6,-7,8,-9,10]
scnd = []
thrd = []
for i in range (len(a)):
    if a[i] > 0:
        scnd.append(a[i])
    else:
        thrd.append(a[i])
print(scnd)
print(thrd)

#task 3
n = int(input())
D = [ int(input()) for i in range(n)]
sum = 0
for i in range(1,n,2):
    sum += D[i]
print(D)
print(sum)

a = [10,20,14,25,17,11,12,13]
print(a)
for i in range(8):
    if a[i] < 15:
        a[i] = a[i] * 2
print(a)

#task 4
n = int(input())
a = [ int(input()) for i in range(n)]
max = a[0]
max_index = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_index = i
print(max_index + 1)

a = [1,2,3,4,5,6,7,8,9,10]
b = []
for i in range(len(a)):
    if a[i] % 2 == 1:
        b.append(a[i])

if len(b) == 0:
    print("no such numbers")
else:
    b.sort()
    print(b[::-1])

#task 5
a = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)):
    print(a[i],-a[i])

a = [1,1,3,4,5,3,3,9,9,9]
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)

#task 6

a = [ int(input()) for i in range(10)]
sum = 0
for i in range(len(a)):
    if a[i] > 5:
        sum += a[i]

#task 7
a = [1,2,3,4,5,6,7,8,9,10]
sum = 0
prdct = 1
for i in range(len(a)):
  if a[i] % 2 != 0:
     prdct *= a[i]
  else:
      sum += a[i]
print(sum)
print(prdct)

a = [1,-200,3,4,5,600,7,8,9]
max = a[0]
max_index = 0
min = a[0]
min_index = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_index = i
    if a[i] < min:
        min = a[i]
        min_index = i
a[min_index] = max
a[max_index] = min
print(a)

#task 8
a = [1,2,3,4,5,6,7,8,9,10]
sum = 0
prdct = 1
for i in range(len(a)):
    prdct *= a[i]
    sum += a[i]
print(sum)
print(prdct)

a = [1,0,3,0,5,0,7,0,9,0]
sum = 0
for i in a:
    sum += i
mean = sum / len(a)
for i in range(len(a)):
    if a[i] == 0:
        a[i] = mean
print(a)

#task 9
n = int(input())
a = [ int(input()) for i in range(n)]
print(min(a, key=abs))
print(a[::-1])

a = [1,2,3,4,5,6,7,8,9,10]
b = [10,9,8,7,6,5,4,3,2,1]
print(a)
print(b)
a,b = b,a
print(a)
print(b)

#task 10
a = [1,3,4,5,9]
b = []
b.append(a[0])
for i in range(1,len(a)):
    if a[i] in b:
        print("dublicate:", a[i])
    else:
        b.append(a[i])
    if(i == len(a) - 1 and len(b) == len(a)):
        print("no dublicates")
print(b)

arr = [1,2,3,4,5,60,50,40,30,20,10]
print(arr)
print([0 if i < 10 else 1 if i > 20 else i for i in arr])

#task 11
n = int(input())
a = [ int(input()) for i in range(n)]
max = 1
for i in range(len(a)):
    if a[i] > max and a[i] % 2 == 0:
        max = a[i]
print(max)

n = int(input())
a = [ int(input()) for i in range(n)]
b = []
for i in range(len(a)):
    if a[i] < 10 and a[i] % 2 == 0:
        b.append(a[i])
    if i == len(a) - 1 and len(b) == 0:
        print("no such numbers")
b.sort()
print(b)

#task 12
n = int(input())
a = [ int(input()) for i in range(n)]
mn = 9999999999
for i in range(len(a)):
    if a[i] % 2 == 1 and a[i] < mn:
        mn = a[i]
print(mn)

a = [1,2,3,4,5,6,7,8,9,10]
b = [10,9,8,7,6,5,4,3,2,1]
print(a)
print(b)
a,b = b,a
print(a)
print(b)

#task 13
a = [1,3,3,3,4,4,5,5,6,9,9]
b = []
b.append(a[0])
for i in range(1,len(a)):
    if a[i] in b:
        print("dublicate:", a[i], i)
    else:
        b.append(a[i])

a = [10,20,14,25,17,11,12,13]
print(a)
for i in range(8):
    if a[i] < 15:
        a[i] = a[i] * 2
print(a)

#task 14
a = [1,-200,3,4,5,600,7,8,9]
max = a[0]
max_index = 0
min = a[0]
min_index = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_index = i
    if a[i] < min:
        min = a[i]
        min_index = i
a[min_index] = max
a[max_index] = min
print(a)

n = int(input())
a = [ int(input()) for i in range(n)]
sum = 0
for i in a:
    sum += i
mean = sum / len(a)
for i in range(len(a)):
    if a[i] > mean:
        a[i] = 1
print(a)

#task 15
a = [1,3,3,3,4,4,5,5,6,9,9]
b = []
b.append(a[0])
for i in range(1,len(a)):
    if a[i] in b:
        print("dublicate:", a[i], i)
    else:
        b.append(a[i])

a = [1,2,3,4,5,6,7,8,9,10]
b = []
for i in range(len(a)):
    if a[i] % 2 == 1:
        b.append(a[i])

if len(b) == 0:
    print("no such numbers")
else:
    b.sort()
    print(b[::-1])