from app.config import HEADERS
from app.models import SessionLocal, Jogo, Serie
from sqlalchemy import extract, cast, literal_column
from sqlalchemy.dialects.postgresql import ARRAY, TEXT

## Validação de jogos

lista_de_generos_jogos = ['Action', 'Indie', 'Adventure', 'RPG', 'Strategy', 'Shooter', 'Casual', 'Simulation', 'Puzzle', 'Arcade', 'Platformer', 'Massively Multiplayer', 'Racing', 'Sports', 'Fighting', 'Family', 'Board Games', 'Card', 'Educational']
lista_de_plataformas_jogos = {'PC': 4, 'macOS': 5, 'Linux': 6, 'iOS': 3, 'Android': 21, 'PlayStation 4': 18, 'Xbox One': 1, 'Nintendo Switch': 7, 'PlayStation 3': 16, 'Xbox 360': 14, 'Nintendo DS': 9, 'Wii': 11, 'Commodore / Amiga': 166, 'PlayStation 2': 15, 'Nintendo 3DS': 8, 'PlayStation': 27, 'PS Vita': 19, 'PSP': 17, 'PlayStation 5': 187, 'Xbox Series S/X': 186, 'Wii U': 10, 'NES': 49, 'SNES': 79, 'Game Boy Advance': 24, 'Genesis': 167, 'Atari ST': 34, 'Xbox': 80, 'Classic Macintosh': 55, 'GameCube': 105, 'Game Boy': 26, 'Game Boy Color': 43, 'Apple II': 41, 'SEGA Saturn': 107, 'Dreamcast': 106, 'Nintendo 64': 83, 'Atari 8-bit': 25, 'Atari 2600': 23, 'SEGA Master System': 74, 'Game Gear': 77, 'SEGA CD': 119, 'Neo Geo': 12, '3DO': 111, 'Atari 7800': 28, 'Atari 5200': 31, 'Atari Lynx': 46, 'SEGA 32X': 117, 'Jaguar': 112, 'Nintendo DSi': 13, 'Atari Flashback': 22, 'Atari XEGS': 50}
lista_de_tags_jogos = {
            'Singleplayer': 31, '2D': 45, 'Pixel Graphics': 122, '3D': 571, 'Short': 111, 'Horror': 16, 'Steam Achievements': 40847, 'Space': 25, 'Retro': 74, 'Multiplayer': 7, 'Cute': 88, 'Atmospheric': 13, 'First-Person': 8, 'Fantasy': 64, 'fun': 2590, 'Top-Down': 61, 'Funny': 4, 'Exploration': 6, 'Colorful': 165, 'Music': 136, 'Story Rich': 118, 'RPG': 24, 'Steam Cloud': 40849, 'Full controller support': 40836, 'Family Sharing': 91686, 'Sci-fi': 32, 'Physics': 114, 'Relaxing': 138, 'Action-Adventure': 69, 'Early Access': 14, 'Dark': 41, 'Minimalist': 112, 'Anime': 134, 'Mystery': 117, 'friends': 744, 'combat': 1465, 'Point & Click': 141, 'Female Protagonist': 189, 'FPS': 30, 'Roguelike': 639, 'Comedy': 123, 'Controller': 115, 'Difficult': 49, 'Third Person': 149, 'Local Multiplayer': 72, 'Co-op': 18, 'Partial Controller Support': 40845, 'VR': 33, 'challenge': 1863, "Shoot 'Em Up": 56}
lista_de_lojas_jogos = ['Steam', 'PlayStation Store', 'Xbox Store', 'App Store', 'GOG', 'Nintendo Store', 'Xbox 360 Store', 'Google Play', 'itch.io', 'Epic Games', ]


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
    
## Validação de Series

lista_de_generos_series = {"Ação e Aventura": 10759, "Animação": 16, "Comédia":35, "Crime":80, "Documentário": 99, "Drama": 18, "Família": 10751, "Infantil": 10762, "Mistério": 9648, "Notícias": 10763, "Reality": 10764, "Sci-fi e Fantasia": 10765, "Novela": 10766, "Conversa": 10766, "Guerra e Política": 10768, "Faroeste": 37}

