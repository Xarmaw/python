import random
i=int(input("ile razy chcesz zagrac"))

wybory=["kamien","papier","papier"]

for z in range(0,i):
    a=str(input("wybierz kamien papier czy nozyce"))
    while a not in wybory:
        a=str(input("nieprawidlowy wybor - wybierz jeszcze raz"))
    komputer=random.choice(wybory)
    if komputer=="kamien" and a=="kamien":
        print("remis")
        break
    
    elif komputer=="kamien" and a=="papier":
        print("wygrales papier bije kamien")
        break
    
    elif komputer=="kamien" and a=="nozyce":
         print("przegrales kamien bije nozyce")
         break
    
    elif komputer=="papier" and a=="kamien":
        print("przegrales papier bije kamien")
    
    elif komputer=="papier" and a=="papier":
        print("remis")
    
    elif komputer=="papier" and a=="nozyce":
        print("wygrales nozyce bija papier")
    
    elif komputer=="nozyce" and a=="kamien":
        print("wygrales kamien bije nozyce")
    
    elif komputer=="nozyce" and a=="papier":
        print("przegrales nozyce bija papier")
    
    elif komputer=="nozyce" and a=="nozyce":
        print("remis")
        break


























































































































































































