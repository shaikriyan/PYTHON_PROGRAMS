'''
input function will always return the string type 




first_name=input("plz enter the first name: ")
last_name=input("plz enter the last name: ")
full_name=first_name+" "+last_name
print(full_name)


first_name ,last_name=input("space seperated first name and last name: ").split()
print(first_name+" "+last_name)

first_name ,last_name=input("commas seperated first name and last name: ").split(",")
print(first_name+" "+last_name)

'''
name="shaik riyan"

print(name[3]) # i
print(name[-11]) # s

# further classes we will study about the loops 

for i in range(len(name)):
    print(f"{name[i]}=name[{i}]")


print(name[::-1]) # this is to reverse the string using string slicing concept

print("In Reverse direction \n")

for i in range(-1,-(len(name)+1),-1):
    print(f"{name[i]}=name[{i}]")








