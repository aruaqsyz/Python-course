# 1st
class Rectangle:
    def __init__ (self,color="green", width=100,height=100, justchange = 0):
        self.color = color
        self.width = width
        self.height = height
        self.justchange = justchange
    def square(self):
        return self.width *self.height
    def setjustchange(self,number):
        self.justchange = number
        print(self.justchange)
rect1 = Rectangle()
print(rect1.color)
print(rect1.square())
rect1 = Rectangle("yellow",23,34)
print(rect1.color)
print(rect1.square())
print()
print(rect1.justchange)
rect1.setjustchange(5) 

# 2nd
class Person:
    def __init__(self,f_name,l_name):
        self.f_name = f_name[0].upper() + f_name[1:len(f_name)].lower()
        self.l_name = l_name[0].upper() + l_name[1:len(l_name)].lower()
    def __repr__(self):
        print(f'{self.f_name} {self.l_name}')
person1= Person("ArMAn","maQSaT" )
print(person1.f_name)
print(person1.l_name)
person1.__repr__()

# 3rd

class Calculator:
    def add(self,num1,num2):
        return  num1 + num2
    def substract(self,num1,num2):
        return num1 - num2
    def multiply(self,num1,num2):
        return  num1 * num2
    def delit(self,num1,num2):
        return num1 / num2
calcul = Calculator()
print(calcul.add(10,5))
print(calcul.substract(10,5))
print(calcul.multiply(10,5))
print(calcul.delit(10,5))