
# syntax(name[start_argument: stopargument+1: step_argument])


name=input("plz enter your name: ")

#name ="shaik riyan"

print(name[0:]) # full name
print(name[:]) # full name
print(name[:len(name)]) #full name

print(name[2:8]) # from 2 to 7 ie "aik ri"

print(name[2:3]) # "a"

print(name[2:-3]) # "aik ri"

print("shaik riyan"[0::2]) #sakryz

# To print the string reverse



print(name[::-1])