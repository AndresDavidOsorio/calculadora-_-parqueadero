class RegistroParqueadero:
    def __init__(self, usuario, carro, puesto, fecha_entrada, hora_entrada):
        self.usuario = usuario
        self.carro = carro
        self.puesto = puesto
        self.fecha_entrada = fecha_entrada
        self.hora_entrada = hora_entrada
        self.hora_salida = ""
        self.estado = "Entrada"

    def registrar_salida(self, hora_salida):
        self.hora_salida = hora_salida
        self.estado = "Salida"

    def mostrar(self):
        return [
            self.usuario.cedula,
            self.usuario.nombre,
            self.usuario.tipo_usuario,
            self.carro.placa,
            self.carro.tipo_carro,
            self.carro.color,
            self.puesto,
            self.fecha_entrada,
            self.hora_entrada,
            self.hora_salida,
            self.estado
        ]