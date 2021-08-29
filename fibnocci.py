'''
fibonacci series 

0 1 1 2 3 5 8 13 .....

To print a fibonacci series upto a given number n

'''

def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        for i in range(n):
            print(a ,end=" ")
            c=a+b
            a=b
            b=c
fib(20)