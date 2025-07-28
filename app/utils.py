import requests, time, random
from app.config import HEADERS, rawg_api_key
from app.models import SessionLocal, Jogo
from sqlalchemy import extract, cast, literal_column
from sqlalchemy.dialects.postgresql import ARRAY, TEXT

def buscar_jogo(plataforma = None, genero = None, loja = None, ano_lancamento = None, tag = None):
    session = SessionLocal()
    query = session.query(Jogo)
    
    if plataforma:
        query = query.filter(Jogo.platforms.contains(cast([plataforma], ARRAY(TEXT))))
    if genero:
        query = query.filter(Jogo.genres.contains(cast([genero], ARRAY(TEXT))))
    if loja:
        query = query.filter((Jogo.stores.contains(cast([loja], ARRAY(TEXT)))))
    if tag:
        query = query.filter((Jogo.tags.contains(cast([tag], ARRAY(TEXT)))))
    if ano_lancamento:
        query = query.filter(extract('year', Jogo.released_date) == int(ano_lancamento))
        
    jogos_filtrados = query.all()
    session.close()
    
    if jogos_filtrados:
        return random.choice(jogos_filtrados)
    else:
        return None