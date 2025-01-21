class Filmek:
    def __init__(self, sor:str):
        tmp:list[str] = sor.strip().split(';')
        self.film_cim:str = tmp[0]
        self.ev:int = int(tmp[1])
        self.mufajok:list[str] = tmp[2].split(", ")