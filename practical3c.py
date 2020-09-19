import math
#p1 = 3x**3 + 4x**2 + x +13
#first polynomial
x= int(input("Enter value for x: "))
b=int(input("enter 1st coefficient:"))
c =int(input("enter 2nd coefficient :"))
x1 = int(input ("Enter degree for first x : "))
x2 = int(input ("Enter degree for 2nd x : "))
c1 = 10
print(b,pow(x,x1))

#2nd polynomial
x2p= input("Enter value for x: ")
b2p=input("enter 1st coefficient:")
c2p=input("enter 2nd coefficient :")
x12p = input ("Enter degree for first x : ")
x22p = input ("Enter degree for 2nd x : ")
c12p = 10
print(b2p,x2p,"^",x12p,"+", c2p,x2p,"^",x22p,"+",c12p)
      



















'''print("Enter the coefficient of the form ax**3 +bx**2 + cx + d")
lst = []
for i in range(0,4):
    a = int(input("Enter coefficient :" ))
    lst.append(a)
x = int(input("Enter the value of x :"))
sum1 = 0
j = 3
for i in range(0,3):
    while (j > 0):
        sum1 = sum1 + (lst[i] * math.pow(x,j))
        break
    j = j+1
sum1 = sum1+lst[3]
print("The value of polynomial is : ",sum1)
'''
