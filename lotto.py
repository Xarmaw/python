import random
bulll=["sam wybiore,wylosuj"]
gracza=[61,62,63,654,65,66]
botwybor=gracza
liczby=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
wybor=(input("czy chcesz sam wybrac liczby czy wylosować "))
w=0
x=0
p=0
if wybor=="sam wybiore":
     for i in range(1,6):
        
        wyborgracz=0
        

        while wyborgracz==gracza[0]:
             print("oto twoje liczby",gracza)
             wyborgracz=int(input("liczba która wybrales jest taka sama jak wybierz inna"))
        
        while wyborgracz==gracza[1]:
             print("oto twoje liczby",gracza)
             wyborgracz=int(input("liczba która wybrales jest taka sama jak wybierz inna"))
        
        while wyborgracz==gracza[2]:
             print("oto twoje liczby",gracza)
             wyborgracz=int(input("liczba która wybrales jest taka sama jak wybierz inna"))
        
        while wyborgracz==gracza[3]:
             print("oto twoje liczby",gracza)
             wyborgracz=int(input("liczba która wybrales jest taka sama jak wybierz inna"))
        
        while wyborgracz==gracza[4]:
             print("oto twoje liczby",gracza)
             wyborgracz=int(input("liczba która wybrales jest taka sama jak wybierz inna"))
        
        while wyborgracz==gracza[5]:
             print("oto twoje liczby",gracza)
             wyborgracz=int(input("liczba która wybrales jest taka sama jak wybierz inna"))
        
        wyborgracz=int(input("wybierz liczbe"))
        gracza[x]=wyborgracz
        while wyborgracz not in liczby:
             wyborgracz=int(input("mozesz wybirac liczby od 1 do 60"))
        x=x+1
        

elif wybor=="wylosuj":
    for i in range(0,6):
        
        botwybor=random.choice(liczby)
        gracza[p]=botwybor
        
        while gracza[p] in gracza:
              botwybor=random.choice(liczby)
        p=p+1




wygrane=[]
for i in range(0,6):
        wygran=random.choice(liczby)
        wygrane.append(wygran)

print(wygrane)        
print(gracza)
z=0
for i in range(1,6):
        if wygrane[0]==gracza[z]:
                w=w+1
                z=z+1
z=0
for i in range(1,6):
        if wygrane[1]==gracza[z]:
                w=w+1
                z=z+1
z=0
for i in range(1,6):
        if wygrane[2]==gracza[z]:
                w=w+1
                z=z+1
z=0
for i in range(1,6):
        if wygrane[3]==gracza[z]:
                w=w+1
                z=z+1
z=0
for i in range(1,6):
        if wygrane[4]==gracza[z]:
                w=w+1
                z=z+1
z=0
for i in range(1,6):
        if wygrane[5]==gracza[z]:
                w=w+1
                z=z+1

print(w)














