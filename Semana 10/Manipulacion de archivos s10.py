import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Inicializa un objeto Producto con su ID, nombre, cantidad y precio.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters
    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        """
        Inicializa un objeto Inventario y carga los productos desde un archivo de texto.
        """
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga los productos desde el archivo de inventario, si existe.
        """
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    for linea in file:
                        id_producto, nombre, cantidad, precio = linea.strip().split(',')
                        self.productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
            except (FileNotFoundError, PermissionError) as e:
                print(f'Error al cargar el archivo de inventario: {e}')
        else:
            print('El archivo de inventario no existe. Se creará uno nuevo.')

    def guardar_inventario(self):
        """
        Guarda todos los productos en el archivo de inventario.
        """
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(f'{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio}\n')
            print("Inventario guardado exitosamente.")
        except (PermissionError, IOError) as e:
            print(f'Error al guardar el archivo de inventario: {e}')

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario y guarda los cambios en el archivo.
        """
        if producto.id_producto in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()
            print(f'Producto {producto.nombre} añadido exitosamente.')

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID y guarda los cambios en el archivo.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print(f'Producto con ID {id_producto} eliminado exitosamente.')
        else:
            print(f'Producto con ID {id_producto} no encontrado en el inventario.')

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto existente y guarda los cambios en el archivo.
        """
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            self.guardar_inventario()
            print(f'Producto con ID {id_producto} actualizado exitosamente.')
        else:
            print(f'Producto con ID {id_producto} no encontrado en el inventario.')

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca productos por nombre en el inventario.
        """
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """
        Muestra todos los productos en el inventario.
        """
        if self.productos:
            for p in self.productos.values():
                print(p)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar productos por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            print("Deje el campo en blanco si no desea actualizarlo.")
            cantidad = input("Ingrese la nueva cantidad del producto: ")
            precio = input("Ingrese el nuevo precio del producto: ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
