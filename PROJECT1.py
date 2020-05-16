#Ds/Dt Calculator
#Algebra Functions

Functions={1:"Numbers",2:"List",3:"Sets",4:"Strings",5:"Tuples",6:"Dictionaries"}
for values,keys in Functions.items():
    print(values,keys) #to print all the keys with their values.
Func_input=int(input("Enter the function to be performed from above options:"))
    

def Number_Operations():
    Number_ops={1:"Add",2:"Subtract",3:"Multiply",4:"Divide",5:"Floor Division",6:"Power",7:"Mod",8:"Square",9:"Square root",10:"Cube",11:"Cube root",12:"Prime",13:"Armstrong",14:"Fibonacci",15:"Factorial",16:"Odd/ Even"}
    for values,keys in Number_ops.items():
        print(values,keys)

    Num_Func=int(input("Enter the Algebra function to be performed from above options:"))
    
         #print(x,y)
    import math
    import Func_module

    if Num_Func==1: #if the user chooses 1 then perform Addition function
        #x, y = map(int, input("Enter two numbers seperated by ',':").split(","))
        print("The sum of numbers is:", Func_module.Add(3,2))

    elif Num_Func==2: #if the user chooses 2 then perform subtraction function
             x, y = map(int, input("Enter two numbers seperated by ',':").split(","))
             print("The difference of numbers is:", Func_module.sub(x,y))

    elif Num_Func==3: #if the user chooses 3 then perform multiplication function
             x, y = map(int, input("Enter two numbers seperated by ',':").split(","))
             print("The product of numbers is:", Func_module.prod(x,y))
             
    elif Num_Func==4: #if the user chooses 4 then perform division function
             x, y = map(int, input("Enter two numbers seperated by ',':").split(","))
             print("The quotient of numbers is:", Func_module.div(x,y))

    elif Num_Func==5:#if the user chooses 5 then perform floor division function
             x, y = map(int, input("Enter two numbers seperated by ',':").split(","))
             print("The floor div of numbers is:", Func_module.Floor_div(x,y))

    elif Num_Func==6:#if the user chooses 6 then perform power function
             print("The power value is:", math.pow(x,y))

    elif Num_Func==7:#if the user chooses 7 then perform mod function
             x, y = map(int, input("Enter two numbers seperated by ',':").split(","))
             print("The Mod of numbers is:", math.fmod(x,y))

    elif Num_Func==8: #if the user chooses 8 then perform square function
             x= int(input("Enter the number:"))
             print("The square of x is:",(x**2))

    elif Num_Func==9: #if the user chooses 9 then perform square root function
             x= int(input("Enter the number:"))
             print("The square root of x is:", math.sqrt(x))
             
             
    elif Num_Func==10: #if the user chooses 10 then perform cube function
             x= int(input("Enter the number:"))
             print("The cube of x is:",(x**3))
    
    elif Num_Func==11: #if the user chooses 11 then perform cube root function
             x= int(input("Enter the number:")) 
             print("The cube root of x is:",(x**(1/3)))

    elif Num_Func==12:#if the user chooses 12 then perform prime number or not function
        x= int(input("Enter the number:"))
        Func_module.Prime_num(x)

    elif Num_Func==13:#if the user chooses 13 then perform Armstrong function
        x= int(input("Enter the number:"))
        Func_module.Armstrong(x)

    elif Num_Func==14: #if the user chooses 14 then perform fibonacci function
        x= int(input("Enter the number:"))
        print("The fibonacci of x is:",Func_module.Fibonacci(x))

    elif Num_Func==15: #if the user chooses 15 then perform factorial function
        x= int(input("Enter the number:"))
        print("The factorial of x is:",math.factorial(x))

    elif Num_Func==16: #if the user chooses 16 then perform odd/even function
            x= int(input("Enter the number:"))
            if (x%2)==0:
                print("Number given is an even number")

            else:
                print("Number given is an odd number")


if Func_input==1:
    Number_Operations()
#End of Number operations...................................................................................................................................

def List_Operations():

        List_ops={1:"Create List",2:"Length of List",3:"Min",4:"Max",5:"Add",6:"Sort",7:"Remove",8:"Concate"}

        for values,keys in List_ops.items():
             print(values,keys) #list out all the list operation

        List_Func=int(input("Enter the List function to be performed from above options:"))

        import List_module

        if List_Func==1:#if the user chooses 1 then create a list
            List1=List_module.create_list()
            print(List1)

        elif List_Func==2:#if the user chooses 2 then create a list and find the length
            print("Length of the List is",List_module.List_len())

        elif List_Func==3:#if the user chooses 3 then create a list and find the minimum value
            print("Minimum value of the List is",List_module.List_min())

        elif List_Func==4: #if the user chooses 4 then create a list and find the maximum value
            print("Maximum value of the List is",List_module.List_max())

        elif List_Func==5: #if the user chooses 5 then create a list and add items to the list
            List1=List_module.create_list()
            print(List1)
            List_module.List_Add(List1)

        elif List_Func==6: #if the user chooses 6 then create a list and sort the list
            print("sorted List is",List_module.List_Sort())

        elif List_Func==7: #if the user chooses 7 then remove the item from list
            print("New List is",List_module.List_Remove())

        elif List_Func==8:#if the user chooses 8 then perform concat function
            print("New List after concatination is",List_module.List_Concat())
        
if Func_input==2:
    List_Operations()
