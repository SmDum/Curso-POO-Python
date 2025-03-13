class ConnectionDB:
    def conectar(self):
        print("Conectando ao banco de dados")
        
        
class SqlRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco SQL")
        
class NoSQLRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco NoSQL")
      
class DBHandler(ConnectionDB):
    def alterTable(self):
        print("Alterando tabela em SQL")
        