class CsvHandler:
    def __init__(self, directory) -> None:
        self.dir = directory
        
    def insert_data_in_csv(self, data):
        print(f"Inserindo {data} em {self.dir}")
        
    def read_data(self):
        print(f"Lendo data no {self.dir }")
        
csv_handle = CsvHandler("caminho/do/diretorio.csv")
csv_handle.insert_data_in_csv("dados de exemplo")