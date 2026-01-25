###########################################################
################### Schere Stein Papier ###################
###########################################################

import random

print("herzlich wilkommen zu schere stein papier")
nochmal = "ja"
spielerpunkte = 0
computerpunkte = 0
while nochmal == "ja":
    gegenstände = ["schere", "stein", "papier"]
    computerwahl = random.choice(gegenstände)
    spielerwahl = input("wählst du schere, stein oder papier ")
    if computerwahl=="schere" and spielerwahl=="schere":
        print("computer wählt schere: unentschieden")
    

    if computerwahl=="schere" and spielerwahl=="stein":
        print("computer wählt schere: gewonnen")
        spielerpunkte = spielerpunkte+1
       

    if computerwahl=="schere" and spielerwahl=="papier":
        print("computer wählt schere: verloren")
        computerpunkte = computerpunkte+1
        nochmal = input("möchtest du nocheinmal spielen?")

    if computerwahl=="stein" and spielerwahl=="schere":
        print("computer wählt stein: verloren")
        computerpunkte = computerpunkte+1
        nochmal = input("möchtest du nocheinmal spielen?")

    if computerwahl=="papier" and spielerwahl=="schere":
        print("computer wählt papier: gewonnen")
        spielerpunkte = spielerpunkte+1

    if computerwahl=="stein" and spielerwahl=="stein":
        print("computer wählt stein: unentschieden")

    if computerwahl=="papier" and spielerwahl=="papier":
        print("computer wählt papier: unentschieden")
    

    if computerwahl=="stein" and spielerwahl=="papier":
        print("computer wählt stein: gewonnen") 
        spielerpunkte = spielerpunkte+1
    
    if computerwahl=="papier" and spielerwahl=="stein":
        print("compter wählt papier: verloren")
        computerpunkte = computerpunkte+1
        nochmal = input("möchtest du nocheinmal spielen?")

    print("computerpunkte " + str(computerpunkte) + " spielerpunkte " + str(spielerpunkte))

if computerpunkte < spielerpunkte:
    print("gewonnen")

if computerpunkte > spielerpunkte:
    print("verloren")  

if computerpunkte == spielerpunkte:
    print("unentschieden")






###########################################################
##################### Zahlensuchspiel #####################
###########################################################

zettel = -1
while zettel != 10:
    zettel = input("wie alt bin ich")
    zettel = int(zettel)
    print (zettel)

    if zettel == 10:
        print("richtig")
    if zettel < 10:
        print("größer")
    if zettel > 10:
        print("kleiner")
    if zettel >20 or zettel <0:
        print("kalt")
    if zettel <=20 and zettel >=0 and zettel!=10:
        print("warm")


        



###########################################################
####################### Tic Tac Toe #######################
###########################################################

def ausgabe(spielfeld):
    reihe1 = spielfeld[0] + " | " + spielfeld[1] + " | " + spielfeld[2]
    reihe2 = spielfeld[3] + " | " + spielfeld[4] + " | " + spielfeld[5]
    reihe3 = spielfeld[6]+ " | " + spielfeld[7] + " | " + spielfeld[8]
    trennreihe = "---------" 
    print(reihe1)
    print(trennreihe)
    print(reihe2)
    print(trennreihe)
    print(reihe3)


