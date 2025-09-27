import math
#for print  # --> used for comment 
print("Hello Python")
#for declaring variable
#types of variables in python : string boolean integer float
#for string 
a="Hello Python String "
#for integer
b=12
#for float
c=13.5
#for boolean
d=True
#for printing variable
#print with some statement like JS 
print(f"The value of a is {a}")
print(b)
print(c)
print(d)
#for taking input we use input() function
v=(input("Enter your name:"))

print(f"My name is {v}")
#typecasting 
#In age we can see that for changing any type we use type() 
f=input("Enter your age:")
f=int(f)
print(f"My age is {f}")
print(f"The age type is {type(f)}")
#how to add and subtract
friends=0
friends+=1
print(friends)
friends-=1
print(friends)
friends**=2
print(friends)

print(math.pi)
#calculate area and perimeter of circle
r=input("Enter the radius :")
r=int(r)
print(f"The perimete rof circle is :{2*math.pi*r}")
rt=float(math.sqrt(r))
print(f"The area of circle is :{math.pi*rt}")

