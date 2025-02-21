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
    if(computer==-1 and you==0):
        print("You win!")
    elif(computer==1 and you==0):
        print("Computr win!")
    elif(computer==0 and you==-1):
        print("Computer win!")
    elif(computer==0 and you==1):
        print("you win!")
    elif(computer==-1 and you==1):
        print("computer win!")
    elif(computer==1 and you==-1):
        print("You win!")
    else:
        print("Something went wrong!")
