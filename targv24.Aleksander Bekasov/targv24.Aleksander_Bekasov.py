


from random import *  #*-koik funktsioonid, randit  as rd funktsioonide umbernimetus
import random
from math import * #pi kasutamiseks ulesanne 4
# Ulesanne 1
print("Salam Aleikum!")
nimi = input("Mis on sinu nimi? ") #lower(), upper(), capitalize()
print("Tere tulemast! ", nimi) 

vanus=int(input("Kui vana sa oled? "))

print(f"Tere tulemast! Tervitan sind {nimi} Sa oled {vanus} aastat vana")

# Ulesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))

# Ulesanne 3
kokku=randint(1,1000)
print(f"Kokku on {kokku} kommi")
kommi=int(input(" Mitu kommi sa tahad võtta? "))
kokku=kokku-kommi
print(f"Jääk on {kokku} kommi")

#Ulesanne 4
print("Läbimõõdu leidmine ")
#l-ümbermõõt
l=float(input("Ümbermõõt: "))
d=l/pi
print(f"Läbimõõdu suurus on {d}")

# Ulesanne 5
import math

print("Tere, see programm on ristkülikukujulise maatüki diagonaali arvutamiseks meetrites! Selleks, et seda ära arvutada tuleb sisestada N ja M diagonaali pikkused!")
N=float(input("Sisestage ristküliku laius (N): ").replace(",", "."))
M=float(input("Nüüd sisestage ristküliku pikkus (M): ").replace(",", "."))
diagonaal= math.sqrt(N**2+M**2)
print(f"Ristkülikukujulise diagonaali pikkus on {diagonaal:.2f} meetrit. Äitah, et kasutasite minu programmi! ;)")

# Ulesanne 6
# Vale kood
# Leidke järgnevast näiteprogrammist semantiline viga:
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = aeg / teepikkus
# print("Sinu kiirus oli " + str(kiirus) + " km/h")

# Õige kood
# Leidke järgnevast näiteprogrammist semantiline viga:
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")

# Ulesanne 7

arvud = []
for i in range(5):
    arv = int(input(f"Sisesta {i+1}. täisarv: "))
    arvud.append(arv)

keskmine = sum(arvud) / len(arvud)

print("Aritmeetiline keskmine on:", keskmine)


# Ulesanne 8 

print("   @..@   ")
print("  (----)  ")
print(" ( \\__/ ) ")
print("^^  \"\"  ^^")

# Ulesanne 9 

a = int(input("Sisesta a pikkus: "))
b = int(input("Sisesta b pikkus: "))
c = int(input("Sisesta c pikkus: "))

P = a + b + c

print("Kolmnurga ümbermõõt on:", P)

# Ulesanne 10

pitsaPrice = 12.90
jootrahaprotsent = 10 / 100  
jootraha = pitsaPrice * jootrahaprotsent
kogusumma = pitsaPrice + jootraha
maksud = kogusumma / 2  
print(f"Igaüks peab maksma: {maksud:.2f}€")

