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