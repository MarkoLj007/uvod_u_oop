class Nekretnina():
    def __init__(self, adresa, kvadratura, bazna_cijena):
        self.adresa = adresa
        self.kvadratura = kvadratura
        self.bazna_cijena = bazna_cijena

    def izracunaj_cijenu(self):
        cijena = self.kvadratura * self.bazna_cijena
        return cijena

    def ispisi_info(self):
        print("-"*20)
        print(f"Adresa: {self.adresa}")
        print(f"Kvadratura: {self.kvadratura}")
        cijena = self.izracunaj_cijenu()
        print(f"Cijena: {cijena}")
    
class Stan(Nekretnina): 
    def __init__(self, adresa, kvadratura, bazna_cijena, kat, ima_lift):
        super().__init__(adresa, kvadratura, bazna_cijena)
        self.kat = kat
        self.ima_lift = ima_lift

    def izracunaj_cijenu(self):
        cijena = super().izracunaj_cijenu()
        if self.kat > 2 and self.ima_lift == False:
            return 0.9*cijena
        elif self.ima_lift == True:
            return 1.05*cijena
    
    def ispisi_info(self):
        super().ispisi_info()
        print(f"Broj kata: {self.kat}")
        if self.ima_lift == True:
            print("Stan ima lift")
        else: 
            print("Stan nema lift")
    
class Kuca(Nekretnina):
    def __init__(self, adresa, kvadratura, bazna_cijena, povrsina_okucnice):
        super().__init__(adresa, kvadratura, bazna_cijena)
        self.povrsina_okucnice = povrsina_okucnice

    def izracunaj_cijenu(self):
        cijena = super().izracunaj_cijenu()
        return cijena + self.povrsina_okucnice*100
    
    def ispisi_info(self):
        super().ispisi_info()
        print(f"Površina okućnice iznosti: {self.povrsina_okucnice} metara kvadratnih")

def ispisi_izbornik():
    print("-"*20)
    print("1. Unos stana")
    print("2. Unos kuće")
    print("3. Ispis svih dostupnih nekretnina")
    print("4. Prodaja nekretnine")
    print("0. Izlaz")

nekretnine = []
while True:
    ispisi_izbornik()
    try:
        izbor = int(input("Odaberite opciju (0/1/2/3/4): "))
        if izbor == 1:
            adresa = input("Unesite adresu stana: ")
            while True:
                try:
                    kvadratura = float(input("Unesite kvadraturu stana u metrima kvadratnim: "))
                    break
                except ValueError:
                    print("Pogrešnka prilikom unosa podataka.")
            while True:
                try:
                    bazna_cijena = float(input("Unesite baznu cijenu stana u eurima: "))
                    break
                except ValueError:
                    print("Pogrešnka prilikom unosa podataka.")
            while True:
                try:
                    kat = int(input("Unesite broj kata na kojem se stan nalazi: "))
                    break
                except ValueError:
                    print("Pogrešnka prilikom unosa podataka.")
            while True:
                ima_lift = input("Ima li stan lift (Da/Ne): ")
                if ima_lift == "Da":
                    ima_lift = True
                    break
                elif ima_lift == "Ne":
                    ima_lift = False
                    break
            stan = Stan(adresa, kvadratura, bazna_cijena, kat, ima_lift)
            nekretnine.append(stan)
        elif izbor == 2:
            adresa = input("Unesite adresu kuće: ")
            while True:
                try:
                    kvadratura = float(input("Unesite kvadraturu kuće u metrima kvadratnim: "))
                    break
                except ValueError:
                    print("Pogreška prilikom unosa podataka.")
            while True:
                try:
                    bazna_cijena = float(input("Unesite baznu cijenu kuće u eurima: "))
                    break
                except ValueError:
                    print("Pogreška prilikom unosa podataka.")
            while True:
                try:
                    povrsina_okucnice = float(input("Unesite površinu okućnice u metrima kvadratnim: "))
                    break
                except ValueError:
                    print("Pogreška prilikom unosa podataka.")
            kuca = Kuca(adresa, kvadratura, bazna_cijena, povrsina_okucnice)
            nekretnine.append(kuca)
        elif izbor == 3:
            if len(nekretnine) == 0:
                print("Popis nekretnina je prazan.")
            else:
                for nekretnina in nekretnine:
                    nekretnina.ispisi_info()
        elif izbor == 4:
            if len(nekretnine) == 0:
                print("Popis nekretnina je prazan.")
            else:
                adresa = input("Unesite adresu stana: ")
                for nekretnina in nekretnine:
                    if nekretnina.adresa == adresa:
                        nekretnine.remove(nekretnina)
                        print("Nekretnina uspješno prodana.")
                    else:
                        print("Nekretnina nije pronađena")
        elif izbor == 0:
            print("Hvala Vam na korištenju programa.")
            break
        else:
            print("Pogreška prilikom unosa podataka")
    except ValueError:
        print("Pogreška prilikom unosa podataka")