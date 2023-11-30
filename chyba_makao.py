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



for z in range(0,2):
    b=random.choice(karty)
    c.append(b)

d=c[0]+c[1]
v=1

while d<21:
    pytanko=a=input(f"oto sa twoje karty czy chcesz dobrac nastepna {c}",)
    if a=="tak" or a=="Tak":
        b=random.choice(karty)
        c.append(b)
        v=v+1
        d=d+c[v]
        
    elif a=="nie" or a=="Nie":
        break
    else:
      a=input(f"oto sa twoje karty czy chcesz dobrac nastepna {c}",)   

if h>21 and d>21:
     print(f"przegrales. twoje karty{c} karty bota {Bot}")

if h>21 and d<21:
     print(f"brawo wygrales twoje karty{c} karty bota {Bot}")

if h<21 and h>d and d<21:
     print(f"przegrales twoje karty{c} karty bota {Bot}")
if h<21 and h<d and d<21:
     print(f"wygrales twoje karty{c} karty bota {Bot}")
if h>21 and h>d and d<21:
     print(f"wygrales twoje karty{c} karty bota {Bot}")
if h<21 and h<d and d>21:
     print(f"przegrales twoje karty{c} karty bota {Bot}")












