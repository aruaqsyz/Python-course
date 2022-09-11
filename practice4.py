# example
from re import X


n = int(input("Number of elements: "))
x = 1
s = 0
print(x)
for i in range(n):
    s += x
    x /= -2
    print(x)
print('Sum of sequence: ', s)
print("\n")

# task 1
price = int(input("Price: "))
for i in range(1,11):
    print("Price of %2d kg is %3d" % (i,i*price))
print("\n")

# task 2
print("sequence: ")
a = int(input())
length_of_seq = 1
sum_of_seq = a
while a != 0:
    a = int(input())
    length_of_seq += 1
    sum_of_seq += a
print("Sum of all numbers in the sequence: ", sum_of_seq)
print("The number of all numbers in the sequence: ", length_of_seq)