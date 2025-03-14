from abc import ABC, abstractmethod
 
class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self) -> None: pass
    
    @abstractmethod
    def ir_para_casa(self)-> None: pass
    
    @abstractmethod
    def consultar_beneficios(self)-> None: pass
    

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print("O professor esta trabalhando")
        
    def ir_para_casa(self)-> None:
        print("O professor esta indo para casa")
        
    def consultar_beneficios(self)-> None:
        print("Consultando beneficios do professor")
        

class ProfessorSubstituto(Trabalhador):
    def trabalhar(self) -> None:
        print("O professor substituto esta trabalhando")
        
    def ir_para_casa(self)-> None:
        print("O professor substituto esta indo para casa")
    
    # Quebra da segregação de interfaces   
    def consultar_beneficios(self)-> None:
        raise Exception("Professor substituto nao tem beneficios")
        
p2 = ProfessorSubstituto()