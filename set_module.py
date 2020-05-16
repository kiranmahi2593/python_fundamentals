def Create_Set(SetInput):
    x = set()
    for i in range(SetInput):
        y = input("Enter the set Value:")
        x.add(y)
    print("the set:",x)
    return x

def AddSet(x):
    val = input("enter the value to Add:")
    x.add(val)
    print("Set After Adding the values:",x)
    return x

def clear(x):
    x.clear()
    print("New set after clearing data:",x)
    return x

def copy(x):
    copy1 = x.copy()
    print("Copied values:",copy1)
    return copy1

def difference(x):
    z = x.difference(y)
    return z

def difference_update(x):
    x.difference_update(y)
    return x

def discard(x):
        
    x.discard(val)
    print("Set After discarding the element:",x)
    return x

def intersection(x):
    z = x.intersection(y)
    return z

def intersection_update(x):
    x.intersection_update(y)
    return x

def pop(x):
    x.pop()
    print("Final set:",x)
    return x

def remove(x):
    val = input("enter the value to remove:")
    x.remove(val)
    print("Set After removing the values:",x)
    return x

def symmetric_difference(x):
    z = x.symmetric_difference(y)
    return z

def symmetric_difference_update(x):
    x.symmetric_difference_update(y)
    return x

def union(x):
    z = x.union(y)
    return z

def update(x):
    x.update(y)
    return x
