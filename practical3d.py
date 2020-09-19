#Factorial and factors using iteration
num = int(input("Enter a number: "))
factorial = 1
factors = []
if  num < 0 :
    print("Factorial does not exist")
elif num == 0 or num==1:
    print("Factorial is of ",num,"is 1")
else:
    for i in range(1,num+1):
        factorial = factorial* i
        if (num%i )==0:
            factors.append(i)
    print("Factorial is   using iteration of ",num,"  is ",factorial)
    print("Factors using iteration of  ",num," is ", factors)




# Factorial of a number using recursion

def factorial_recursion(n):
   if n == 1:
       return n
   else:
       return n*factorial_recursion(n-1)
num = int(input("Enter a number: "))

if  num < 0 :
    print("Factorial does not exist")
elif num == 0 or num==1:
    print("Factorial is of ",num,"is 1")
else:
    for i in range(1,num+1):
        factorial = factorial* i
        if (num%i )==0:
            factors.append(i)
    print("Factorial using recursion of ",num,"  is ",factorial_recursion(num))


def factors_recursion(x,i):
    if i==x+1:
        return
    if x%i == 0:
        print(i)
    return factors_recursion(x,i+1) #simpler version of the problem

factors_recursion(10,1)
