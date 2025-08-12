class Mamifero:
    def __init__(self, localizacao : str) -> None:
        self.localizacao = localizacao
        
    def andar(self) -> None:
        print(f"O animal está andando pelo {self.localizacao}")
            
class Cachorro(Mamifero):
    
    def __init__(self, localizacao : str) -> None:
        super().__init__(localizacao) # Chama o construtor da classe pai
    
    def latir(self) -> None:
        print("O Cachorro está latindo")
        self.andar()
        
class Gato(Mamifero):
    
    def __init__(self, localizacao : str) -> None:
        super().__init__(localizacao) # Chama o construtor da classe pai
        
    def miar(self) -> None:
        print("O Gato está miando")
        self.andar()
  
dog = Cachorro("Chile")
dog.latir()
print("\n")
cat = Gato("Brasil")
cat.miar()