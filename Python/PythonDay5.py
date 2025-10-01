#for loop
#in reverse case 
# for i in reversed(range(0,5)):
#     print(i)
#in increment case
# for x in range(1,11,3):
#     print(x)
#for continue case
for i in range(1,11):
    if i==3:
        continue
    else :
      print(i)
#normal case
for i in range(0,5):
    print(i)
print()
    #countdown timer
import time
seconds=int(input("Enter the countdown in seconds : "))
minutes=int(input("Enter the countdown in minute: "))
hours=int(input("Enter the countdown in hrs : "))
total=hours*3600+minutes*60+seconds
for timer in range (total,-1,-1):
     hr=timer
     min=(timer%360)
     sec=(timer%3600)
     print(f"{hr:02d}:{min:02d}:{sec:02d}")
     time.sleep(1)
print("Time Up!")
        