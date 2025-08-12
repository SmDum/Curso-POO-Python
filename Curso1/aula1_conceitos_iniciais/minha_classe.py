class MinhaClasse:
    
    def __init__(self, info, elem): #metodo construtor é o primeiro!
        self.atributo_1 = "Atributo 1"
        self.atributo_2 = elem
        self.atributo_3 = [1, 2, "a"]
        self.new_atribute = info
        print(self.new_atribute)
    
    
    def metodo_1(self):
        print("Minha Ação 1")
        print("Minha Ação 2")
        print(self.atributo_2)
        return "Ola Mundo"
    
    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo_3[1] + numero)
    
#objeto        #classe --> instanciamos um objeto
minha_classe = MinhaClasse("Info aqui no construtor", 213)

minha_classe.metodo_2(3)