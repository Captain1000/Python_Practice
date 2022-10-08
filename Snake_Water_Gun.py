import random
game_list=["s","w","g"]
choice_list={"s":"Snake","w":"Water","g":"Gun"}
print("Welcome to snake water and Gun game")
print("Let's play the game")
choose='y'
for option,game in choice_list.items():
    print("Enter",option,"for",game)
playing_number=10
you_won=0
computer_won=0
while choose!='n' and choose=='y':
    while playing_number>0:
        random_genarate = random.choice(game_list)
        random_option = choice_list[random_genarate]
        choice = input("Enter: ")
        if choice == 's' or choice == 'w' or choice == 'g':
            print("You choose",choice_list[choice])
            print("Computer choose: ",random_option)
            if choice=='s' and random_option=="Water":
                print("You win this round!!")
                you_won+=1
            elif choice=='w' and random_option=="Gun":
                print("You win this round!!")
                you_won+=1
            elif choice=='g' and random_option=="Snake":
                print("You won this Round!!")
                you_won+=1
            elif choice==random_option:
                print("Round is tie")
            else:
                print("Computer won this round!!")
                computer_won+=1
            playing_number -= 1
            print(playing_number, "rounds are left")
        else:
            print("You enter wrong input!!! try again")
    if you_won>computer_won:
        print("Congratulation!!! you won this match")
    elif you_won<computer_won:
        print("Sorry!!! you lost this match")
    else:
        print("Match draw!!")
    choose=input("Try again?  y/n: ")
print("The game has Ended")
