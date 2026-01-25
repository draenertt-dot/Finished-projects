feld1="1"
feld2="2"
feld3="3"
feld4="4"
feld5="5"
feld6="6"
feld7="7"
feld8="8"
feld9="9"

while True:
    reihe1 = feld1 + " | " + feld2 + " | " + feld3
    reihe2 = feld4 + " | " + feld5 + " | " + feld6
    reihe3 = feld7 + " | " + feld8 + " | " + feld9
    trennreihe = "---------" 
    print(reihe1)
    print(trennreihe)
    print(reihe2)
    print(trennreihe)
    print(reihe3)
    zeichen=input("Spieler 1 wählst du feld1 feld2 feld3 feld4 feld5 feld6 feld7 feld8 oder feld9 ?")
    if zeichen == "5" and feld5 == "5":
        feld5 = "X"
    if zeichen == "4" and feld4 == "4":
        feld4 = "X"
    if zeichen == "3" and feld3 == "3":
        feld3 = "X"
    if zeichen == "2" and feld2 == "2":
        feld2 = "X"
    if zeichen == "1" and feld1 == "1":
        feld1 = "X"
    if zeichen == "6" and feld6 == "6":
        feld6 = "X"
    if zeichen == "7" and feld7 == "7":
        feld7 = "X"
    if zeichen == "8" and feld8 == "8":
        feld8 = "X"
    if zeichen == "9" and feld9 == "9":
        feld9 = "X"

    if feld1 == "X" and feld2 == "X" and feld3 == "X":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break

    if feld4 == "X" and feld5 == "X" and feld6 == "X":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break
    if feld7 == "X" and feld8 == "X" and feld9 == "X":
        print ("spieler 1 gückwunsch du hast gewonnen ")

    if feld3 == "X" and feld6 == "X" and feld9 == "X":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break
    if feld1 == "X" and feld4 == "X" and feld7 == "X":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break
    if feld2 == "X" and feld5 == "X" and feld8 == "X":
        print ("spieler 1 gückwunsch du hast gewonnen ")

    if feld1 == "X" and feld5 == "X" and feld9 == "X":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break
    if feld3 == "X" and feld5 == "X" and feld7 == "X":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break



    reihe1 = feld1 + " | " + feld2 + " | " + feld3
    reihe2 = feld4 + " | " + feld5 + " | " + feld6
    reihe3 = feld7 + " | " + feld8 + " | " + feld9
    trennreihe = "---------" 
    print(reihe1)
    print(trennreihe)
    print(reihe2)
    print(trennreihe)
    print(reihe3)
    zeichen=input("Spieler 2 wählst du feld1 feld2 feld3 feld4 feld5 feld6 feld7 feld8 oder feld9 ?")
    if zeichen == "5" and feld5 == "5":
        feld5 = "O"
    if zeichen == "4" and feld4 == "4":
        feld4 = "O"
    if zeichen == "3" and feld3 == "3":
        feld3 = "O"
    if zeichen == "2" and feld2 == "2":
        feld2 = "O"
    if zeichen == "1" and feld1 == "1":
        feld1 = "O"
    if zeichen == "6" and feld6 == "6":
        feld6 = "O"
    if zeichen == "7" and feld7 == "7":
        feld7 = "O"
    if zeichen == "8" and feld8 == "8" :
        feld8 = "O"
    if zeichen == "9" and feld9 == "9":
        feld9 = "O"

    reihe1 = feld1 + " | " + feld2 + " | " + feld3
    reihe2 = feld4 + " | " + feld5 + " | " + feld6
    reihe3 = feld7 + " | " + feld8 + " | " + feld9
    trennreihe = "---------" 

    if feld1 == "O" and feld2 == "O" and feld3 == "O":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break
    if feld4 == "O" and feld5 == "O" and feld6 == "O":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break
    if feld7 == "O" and feld8 == "O" and feld9 == "O":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break
    if feld3 == "O" and feld6 == "O" and feld9 == "O":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break
    if feld1 == "O" and feld4 == "O" and feld7 == "O":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break
    if feld2 == "O" and feld5 == "O" and feld8 == "O":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break
    if feld1 == "O" and feld5 == "O" and feld9 == "O":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break
    if feld3 == "O" and feld5 == "O" and feld7 == "O":
        print ("spieler 1 gückwunsch du hast gewonnen ")
        break

