class Pessoa:
    def __init__(self, nome, altura, idade):
        self.nome = nome
        self.altura = altura
        self.idade = idade
        
    def correr(self):
        print(f"A pessoa {self.nome} está correndo")
        
    def comer(self, alimento):
        print(f"A pessoa {self.nome} está comendo {alimento}")
        
        
p1 = Pessoa("João", 1.75, 30)
p1.correr()
p1.comer("maçã")


p2 = Pessoa("Maria", 1.65, 25)
p2.correr()
p2.comer("banana")