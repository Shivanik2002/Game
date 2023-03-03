import random

Cchoice = ["Rock","Paper","Scisser"]          # list for computer

while True:
    print("Rock Paper scissor Game:")
    youwin,computerwin = 0,0

    for i in range(1,3):             # five round game
        print("Round",i,"start:")
        print("Please select any one option:")
        print("1.Rock","2.Paper","3.Scissor",sep="\n")   # choice any option
        yourchoice = int(input("enter your choice:"))

        if yourchoice==1:           
            print("You select Rock")
            yourchoice = "Rock"

        elif yourchoice==2:
            print("You select paper") 
            yourchoice = "Paper"   

        elif yourchoice==3:
            print("You select Scissor")
            yourchoice = "Scissor"    

        else:
            print("Invalid Choice")
            break

        computerchoice = random.choice(Cchoice)           # random select by computer
        print("Computer select:",computerchoice)

        if yourchoice == computerchoice:
            youwin += 1
            computerwin += 1
            print("This Round is Drawn:")

        elif (yourchoice == "Paper" and computerchoice == "Rock") or (yourchoice == "Rock" and computerchoice == "Scissor") or (yourchoice == "Scissor" and computerchoice == "Paper"):
            youwin += 1
            print("You win this Round")   

        else:
            computerwin += 1
            print("Computer win this Round")  

        # if your more point than computer then your win and vice versa

    if youwin>computerwin:
        print("You win the game:")          
        print("Score is :","your score :",youwin,"computer score :",computerwin,sep=" ")

    elif computerwin>youwin:
        print("You lose the game . Computer win the game:")    
        print("Score is:","Your score",youwin,"Computer score:",computerwin,sep=" ")

    else:
        print("Match Drewn")    
        print("Score is :","Your score :",youwin,"computer score :",computerwin,sep=" ")
    
    user_choice = input("want to play again?(yes/Exit)")

    if user_choice == "Yes" or user_choice == "Yes":
        continue

    else:
        break    
