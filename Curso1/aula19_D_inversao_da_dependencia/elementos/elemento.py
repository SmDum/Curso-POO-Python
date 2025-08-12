from .interfaces.elemento_interface import ElementoInterface

class Elemento(ElementoInterface):
    def executar(self):
        print("Estou executando o elemento")