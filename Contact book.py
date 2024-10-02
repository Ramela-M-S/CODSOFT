print("Welcome to Calculator python project")
cont=[]
def con(x):
    if x==0:
        nc=int(input("enter how many contacts to be  added:"))
        for i in range(nc):
            l=[]
            name=input("enter name:")
            phn=int(input("enter phone number:"))
            email=input("enter mailid:")
            addr=input("enter address:")
            l=[name,phn,email,addr]
            cont.append(l)

    elif x==1:
        if not cont:
            print("No contacts added")
        else:
            print("saved contacts details are:")
            for i in cont:
                print(i[0],i[1])


    elif x==2:
        print("1 - To search by name")
        print("2 - To search by phone no.")
        c=int(input("enter your choice:"))
        if c==1:
            n=input("enter name to be searched:")
            for i in cont:
                if i[0]==n:
                    print(i)
        elif c==2:
            pn=int(input("enter phone number:"))
            for i in cont:
                if i[1]==pn:
                    print(i)

        else:
            print("Entered wrong option")




    elif x==3:
        print("0 - To update name")
        print("1 - To update phone number")
        print("2 - To update mail-id")
        print("3 - To update address")
        c=int(input("enter your choice:"))
        if c==0:
            un=input("enter name to be updated:")
            for i in cont:
                if i[0]==un:
                    n=input("enter new name :")
                    i[0]=n
                    print("Updated sucessfully")
        
        elif c==1:
            up=int(input("enter phone no. to be updated:"))
            for i in cont:
                if i[1]==up:
                    n=int(input("enter new no. :"))
                    i[1]=n
                    print("Updated sucessfully")


        elif c==2:
            um=input("enter mailid:")
            for i in cont:
                if i[2]==um:
                    n=input("enter new mailid:")
                    i[2]=n
                    print("Updated sucessfully")
        elif c==3:
            ua=input("enter address:")
            for i in cont:
                if i[3]==ua:
                    n=input("enter new address :")
                    i[3]=n
                    print("Updated sucessfully")
        else:
            print("Entered wrong option")
       

    else:
        n=input("enter name whose contact to be deleted:")
        for i in cont:
            if i[0]==n:
                cont.remove(i)
        print("contact deleted successfully")

    return cont
            
        



while True:
    print("0 - To add contacts")
    print("1 - To view contact")
    print("2 - To search contact")
    print("3 - To update contact")
    print("4 - To delete contact")
    z=int(input("enter your choice:"))
    if z>=0 and z<=4:
        cont=con(z)
    else:
        print("The stored contacts are:")
        for i in cont:
            print(i)
        print("Exiting... calculator python project")
        print("Thank you for visiting")
        break
        