nochmal = "ja"
spielerpunkte = [0, 0]
while  nochmal == "ja" or nochmal == "Ja":

    print ("punkte spieler 1: " + str(spielerpunkte[0]) + " punkte spieler 2: " + str(spielerpunkte[1]) )

    spielfeld = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    spieler = 1

    while True:
        if spieler == 1:
            symbol = "X"
        else:
            symbol = "O"

        ausgabe(spielfeld)
        zeichen = input("Spieler " + str(spieler) + " wählst du feld1 feld2 feld3 feld4 feld5 feld6 feld7 feld8 oder feld9? ")
        if spielfeld[int(zeichen) - 1] == zeichen:
            spielfeld[int(zeichen) - 1] = symbol
                
        if spielfeld[0] == symbol and spielfeld[1] == symbol and spielfeld[2] == symbol:
            ausgabe(spielfeld)
            print ("spieler " + str(spieler) + " glückwunsch du hast gewonnen ")
            spielerpunkte[spieler - 1] += 1
            break
        if spielfeld[3] == symbol and spielfeld[4] == symbol and spielfeld[5] == symbol:
            ausgabe(spielfeld)
            print ("spieler " + str(spieler) + " glückwunsch du hast gewonnen ")
            spielerpunkte[spieler - 1] += 1
            break
        if spielfeld[6] == symbol and spielfeld[7] == symbol and spielfeld[8] == symbol:
            ausgabe(spielfeld)
            print ("spieler " + str(spieler) + " glückwunsch du hast gewonnen ")
            spielerpunkte[spieler - 1] += 1
            break
        if spielfeld[2] == symbol and spielfeld[5] == symbol and spielfeld[8] == symbol:
            ausgabe(spielfeld)
            print ("spieler " + str(spieler) + " glückwunsch du hast gewonnen ")
            spielerpunkte[spieler - 1] += 1
            break
        if spielfeld[1] == symbol and spielfeld[4] == symbol and spielfeld[7] == symbol:
            ausgabe(spielfeld)
            print ("spieler " + str(spieler) + " glückwunsch du hast gewonnen ")
            spielerpunkte[spieler - 1] += 1
            break
        if spielfeld[0] == symbol and spielfeld[3] == symbol and spielfeld[6] == symbol:
            ausgabe(spielfeld)
            print ("spieler " + str(spieler) + " glückwunsch du hast gewonnen ")
            spielerpunkte[spieler - 1] += 1
            break
        if spielfeld[0] == symbol and spielfeld[4] == symbol and spielfeld[8] == symbol:
            ausgabe(spielfeld)
            print ("spieler " + str(spieler) + " glückwunsch du hast gewonnen ")
            spielerpunkte[spieler - 1] += 1
            break
        if spielfeld[2] == symbol and spielfeld[4] == symbol and spielfeld[6] == symbol:
            ausgabe(spielfeld)
            print ("spieler " + str(spieler) + " glückwunsch du hast gewonnen ")
            spielerpunkte[spieler - 1] += 1
            break

        if spieler == 1:
            spieler = 2
        else:
            spieler = 1
        if spielfeld[0] != "1" and spielfeld[1] != "2" and spielfeld[2] != "3" and spielfeld[3] != "4" and spielfeld[4] != "5" and spielfeld[5] != "6" and spielfeld[6] != "7" and spielfeld[7] != "8" and spielfeld[8] != "9"  :
            print ("unentschieden") 
            break
        
    print ("punkte spieler 1: " + str(spielerpunkte[0]) + " punkte spieler 2: " + str(spielerpunkte[1]) )

    nochmal = input("Möchtest du noch einmal spielen? ")

    




###########################################################
####################### Funktionen ########################
###########################################################

import random


def funktion4(zahl):
    if 0 > zahl:
        print("nicht positiv")
    else:
        print("positiv")
# funktion4(2)

def funktion5(zahl1 , zahl2):
    if zahl1 == zahl2:
        print("gleich")
    else:
        print("nicht gleich")
# funktion5(5, 3)

def funktion6(zahl1 , zahl2):
    if zahl1 < zahl2:
        print(zahl2)
    else:
        print(zahl1)
# funktion6(1221331 , 2001)

def funktion7(zahl1 , zahl2 , zahl3):
    print(zahl1 * zahl2 * zahl3)
# funktion7(2, 3, 4)

def funktion8():
    t = random.randint(1, 100)
    return t 
f8 = funktion8()
# print(f8)

def funktion9(zahl3 , zahl4):
    if zahl3 < zahl4:
        return zahl4
    else:
        return zahl3

def funktion10(zahl5 , zahl6 , zahl7):
    if  zahl6 <= zahl7 and zahl5 <= zahl7 :
       return zahl7
    elif zahl5 >= zahl6  and zahl5 >= zahl7:
       return zahl5
    else:
       return zahl6
