class Vozilo:
    def __init__(self, marka, model, godina_proizvodnje, cijena):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.cijena = cijena

    def info(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Cijena: {self.cijena}")

    def promijeni_cijenu(self, nova_cijena):
        self.cijena = nova_cijena
        print("Uspješno ste promijenili cijenu vozila")

class ElektricnoVozilo(Vozilo):
    def __init__(self, marka, model, godina_proizvodnje, cijena, domet_baterije):
        super().__init__(marka, model, godina_proizvodnje, cijena)
        self.domet_baterije = domet_baterije

    def info(self):
        super().info()
        print(f"Domet baterije: {self.domet_baterije}")

def ispisi_izbornik():
    print("\n--- AUTOSALON v2.0 ---")
    print("1. Dodaj novo (obično) vozilo")
    print("2. Dodaj novo (električno) vozilo")
    print("3. Ispiši podatke o određenom vozilu")
    print("4. Promijeni cijenu vozilu")
    print("5. Ispiši sva vozila")
    print("0. Izlaz")
    print("-"*20)
    
def UnosVozila():
    print("\n --- Unos običnog vozila ---")
    marka = input("Unesite marku vozila: ")
    model = input("Unesite model vozila: ")

    while True:
        try:
            godina_proizvodnje = int(input("Unesite godinu proizvodnje vozila: "))
            cijena = float(input("Unesite cijenu vozila: "))
            break
        except ValueError:
            print("Pogrešno unesen podatak")

    return Vozilo(marka, model, godina_proizvodnje, cijena)

def UnosElVozila():
    print("\n --- Unos električno vozila ---")
    marka = input("Unesite marku vozila: ")
    model = input("Unesite model vozila: ")

    while True:
        try:
            godina_proizvodnje = int(input("Unesite godinu proizvodnje vozila: "))
            cijena = float(input("Unesite cijenu vozila (EUR): "))
            domet_baterije = float(input("Unesite domet baterije (km): "))
            break
        except ValueError:
            print("Pogrešno unesen podatak")

    return ElektricnoVozilo(marka, model, godina_proizvodnje, cijena, domet_baterije)


def pronadji_vozilo(lista_vozila):
    if len(lista_vozila) == 0:
        print("Lista vozila je prazna")
        return None
    else:
        marka = input("Unesite marku vozila: ")
        model = input("Unesite model vozila: ")
        
        for vozilo in lista_vozila:
            if vozilo.marka == marka and vozilo.model == model:
                return vozilo
            
        print("Vozilo nije pronađeno")
        return None


autosalon = []
while True:
    ispisi_izbornik()
    try:
        izbor = int(input("Unesite Vaš odabir: "))
        if izbor == 1:
            vozilo = UnosVozila()
            autosalon.append(vozilo)
            print("Vozilo uspješno uneseno")
        elif izbor == 2:
            el_vozilo = UnosElVozila()
            autosalon.append(el_vozilo)
            print("Vozilo uspješno uneseno")
        elif izbor == 3:
            vozilo = pronadji_vozilo(autosalon)
            if vozilo is not None:
                vozilo.info()
        elif izbor == 4:
            vozilo = pronadji_vozilo(autosalon)
            if vozilo is not None:
                try:
                    nova_cijena = float(input("Unesite novu cijenu vozila: "))
                except ValueError:
                    print("Pogrešan unos podataka")
                vozilo.promijeni_cijenu(nova_cijena)
        elif izbor == 5:
            if not autosalon:
                print("Evidencija je prazna")
            else:
                for vozilo in autosalon:
                    print("-"*30)
                    vozilo.info()
                    print("-"*30)
        elif izbor == 0:
            print("Hvala Vam na korištenju sustava evidencije automobila u autosalonu")
            break
        else:
            print("Pogrešan odabir, molimo unesite opciju između 0 i 5")
            
    except ValueError:
        print("Pogrešan odabir")










