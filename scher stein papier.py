import random

print("herzlich wilkommen zu schere stein papier")
nochmal="ja"
spielerpunkte = 0
computerpunkte = 0
while  nochmal == "ja":
    gegenstände = ["schere", "stein", "papier"]
    computerwahl = random.choice(gegenstände)
    spielerwahl=input("wählst du schere, stein oder papier ")
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

if  computerpunkte < spielerpunkte:
    print("gewonnen")

if computerpunkte > spielerpunkte:
    print("verloren")  

if computerpunkte == spielerpunkte:
    print("unentschieden")