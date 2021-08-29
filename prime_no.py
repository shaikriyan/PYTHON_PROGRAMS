'''
number having factor itself and 1 then it is called as prime number




'''


def is_prime(n):
    if n>=0:
        if n==0 or n==1:
            return False
        elif n==2:
            return True
        else:
            for i in range(2,n):
                if n%i==0:
                    return False
            return True
    else:
        return False

for i in range(3):
    num=int(input("plz enter a number : "))
    print(is_prime(num))



