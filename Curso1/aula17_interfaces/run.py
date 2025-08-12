from abc import ABC, abstractmethod
 
class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self) -> None: pass
    
    @abstractmethod
    def ir_para_casa(self)-> None: pass
    
    @abstractmethod
    def horario_de_almoco(self)-> None: pass
    
class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print("O professor esta trabalhando")
        
    def ir_para_casa(self)-> None:
        print("O professor esta indo para casa")
        
    def horario_de_almoco(self)-> None:
        print("O professor esta almoçando")
        
class engenheiro(Trabalhador):
    def trabalhar(self) -> None:
        print("O engenheiro esta trabalhando")
        
    def ir_para_casa(self)-> None:
        print("O engenheiro esta indo para casa")
        
    def horario_de_almoco(self)-> None:
        print("O engenheiro esta almoçando")
        
        
def comunicar_o_trabalhador(trabalhador : Trabalhador):
    trabalhador.trabalhar()
    print("Comunicar o trabalhador para ir para casa")
    trabalhador.ir_para_casa()
    
p1 = Professor()
p2 = engenheiro()

comunicar_o_trabalhador(p1)
comunicar_o_trabalhador(p2)
