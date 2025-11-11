import csv
import ast


class Ucenik:
    def __init__(self, ime, prezime, razred):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.ocjene = [] 

    def dodaj_ocjenu(self, ocjena):
        if isinstance(ocjena, int) and 1 <= ocjena <= 5:
            self.ocjene.append(ocjena)
            print(f"INFO: Učeniku {self.ime} {self.prezime} je upisana ocjena {ocjena}.")
        else:
            print(f"GREŠKA: Ocjena '{ocjena}' nije važeća. Molimo unesite broj od 1 do 5.")

    def izracunaj_prosjek(self):
        if not self.ocjene:
            return 0.0
        
        return sum(self.ocjene) / len(self.ocjene)

    def info(self):
        print("-" * 30)
        print(f"Ime i prezime: {self.ime} {self.prezime}")
        print(f"Razred: {self.razred}")
        
        if self.ocjene:
            print(f"Ocjene: {self.ocjene}")
        else:
            print("Ocjene: (nema upisanih ocjena)")
            
        prosjek = self.izracunaj_prosjek()
        print(f"Prosjek ocjena: {prosjek:.2f}") 
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

def upisUcenika(ime, prezime, razred):
    ucenik = Ucenik(ime, prezime, razred)
    return ucenik

def upisOcjene(ucenik, ocjena):
    ucenik.dodaj_ocjenu(ocjena)

def ispisPodataka(ucenik):
    ucenik.info()

lista_ucenika = []
provjera = False

def spremi_podatke(lista_ucenika, ime_datoteke):
    with open(ime_datoteke, mode="w", newline="", encoding="utf-8") as datoteka:
        polja = ["ime", "prezime", "razred", "ocjene"]
        writer = csv.DictWriter(datoteka, fieldnames=polja)
        writer.writeheader()
        for p in lista_ucenika:
            writer.writerow({"ime": p.ime, "prezime": p.prezime, "razred": p.razred, "ocjene": p.ocjene})
        print(f"Spremljeno u {ime_datoteke}")
def ucitaj_ucenike(ime_datoteke):
    ucitani_ucenici = []
    with open(ime_datoteke, mode="r", encoding="utf-8") as datoteka:
        reader = csv.DictReader(datoteka)
        for red in reader:
            ocjene = ast.literal_eval(red["ocjene"])  # pretvara string "[5, 4]" u listu [5, 4]
            p = Ucenik(red["ime"], red["prezime"], red["razred"])
            p.ocjene = ocjene
            ucitani_ucenici.append(p)
    print(f"Učitano iz {ime_datoteke}")
    return ucitani_ucenici
    
#spremi_podatke(lista_ucenika, "ucenici.csv")
#nova_lista = ucitaj_ucenike("ucenici.csv")
#for p in nova_lista:
#    print(p.ime, p.prezime, p.razred, p.ocjene)


while True:
    ucitani_ucenici = ucitaj_ucenike("ucenici.csv")
    lista_ucenika.extend(ucitani_ucenici)
    ispisi_izbornik()
    try:
        izbor = int(input("Unesite izbor (0/1/2/3): "))
        if izbor == 1:
            print("Unos novog učenika")
            ime = input("Unesite ime učenika: ")
            prezime = input("Unesite prezime učenika: ")
            razred = input("Unesite razred učenika: ")
            ucenik = upisUcenika(ime, prezime, razred)
            lista_ucenika.append(ucenik)
        elif izbor == 2:
            ime = input("Unesite ime učenika: ")
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
                ispisPodataka(ucenik)
                break

        elif izbor == 0:
            spremi_podatke(lista_ucenika, "ucenici.csv")
            print("Hvala na korištenju programa.")
            break
        else: 
            print("Greška")
    except ValueError:
        print("Molimo unesite ispravan odabir (0/1/2/3).")
    
  
