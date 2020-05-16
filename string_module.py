def Len_module():
    x=input("Enter the string:")
    n=len(x)
    return n

def Reverse():
    x=input("Enter the string:")
    n=x[::-1]
    return n

def Join_string():
    x=input("Enter the string:")
    y=input("Enter the string:")
    str=x+y
    return str

def Split():
    x= input("Enter the string:")
    n = x.split()
    return n

def Palindrome():
    x= input("Enter the string:")
    n = x[::-1]
    if(n==x):
        print("string is a palindrome")

    else:
        print("string is not a palindrome")

def Add_String():
    x=input("Enter the string:")
    y=input("Enter the string:")
    str=x+ " "+y
    return str

def Start_char():
    x=input("Enter the string:")
    n=x[0]
    return n

def End_char():
    x=input("Enter the string:")
    n=x[-1]
    return n

def ASCII_char():
    x=input("Enter the character:")
    c=ord(x)
    return c

def Vowels():
    x=input("Enter the character:")
    vowels=0
    for i in x:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
            print(i)
    print("Number of vowels are:",vowels)
    
def Replace_char():
    x=input("Enter the string:")
    y=input("Enter the string:")
    s=int(input("Enter the index to be replaced:"))
    n = x.replace(x[s],y)
    return n
