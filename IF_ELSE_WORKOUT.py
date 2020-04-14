#check if string is palindrme or not
'''
x= input("enter the string")
if x == x[::-1]:
    print("the string is palindrom")
else:
    print("the string is not palindrom")

'''

###################################################3
'''
##check whether first char, middle char, last char of a string is same or different
x=(input("enter the string"))
if x[0]==x[(len(x)//2)]==x[-1]:
    print("first char, middle char, last char is same")
else:
    print("its not same")
'''
#######################################################

#pgm2
#get a mark from student ()

#0 - 100 ==> valid
    #100 grade a
    #90 to 99 grade b
    #80 to 89 grade c
    #70 to 79 grade d
    #50 to 69 grade e
    # 0 to 49 fail grade f

#otherwise ===> invalid

x=int(input("get a mark from student"))
if x==100:
    print("grade a")
elif x>90 and x<99:
    print("grade b")
elif x>80 and x<89:
    print("grade c")
elif x>70 and x<79:
    print("grade d")
elif x>60 and x<69:
    print("grade e")
elif x>0 and x<49:
    print("grade f")    
else:
    print("invalid")
    
    


