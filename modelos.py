from datetime import datetime
from sqlalchemy import String, Integer, Boolean , CheckConstraint, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase ,Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Sala(Base):
    __tablename__ = "sala"

    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=True)
    capacidad: Mapped[int] = mapped_column(Integer, nullable= False)
    disponible: Mapped[bool] = mapped_column(Boolean, default=True)

    reservas: Mapped[list["Reserva"]] = relationship(back_populates="sala")

    __table_args__ = (
        CheckConstraint("capacidad > 0", name= "Capacidad_mayor_que_cero"),
    )

    def __repr__(self) -> str:
        return f"""
        ---- Sala ----
        ID: {self.id}
        Nombre: {self.nombre}
        Capacidad: {self.capacidad}
        Disponible: {self.disponible}
    """
class Reserva(Base):
    __tablename__ = "reserva"

    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    estudiante: Mapped[str] = mapped_column(String(100), nullable= False)
    sala_id: Mapped[int] = mapped_column(ForeignKey("sala.id"), nullable=False)
    fecha: Mapped[datetime] = mapped_column(DateTime, nullable= False)


    sala: Mapped["Sala"] = relationship(
        back_populates="reservas"
    )
    def __repr__(self) -> str:
        return f"""
        ---- Sala ----
        ID: {self.id}
        Reservado por: {self.estudiante}
        Sala: {self.sala_id}
        Fecha: {self.fecha}
    """