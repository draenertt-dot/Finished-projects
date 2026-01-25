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