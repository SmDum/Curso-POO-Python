from .interfaces.elemento_interface import ElementoInterface

class Elemento2(ElementoInterface):
    def executar(self):
        print("Estou executando o elemento alternativo")