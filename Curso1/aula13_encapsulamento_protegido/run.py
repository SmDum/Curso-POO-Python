class Mamifero:
    def __init__(self, localizacao : str) -> None:
        self.localizacao = localizacao
        self._tamanho = 1.23
        
    def andar(self) -> None:
        print(f"O animal está andando pelo {self.localizacao}")
    
    def _dormir(self) -> None: # Método protegido
        print("O animal está dormindo")
        
class Gato(Mamifero):
    
    def __init__(self, localizacao : str) -> None:
        super().__init__(localizacao)
        
    def miar(self) -> None:
        print("O Gato está miando")
        self.andar()
        self._dormir()
        print(self._tamanho)

cat = Gato("Argentina")
cat.miar()
cat._dormir() # Deveria dar erro / elementos protegidos não são chamados por objetos
print(cat._tamanho) # Deveria dar erro / elementos protegidos não são chamados por objetos