lista_de_idiomas_series = {"Bósnio": "bs",
    "Francês": "fr",
    "Panjabi": "pa",
    "Eslovaco": "sk",
    "Inglês": "en",
    "Hindi": "hi",
    "Africâner": "af",
    "Búlgaro": "bg",
    "Russo": "ru",
    "Hebraico": "he",
    "Persa": "fa",
    "Guzerate": "gu",
    "Croata": "hr",
    "Sem idioma / Indeterminado": "xx",
    "Tcheco": "cs",
    "Japonês": "ja",
    "Lituano": "lt",
    "Georgiano": "ka",
    "Cantonês": "cn",
    "Basco": "eu",
    "Romeno": "ro",
    "Telugu": "te",
    "Tâmil": "ta",
    "Zulu": "zu",
    "Malaio": "ms",
    "Estoniano": "et",
    "Árabe": "ar",
    "Catalão": "ca",
    "Tailandês": "th",
    "Português": "pt",
    "Urdu": "ur",
    "Khmer": "km",
    "Húngaro": "hu",
    "Polonês": "pl",
    "Chinês": "zh",
    "Letão": "lv",
    "Espanhol": "es",
    "Irlandês": "ga",
    "Sérvio": "sr",
    "Hauçá": "ha",
    "Turco": "tr",
    "Finlandês": "fi",
    "Ucraniano": "uk",
    "Marata": "mr",
    "Vietnamita": "vi",
    "Islandês": "is",
    "Sueco": "sv",
    "Canarês": "kn",
    "Bengali": "bn",
    "Alemão": "de",
    "Holandês": "nl",
    "Indonésio": "id",
    "Tagalo": "tl",
    "Esloveno": "sl",
    "Norueguês": "no",
    "Grego": "el",
    "Norueguês Bokmål": "nb",
    "Coreano": "ko",
    "Malaiala": "ml",
    "Italiano": "it",
    "Dinamarquês": "da",
    "Servo-croata": "sh",
}

lista_de_paises_series = {
    "Albânia": "AL",
    "Emirados Árabes Unidos": "AE",
    "Argentina": "AR",
    "Áustria": "AT",
    "Austrália": "AU",
    "Aruba": "AW",
    "Bangladesh": "BD",
    "Bélgica": "BE",
    "Bulgária": "BG",
    "Brasil": "BR",
    "Bielorrússia": "BY",
    "Belize": "BZ",
    "Canadá": "CA",
    "Suíça": "CH",
    "Chile": "CL",
    "Camarões": "CM",
    "China": "CN",
    "Colômbia": "CO",
    "Croácia": "HR",
    "Chéquia": "CZ",
    "Alemanha": "DE",
    "Dinamarca": "DK",
    "Argélia": "DZ",
    "Equador": "EC",
    "Estônia": "EE",
    "Egito": "EG",
    "Espanha": "ES",
    "Finlândia": "FI",
    "França": "FR",
    "Reino Unido": "GB",
    "Geórgia": "GE",
    "Grécia": "GR",
    "Guiné-Bissau": "GW",
    "Hong Kong": "HK",
    "Hungria": "HU",
    "Indonésia": "ID",
    "Irlanda": "IE",
    "Israel": "IL",
    "Índia": "IN",
    "Território Britânico do Oceano Índico": "IO",
    "Iraque": "IQ",
    "Irã": "IR",
    "Islândia": "IS",
    "Itália": "IT",
    "Jamaica": "JM",
    "Jordânia": "JO",
    "Japão": "JP",
    "Camboja": "KH",
    "Coreia do Norte": "KP",
    "Coreia do Sul": "KR",
    "Kuwait": "KW",
    "Líbano": "LB",
    "Lituânia": "LT",
    "Letônia": "LV",
    "Líbia": "LY",
    "Malta": "MT",
    "México": "MX",
    "Malásia": "MY",
    "Nigéria": "NG",
    "Países Baixos": "NL",
    "Noruega": "NO",
    "Nova Zelândia": "NZ",
    "Peru": "PE",
    "Filipinas": "PH",
    "Paquistão": "PK",
    "Polônia": "PL",
    "Porto Rico": "PR",
    "Portugal": "PT",
    "Paraguai": "PY",
    "Romênia": "RO",
    "Sérvia": "RS",
    "Rússia": "RU",
    "Arábia Saudita": "SA",
    "Suécia": "SE",
    "Singapura": "SG",
    "Eslovênia": "SI",
    "Eslováquia": "SK",
    "União Soviética": "SU", # Nota: Código obsoleto
    "Síria": "SY",
    "Tailândia": "TH",
    "Tunísia": "TN",
    "Turquia": "TR",
    "Trinidad e Tobago": "TT",
    "Taiwan": "TW",
    "Ucrânia": "UA",
    "Estados Unidos": "US",
    "Venezuela": "VE",
    "Vietnã": "VN",
    "Checoslováquia": "XC", # Nota: Código obsoleto
    "Alemanha Oriental": "XG", # Nota: Código obsoleto
    "Iugoslávia": "YU", # Nota: Código obsoleto
    "África do Sul": "ZA",
}

def buscar_serie(genero = None, ano = None, pais = None, idioma = None):
    session = SessionLocal()
    query = session.query(Serie)
    
    if genero:
        codigo_genero = lista_de_generos_series.get(genero)
        if codigo_genero:
            query = query.filter(Serie.genres.contains([codigo_genero]))
    if ano:
        query = query.filter(extract('year', Serie.first_air_date) == int(ano))
    if pais:
        codigo_pais = lista_de_paises_series.get(pais)
        if codigo_pais:
            query = query.filter(Serie.origin_country.contains(codigo_pais))
    if idioma:
        codigo_idioma = lista_de_idiomas_series.get(idioma)
        if codigo_idioma:
            query = query.filter(Serie.original_language.contains(codigo_idioma))
        
    series_filtradas = query.all()
    session.close()
    
    if series_filtradas:
        return series_filtradas
    
    return None