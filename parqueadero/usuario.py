class Usuario:
    def __init__(self, cedula, nombre, tipo_usuario):
        self.cedula = cedula
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario

    def mostrar(self):
        return f"{self.cedula} - {self.nombre} - {self.tipo_usuario}"
    