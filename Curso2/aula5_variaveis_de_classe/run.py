class MinhaClasse:
    
    estatico = "lhama"
    
    def __init__(self, estado) -> None:
        self.__estado = estado
        
        

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

MinhaClasse.estatico = "cavalo"
obj1.estatico = "gato"
MinhaClasse.estatico = "cachorro"

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)