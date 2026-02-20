from usuario import Usuario
from calculadora import Calculadora
from numero import Numero

# Crear usuario
usuario1 = Usuario("Andres Osorio", "1234567890")

# Crear números
numero1 = Numero(20)
numero2 = Numero(10)

# Crear calculadora
calculadora1 = Calculadora(usuario1, numero1, numero2, "2025-02-18")

# Operaciones
suma = calculadora1.calcular_sumar()
resta = calculadora1.calcular_restar()
multiplicacion = calculadora1.calcular_multiplicar()
division = calculadora1.calcular_dividir()

# Mostrar resultados
print(usuario1.mostrar_info())
print(calculadora1.mostrar_info())
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Fecha actual: {calculadora1.get_fecha()}")

# Cambiar fecha
calculadora1.set_fecha("2025-02-19")
print(f"Nueva fecha: {calculadora1.get_fecha()}")