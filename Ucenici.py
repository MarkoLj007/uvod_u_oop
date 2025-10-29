class Ucenik:
    """
    Nacrt (klasa) za stvaranje objekata koji predstavljaju učenike.
    Svaki učenik ima ime, prezime, razred i listu ocjena.
    """

    # Konstruktor - posebna metoda koja se poziva pri stvaranju novog objekta
    def __init__(self, ime, prezime, razred):
        """Inicijalizira novi objekt Učenik s početnim podacima."""
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.ocjene = []  # Atribut 'ocjene' se inicijalizira kao prazna lista

    # Metode - funkcije unutar klase koje definiraju što objekt može raditi
    def dodaj_ocjenu(self, ocjena):
        """Dodaje novu ocjenu u listu ocjena učenika."""
        if isinstance(ocjena, int) and 1 <= ocjena <= 5:
            self.ocjene.append(ocjena)
            print(f"INFO: Učeniku {self.ime} {self.prezime} je upisana ocjena {ocjena}.")
        else:
            print(f"GREŠKA: Ocjena '{ocjena}' nije važeća. Molimo unesite broj od 1 do 5.")

    def izracunaj_prosjek(self):
        """Vraća prosjek svih ocjena učenika."""
        # Provjera ako je lista ocjena prazna da se izbjegne dijeljenje s nulom
        if not self.ocjene:
            return 0.0
        
        return sum(self.ocjene) / len(self.ocjene)

    def info(self):
        """Ispisuje sve dostupne informacije o učeniku na konzolu."""
        print("-" * 30)
        print(f"Ime i prezime: {self.ime} {self.prezime}")
        print(f"Razred: {self.razred}")
        
        # Ispis ocjena, ili poruka ako nema ocjena
        if self.ocjene:
            print(f"Ocjene: {self.ocjene}")
        else:
            print("Ocjene: (nema upisanih ocjena)")
            
        prosjek = self.izracunaj_prosjek()
        print(f"Prosjek ocjena: {prosjek:.2f}") # Formatiranje na dvije decimale
        print("-" * 30)

def ispisi_izbornik():
    print("-"*50)
    print("Glavni izbornik")
    print("-"*50)
    print("0. Izlaz iz programa")
    print("1. Unos novog učenika")
    print("2. Unos ocjena za učenika")
    print("3. Ispis podataka o učenicima")
    print("-"*50)

def upisUcenice(ime, prezime, razred):
    ucenik = Ucenik(ime, prezime, razred)
    return ucenik

def upisOcjene(ucenik, ocjena):
    ucenik.dodaj_ocjenu(ocjena)

def ispisPodataka(ucenik):
    ucenik.info()

lista_ucenika = []
provjera = False

while True: 
    ispisi_izbornik()
    try:
        izbor = int(input("Unesite izbor (0/1/2/3): "))
        if izbor == 1:
            print("Unos nove učenice")
            ime = input("Unesite ime učenice: ")
            prezime = input("Unesite prezime učenice: ")
            razred = input("Unesite razred učenice: ")
            ucenik = upisUcenice(ime, prezime, razred)
            lista_ucenika.append(ucenik)
        elif izbor == 2:
            ime = input("Unesite ime učenice: ")
            for ucenik in lista_ucenika:
                if ucenik.ime == ime:
                    provjera = True
                    break
                else: 
                    provjera = False
            if provjera:
                ocjena = int(input("Unesite ocjenu: "))
                upisOcjene(ucenik, ocjena)
            else: 
                print("Učenik nije pronađen")
        elif izbor == 3:
            for ucenik in lista_ucenika:
                if ucenik.ime == ime:
                    ispisPodataka(ucenik)
                    break
                else: 
                    print("Učenik nije pronađen.")
        elif izbor == 0:
            print("Hvala na korištenju programa.")
            break
        else: 
            print("Greška")
    except ValueError:
        print("Molimo unesite ispravan odabir (0/1/2/3).")
    
    for ucenik in lista_ucenika:
        ucenik.info()