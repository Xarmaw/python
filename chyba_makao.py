import random
J=10
Q=10
K=10
A=11
bull=["Tak","tak","Nie","nie"]
karty=[2,3,4,5,6,7,8,9,J,Q,K,A]
c=[]
Bot=[]
for z in range(0,2):
    p=random.choice(karty)
    Bot.append(p)
h=Bot[0]+Bot[1]
if h<21:
    j=random.choice(bull)
if j=="tak" or j=="Tak":
            p=random.choice(karty)
            Bot.append(p)
elif j=="nie" or j=="Nie":
      print()



for z in range(0,2):
    b=random.choice(karty)
    c.append(b)
print(c)
d=c[0]+c[1]
v=1

while d<21:
    a=input(f"oto sa twoje karty czy chcesz dobrac nastepna {c}",)
    while a not in bull:
        a=input("chcesz dobrac karte tak lub nie przypominam twojimi kartami sa",c)
        if a=="tak" or a=="Tak":
            b=random.choice(karty)
            c.append(b)
            v=v+1
            d+c[v]

        elif a=="nie" or a=="Nie":
            break

if h>21 and d<21:
     print("brawo wygrales")