f10 = funktion10(20, 20, 3)
# print(f10)

def funktion11(liste):
    index = 0
    länge = len(liste)
    größte_zahl = liste[0]
    while index < länge:
       if liste[index] > größte_zahl:
           größte_zahl = liste[index]
       index = index + 1
    return größte_zahl
f11 = funktion11([0, 0, 0, 0, 0, 1]) 
# print(f11)

def funktion12(liste):
    index = 0
    länge = len(liste)
    kleinste_zahl = liste[0]
    while index < länge:
        if liste[index] < kleinste_zahl:
            kleinste_zahl = liste[index]
        index = index + 1
    return kleinste_zahl
f12 = funktion12([3, 7, 2, 5, 2, 1]) 
# print(f12)

def zweitkleinste_zahl(liste):
    index = 0
    länge = len(liste)
    kleinste_zahl = liste[0]
    while index < länge:
       if liste[index] < kleinste_zahl:
           kleinste_zahl = liste[index]
       index = index + 1
    liste.remove(kleinste_zahl)
    index = 0
    länge = len(liste)
    kleinste_zahl = liste[0]
    while index < länge:
       if liste[index] < kleinste_zahl:
           kleinste_zahl = liste[index]
       index = index + 1
    return kleinste_zahl
zwz = zweitkleinste_zahl([33453, 72342, 2342, 5322, 22453, 241])
# print(zwz)  

def zweitkleinste_zahl2(liste):
    index = 0
    länge = len(liste)
    if liste[0] < liste[1]:
       zweitklinste_zahl = liste[1]
       kleinste_zahl = liste[0]
    else:
       kleinste_zahl = liste[1]
       zweitklinste_zahl = liste[0]
    while index < länge :
        if liste[index] < kleinste_zahl and liste[index] < zweitklinste_zahl:
           zweitklinste_zahl = kleinste_zahl
           kleinste_zahl = liste[index]
        if liste[index] > kleinste_zahl and liste[index] < zweitklinste_zahl:
           zweitklinste_zahl = liste[index]
        index = index + 1
    return zweitklinste_zahl
zwz2 = zweitkleinste_zahl2([4, 5, 2, 3, 7])
# print(zwz2)

def zweitgrößte_zahl(liste):
    index = 0
    länge = len(liste)
    if  liste[0] > liste[1]:
       zweitgröste_zahl = liste[1]
       gröste_zahl = liste[0]
    else:
       gröste_zahl = liste[1]
       zweitgröste_zahl = liste[0]
    while index < länge :
        if liste[index] > gröste_zahl and liste[index] > zweitgröste_zahl:
           zweitgröste_zahl = gröste_zahl
           gröste_zahl = liste[index]
        if liste[index] < gröste_zahl and liste[index] > zweitgröste_zahl:
           zweitgröste_zahl = liste[index]
        index = index + 1
    return zweitgröste_zahl
zwg2 = zweitgrößte_zahl([4, 5, 2, 3, 7])
# print(zwg2)

def ergebnis(liste):
    index = 0
    länge = len(liste)
    summe = 0
    while index < länge :
       summe = summe + liste[index]
       index = index + 1
    return summe
su = ergebnis([5, 1, 4, 2])
# print(su)

def multi(liste):
    index = 0
    länge = len(liste)
    mult = 1
    while index < länge:
        mult = mult  * liste[index]
        index = index + 1
    return mult
mu = multi([3, 4, 5, 3])
# print(mu)

def pos(liste):
    index = 0 
    länge = len(liste)
    po = 0
    while index < länge:
        if 0 < liste[index]:
            po = po + liste[index]
        index = index + 1
    return po
p = pos([3, 0, -1, -2, 5])
# print(p)

def lis(liste, grenze):
    index = 0
    länge = len(liste)
    li = 0
    while index < länge:
        if grenze < liste[index]:
            li = li + liste[index]
        index = index + 1
    return li
l = lis([3, 5, 5, 1, 8, 3], 9)
# print(l)

