def sortieren1(liste):
    liste_sortiert = []
    index1 = 0
    länge1 = len(liste)
    while index1 < länge1:
        index = 0
        länge = len(liste)
        kleinstezahl = liste[0]
        while index < länge:
            if liste[index] < kleinstezahl:
                kleinstezahl = liste[index]
            index = index + 1
        liste.remove(kleinstezahl)
        liste_sortiert.append(kleinstezahl)
        index1 = index1 + 1
    return liste_sortiert
s1 = sortieren1([2, 8, 3, 5, 9, 4])
#print(s1)

def sortieren2(liste):
    index = 0
    länge = len(liste)
    ls2 = []
    kzl = 0
    while index < länge:
        index1 = 0
        länge1 = len(ls2)
        kzl = liste[index]
        index = index + 1
        while index1 < länge1 and kzl > ls2[index1]:
          
          index1 = index1 + 1
        ls2.insert(index1, kzl)
    return ls2
s2 = sortieren2([4, 4, 9, 0, 5])
#print(s2)



# TODO Hausaufgabe auf 6.10.:
# Erstelle eine Liste von 10.000 Zufallszahlen zwischen 1 und 100.000



import random



def zufallszahlen():
  zufallsliste = []
  index = 0
  while index < 100:
      zz = random.randint(1, 100)
      zufallsliste.append(zz)
      index = index + 1
  return zufallsliste
zt = zufallszahlen()
#print(zt)

# TODO Hausaufgabe auf 13. Oktober
# Gibt True zurück, falls liste aufsteigend sortiert ist, ansonsten False
#def sortiert(liste: list) -> bool:
 # index = 0
  #länge = len(liste)
  #while index < länge - 1:
   # if liste[index] > liste[index + 1]: 
    #  return False
    #index = index + 1
  #return True
#s = sortiert([1, 4, 8, 9, 9999]) 
#print(s)



def sortiert(liste: list) -> bool:
  index = 0
  länge = len(liste)
  while index < länge - 1:
    if liste[index] > liste[index + 1]:
      return False
    index = index + 1
  return True
s = sortiert([9, 8, 7, 1]) 
# print(s)

import random
from random import choice
def mischen( liste: list) -> list:
  index = 0
  länge = len(liste)
  liste_gemischt = []
  while index < länge:
    zz = choice(liste)
    choice(liste)
    liste_gemischt.append(zz)
    liste.remove(zz)
    index = index + 1
  return liste_gemischt
m = mischen([2, 5, 1, 4, 9, 2, 8])
#print(m)
#TODO am 20.10. hier weiter

def mehrmalsmischen(liste: list) -> list:
  while True:
    liste = mischen(liste)
    if sortiert(liste) == True:
      return liste
#print(mehrmalsmischen([9, 8, 7, 6, 5, 4, 3, 2, 1]))

# TODO Nächsten Sortieralgorithmus

def benachbarte_elemente(liste):
  index = 0
  länge = len(liste)
  tr = True
  while tr :
    index = 0
    while index < länge - 1:
      zahl = liste[index]
      nachfolger = liste[index + 1]
      if  zahl > nachfolger:
        liste[index + 1] = zahl
        liste[index] = nachfolger
      index = index + 1
    if sortiert(liste):
      tr = False
  return liste
be = benachbarte_elemente([2, 3, 4, 5])
#print(be)
# TODO Für 10. November: benachbarte_elemente fertigstellen

# TODO Benchmarking 17. 11.
# TODO Am 1.12. hier weiter
import time

zz = zufallszahlen()
index = 0
zz1 = []
while index < len(zz):
  zz1.append(zz[index])
  index = index + 1
index = 0
zz2 = []
while index < len(zz):
  zz2.append(zz[index])
  index = index + 1
tt = time.time()
sortieren2(zz)
tt2 = time.time()
dauer = tt2 - tt
print(dauer)
tt = time.time()
sortieren1(zz1)
tt2 = time.time()
daue = tt2 - tt
print(daue)
tt = time.time()
benachbarte_elemente(zz2)
tt2 = time.time()
dau = tt2 - tt
print(dau)









