a=float(input("podaj pierwsza liczbe"))
b=float(input("podaj druga liczba liczbe"))
c=input("jakie dzialanie chcesz wykonac")


if c=="dzielenie":
    while b ==0:
        print("nie dziel przez zero")
        b=float(input("wprowadz jeszcze raz druga liczba"))
    else:
        print(a/b)
if c==("mnozenie"):
    print(a*b)
if c==("dodawanie"):
    print(a+b)

if c==("odejmowanie"):
    print(a-b)

if c==("potegowanie"):
    print(a**b)

if c==("modulo"):
    while b ==0:
            print("nie dziel przez zero")
            b=float(input("wprowadz jeszcze raz druga liczba"))
    else:
            print(a%b)