def lou(liste, oberregrenze, unteregrenze):
    index = 0
    länge = len(liste)
    lo = 0
    while index < länge:
        if oberregrenze > liste[index] and unteregrenze < liste[index]:
            lo = lo + liste[index]
        index = index + 1
    return lo
o = lou([3, 3, 4, 3, 4, 7, 8, 3], 2, 6)
# print(o)

def gren(liste, grenze):
    index = 0
    länge = len(liste)
    gre = 0

    while index < länge:
        if grenze < liste[index]:
           gre = gre + 1 
        index = index + 1
    return gre
gr = gren([3, 7, 4, 4, 45, 9], 0)
# print(gr)

# Eine Funktion, die zwei gleich lange listen von zahlen bekommt und eine liste zurrück gibt, deren i-ter Eintrag die summe des i-ten Eintrags der Ersten Liste sowie der zweiten liste ist
def parl(liste1, liste2):
    index = 0
    länge = len(liste1)
    par = 0
    while index < länge:
       par = par + 1
       index = index + 1
    erg = par
    index = 0
    länge = len(liste2)
    par = 0
    while index < länge :
       par = par + 1
       index = index + 1
    er = par
    erg = erg + er
    return erg
e = parl([3, 5 , 4 , 83 , 3], [2 , 5 , 3 , 8])
# print(e)

def summe(liste1: list, liste2: list) -> list:
    liste = []
  
    i = 0
    while i < len(liste1):
       liste.append(liste1[i] + liste2[i])
       print(liste)
       i = i + 1
    return liste
# print(summe([3, 2, 6, 7, 8], [2, 1, 6, 8, 3]))

def  _1_bis_100()-> list:
   liste = []
   i = 1
   while i <= 100:
       liste.append(i)
       i = i + 1
   return liste
# print(_1_bis_100())

def _1_obere_grenze(oberegrenze: int) -> list:
    liste = []
    i = 1
    while i <= oberegrenze:
       liste.append(i)
       i = i + 1
    return liste
# print(_1_obere_grenze(10))

def _unteregrenze_bis_oberegrenze(unteregrenze: int, oberegrenze: int) -> list:
    liste = []
    i = unteregrenze
    while i <= oberegrenze:
       liste.append(i)
       i = i + 1
    return liste
#print(_unteregrenze_bis_oberegrenze(100, 1000))

def flexieblegrenze_grenzen(grenze1: int, grenze2: int) -> list:
    liste = []
    if grenze1 < grenze2 :
       i = grenze1
       o = grenze2
    else :
       i = grenze2
       o = grenze1
    while i <= o :
       liste.append(i)
       i = i + 1 
    return liste
# print(flexieblegrenze_grenzen(1000, 200))

def flexieblegrenze_grenze(grenze1: int = 400, grenze2: int = 3000, schrittweite: int = 100) -> list:
    liste = []
    s = schrittweite
    if grenze1 < grenze2:
       i = grenze1
       o = grenze2
    else:
       i = grenze2
       o = grenze1
    while i <= o:
       liste.append(i)
       i = i + s
    return liste
print(flexieblegrenze_grenze())

def summe(liste:  list, liste2: list) -> int:
    index = 0
    länge = len(liste)
    sum = 0
    while index < länge:
        sum = sum + liste[index] 
        index = index + 1
    index = 0
    länge = len(liste2)
    while index < länge:
        sum = sum + liste2[index]
        index = index + 1
    return sum
# print(summe([3, 4, 9, 9], [4, 8, 4, 2]))

def eineliste(liste):
  index = 0
  länge = len(liste)
  list = 0
  while index < länge :
   if liste[index] == 0 :
     list = list + 1
   index = index + 1
  return list
# print(eineliste([0, 0, 0, 0, 0]))

def liste(liste):
  länge = len(liste)
  index2 = 0
  while index2 < länge:
    index = 0
  länge = len(liste)
  spich = 0
  index2 = index2 + 1
  while index + 1 < länge  :
     if liste[index] > liste[index + 1] :
       spich = liste[index + 1]
       liste[index + 1] = liste[index] 
       liste[index] = spich
     print(liste)
     index = index + 1
  return liste
