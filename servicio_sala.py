from modelos import Sala
from conexion import SessionLocal
from sqlalchemy import select

def insertar_sala(nombre, capacidad):
    if not isinstance(nombre, str) or not nombre.strip():
        print("Nombre inválido")
        return

    if type(capacidad) is not int or capacidad <= 0:
        print("Capacidad inválida")
        return

    with SessionLocal.begin() as session:
        sala = Sala(nombre=nombre.strip(),capacidad=capacidad)
        session.add(sala)


def consultar_salas():
    with SessionLocal() as session:
        stmt = select(Sala)
        salas = session.scalars(stmt)
        for sala in salas:
            print(sala)