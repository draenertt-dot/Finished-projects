import random
#def hallo_unendlich():
 #   print("Hallo")
  #  hallo_unendlich()
# hallo_unendlich()

#def hallo_n(n):
 #   if n == 0:
  #      return
   # print("Hallo")
    #hallo_n(n - 1)
#hallo_n(10)

#def fakultät(n):
 #   if n == 0:
  #      return 1
   # vorgänger = fakultät(n - 1)
    #ergebnis = vorgänger * n
    #return ergebnis 
#print(len(str(fakultät(997))))

# 0! = 1
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# 6! = 720 (= 6 * 5!)
# ...

# Gibt 2 hoch n zurück
def zwei_hoch(n):
    if n == 0:
        return 1
    vorgänger = zwei_hoch(n - 1)
    erg = vorgänger * 2
    return erg
#print(zwei_hoch(10)) # 16

#2 hoch 4 = 2 hoch 3 mal 2

# 2 hoch 0 = 1
# 2 hoch 1 = 2
# 2 hoch 2 = 4
# 2 hoch 3 = 8
# ...
# TODO Auf 15.12.: Fülle die Fragezeichen aus

# Gibt m hoch n zurück
def hoch(basis, exponent):
    if exponent == 0:
        return 1
    vorgänger = hoch(basis, exponent - 1)
    erg = vorgänger * basis
    return erg
#print(hoch(5, 3)) # 125

# Die Fibonacci-Folge lautet:
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 ...
# Gibt die n'te Fibonacci-Zahl zurück
# fibonacci(0) = 0, fibonacci(1) = 1, fibonacci(2) = 1, fibonacci(3) = 2, ...
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    vorgänger = fibonacci(n - 1)
    vorvorgänger = fibonacci(n - 2)
    vv  = vorgänger + vorvorgänger
    return vv
# print(fibonacci(10))


# Gibt die Summe aller Zahlen von 0 bis n zurück
def summe_bis_n(n):
    if n == 0:
        return 0
    m = summe_bis_n(n - 1)
    e = m + n
#    return e

#print(summe_bis_n(10))

def alle_von_n_bis_1(n):
    if n < 1:
        return
    print(n) 
    alle_von_n_bis_1(n - 1)
# alle_von_n_bis_1(10)

# Gibt n Mal die Zahl 1 aus
def n_mal_1(n):
    if n < 1:
        return
    print(1)
    n_mal_1(n - 1)
#n_mal_1(10)

# Gibt alle geraden Zahlen von n bis 0 aus (Annahme: Die Funktion wird nur für gerade n aufgerufen)
def gerade_von_bis_1(n):
    if n < 0:
        return
#    print(n)
    gerade_von_bis_1(n - 2)
gerade_von_bis_1(20)

# Gibt eine Liste zurück, die n Mal die Zahl 1 enthält
def liste_n_mal_1(n):
    if n < 1:
        return []
    erg = liste_n_mal_1(n - 1)
    erg.append(n)
    return erg
r = liste_n_mal_1(10)
#print(r)

# Gibt eine Liste zurück, die n Zufallszahlen zwischen 1 und 100 enthält
def liste_n_mal_zufallszahl(n):
    if n < 1:
        return []
    er = liste_n_mal_zufallszahl(n - 1)
    z = random.randint(1, 100)
    er.append(z)
    return er
e = liste_n_mal_zufallszahl(100)
#print(e)        

def alle_von_n_bis_1(n):
    if n < 1:
        return
    print(n) 
    alle_von_n_bis_1(n - 1)
# alle_von_n_bis_1(10)

# Gibt alle Zahlen von 1 bis n aus
def eins_bis_n(n):
    if 1 > n:
        return 
    eins_bis_n(n - 1)
    print(n)
#eins_bis_n(10)

# Gibt alle Zahlen von m bis n aus (von klein nach groß)
def m_bis_n_aufsteigend(m, n):
    if m > n:
        return
    print(m)
    m_bis_n_aufsteigend(m + 1, n)
#m_bis_n_aufsteigend(10, 20)

# Gibt alle Zahlen von m bis n aus (von groß nach klein)
def m_bis_n_absteigend(m, n):
    if m < n:
        return
    print(m)
    m_bis_n_absteigend(m - 1, n)
#m_bis_n_absteigend(20, 10)

# Gibt n Zufallszahlen zwischen 1 und 100 aus
def n_zufallszahlen(n):
    if n < 1:
        return

    nz = random.randint(1, 100)
    print(nz)
    n_zufallszahlen(n - 1)

#n_zufallszahlen(10)

# Gibt die Summe von n Zufallszahlen zwischen 1 und 100 zurück
def n_zufallszahlen_summe(n):
    if n < 1:
        return 0
    zwischenergebnis = n_zufallszahlen_summe(n - 1)
    nzz = random.randint(1, 100)
    ergebnis = zwischenergebnis + nzz
    return ergebnis

ny = n_zufallszahlen_summe(10)
# print(ny)

# Gibt die Summe aller Zahlen von m bis n zurück
def summe_m_bis_n(m, n):
    if n < m:
        return 0
    zw = summe_m_bis_n(m, n - 1)

    er = zw + n
    return er

sm = summe_m_bis_n(10, 20)
# print(sm)

# Gibt die Länge der Liste l zurück
def länge(l):
    if l == []:
        return 0
    l.pop(0)
    ze = länge(l)
    erg = ze + 1
    return erg
lä = länge([6, 2, 3, 4, 1, 5])
# print(lä)
liste = [4, 1, 5]
liste.pop(1) # Entfernt das zweite Element (die 1)

# Gibt die Summe aller Zahlen in der Liste l zurück
def summe(l):
    if l == []:
        return 0
    zez = l[0]
    l.pop(0)
    zwe = summe(l)
    erg = zwe + zez
    return erg
    
print(summe([1, 2, 3]))
# Bei länge entfernen wir das erste Element der Liste und rechnen dafür plus 1
# Bei summe entfernen wir das erste Element der Liste und rechnen dafür plus dieses Element
