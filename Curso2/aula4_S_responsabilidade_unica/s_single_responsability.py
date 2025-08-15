class SistemaCadastral:
    
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validate_input(nome, idade):
           self.__register_user(nome, idade)
        else:
            self.__error_handle()
            
    def __validate_input(self, nome: str, idade: int) -> bool: 
        if isinstance(nome, dict) and isinstance(idade, int):
            return True
        return False
    
    def __register_user(self, nome: str, idade: int) -> None:
        print("Acessando o banco de dados...")
        print(f"Cadastrando {nome} com idade {idade}.")
        
    def __error_handle(self) -> None:
        print(f"Dados Inválidos")
        

sistema = SistemaCadastral()
sistema.cadastrar("João", 30)