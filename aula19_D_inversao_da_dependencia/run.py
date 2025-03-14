from elementos.interfaces.elemento_interface import ElementoInterface
from elementos.elemento import Elemento
from elementos.elemento2 import Elemento2

class Principal:
    def __init__(self, elem : ElementoInterface)->None:
        self.__elem = Elemento()

    def run(self)->None:
        elem = Elemento()
        self.__elem.executar(self)
        print("Estou finalizando na classe principal")
        
el = Elemento()
el2 = Elemento2()

cl1 = Principal(el)
cl2 = Principal(el2)

cl1.run()
cl2.run()