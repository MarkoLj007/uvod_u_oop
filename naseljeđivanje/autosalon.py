class Vozilo:
    def __init__(self, marka, model, godina_proizvodnje, cijena):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.cijena = cijena
    
    def info(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Godina: {self.godina}, Cijena: {self.cijena} EUR")

    def promijeni_cijenu(self, nova_cijena):
        self.cijena = nova_cijena
        print("Uspješno ste promijenili cijenu vozila") 

class ElektricnoVozilo(Vozilo):
    def __init__(self, marka, model, godina_proizvodnje, cijena, domet_baterije)
        super().__init__(marka, model, godina_proizvodnje, cijena)
        self.domet_baterije = domet_baterije