class Numero:

    def __init__(self, valor):
        self.valor = valor  
    
    def set_valor(self, nuevo_valor):
        self.valor = nuevo_valor
    def get_valor(self):
        return self.valor
    
    def mostrar_info(self):
        print(f"Valor del número: {self.valor}")