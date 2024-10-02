import random
print("Welcome to rock_paper_scissors python project")
con=["rock","scissors","paper"]
ur=0
cr=0
def rps(xur,ycr,zuc):
    cc=random.choice(con)
    print("Computer's choice :",cc)
    if zuc==cc:
        xur+=0.5
        ycr+=0.5
        print("draw")
        

    elif zuc=="rock":
        if cc=="paper":
            ycr+=1
            print("computer won")
        else:
            xur+=1
            print("user won")

    elif zuc=="paper":
        if cc=="scissors":
            ycr+=1
            print("computer won")
        else:
            print("user won")
            xur+=1

        

    elif zuc=="scissors":
        if cc=="rock":
            ycr+=1
            print("computer won")
        else:
            xur+=1
            print("user won")
    return xur,ycr
        

 
while True:
    
    print("1 to start or continue or other no. to exit")
    y=int(input("enter the choice:"))
    if y==1:
        uc=input("enter rock,paper or scissors:").lower()
        ur,cr=rps(ur,cr,uc)
    else:
        if ur>cr:
            print("User won the game")
        elif ur==cr:
            print("Draw game")
        else:
            print("Computer won the game")
        print("Exiting... rock_paper_scissors python project")
        print("Thank you for visiting")
        break