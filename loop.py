
'''
sum of first n natural numbers 
'''

n=int(input("plz enter a number : "))

sum=0
for i in range(1,n+1):
    sum+=i
print("The sum of first {} natural number is {}" .format(n,sum)) 

j=1
total=0
print(f"n={n}")
while j<=n:
    total+=j
    j+=1
print(f"The sum of {n} natural number is :{total}")    
    