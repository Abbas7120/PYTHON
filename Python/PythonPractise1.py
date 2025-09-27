import math
#Calculate perimeter and area of rectangle
l=input("Enter the length of rectangle : ")
l=int(l)
b=input("Enter the breadth of rectangle : ")
b=int(b)
print(f"The perimeter of rectangle is :{2*(l+b)}")
print(f"The area of rectangle : {l*b}")

#print hypotenuse of triangle
p=int(input("Enter the perimeter of traingle"))
b=int(input("Enter the base of triangle"))
h=math.sqrt(pow(p,2)+pow(b,2))
print(f"The hypotenuse of a triangle is : {h} ")
#shopping cart program
print("Pick up those items whose price is less than 100")
item1=40

item2=60

item3=20

itemPrice=item1+item2+item3
if itemPrice<100:
    print("Pack all these items")
else:
    print("Don't pack all these items ")

    
