class SistemaCadastral:
    
    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int): #1
            print("Acessando banco de dados...") #2
            print(f"Cadastrar usuário {nome}, idade {idade}")
        
        else:
            print("Dados inválidos") #3
              
# SOLID
# S - Single Responsibility Principle / Responsabilidade Única