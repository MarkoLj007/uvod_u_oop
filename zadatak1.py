class Knjiga:
    def __init__(self, naslov, autor, godina_izdanja):
        self. naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja

        print(self.naslov)
        print(self.autor)
        print(self.godina_izdanja)
        print("-"*30)

knjiga1 = Knjiga("Zlocin i kazna", "Fjodor Dostojevski", 1866)
knjiga2 = Knjiga("Preobražaj", "Franz Kafka", 1915)