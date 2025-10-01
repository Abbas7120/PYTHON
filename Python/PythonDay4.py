#compund interest calc
principle=float(input("Enter the principle amount: "))
rate=float(input("Enter the rate of interest: "))
time=float(input("Enter the time in years: "))
total=principle*(pow(1+rate/100,time))
print(f"The CI is {total:.2f}")

#while loop
i = 1
while i <= 5:
    print(i)
    i += 1


