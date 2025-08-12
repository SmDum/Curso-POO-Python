class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None
        
    def setter_valor(self, valor: int) -> None:
        self.__valor = valor
        
    def getter_valor(self) -> int:
        return self.__valor

my_class = MinhaClasse()
#my_class.valor = 3 #Ferindo o Encapsulamento
my_class.setter_valor(42)  # Usando o setter para definir o valor
valor = my_class.getter_valor()  # Usando o getter para obter o valor
print(valor)  # Saída: 42


