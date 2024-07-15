# EjemplosMundoReal_POO/sistema_reservas.py

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            return True
        return False

    def liberar(self):
        self.ocupada = False

    def __str__(self):
        estado = 'ocupada' if self.ocupada else 'disponible'
        return f'Habitación {self.numero}: Tipo {self.tipo}, Precio {self.precio} - {estado}'

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        for habitacion in self.habitaciones:
            print(habitacion)

    def reservar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                return habitacion.reservar()
        return False

    def liberar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                habitacion.liberar()
                return True
        return False

# Crear instancias y mostrar la interacción
hotel = Hotel("Hotel Python")

# Agregar habitaciones al hotel
hotel.agregar_habitacion(Habitacion(101, "Individual", 50))
hotel.agregar_habitacion(Habitacion(102, "Doble", 75))
hotel.agregar_habitacion(Habitacion(103, "Suite", 150))

# Mostrar habitaciones
print("Estado inicial de las habitaciones:")
hotel.mostrar_habitaciones()

# Reservar una habitación
print("\nReservando la habitación 101...")
hotel.reservar_habitacion(101)
hotel.mostrar_habitaciones()

# Liberar una habitación
print("\nLiberando la habitación 101...")
hotel.liberar_habitacion(101)
hotel.mostrar_habitaciones()