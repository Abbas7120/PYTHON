# #square pattern
# for i in range(0,6):
#     for j in range(0,4):
#         print("*",end=" ")
#     print()

#     #number pattern
#     for i in range(0,6):
#      for j in range(0,4):
#         print(j,end=" ")
#     print()

#right angle triangle
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

#printing cordinates
for i in range(3):
    for j in range(3):
        print(f"{(i),(j)}")

#multiplication table
for i in range (1,11): 
    for j in range (1,11):
     print(f"{i}x{j}={i*j}",end="\t")
    print()       