class Recept:
    def __init__(self, naziv):
        self.naziv = naziv
        self.sastojci = []  
    def dodaj_sastojak(self, sastojak, kolicina):
        self.sastojci.append({'naziv': sastojak, 'količina': kolicina})

    def prikazi(self):
        print(f"Recept: {self.naziv}")
        if not self.sastojci:
            print("Nema dodanih sastojaka.")
        else:
            print("Sastojci:")
            for s in self.sastojci:
                print(f"- {s['naziv']}: {s['količina']}")

class Kuharica:
    def __init__(self, naziv):
        self.naziv = naziv
        self.recepti = []  

    def dodaj_recept(self, recept):
        self.recepti.append(recept)

    def pronadi_recept(self, naziv_recepta):
        for r in self.recepti:
            if r.naziv == naziv_recepta:
                r.prikazi()
                return
        print(f"Recept '{naziv_recepta}' nije pronađen u kuharici.")

moja_kuharica = Kuharica("Moja kuharica")

palacinke = Recept("Palačinke")
juha = Recept("Juha")

palacinke.dodaj_sastojak("Brašno", "200 g")
palacinke.dodaj_sastojak("Jaja", "2 kom")
palacinke.dodaj_sastojak("Mlijeko", "300 ml")


juha.dodaj_sastojak("Mrkva", "2 kom")
juha.dodaj_sastojak("Krumpir", "3 kom")
juha.dodaj_sastojak("Voda", "1 l")

# Dodajemo recepte u kuharicu
moja_kuharica.dodaj_recept(palacinke)
moja_kuharica.dodaj_recept(juha)

# Pretražujemo i prikazujemo recept
moja_kuharica.pronadi_recept("Palačinke")