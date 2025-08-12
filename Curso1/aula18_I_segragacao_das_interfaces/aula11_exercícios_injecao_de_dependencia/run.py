class ConectorBancoDeDados:
    
    def __init__(self) -> None:
        self.conection = None
    
    def conectar_ao_banco(self) -> None:
        self.conection = True
        
class RepositorioDeBanco:
    
    def __init__(self, conexao: ConectorBancoDeDados) -> None:
        self.__conexao = conexao
        
    def busca_dados(self) -> None:
        if self.__conexao.conection:
            return [1, 2, 3, 4, 5]
        else:
            return None

class RegraDeNegocio:
    
    def __init__(self, repo: RepositorioDeBanco) -> None:
        self.__repo = repo
        
    def calcular_resultado(self) -> None:
        dados = self.__repo.busca_dados()
        if not dados:
            print("Dados não encontrado. Verifique a conexão com o banco de dados.")
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f"Resultado: {resposta}")
            
conn = ConectorBancoDeDados()
conn.conectar_ao_banco()

repo = RepositorioDeBanco(conn)
regra = RegraDeNegocio(repo)

regra.calcular_resultado()