#End of List Operations.........................................................................................................................................
def Set_Operations():
    set_ops={1:"Add",2:"clear",3:"copy",4:"difference",5:"difference_update",6:"discard",7:"intersection",8:"intersection_update",9:"pop",10:"remove",11:"symmetric_difference",12:"symmetric_difference_update",13:"union"}
    for values,keys in set_ops.items():
             print(values,keys)

    set_func=int(input("Enter the set function to be performed from above options:"))
    import set_module
    lset1 = int(input("Enter the Length of Set to be create :\n"))
    set1 = set_module.Create_Set(lset1)

    if set_func == 1:
        set_module.AddSet(set1)

    elif set_func == 2:
        set_module.clear(set1)

    elif set_func == 3:
        set_module.copy(set1)

    elif set_func == 4:
        Dset1 = int(input("Enter the Length :"))
        DSet2 = set_module.Create_Set(Dset1)
        set2 = set1.difference(DSet2)
        print("Set Value differences:",set2)

    elif set_func == 5:
        Dset1 = int(input("Enter the Length :"))
        DSet2 = set_module.Create_Set(Dset1)
        set1.difference_update(DSet2)
        print("Set Value differences:",set1)

    elif set_func == 6:
        dis1 = input("Enter the value to be dicarded:")
        set1.discard(dis1)
        print("discarded value:",set1)

    elif set_func == 7:
        x = int(input("Enter the Length of set 2:"))
        set2 = set_module.Create_Set(x)
        new_set = set1.intersection(set2)
        print("Set after intersection:",new_set)

    elif set_func == 8:
        x = int(input("Enter the Length of set 2:"))
        set2 = set_module.Create_Set(x)
        set1.intersection_update(set2)
        print("Set after intersection_update:",set1)

    elif set_func == 9:
        set_module.pop(set1)

    elif set_func == 10:
        set_module.remove(set1)

    elif set_func == 11:
        x = int(input("Enter the Length of set 2:"))
        set2 = set_module.Create_Set(x)
        set3 = set1.symmetric_difference(set2)

    elif set_func == 12:
        x = int(input("Enter the Length of set 2:"))
        set2 = set_module.Create_Set(x)
        set1.symmetric_difference_update(set2)
        print("symmetric_difference_update of set1:",set1)

    elif set_func == 13:
        union1 = int(input("Enter the length of second set :\n"))
        uset = set_module.Create_Set(union1)
        uset1 = set1.union(uset)
        print("union set:",uset1)

       

if Func_input==3:
    Set_Operations()
#End of set operation...........................................................................................................................................
def String_Operations():

        string_ops={1:"Length",2:"Reverse",3:"Join",4:"Split",5:"Palindrome",6:"Add two String",7:"Starts with",8:"Ends with",9:"Ascii",10:"Vowels",11:"Replace"}

        for values,keys in string_ops.items():
             print(values,keys)

        str_func=int(input("Enter the string function to be performed from above options:"))

        import string_module

        if str_func==1:
            print(string_module.Len_module())

        if str_func==2:
            print(string_module.Reverse())

        if str_func==3:
            print(string_module.Join_string())

        if str_func==4:
            print(string_module.Split())

        if str_func==5:
            s=string_module.Add_String()

        if str_func==6:
            print(string_module.Add_String())

        if str_func==7:
            print("The start of string is:",string_module.Start_char())

        if str_func==8:
            print("The end of string is:",string_module.End_char())

        if str_func==9:
            print("The ASCII value of string is:",string_module.ASCII_char())


        if str_func==10:
            s=string_module.Vowels()

        if str_func==11:
            print("The ASCII value of string is:",string_module.Replace_char())

        
if Func_input==4:
    String_Operations()
#End of String options=================================================================================================================
    
def Tuple_Operations():

    Tuple_ops = { 1:"length","2":"count","3":"index","4":"slicing"}

    for values,keys in Tuple_ops.items():
             print(values,keys)

    tuple_func=int(input("Enter the tuple function to be performed from above options:"))

    import tuple_module
    tup1 = int(input("Enter the Length of Tuple to be created:"))
    utup = tuple_module.create_tuple(tup1)

    if tuple_func == 1:
        print("The length of the Tuple is :",tuple_module.Length(utup))
        
    elif uple_func == 2:
        tuple_module.count(utup)
        
    elif uple_func == 3:
        tuple_module.indexing(utup)
        
    elif uple_func == 4:
        print("The finalized tuple after slicing :",tuple_module.slicing(utup))
        
if Func_input==5:
    Tuple_Operations()
#End of Tuple operation================================================================================================================

def Dictionary_Operations():

    Dictn_ops = { 1:"Add",2:"Remove",3:"Remove last element",4:"Get Keys",5:"Get Values",6:"Items",7:"Replace"}

    for values,keys in Dictn_ops.items():
             print(values,keys)

    Dictn_func=int(input("Enter the Dictionary function to be performed from above options:"))

    import dict_module

    udict = int(input("Enter the length of dictionary:"))

    if Dictn_func==1:
        
        udict1 = dict_module.Add(udict)


    if Dictn_func==2:
        udict1 = dict_module.Add(udict)
        dict_module.Remove(udict1)

    if Dictn_func==3:
        udict1 = dict_module.Add(udict)
        dict_module.Remove_last(udict1)

    

    if Dictn_func==4:
        udict1 = dict_module.Add(udict)
        dict_module.Get_keys(udict1)

    if Dictn_func==5:
        udict1 = dict_module.Add(udict)
        dict_module.Get_Values(udict1)

    if Dictn_func==6:
        udict1 = dict_module.Add(udict)

    if Dictn_func==7:
        udict1 = dict_module.Add(udict)
        dict_module.Replace(udict1)
        
        

if Func_input==6:
    Dictionary_Operations()
