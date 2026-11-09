from modelos import Reserva, Sala
from conexion import SessionLocal
from sqlalchemy import select

def registrar_reserva(estudiante, sala_id, fecha):
    if not isinstance(estudiante, str) or not estudiante.strip():
        print("Estudiante inválido")
        return

    if type(sala_id) is not int or sala_id <= 0 or fecha is None:
        print("Datos inválidos")
        return

    with SessionLocal.begin() as session:
        sala = session.get(Sala, sala_id)

        if sala is None:
            print("Sala no encontrada")
            return

        if not sala.disponible:
            print("Sala no disponible")
            return

        reserva = Reserva(estudiante=estudiante.strip(), sala_id=sala_id, fecha=fecha)

        session.add(reserva)
        sala.disponible = False
        print("Reserva registrada")

def consultar_reservas():
    with SessionLocal() as session:
        stmt = select(Reserva)
        reservas = session.scalars(stmt)
        for reserva in reservas:
            print(reserva)

def cancelar_reserva(id_reserva):
    with SessionLocal.begin() as session:
        reserva = session.get(Reserva, id_reserva)

        if reserva is None:
            print("Reserva no encontrada")
            return

        reserva.sala.disponible = True

        session.delete(reserva)

        print("Reserva cancelada")

