class Carro:
    def __init__(self, placa, tipo_carro, color):
        self.placa = placa
        self.tipo_carro = tipo_carro
        self.color = color

    def mostrar(self):
        return f"{self.placa} - {self.tipo_carro} - {self.color}"