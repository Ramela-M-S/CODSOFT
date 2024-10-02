print("Welcome to Calculator python project")
def arith(y):
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    if y==0:
        print("Addition of a and b is:",a+b)
    elif y==1:
        print("Subraction of a and b is:",a-b)
    elif y==2:
        print("Multiplication  of a and b is:",a*b)
    elif y==3:
        print("Quotient of a and b is:",a/b)
    else:
        print("Remainder of a and b is:",a%b)




while True:
    
    print("0 - For addition")
    print("1 - For subraction")
    print("2 - For multiplication")
    print("3 - For quotient")
    print("4 - For remainder")
    x=int(input("enter the option:"))
    if x>=0 and x<=4:
        arith(x)
    else:
        print("Exiting the Calculator python project")
        print("Thank you for visiting")
        break

    
