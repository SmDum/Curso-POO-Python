class Artista:
    def __init__(self, tipo : str) -> None:
        self.tipo = tipo
        
    def apresentar_show(self) -> None:
        print(f"O {self.tipo} esta apresentando seu show")

class Circo:
    
    def apresentar(self, artista : Artista) -> None:
        print("O circo esta abrindo!")
        artista.apresentar_show()
        print("O publico aplaude!")
        
circo = Circo()
palhaco = Artista("Palhaço")
magico = Artista("Mágico")

circo.apresentar(palhaco)
circo.apresentar(magico)