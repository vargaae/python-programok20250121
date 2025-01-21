class Filmek:
    def __init__(self, sor:str):
        tmp:list[str] = sor.strip().split(';')
        self.film_cim:str = tmp[0]
        self.ev:int = tmp[1]
        self.title = tmp[0]
        self.year = int(tmp[1])
        self.mufajok = tmp[2].split(", ")