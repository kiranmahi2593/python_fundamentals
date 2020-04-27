#data structure and data types

print("\n*****welcome to DS-DT calulator*****")
print("\nbelow are available functons")

available_functions ={1:'list',2:'Numbers',3:'set',4:'tuple',5:'string'}
for values,keys in available_functions.items():
    print(values,keys)
    
print("\n****************")

user_input=int(input("enter  above available functions :"))

#print("user input is :",user_input)

print("****************")

n=1


def list11():
    global n
    while n<=13:
        
        n=n+1
        #import list_function
        
        list_input =int(input("\nmx length of the list needed"))
        UserList=[]
        for i in range (0,list_input):
            UserListInput=int(input("enter the list value"))
            UserList.append(UserListInput)
        lil=UserList
        print("\nselected userlist is :",lil)

        if user_input==1:            
            #lil=[1,11,2,2,3,4]
            list_operations = {1:'COUNT',2:'INSERT',3:'REMOVE',4:'POP',5:'CLEAR',6:'EXTEND',7:'INDEX',8:'APPEND',9:'SORT',10:'MIN',11:'MAX',12:'REVERSE'}
            for values,keys in list_operations.items():
                print('\n',values,keys)
                
        selected_list = int(input("\nselect any one of above list operation :"))
       

        if selected_list ==1:  
            x=lil.count(4)
            print("count output is ",x ,'\n')
                    
        elif selected_list ==2:
            lil.insert(1, "orange")
            print("\ninsert output is ",lil ,'\n')

        elif selected_list ==3:
            lil.remove(1)
            print("\nremove output is ",lil ,'\n')

        elif selected_list ==4:
            x=lil.pop(1)
            print("\npop output is",x ,'\n')

        elif selected_list ==5:
            lil.clear()
            print("\nclear output is",lil ,'\n')
                    
        elif selected_list ==6:
            lil.extend("one")
            print("\nextend output is",lil ,'\n')
            
        elif selected_list ==7:
            x=lil.index(1)
            print("\nindex output is",x ,'\n')
            
        elif selected_list ==8:
            lil.append("name")
            print("\nappend output is",lil ,'\n')
            
        elif selected_list ==9:
            lil.sort()
            print("\nsort output is",lil ,'\n')
            
        elif selected_list ==10:
            a=min(lil)
            print("\nmin output is",a ,'\n')

        elif selected_list ==11:
            a=max(lil)
            print("\nmin output is",a,'\n')
            
        elif selected_list ==12:
            lil.reverse()
            print("\nreverse output is",lil ,'\n')
            
        else:
            
            print("\ninvalid input , please enter a valid input value\n")
            break



 #######################
def numbers11():
    global n
    while n<=13:
        if user_input==2:
           
    
            num_operations = {1:'ADD',2:'SUB',3:'MUL',4:'DIVIDE',5:'FLOOR DIVISION',6:'POWER',7:'MOD',8:'SQUARE',9:'SQUARE ROOT',10:'CUBE ROOT',11:'CUBE',12:'PRIME',13:"Factorial"}
            for values,keys in num_operations.items():
                print(values,keys)
        n=n+1
        x = int(input("\nenter a number x:"))
        y = int(input("enter a number y:"))    
        selected_num = int(input("select any one of above numbers operation :"))
        c={}
        fact=1
                
        import math
        if selected_num==1:
            add=x+y
            print("\noutput of add :", add)            
        elif selected_num==2:
            sub=x-y
            print("\noutput of sub :",sub)
        elif selected_num==3:
            mul=x*y
            print("\noutput of mul :",mul)            
        elif selected_num==4:
            div=x/y
            print("\noutput of div :",div)
        elif selected_num==5:
            fd=x//y
            print("\noutput of fd :",fd)
        elif selected_num==6:
            mul=x*y
            print("\noutput of power power:",math.floor(x//y))
        elif selected_num==7:
            mod=x%y
            print("\noutput of mod :",mod)
        elif selected_num==8:
            square=x**2
            print("\nsquare of square :",square)
        elif selected_num==9:
            square_root=x**2
            print("\nsquare of squareroot :",square_root)
        elif selected_num==11:
            cube=x**3
            print("\nsquare of fd :",cube)
        elif selected_num==10:
            cube_root=x**3
            print("\square of fd :",(x**(1/3)))
                  
        elif selected_num==12:
            for c in range(x,y+1):
                for i in range(2,c):
                    if c%i==0:           
                        print(c,"it is not a prime")            
                        break           
            else:
                print(c," is not a prime")

        
        elif selected_num==13:
            for i in range(1,x+1):    
                fact=fact*i
                print("factorial",fact)
                break
        else:
            
            print("\ninvalid input , please enter a valid input value\n")
            break

#######################
def set11():
    global n
    while n<=13:
        if user_input==3:

            #set1={1,11,2,2,3,4}
            #set2={8,1,2,4,6,4}
            #print("set1 = ",set1)
            #print("set3 = ",set2)
            set_operations = {1:'UPDATE',2:'DISCARD',3:'REMOVE',4:'UNION',5:'INTERSECTION',6:'DIFFRENCE',7:'SYMMETRIC',8:"superset",9:'subset',10:'disjoint',11:'add'}
            for values,keys in set_operations.items():
                print(values,keys)
        n=n+1
        set_input =int(input("\nmx length of the set needed"))
        UserSet=[]
        for i in range (0,set_input):
            UserSetInput=int(input("enter the set value"))
            UserSet.append(UserSetInput)
        
        print("\nselected userlist is :",UserSet)
        a=UserSet
        set1=set(a)
        print("set1 is :",set1)

       
        set2_input =int(input("\nmx length of the set needed"))
        UserSet2=[]
        for i in range (0,set2_input):
            UserSet2Input=int(input("enter the set value"))
            UserSet2.append(UserSet2Input)
        
        print("\nselected userlist is :",UserSet2)
        a=UserSet2
        set2=set(a)
        print("set2 is :",set2)

        selected_set = int(input("select any one of above set operation :"))
        


        if selected_set==1:
            set1.update(set2)
            print("update output is ",set1)
        elif selected_set ==2:
            set1.discard(11)
            print("discard output is",set1)
        elif selected_set ==3:
            set1.remove(2)
            print("remove output is",set1)
        elif selected_set ==4:
            set1.union(set2)
            print("union output is",set1)
        elif selected_set ==5:
            set1.intersection(set2)
            print("intersection output is",set1)
        elif selected_set ==6:
            x=set1.difference(set2)
            print("difference output is",x)
        elif selected_set ==7:
            x=set1.symmetric(set2)
            print("symmetric output is",x)
        elif selected_set ==8:
            x=set2.issuperset(set1)
            print("superset output is",x)
        elif selected_set ==9:
            x=set1.issubset(set2)
            print("subset output is",x)
        elif selected_set ==10:
            z = set1.isdisjoint(set2) 
            print("isdisjoint is :",z)
        elif selected_set ==11:
            set1.add(6)
            print(set1)
        else:
            print("\ninvalid input , please enter a valid input value\n")

            break


if user_input==1:
    list11()
   
elif user_input==2:
     numbers11()

elif user_input==3:
     set11()
# print("\ninvalid input , please enter a valid input value\n")    
 

