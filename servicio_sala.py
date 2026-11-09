from modelos import Sala
from conexion import SessionLocal
from sqlalchemy import select

def insertar_sala(nombre, capacidad):
    if not isinstance(nombre, str) or not nombre.strip():
        print("Nombre invalido")
        return

    if type(capacidad) is not int or capacidad <= 0:
        print("Capacidad invalida")
        return

    with SessionLocal.begin() as session:
        sala = Sala(nombre=nombre.strip(),capacidad=capacidad)
        session.add(sala)
        print("Sala registrada")


def consultar_salas():
    with SessionLocal() as session:
        stmt = select(Sala)
        salas = session.scalars(stmt)
        for sala in salas:
            print(sala)