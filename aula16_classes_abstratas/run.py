from abc import ABC, abstractclassmethod

class Pessoa(ABC): # Classe abstrata não possui objetos - so pode ser mãe (herança)
    def correr(self):
        print('A pessoa esta correndo de manha')
        
    @abstractclassmethod # A classe filha DEVE criar o método trabalhar
    def trabalhar(self):
        pass
        
class Professor(Pessoa):
    def trabalhar(self):
        print('O professor esta trabalhando')
        
class Cozinheiro(Pessoa):
    def trabalhar(self):
        print('O cozinheiro esta trabalhando')
        
p1 = Professor()
p1.correr()
p1.trabalhar()