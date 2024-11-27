# Ulesanne 1
# Kirjuta programm, mis sind tervitab ja kuvab ekraanile tänane kuupäev moduli datetime kasutades ja date.today() funktsiooni abil.
from datetime import *
import math
from calendar import *

tana=date.today().strftime("%B, %d, %Y")

print(f"Tere!, Täna on {tana}")

d=date.today().day

print(d)




# Ulesanne 2 

# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# +Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

a=int( 3 + 8 / (4 - 2) * 4)
b=int( (3 + 8) / 4 - 2 * 4)
c=int( 3 + 8 / 4 - 2 * 4)
d=int( (3 + 8) / (4 - 2) * 4)
print(a)
print(b)
print(c)
print(d)

# Funktsioonid day(), month(), year() kasutatakse päeva, kuu ja aasta parameetri leidmiseks date klassist.
# Arvuta mitu päeva on jäänud kuu lõppuni, aasta lõppuni.

paevadekogus=monthrange(2024,11)[1] # calendar modulist
print(paevadekogus)

detsP=monthrange(2024,12)[1] #31
novP=monthrange(2024,11)[1] #30
jaak=detsP+novP-d
jaak2=novP-d
print(f"Aasta lõppuni on {jaak}")
print(f"Kuu lõppuni on {jaak2}")


# Ülesanne 3
# Ruudu sees asub ring. Ringi raadius on R.
# Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.


r=float(input("Sisesta palun raadius r: "))

# Ruudu pindala
A_ruut = 2 * r**2

# Ruudu ümbermõõt
U_ruut = 4 * r * math.sqrt(2)

# Ringi pindala
A_ring = math.pi * r**2

# Ringi ümbermõõt
U_ring = 2 * math.pi * r

print(f"Ruudu pindala: {A_ruut:.2f}") #2f = 2 decimal places
print(f"Ruudu ümbermõõt: {U_ruut:.2f}")
print(f"Ringi pindala: {A_ring:.2f}")
print(f"Ringi ümbermõõt: {U_ring:.2f}")

# Ülesanne 4
# Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu
#  kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. Kasuta teadmist, et Maa raadius ekvaatori kohal on 6378 km. 

d=2.575 # mundi diameeter cm
maa=6378 #maa radius km
maa*=100000 # maa raadius in cm
Labimootmaa=2*math.pi*maa
kogus=int(Labimootmaa/d)
print(f"On vaja {kogus} mündi. \nMeil on vaja {kogus*2} eur")

# Ülesanne 5
# Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:
# kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll
# kill-koll

