#Take input from user
name = input("Enter your name: ")
print(name)

#Take integer input from user
number = int(input("Enter a number:"))
print(number+1)

#Take multiple inputs 
a, b, c = map(int,input("Enter numbers: ").split())
print(a,b,c)

#Take inputs for sequential data list, set
L = list()
S = set()
Llen = int(input("Enter list length: "))
for i in range(0,Llen):
    L.append(int(input("Enter "+ str(i) +" index position element: ")))
Slen = int(input("Enter Set length: "))
for i in range(0,Slen):
    S.add(int(input("Enter "+ str(i) +" index position element: ")))
print(L, S)

#Using map
L = list(map(int,input("Enter numbers: ").split()))
S = set(map(int, input("Enter numbers: ").split()))
print(L, S)

#Add elements to tuple
T = (1,2,4,5,6)
L=list(T)
L.append(int(input("Enter tuple element: ")))
T = tuple(L)
print(T)

#Output in Python
# print(value, end='', sep='', file="", flush=true)
# end - specify what to print in end. Default /n 
# sep - Specify what to print when many items are present
# file - object Name
# flush - boolean value - flush the output or buffered

# print() method
print("GFG", end = "\n")
 
# code for disabling the softspace feature 
print('G', 'F', 'G', sep="#")

#formatting output in Python
name = "Mohan"
print(f'Hi my name is {name}')
a=b=20
sum = a+b
sub = a-b+30
print("a is {0}, b is {1}, sum is {2}".format(a,b,sum))
print("a is {A}, b is {B}, sub is {C}".format(A=a,B=b,C=sub))

# %d -int
# %f -float
# %s -string
# %o -octal
# %x -hexadecimal
print("Sum is %d" %sum)

