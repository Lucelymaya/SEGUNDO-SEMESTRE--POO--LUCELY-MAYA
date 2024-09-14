import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación de Gestión de Datos")

# Lista para almacenar los datos ingresados
datos = []

# Función para agregar información a la lista
def agregar_dato():
    dato = entry_dato.get()
    if dato:
        lista_datos.insert(tk.END, dato)  # Añadir dato a la lista visual
        datos.append(dato)  # Añadir dato a la lista interna
        entry_dato.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista y el campo de texto
def limpiar_datos():
    lista_datos.delete(0, tk.END)  # Limpiar la lista visual
    datos.clear()  # Limpiar la lista interna
    entry_dato.delete(0, tk.END)  # Limpiar el campo de texto

# Etiqueta
label_titulo = tk.Label(root, text="Gestión de Datos", font=("Arial", 16))
label_titulo.pack(pady=10)

# Campo de texto para ingresar datos
entry_dato = tk.Entry(root, width=40)
entry_dato.pack(pady=5)

# Botón para agregar datos
boton_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos
lista_datos = tk.Listbox(root, width=50, height=10)
lista_datos.pack(pady=10)

# Botón para limpiar la lista
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Ejecutar la ventana
root.mainloop()
