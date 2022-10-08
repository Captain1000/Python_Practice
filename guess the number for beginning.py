# n =  15
# i= 0
# while(i<10):
#     print(10-i,"chances are left")
#     i=i+1
#     num=int(input("Enter the guessing number\n"))
#
#     if num==n:
#         print("Correct guess. The number is",n)
#         print("\nYou guess the number in", i, "chance")
#         break
#     elif num<n:
#         print("Too short")
#     elif num>n:
#         print("Too high")
#
# print("Game over")

import random
random_choice=random.randint(0,100)
choice='y'
while choice!='n':
    i=0
    while i<=10:
        print(10-i,"chance left")
        x=int(input("Enter the number: "))
        if x>random_choice:
            print("Enter a smaller value\n")
        elif x<random_choice:
            print("Enter a bigger value\n")
        else:
            print("Element is found")
            print("you search the number after",i+1,"time\n" )
            break
        i=i+1
    choice = input("Try again?? y/n")

print("game over")