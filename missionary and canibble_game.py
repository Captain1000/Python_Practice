print("Wellcome to the game")
left_missio=3
right_mission=0
left_cani=3
right_cani=0
k = 00
print("M M M C C C |-->|")
while(True):
    while(True):
        print("\nSend to right--->")
        user_mission=int(input("Enter the value of missionary: "))
        user_cani=int(input("Enter the value of canible: "))
        if(user_mission==0) and (user_cani==0):
            print("Nouka kon tera baap chalayaga??")
        elif (((user_mission + user_cani) <= 2) and ((left_cani - user_cani) >= 0) and ((left_missio - user_mission) >= 0)):
            break
        else:
            print("wrong input")
            print("Try again")
    left_missio-=user_mission
    left_cani-=user_cani
    right_mission+=user_mission
    right_cani+=user_cani
    k+=1
    for i in range(0,left_missio):
        print("M",end=" ")
    for i in range(0,left_cani):
        print("C",end=" ")
    print("-->",end=" ")
    for i in range(0,right_mission):
        print("M",end=" ")
    for i in range(0,right_cani):
        print("C",end=" ")
    if (left_missio != 0 and left_cani > left_missio) or (right_mission != 0 and right_cani > right_mission):
        print("Canibbel eat missionary")
        print("You lost this match")
        break
    if (right_cani+right_mission)==6:
        print("\ncogratulation!!! You won this match")
        print("You took",k,"steps to finish the game")
        break
    while(True):
        print("\nSend to left--->")
        user_mission = int(input("Enter the value of missionary: "))
        user_cani = int(input("Enter the value of canible: "))
        if (user_mission == 0) and (user_cani == 0):
            print("Nouka kon tera baap chalayaga??")
        elif (((user_mission+user_cani)<=2) and ((right_cani-user_cani)>=0) and ((right_mission-user_mission)>=0)):
            break
        else:
            print("wrong input")
            print("Try again")
    left_missio += user_mission
    left_cani += user_cani
    right_mission -= user_mission
    right_cani -= user_cani
    k += 1
    for i in range(0, left_missio):
        print("M", end=" ")
    for i in range(0, left_cani):
        print("C", end=" ")
    print("<--",end=" ")
    for i in range(0, right_mission):
        print("M", end=" ")
    for i in range(0, right_cani):
        print("C",end=" ")
    if (left_missio!=0 and left_cani > left_missio) or (right_mission!= 0 and right_cani > right_mission):
        print("Canibbel eat missionary")
        print("You lost this match")
        break
    if (right_cani+right_mission)==6:
        print("cogratulation!!! You won this match")
        print("You took",k,"steps to finish the game")
        break


