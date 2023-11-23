'''
print("hello world")
a=10
b=10.5
print(a)
print('%.20f'%b)
tekst1='ala ma kota'
tekst2="Ala ma kota"
print("Wartosc zmiennej a wynosi: ",a)
print("Wartosc zmiennej a wynosi: %.2f" %a)
#print(f"Wartosc zmiennej a wynosi:{a}")
print("Wartosc zmiennej a wynosi: ",str (a))
imie=input("wprowadz imie")
print("czesc",imie)
wiek=int(input("ile masz lat?"))
print(wiek)
sume=1+1
roznica=2-1
iloczyn=3*8
iloraz=20/4
modulo=4%2
potega=2**3
if a >0:
    print("liczba a jest wieksza od 0")
elif a==0:
    print("liczba jest rowna 0")
else:
    print("Liczba jest mniejsza od 0")

if a>0:
    print("liczba jest wieksza od 0")
elif a==0:
    print("liczba jest rowna 0")
else:
    print("liczba jest nieparzysta") 
'''
'''
for i in range(3):
    print(i)
for i in range(100):
    print(i)
for i in range(1,100):
    print(i)
for i in range(1, 100, 2):
    print(i)
for i in range(100, 0 -1):
    print(i)

for i in range(1, 101):
    if i%2==0:
        print("liczba jest parzysta")
    else: 
        print("liczba jest nie parzysta")

for i in range(6):
    print(random,randint(1,100))
for i in "string":
    if 1=="r":
        break
    print(i)
while a>0:
    print("liczba",a,"jest wieksza od 0")
    a-=1

#while True:
    #print("to zawsze prawda")
liczba=int(input("podaj liczbe:"))
while liczba<=0:
    liczba=int(input("Podaj liczbe jeszcze raz:"))
def powitanie():
    print("Czesc")
powitanie()
def powitanie_imienne(imie):
    print("czesc",imie)
powitanie_imienne()
def dzielenie(dzielna, dzielnik):
    if dzielnik ==0:
        return "blad"
    else:
        return dzielna/dzielnik
print(dzielenie(4,2))
x=dzielenie(4,2)
print(x)

#listy
lista=[7,18,67,92,32]
print(lista)
#print(*lista) #pisze liste bez nawiasu
#print(*lista, sep=";") 
lista.sort()
print(lista)
lista.reverse()
print(lista)


lista.append(123)

lista[0]=32
print(lista)

lista.sort()
print(lista)

print(lista.count(32))
print(len(lista))

lista.remove(32)
print(lista)

tupla=(1,2,3) 
#lista do ktorej nic nie da sie dodac
a=(1)
b=(2,)
print(type(a))
print(type(b))

print(len(tupla))
#print(tupla[0.4]) #nie mozna dac floata musi byc int
print(tupla[0])
print(tupla[-2])


t=(1,2,3,4,5,6,7,8,9)
i=3
print(t[i:6])
print(t[3:])
print(t[:4])
#del tupla 
#del lista del usuwa liste lub tuple
krotka=(1,2,3)
p,o,l=krotka
print(p)
print(o)
print(l)



kontakty={
    "Jan":123456789,
    "Jacek":234567890,
    "Janusz":345678901
}

print(kontakty["Janusz"])
for imie, numer in kontakty.items():
    print("%s ma numer telefonu: %d"%(imie,numer))

print(kontakty.keys())
print(kontakty.values())

zbior={1,2,3,4}

'''

f=open("text.txt", "r")
print(f.read())
f.close()

f=open("text.txt", "a")
f.write("gzz")
f.close

f=open("text.txt", "a")
f.writre("ggg\n")
f.close()

f=open("text.txt", "r")


for i in f:
    print(i)

f.close







