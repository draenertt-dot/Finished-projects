class Suchbaum:
    def __init__(self):
        self.wurzel = None

    def hinzufügen(self,wert):
        if not self.wurzel:
            self.wurzel = Knoten(wert)
        else:
            self.wurzel.hinzufügen(wert)
        
    def graphviz(self):
        if self.wurzel:
            with open("baum.dot", "w") as f:
                f.write("digraph {")
                self.wurzel.graphviz(f)
                f.write("}")

class Knoten:
    def __init__(self,wert):
        self.wert = wert
        self.links = None
        self.rechts = None

    def hinzufügen(self,wert):
        if wert <= self.wert:
            if not self.links:
                self.links = Knoten(wert)
            else: 
                self.links.hinzufügen(wert)
        else: 
            if not self.rechts:
                self.rechts = Knoten(wert)
            else:
                self.rechts.hinzufügen(wert)

    def graphviz(self, f):
        if self.links:
            f.write(str(self.wert) + " -> " + str(self.links.wert) + ";")
            self.links.graphviz(f)
        if self.rechts:
            f.write(str(self.wert) + " -> " + str(self.rechts.wert) + ";")
            self.rechts.graphviz(f)




b = Suchbaum()
b.hinzufügen(50)
b.hinzufügen(20)
b.hinzufügen(80)
b.hinzufügen(60)
b.graphviz()
