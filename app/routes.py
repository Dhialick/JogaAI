from flask import request, render_template, Blueprint
from app.utils import buscar_jogo

bp = Blueprint('main', __name__)

@bp.route("/")
def homepage():
    return render_template("index.html")

@bp.route("/jogos", methods=["GET", "POST"])
def recomendar_jogo():
    lista_de_generos = ['Action', 'Indie', 'Adventure', 'RPG', 'Strategy', 'Shooter', 'Casual', 'Simulation', 'Puzzle', 'Arcade', 'Platformer', 'Massively Multiplayer', 'Racing', 'Sports', 'Fighting', 'Family', 'Board Games', 'Card', 'Educational']
    lista_de_plataformas = {'PC': 4, 'macOS': 5, 'Linux': 6, 'iOS': 3, 'Android': 21, 'PlayStation 4': 18, 'Xbox One': 1, 'Nintendo Switch': 7, 'PlayStation 3': 16, 'Xbox 360': 14, 'Nintendo DS': 9, 'Wii': 11, 'Commodore / Amiga': 166, 'PlayStation 2': 15, 'Nintendo 3DS': 8, 'PlayStation': 27, 'PS Vita': 19, 'PSP': 17, 'PlayStation 5': 187, 'Xbox Series S/X': 186, 'Wii U': 10, 'NES': 49, 'SNES': 79, 'Game Boy Advance': 24, 'Genesis': 167, 'Atari ST': 34, 'Xbox': 80, 'Classic Macintosh': 55, 'GameCube': 105, 'Game Boy': 26, 'Game Boy Color': 43, 'Apple II': 41, 'SEGA Saturn': 107, 'Dreamcast': 106, 'Nintendo 64': 83, 'Atari 8-bit': 25, 'Atari 2600': 23, 'SEGA Master System': 74, 'Game Gear': 77, 'SEGA CD': 119, 'Neo Geo': 12, '3DO': 111, 'Atari 7800': 28, 'Atari 5200': 31, 'Atari Lynx': 46, 'SEGA 32X': 117, 'Jaguar': 112, 'Nintendo DSi': 13, 'Atari Flashback': 22, 'Atari XEGS': 50}
    lista_de_tags = {
        'Singleplayer': 31, '2D': 45, 'Pixel Graphics': 122, '3D': 571, 'Short': 111, 'Horror': 16, 'Steam Achievements': 40847, 'Space': 25, 'Retro': 74, 'Multiplayer': 7, 'Cute': 88, 'Atmospheric': 13, 'First-Person': 8, 'Fantasy': 64, 'fun': 2590, 'Top-Down': 61, 'Funny': 4, 'Exploration': 6, 'Colorful': 165, 'Music': 136, 'Story Rich': 118, 'RPG': 24, 'Steam Cloud': 40849, 'Full controller support': 40836, 'Family Sharing': 91686, 'Sci-fi': 32, 'Physics': 114, 'Relaxing': 138, 'Action-Adventure': 69, 'Early Access': 14, 'Dark': 41, 'Minimalist': 112, 'Anime': 134, 'Mystery': 117, 'friends': 744, 'combat': 1465, 'Point & Click': 141, 'Female Protagonist': 189, 'FPS': 30, 'Roguelike': 639, 'Comedy': 123, 'Controller': 115, 'Difficult': 49, 'Third Person': 149, 'Local Multiplayer': 72, 'Co-op': 18, 'Partial Controller Support': 40845, 'VR': 33, 'challenge': 1863, "Shoot 'Em Up": 56}
    lista_de_lojas = ['Steam', 'Playstation Store', 'Xbox Store', 'App Store', 'GOG', 'Nintendo Store', 'Xbox 360 Store', 'Google Play', 'itch.io', 'Epic Games', ]
    
    plataforma = request.form.get('platform')
    genero = request.form.get('genre')
    loja = request.form.get('store')
    year = request.form.get('year')
    tag = request.form.get('tag')
    
    recomendacao = buscar_jogo(plataforma=plataforma, genero=genero, loja=loja, ano_lancamento=year, tag=tag)
    
    if recomendacao:
        dados = {
            "id": recomendacao.id,
            "titulo": recomendacao.name,
            "generos": recomendacao.genres,
            "plataformas": recomendacao.platforms,
            "loja": recomendacao.stores,
            "lancamento": recomendacao.released_date,
            "tags": recomendacao.tags,
            "background_image": recomendacao.background_image}
        
        return render_template("recomendar_jogo.html", dados_jogo = dados,
                               plataformas=sorted(lista_de_plataformas),
                               tags=sorted(lista_de_tags),
                               lojas=sorted(lista_de_lojas),
                               generos=sorted(lista_de_generos))
    else:
        return({"mensagem": "Nenhum jogo encontrado!"})
            
@bp.route("/filmes")
def recomendar_filme():
    return render_template("recomendar_filme.html")

@bp.route("/series")
def recomendar_serie():
    return render_template("recomendar_serie.html")

@bp.route("/livros")
def recomendar_livro(): 
    return render_template("recomendar_livro.html")