class BankovniRacun:
    def __init__(self, ime_vlasnika, broj_racuna, stanje):
        self.ime_vlasnika = ime_vlasnika
        self.broj_racuna = broj_racuna
        self.stanje = stanje

        self.stanje = 0.0

    def uplati(self, iznos):
        if iznos > 0:
            self.stanje = self.stanje + iznos
            print(f"Uplata na račun {self.stanje} je uspješno provedena.")
        else:
            print("Iznos uplate mora biti pozitivan broj.")

    def isplati(self, iznos):
        if iznos > 0: 
            if iznos <= self.stanje:
                self. stanje = self.stanje - iznos
                print(f"Isplata sa računa od {iznos} je uspješno provedena.")
            else:
                print("Nedovoljno sredstava na računu za isplatu.")
        else: 
            print("Iznos isplate mora biti pozitivan broj.")

    def info(self):
        print(f"Vlasnik računa: {self.ime_vlasnika}")
        print(f"Broj računa: {self.broj_racuna}")
        print(f"Trenutno stanje: {self.stanje:.2f}")

racun1 = BankovniRacun("Ivan Horvat", "HR1234567890123456789", 1000.0)
racun1.info()
print("-"*30)
racun1.uplati(500.0)
racun1.isplati(200.0)
racun1.isplati(2000.0)
racun1.info()
