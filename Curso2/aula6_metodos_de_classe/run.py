class MinhaClasse:
    
    estatico = "lhama"
    
    def __init__(self, estado) -> None:
        self.__estado = estado
        
    def print_variavel_de_classica(self):
        print(self.estatico)
        
    @classmethod
    def alterar_variavel_de_classe(cls):
        cls.estatico = "novo_valor"
        #MinhaClasse.estatico = "novo_valor"
        

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)


obj1.print_variavel_de_classica()
obj1.alterar_variavel_de_classe()

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)