class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf 
        
    def apresentar(self):
        print(f"Olá! Minha altura é {self.altura}m.")
        self.__coletar_documento()
        
    def __coletar_documento(self):
        print(f"Meu CPF é {self.__cpf}.")
        
jorge = Pessoa(1.75, "123.456.789-00")
jorge.apresentar()

#jorge.__coletar_documento()  # Isso causará um erro, pois o método é privado
#Métodos privados só podem ser acessados dentro da própria classe.