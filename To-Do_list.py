print("Welcome to To-Do list python project")
lst=[]
def todo(y):
    if y==0:
        nadd=int(input("enter the no. of task to be added:"))
        for i in range(nadd):
            add=input("enter the task:")
            lst.append(add)
        print("Tasks added successfully")

    elif y==1:
        if len(lst)==0:
            print("No tasks yet added")
        else:
            print("Tasks tracked so far:")
            for i,j in enumerate(lst):
                print(i,"-",j)
    
    elif y==2:
        ut=input("enter task to be updated:")
        for i in range(len(lst)):
            if lst[i]==ut:
               x=input("enter updated task:")
               lst[i]=x
            else:
                print("No such task entered")

    elif y==3:
        dr=input("enter task needed to be marked as completed and deleted:")
        if dr in lst:
            print(dr,"task is completed")
            lst.remove(dr)
        else:
            print("No such task entered")


    return lst

 
while True:
    
    print("0 - To create tasks")
    print("1 - To track tasks")
    print("2 - To update")
    print("3 - To mark complete and delete")
    print("any other no. to exit To-Do list")
    x=int(input("enter the option:"))
    if x>=0 and x<=3:
        todo(x)
    else:
        print("The remaining tasks are:")
        if len(lst)==0:
            print("No tasks had been added")
        else:
            for i in lst:
                print(i)
        print("Exiting...the todo list")
        print("Thank you for visiting")
        break
