from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///reservas.db", echo= False)
SessionLocal = sessionmaker(bind=engine)