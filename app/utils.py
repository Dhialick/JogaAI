import random
from app.config import HEADERS
from app.models import SessionLocal, Jogo
from sqlalchemy import extract, cast, literal_column
from sqlalchemy.dialects.postgresql import ARRAY, TEXT

## Validação de jogos

lista_de_generos = ['Action', 'Indie', 'Adventure', 'RPG', 'Strategy', 'Shooter', 'Casual', 'Simulation', 'Puzzle', 'Arcade', 'Platformer', 'Massively Multiplayer', 'Racing', 'Sports', 'Fighting', 'Family', 'Board Games', 'Card', 'Educational']
lista_de_plataformas = {'PC': 4, 'macOS': 5, 'Linux': 6, 'iOS': 3, 'Android': 21, 'PlayStation 4': 18, 'Xbox One': 1, 'Nintendo Switch': 7, 'PlayStation 3': 16, 'Xbox 360': 14, 'Nintendo DS': 9, 'Wii': 11, 'Commodore / Amiga': 166, 'PlayStation 2': 15, 'Nintendo 3DS': 8, 'PlayStation': 27, 'PS Vita': 19, 'PSP': 17, 'PlayStation 5': 187, 'Xbox Series S/X': 186, 'Wii U': 10, 'NES': 49, 'SNES': 79, 'Game Boy Advance': 24, 'Genesis': 167, 'Atari ST': 34, 'Xbox': 80, 'Classic Macintosh': 55, 'GameCube': 105, 'Game Boy': 26, 'Game Boy Color': 43, 'Apple II': 41, 'SEGA Saturn': 107, 'Dreamcast': 106, 'Nintendo 64': 83, 'Atari 8-bit': 25, 'Atari 2600': 23, 'SEGA Master System': 74, 'Game Gear': 77, 'SEGA CD': 119, 'Neo Geo': 12, '3DO': 111, 'Atari 7800': 28, 'Atari 5200': 31, 'Atari Lynx': 46, 'SEGA 32X': 117, 'Jaguar': 112, 'Nintendo DSi': 13, 'Atari Flashback': 22, 'Atari XEGS': 50}
lista_de_tags = {
            'Singleplayer': 31, '2D': 45, 'Pixel Graphics': 122, '3D': 571, 'Short': 111, 'Horror': 16, 'Steam Achievements': 40847, 'Space': 25, 'Retro': 74, 'Multiplayer': 7, 'Cute': 88, 'Atmospheric': 13, 'First-Person': 8, 'Fantasy': 64, 'fun': 2590, 'Top-Down': 61, 'Funny': 4, 'Exploration': 6, 'Colorful': 165, 'Music': 136, 'Story Rich': 118, 'RPG': 24, 'Steam Cloud': 40849, 'Full controller support': 40836, 'Family Sharing': 91686, 'Sci-fi': 32, 'Physics': 114, 'Relaxing': 138, 'Action-Adventure': 69, 'Early Access': 14, 'Dark': 41, 'Minimalist': 112, 'Anime': 134, 'Mystery': 117, 'friends': 744, 'combat': 1465, 'Point & Click': 141, 'Female Protagonist': 189, 'FPS': 30, 'Roguelike': 639, 'Comedy': 123, 'Controller': 115, 'Difficult': 49, 'Third Person': 149, 'Local Multiplayer': 72, 'Co-op': 18, 'Partial Controller Support': 40845, 'VR': 33, 'challenge': 1863, "Shoot 'Em Up": 56}
lista_de_lojas = ['Steam', 'PlayStation Store', 'Xbox Store', 'App Store', 'GOG', 'Nintendo Store', 'Xbox 360 Store', 'Google Play', 'itch.io', 'Epic Games', ]


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
        return jogos_filtrados
    else:
        return None
    
## Validação de Filmes
