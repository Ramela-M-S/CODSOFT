print("Welcome to password generator python project")
import random
num=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alp=[ "A", "B","C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
sym=["~","!","@","#","$","%","^","&","*","|"]
passwd=""

n=int(input("enter no. of ints to be in password:"))
for i in range(n):
    x=random.choice(num)
    passwd+=x

a=int(input("enter no. of alphabets to be in password:"))
for i in range(a):
    x=random.choice(alp)
    passwd+=x

s=int(input("enter no. of symbols to be in password:"))
for i in range(s):
    x=random.choice(sym)
    passwd+=x


print("1 for easy rememberable password")
print("2 for strong password")

user=int(input("enter the choice:"))
if user==1:
    print(passwd)
elif user==2:
    l=list(passwd)
    random.shuffle(l)
    sp="".join(l)
    print(sp)
else:
    print("entered wrong choice")