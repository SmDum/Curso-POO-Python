class Interrupitor:
    def __init__(self, comodo : str) -> None:
        self.comodo = comodo
    
    def acender(self) -> None:
        print(f"Estou acendendo a luz do comodo: {self.comodo}")
    
    def apagar(self) -> None:
        print(f"Estou apagando a luz do comodo: {self.comodo}")
        
class Pessoa:
    def acender_luzes(self, interrupitor : Interrupitor) -> None:
        interrupitor.acender()
    
    def apagar_luzes(self, interrupitor : Interrupitor) -> None:
        interrupitor.apagar()
    
    def dormir(self) -> None:
        print("A pessoa foi dormir")
        
agnaldo = Pessoa()
interrupitor_sala = Interrupitor("Sala")
interrupitor_quarto = Interrupitor("Quarto")
agnaldo.acender_luzes(interrupitor_sala)
agnaldo.apagar_luzes(interrupitor_quarto)
