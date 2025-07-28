from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import db_login, db_senha

database_url = f"postgresql://{db_login}:{db_senha}@localhost:5432/jogaai"

engine = create_engine(database_url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Jogo(Base):
    __tablename__ = "jogaai_jogos"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    released_date = Column(Date)
    background_image = Column(String)
    platforms = Column(ARRAY(String))
    tags = Column(ARRAY(String))
    stores = Column(ARRAY(String))
    genres = Column(ARRAY(String))
