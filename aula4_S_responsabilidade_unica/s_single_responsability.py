class SistemaCadastral:
    
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validate_input(nome, idade):
            self.__registe_user(nome, idade)
        
        else:
            self.__erro_handle()
        
    def __validate_input(self, nome: str, idade: int):
        return isinstance(nome, str) and isinstance(idade, int) #1
    
    def __registe_user(self, nome: str, idade: int) -> None:
        print("Acessando banco de dados...") #2
        print(f"Cadastrar usuário {nome}, idade {idade}")
        
    def __erro_handle(self) -> None:
        print("Dados inválidos") #3
        
sistema = SistemaCadastral()
sistema.cadastrar("João", 30)