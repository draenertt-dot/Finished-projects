class Tier:
    def __init__(self, art: str, alter: int, gewicht: float, fleischfressend: bool, lebensraum: str) -> None:
        self.art = art
        self.alter = alter
        self.gewicht = gewicht
        self.fleischfressend = fleischfressend
        self.lebensraum = lebensraum
    
    # Gib eine kompakte String-Darstellung des Tieres zurück
    def __repr__(self) -> str:
        return f"Tier | Tierart: {self.art}, Alter: {self.alter} Jahre, Gewicht: {self.gewicht}kg"

    # Lässt das Tier um ein Jahr altern und gibt das neue Alter zurück
    def geburtstag(self) -> int:
      self.alter = self.alter + 1
      return self.alter

    # Füttert das Tier mit dem übergebenen Futtergewicht. Das Tier nimmt um die Hälfte dessen an Gewicht zu. Das neue Gewicht wird zurückgegeben.
    def füttern(self, futtergewicht: float) -> float:
        futtergewicht = futtergewicht / 2

        self.gewicht = self.gewicht + futtergewicht
        return self.gewicht

    # Frisst das übergebene Tier. Das Tier nimmt um 10% des Gewichts des gefressenen Tiers zu. Das neue Gewicht wird zurückgegeben.
    def fressen(self, tier: "Tier") -> float:
        self.gewicht = self.gewicht + tier.gewicht / 10
        return self.gewicht

    # Das Tier rennt für die übergebene Dauer (Anzahl von Minuten). Jede Minute nimmt es um 1% ab.
    # Hinweis: Eine Schleife könnte helfen.
    def rennen(self, dauer: int) -> float:
        while dauer > 0:
            self.gewicht = self.gewicht - self.gewicht / 100
            dauer = dauer - 1
        return self.gewicht


class Zoo:
    def __init__(self, tiere: list, eintrittspreis: float, adresse: str, gründungsjahr: int, offen: bool) -> None:
        self.tiere = tiere
        self.eintrittspreis = eintrittspreis
        self.adresse = adresse
        self.gründungsjahr = gründungsjahr
        self.offen = offen
    
    # Der Zoo nimmt das übergebene Tier auf
    def hinzufügen(self, tier: Tier) -> None:
        self.tiere.append(tier)

    # Gibt die Anzahl der im Zoo lebenden Tiere zurück
    def anzahl_tiere(self) -> int:
        return len(self.tiere)

    # Gibt zurück, wie viel Eintrittspreis pro Tier man bezahlt
    def eintrittspreis_pro_tier(self) -> float:
       self.eintrittspreis = self.eintrittspreis / len(self.tiere)
       return self.eintrittspreis

    # Gibt zurück, wie viele Tiere im Zoo mehr als 100kg wiegen
    def anzahl_mehr_als_100kg(self):
        anzahl = 0
        index = 0
        while len(self.tiere) > index:
            if self.tiere[index].gewicht >  100:
                anzahl = anzahl + 1
            index = index + 1
        return anzahl

    # Gibt das Durchschnittsgewicht aller Tiere im Zoo zurück
    def durchschnittsgewicht(self):
        gg = 0
        index = 0
        while len(self.tiere) > index:
            gg = gg  + self.tiere[index].gewicht
            index = index + 1
        gg = gg / len(self.tiere)
        return gg

    # Gibt das maximale unter allen Tieren im Zoo vorkommende Gewicht zurück
    def maximalgewicht(self):
        index = 0
        maxt = self.tiere[index].gewicht
        while len(self.tiere) > index:
            if maxt < self.tiere[index].gewicht:
                maxt = self.tiere[index].gewicht
            index = index + 1
        return maxt

        

# TODO
# 27.04.: Projekt
        

        


tier1 = Tier("Elefant", 37, 6000.0, False, "Savanne")
print(tier1)

tier2 = Tier("Kamel", 23, 480.0, False, "Wüste")
print(tier2)

tier3 = Tier("Löwe", 34, 186.0, True, "Savanne")
print(tier3)

tier4 = Tier("Wolf", 19, 80.0, True, "Wald")
print(tier4)

tier5 = Tier("Adler", 28, 6.3, True, "Berge")
print(tier5)

tier5.geburtstag()
print(tier5)

tier4.füttern(10.0)
print(tier4)

tier3.fressen(tier5)
print(tier3)

zoo = Zoo([tier1, tier2, tier3, tier4, tier5], 15.0, "Waldperlach", 1990, True)
print(zoo.anzahl_mehr_als_100kg())
print(zoo.durchschnittsgewicht())
print(zoo.maximalgewicht())

