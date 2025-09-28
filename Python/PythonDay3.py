#calculator program -->Ex1
operator=input("Enter the operator (+,-,*,/) :")
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
if operator=="+":
   print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
   print(a*b)       
elif operator=="/":
   print(a/b)
else:
    print("Invalid operator")

#weight converter --> Ex2
weight=float(input("Enter the weight :"))
unit=input("Enter the unit (kg or lb) :")
if unit=="kg":
   print(f"Weight in pounds: {weight*2.20462}")
elif unit=="lb":
   print(f"Weight in kg : {weight/2.20462}")
else:
   print("Invalid unit")

#and or not logical operator
age=int(input("Enter your age:"))
if age>=19 and age<=65:
 print("You are eligible to work")
else:
 print("You are not eligible to work")

#shortcut for if else statement
group=input("Enter your group (A,B,C):")
print("You are eligible" if group=="A" or group=="B" else "Not eligible")

#string method 
name=input("Enter your name : ")
length=len(name)
print(f"{length}")
character=name.find("s")
print(f"{character}")
print(name.upper())
print(name.capitalize())
print(name.isdigit())
print(name.isalpha())
print(name.count("a"))
print(name.replace("a",""))
#string indexing and slicing [start:stop:step]
credit="1234-5678-9123"
#starting index is 1
print(credit[1:])
#starting index is 1 and ending index is 4
print(credit[1:4])
#starting index is from last index
print(credit[-1:])
#starting index is from 1 and ending index is last but with 2 number gap
print(credit[: : 2])