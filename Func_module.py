import math

def Add(x,y):
    sum1=x+y
    return sum1

def sub(x,y):
    sub=x-y
    return sub

def prod(x,y):
    prod=x*y
    return prod

def div(x,y):
    div=x/y
    return div

def Floor_div(x,y):
    z= math.floor(x//y)
    return z

def Prime_num(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
            else:
                print(num, "is a prime number")
                break
    else:
        print(num, "is not a prime number")

def Armstrong(x):
    #num = int(input("Enter a number: "))

     # initialize sum
    sum = 0

     # find the sum of the cube of each digit
    temp = x
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

     # display the result
    if x == sum:
         print(x,"is an Armstrong number")
    else:
         print(x,"is not an Armstrong number")

def Fibonacci(x): 
    if x<0: 
        print("Incorrect input") 
        # First Fibonacci number is 0 
    elif x==1: 
        return 0
        # Second Fibonacci number is 1 
    elif x==2: 
        return 1
    else: 
        return Fibonacci(x-1)+Fibonacci(x-2) 
  
        # Driver Program 
  

                

