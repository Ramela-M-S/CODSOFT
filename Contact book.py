print("Welcome to Calculator python project")
cont=[]
while True:
    print("0 - To add contacts")
    print("1 - To view contact")
    print("2 - To seacrch contact")
    print("3 - To update contact")
    print("4 - To delete contact")
    z=int(input("enter your choice:"))
    if z>=0 and z=4:
        con(z)
    else:
        print("The stored contacts are:")
        for i in cont:
            print(i)
        
