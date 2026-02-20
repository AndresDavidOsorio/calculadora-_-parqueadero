class Calculadora:

    def __init__(self, usuario, num1, num2, fecha):
        self.usuario = usuario
        self.numero1 = num1
        self.numero2 = num2
        self.fecha = fecha

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, nueva_fecha):
        self.fecha = nueva_fecha
        return self.fecha

    def calcular_sumar(self):
        return self.numero1.get_valor() + self.numero2.get_valor()

    def calcular_restar(self):
        return self.numero1.get_valor() - self.numero2.get_valor()

    def calcular_multiplicar(self):
        return self.numero1.get_valor() * self.numero2.get_valor()

    def calcular_dividir(self):
        if self.numero2.get_valor() == 0:
            return "No se puede dividir por cero"
        return self.numero1.get_valor() / self.numero2.get_valor()

    def mostrar_info(self):
        return f"Calculadora del usuario {self.usuario.get_nombre()} - Fecha: {self.fecha}"