# print(liste([3, 6, 1, 8, 2, 0]))

# Gibt eine liste zurrük die alle zahlen wie die übergebene liste enthält bis auf zu_löschende_zahlen (Tipp: Schleife und liste.append(...))
def zahl_löschen(liste, zu_löschende_zahl):
 index = 0
 länge = len(liste)
 neue_liste = []
 while index < länge :
  if liste[index] != zu_löschende_zahl:
   neue_liste.append(liste[index]) 
  index = index + 1
 return neue_liste
# print(zahl_löschen([4, 5, 3, 7, 5, 1], 0))

# Gibt zurrück wie oft zahl in liste vorkommt
def anzahl(zahl, liste):
     index = 0
     länge = len(liste)
     zählzahl = 0
     while index < länge:
       if liste[index] == zahl:
         zählzahl = zählzahl + 1
       
       index = index + 1
     return zählzahl
zl = anzahl(49, [4, 9, 9, 9, 2])
# print(zl)

# Bekommt zwei Listen von Zahlen und zählt für jede Zahl aus der ersten Liste, wie oft diese in der zweiten Liste vorkommt
# Die Ergebnisse werden als Liste zurückgegeben
def anzahlen(zahlen, liste):
    index = 0
    länge = len(zahlen)
    ergebnisliste = []
    while index < länge:
       anz = anzahl(zahlen[index], liste)
       ergebnisliste.append(anz)
       index = index + 1
    return ergebnisliste
zl = anzahlen([2, 7], [7, 4, 1, 2, 2, 8, 8, 4]) # [2, 1] 
# print(zl)

# Bekommt zwei Listen von Zahlen und gibt eine der Zahl der ersten Liste zurück, die am häufigsten in der zweiten Liste vorkommen
def häufigste(zahlen, liste):
   anz = anzahlen(zahlen, liste)
   max_index = 0
   index = 0
   while index < len(anz):
       if anz[max_index] < anz[index]:
           max_index = index
       index = index + 1
   return zahlen[max_index]
zl = häufigste([5, 2, 3], [3, 2, 4, 2, 5, 5, 3])
# print(zl)






###########################################################
####################### Kochkurve #########################
###########################################################

from turtle import *

def schneeflocke(stufe, länge):
    if stufe == 0:
        forward(länge)
    else:
        schneeflocke(stufe - 1, länge / 3)
        left(60)
        schneeflocke(stufe - 1, länge / 3)
        right(120)
        schneeflocke(stufe - 1, länge / 3)
        left(60)
        schneeflocke(stufe - 1, länge / 3)

speed(-12)

color("blue", "red")

begin_fill()

schneeflocke(4, 500)
right(120)
schneeflocke(4, 500)
right(120)
schneeflocke(4, 500)

end_fill()

done()






###########################################################
################## Sortieralgorithmen #####################
###########################################################

def selection_sort(liste):
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
s1 = selection_sort([2, 8, 3, 5, 9, 4])
# print(s1)

def insertion_sort(liste):
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
s2 = insertion_sort([4, 4, 9, 0, 5])
# print(s2)

import random

def zufallszahlen():
  zufallsliste = []
  index = 0
  while index < 10000:
      zz = random.randint(1, 10000)
      zufallsliste.append(zz)
      index = index + 1
  return zufallsliste
zt = zufallszahlen()
# print(zt)

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

def bubble_sort(liste):
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
be = bubble_sort([2, 3, 4, 5])
# print(be)

# Wir vergleichen die drei Sortieralgorithmen hinsichtlich ihrer Laufzeit

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
insertion_sort(zz)
tt2 = time.time()
dauer = tt2 - tt
# print("Insertion Sort:", dauer)
tt = time.time()
selection_sort(zz1)
tt2 = time.time()
daue = tt2 - tt
# print("Selection Sort:", daue)
tt = time.time()
bubble_sort(zz2)
tt2 = time.time()
dau = tt2 - tt
# print("Bubble Sort:", dau)