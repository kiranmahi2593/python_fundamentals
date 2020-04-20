#snake gun ==> gun
#gun water ==> water
#snake water ==> water

#clues:
#get one value form user
#random choic
#total 10 attempts played  with user 4 attemps /system 3/tie system


attempt = 10
user=0
system=0
draw=0
i=0
import random
a=("snake","gun","water")
while i<10:
    a1=(random.choice(a))
    x=input("enter the string : ")
    if x== ("snake"):
        if a1==("water"):
            print("user")
            user=user+1
        elif a1==("gun"):
            print("system")
            system=system+1
        elif a1==("snake"):
            print("draw")
            draw=draw+1

    elif x== ("gun"):
        if a1==("water"):
            print("system")
            system=system+1            
        elif a1==("gun"):
            print("draw")
            draw=draw+1            
        elif a1==("snake"):
            print("user")            
            user=user+1

    elif x== ("water"):
        if a1==("snake"):
            print("system")
            system=system+1            
        elif a1==("water"):
            print("draw")
            draw=draw+1            
        elif a1==("gun"):
            print("system")            
            user=user+1
    i=i+1

print("points of user:",user)
print("points of system:",system)
print("draw points", draw)



    
        
    





        
    
        
        
