
'''
strings are immutable ie they cant be modified in python 


1.len()

2.lower()

3.upper()

4.title()

5.count()

6.strip()
   i)lstrip()
   ii)rstrip()

7.replace()

8.find()

9.center() method  ----->  ****riyan****


'''
name="shaik riyan"

#print(name+3) will give error of concatenation not possible for str and number
print(name+str(3))
print(name+"3")
print(name*3)
print(3*name)

string ="she is beautiful and she is a good dancer"

print(len(name))

print(name.lower())

print(name.upper())

print(name.title())

print(string.count("is"))

name="   hande ercel    "
dots="..............."

print(name+dots)

print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)

print(string.replace(" ","_"))

print(string.find("is"))

print(name.center(len(name)+2," "))
print(name.center(len(name)+8-2,"*"))