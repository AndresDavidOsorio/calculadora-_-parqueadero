import tkinter as tk
from usuario import Usuario
from carro import Carro
from parqueadero import RegistroParqueadero

ventana = tk.Tk()
ventana.title("Parqueadero")
ventana.geometry("400x600")

tk.Label(ventana, text="Cedula").pack()
cedula = tk.Entry(ventana)
cedula.pack()

tk.Label(ventana, text="Nombre").pack()
nombre = tk.Entry(ventana)
nombre.pack()

tk.Label(ventana, text="Tipo usuario").pack()
tipo = tk.Entry(ventana)
tipo.pack()

tk.Label(ventana, text="Placa").pack()
placa = tk.Entry(ventana)
placa.pack()

tk.Label(ventana, text="Tipo carro").pack()
tipo_carro = tk.Entry(ventana)
tipo_carro.pack()

tk.Label(ventana, text="Color").pack()
color = tk.Entry(ventana)
color.pack()

tk.Label(ventana, text="Puesto").pack()
puesto = tk.Entry(ventana)
puesto.pack()

tk.Label(ventana, text="Fecha").pack()
fecha = tk.Entry(ventana)
fecha.pack()

tk.Label(ventana, text="Hora").pack()
hora = tk.Entry(ventana)
hora.pack()

lista = tk.Listbox(ventana)
lista.pack()

def guardar():

    u = Usuario(cedula.get(), nombre.get(), tipo.get())
    c = Carro(placa.get(), tipo_carro.get(), color.get())

    r = RegistroParqueadero(u, c, puesto.get(), fecha.get(), hora.get())

    lista.insert(tk.END, r.mostrar())

boton = tk.Button(ventana, text="Guardar", command=guardar)
boton.pack()

ventana.mainloop()