
'''
basic syntax of a function in python is 

def function_name (parameter1,parameter2,....):
    statements1
    statements2
    statements3
    statements4
    .....

    return output



'''

#greatest of two numbers

def greater(a,b):
    if a>b:
        return a
    return b
print(greater(34,43))


def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    return c
print(greatest(10,20,30))


#function inside function 

def new_greatest(a,b,c):
    return greater(greater(a,b),c)
print(f"The greatest of three numbers is : {new_greatest(1,2,3)}")
