import os

class Producto:
    # Constructor de la clase Producto para inicializar sus atributos
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getter para obtener los valores de los atributos de Producto
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setter para modificar los valores de los atributos de Producto
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Método para convertir un objeto Producto a una cadena en formato CSV
    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio:.2f}"


class Inventario:
    # Constructor de la clase Inventario, inicializa el inventario y carga los productos desde un archivo
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    # Método para cargar el inventario desde un archivo al iniciar el programa
    def cargar_inventario(self):
        """Carga el inventario desde un archivo al iniciar el programa."""
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    # Separar los valores por coma y convertirlos al tipo de dato correspondiente
                    id, nombre, cantidad, precio = linea.strip().split(",")
                    producto = Producto(id, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)  # Agregar el producto al inventario
            print(f"Inventario cargado desde {self.archivo}.")
        except FileNotFoundError:
            print(f"{self.archivo} no encontrado. Se creará un nuevo archivo.")
        except PermissionError:
            print(f"No se tiene permiso para leer {self.archivo}.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    # Método para guardar el inventario en un archivo
    def guardar_inventario(self):
        """Guarda el inventario en un archivo."""
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(str(producto) + "\n")  # Escribir cada producto en el archivo
            print(f"Inventario guardado en {self.archivo}.")
        except PermissionError:
            print(f"No se tiene permiso para escribir en {self.archivo}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    # Método para añadir un producto al inventario
    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: ID ya existe.")  # Verificar si el ID ya existe
                return
        self.productos.append(producto)
        self.guardar_inventario()  # Guardar el inventario actualizado en el archivo
        print("Producto añadido con éxito.")

    # Método para eliminar un producto del inventario por su ID
    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.get_id() != id]  # Eliminar el producto con el ID dado
        self.guardar_inventario()  # Guardar el inventario actualizado en el archivo
        print(f"Producto con ID {id} eliminado.")

    # Método para actualizar la cantidad o el precio de un producto en el inventario
    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                self.guardar_inventario()  # Guardar el inventario actualizado en el archivo
                print(f"Producto con ID {id} actualizado.")
                return
        print("Producto no encontrado.")  # Si no se encuentra el producto, mostrar un mensaje de error

    # Método para buscar productos en el inventario por nombre
    def buscar_productos(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(p)  # Mostrar los productos encontrados
        else:
            print("No se encontraron productos con ese nombre.")  # Mostrar un mensaje si no se encuentra ningún producto

    # Método para mostrar todos los productos en el inventario
    def mostrar_productos(self):
        if self.productos:
            for p in self.productos:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: ${p.get_precio():.2f}")
        else:
            print("No hay productos en el inventario.")  # Mostrar un mensaje si el inventario está vacío


# Función para mostrar el menú de opciones al usuario
def mostrar_menu():
    print("\nMenú de Inventario:")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


# Función principal que controla el flujo del programa
def main():
    inventario = Inventario()  # Crear una instancia de Inventario y cargar los productos desde el archivo

    while True:
        mostrar_menu()  # Mostrar el menú al usuario
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese nuevo precio (deje en blanco si no desea cambiarlo): ")
            inventario.actualizar_producto(id, int(cantidad) if cantidad else None, float(precio) if precio else None)

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_productos(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Verifica si el script es ejecutado directamente (y no importado) antes de llamar a main()
if __name__ == "__main__":
    main()





