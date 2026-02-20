class Usuario:

    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_documento(self):
        return self.documento
    
    def set_documento(self, nuevo_documento):
        self.documento = nuevo_documento

    def mostrar_info(self):
        return f"Usuario: {self.nombre} - Documento: {self.documento}"