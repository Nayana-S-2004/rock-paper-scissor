import random

print("enter r for rock\nenter p for paper\nenter s for scissor")

computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youDict={"r":1,"p":-1,"s":0}
reverseDict={1:"rock",-1:"paper",0:"scissor"}

you=youDict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer==you):
    print("It's a draw")

else:
    # if(computer==-1 and you==0):(computer-you=-1)
    #     print("You win!")
    # elif(computer==1 and you==0):(computer-you=1)
    #     print("You lose!")
    # elif(computer==0 and you==-1):(computer-you=1)
    #     print("You lose!")
    # elif(computer==0 and you==1):(computer-you=-1)
    #     print("you win!")
    # elif(computer==-1 and you==1):(computer-you=-2)
    #     print("you lose!")
    # elif(computer==1 and you==-1):(computer-you=2)
    #     print("Yoy win!")h
    if(computer-you==-1 or computer-you==2):
        print("You Win!")
    else:
        print("You lose!")
