class Celular:
    
    def __init__(self, modelo : str)->None:
        self.modelo = modelo
    
    def enviar_mensagem(self, mensagem : str)->None:
        print(f"Enviando mensagem: {mensagem}")
        
    def abrir_emails(self)->None:
        print("Abrindo emails...")
        
    def abrir_youtube(self)->None:
        print("Abrindo Youtube...")
        
        
class Pessoa:
    def __init__(self, celular : Celular)->None:
        self.celular = celular
    
    def pedir_pizza(self)->None:
        print("Buscando o celular...")
        print("Definindo o sabor...")
        self.celular.enviar_mensagem("Quero uma de calabresa")
        print("Aguardando a chegada")
        
    def estudar(self)->None:
        print("Sentando no computador...")
        self.celular.abrir_youtube()
        print("Anotando o conteúdo")

android = Celular("Samsung")
iphone = Celular("Iphone")

reginaldo = Pessoa(android)
marlene = Pessoa(iphone)

reginaldo.pedir_pizza()
print("\n")
marlene.estudar()
