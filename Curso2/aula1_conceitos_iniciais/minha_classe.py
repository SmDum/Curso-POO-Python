class MinhaClasse:
    
    def __init__(self, info): # Método construtor
        self.atributo1 = "Meu atributo 1"
        self.atributo2 = "Meu atributo 2"
        self.atributo3 = [1,2,"a"]
        self.new_atribute = info
        print(self.new_atribute)
    
    def metodo1(self): #self é usado para se referir à instância da classe "MuinhaClasse"
       print("Minha ação 1")
       print("Minha ação 2")
       print(self.atributo2)
       return "Olá Mundo!"

    def metodo2(self, numero):
        print(self.atributo3[1] + numero)
    
 #objeto      #classe --> Instanciamos um objeto       
minhaclasse = MinhaClasse("Info aqui no construtor") #instanciando a classe

response = minhaclasse.metodo1() #chamando o método da classe MinhaClasse
minhaclasse.metodo2(10) #chamando o método com parâmetro
print(response) #imprimindo o retorno do método