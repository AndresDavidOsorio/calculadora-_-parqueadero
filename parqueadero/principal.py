from usuario import Usuario
from carro import Carro
from parqueadero import RegistroParqueadero

# Crear registros directamente en la lista
registros = [
    RegistroParqueadero(
        Usuario("1020345678", "Juan García", "Administrador"),
        Carro("ABC123", "Sedan", "Negro"),
        "A-01", "2026-02-20", "08:00"
    ),
    RegistroParqueadero(
        Usuario("1020345679", "María López", "Cliente"),
        Carro("XYZ789", "SUV", "Blanco"),
        "B-05", "2026-02-20", "09:15"
    ),
    RegistroParqueadero(
        Usuario("1020345680", "Carlos Rodríguez", "Cliente"),
        Carro("KLM456", "Pickup", "Azul"),
        "C-12", "2026-02-20", "07:45"
    ),
    RegistroParqueadero(
        Usuario("1020345681", "Ana Martínez", "Administradora"),
        Carro("DEF321", "Hatchback", "Rojo"),
        "A-03", "2026-02-20", "11:20"
    )
]

# Registrar salidas (solo algunos)
registros[0].registrar_salida("10:30")
registros[2].registrar_salida("12:00")

# Imprimir tabla

print(f"{'Cédula':<12} {'Nombre':<20} {'Tipo Usuario':<15} {'Placa':<10} "
      f"{'Tipo Carro':<12} {'Color':<10} {'Puesto':<8} "
      f"{'Fecha':<12} {'Hora Entrada':<12} {'Hora Salida':<12} {'Estado':<10}")


for registro in registros:
    d = registro.mostrar()
    print(f"{d[0]:<12} {d[1]:<20} {d[2]:<15} {d[3]:<10} "
          f"{d[4]:<12} {d[5]:<10} {d[6]:<8} "
          f"{d[7]:<12} {d[8]:<12} {d[9]:<12} {d[10]:<10}")

