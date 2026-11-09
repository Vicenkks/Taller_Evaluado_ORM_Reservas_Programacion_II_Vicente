from conexion import engine
from modelos import Base
from servicio_reserva import *
from servicio_sala import *
from datetime import datetime

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    while True:
        print("""
        ========== SISTEMA DE BIBLIOTECA ==========
        1. Registrar sala
        2. Consultar salas
        3. Registrar reserva
        4. Consultar reservas
        5. Cancelar reserva
        0. Salir
        """)

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número")
            continue

        if opcion == 0:
            break

        elif opcion == 1:
            nombre = input("Nombre de la sala: ")
            try:
                capacidad = int(input("Capacidad: "))
            except ValueError:
                print("La capacidad debe ser un número entero")
                continue

            insertar_sala(nombre, capacidad)

        elif opcion == 2:
            consultar_salas()

        elif opcion == 3:
            estudiante = input("Nombre del estudiante: ")

            try:
                sala_id = int(input("ID de la sala: "))
                fecha = datetime.strptime(input("Fecha AAAA-MM-DD: "), "%Y-%m-%d")
            except ValueError:
                print("ID o fecha inválida")
                continue

            registrar_reserva(estudiante, sala_id, fecha)

        elif opcion == 4:
            consultar_reservas()

        elif opcion == 5:
            try:
                id_reserva = int(input("ID de la reserva: "))
            except ValueError:
                print("ID inválido")
                continue

            cancelar_reserva(id_reserva)

        else:
            print("Opción inválida")