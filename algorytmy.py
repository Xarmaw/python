'''
n=int(input("podaj liczbe calkowita:"))
suma=0
i=1
while i<=n:
    suma+=i
    i+=1
print(suma)

import time
start=time.time()
end=time.time()
print(start-end)


x=int(input("Wprowadz wartosc dodatnia: "))
if x%2==0:
    print(x/2)
else:
    j=0
    suma2=0
    while j<x:
        suma2=suma2+2*j
        j+=1
    print(suma2)

#zlozonosc O(1) stala nie ma znaczeni co wpiszemy



#zlozonosc O(n) im wiecej tym dluzej
lista=[1,2,3,4,5,6,7,8,9,10]
for i in lista:
    print(i)
'''

import time
start=time.time()
n=int(input("podaj liczbe calkowita"))
for i in range(n):
    for j in range(n):
        print("#",end='')

end=time.time()
print(end-start)




































































