#WHILE LOOP


c=9
while c>3:
    print(c)
    c=c-1
print("end")
'''
'''
c=9
while c>3:
    print(c)
    c=c+1
    #the abov statement giv infinite number
print("end")


#get a number form user and print till that partcular nuber

x=(int(input("enter the number")))
i=0
while i<=x:
    i=i+1
    print(i)


#print evn numbers from zero to twenty
x=2
while x<=20:
    print(x)
    x += 2


#even numbers from user input to user input
x=int(input("enter the number 1"))
y=int(input("enter the number 2"))

while y<=x:
    print(y)
    y=y+2


# multiples of 5 from 100 to 200

x=200
y=int(input("enter the number"))

while y<=x:
    print(y)
    y=y+5

##multiples of 8 from user input to user input

x=int(input("enter 1"))
y=int(input("enter 2"))

while y<=x:
    print(y)
    y=y+8
