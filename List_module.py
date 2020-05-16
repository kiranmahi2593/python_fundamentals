def create_list():
    # creating an empty list 
    lst = [] 
  
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input()) 
        lst.append(ele) # adding the element 
      
    return lst

#####################################################
def List_len():
    

    n=create_list()
    length=len(n)
    return length
#####################################################
def List_min():
    n=create_list()
    min1= min(n)
    return min1

#####################################################
def List_max():
    n=create_list()
    max1= max(n)
    return max1
#####################################################
def List_Add(x):
    val=int(input("Enter the value to be added:"))
    x.append(val)
    print("The new list is:",x)
    return x
#####################################################
def List_Sort():
    n=create_list()
    sorted_list= sorted(n)
    return sorted_list
####################################################
def List_Remove():
    n=create_list()
    x=int(input("Enter the value needs to be removed:"))
    n.remove(x)
    return n
####################################################
def List_Concat():
    n=create_list()
    p=create_list()
    for x in p:
        n.append(x)
    return n
####################################################

      
