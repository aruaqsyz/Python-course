#task 1
a=[1,2,3,4,5,6,7,8,9,10]
print(a[::-1])

#task 2
def change(a):
    a[0],a[len(a)-1] = a[len(a)-1],a[0]
a = [1,2,3]
change(a)
print(a)

#task 3
def to_list(*a):
    return list(a)
print(to_list(1,2,3,4,5,6,7,8,9,10))

#task 4
def uselessNumber(a):
    return max(a)/len(a)
print(uselessNumber(a))

#task 5
def list_sort(a):
    return sorted(map(abs, a), reverse=True)
temp = [1,-2,3,-4,5,-6,7,8,-9,-10]
print(list_sort(temp))

#task 6
a = ["short", "shrt", "looooooooooooooong"]
print([i.rjust(len(max(a, key = len)), '_') for i in a])
