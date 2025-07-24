from flask import request, render_template, Blueprint
from app.utils import get_game_list, get_rawg_data
import random

bp = Blueprint('main', __name__)

@bp.route("/", methods=["GET", "POST"])
def homepage():
    game_recommendation = None
    
    lista_de_generos = get_rawg_data("genres")
    lista_de_plataformas = get_rawg_data("platforms")
    lista_de_publisher ={
        'Electronic Arts': 354, 'SEGA': 3408, 'Nintendo': 10681, 'Ubisoft Entertainment': 918, 'Konami': 10691, 'Activision Blizzard': 10830, 'Capcom': 2150, 'Bandai Namco Entertainment': 8352, 'Square Enix': 308, 'Atari': 1779, 'Microsoft Studios': 20987, 'THQ': 6062, 'Sony Computer Entertainment': 10212, 'Disney Interactive': 250, 'Alawar Entertainment': 3693, 'Sony Interactive Entertainment': 11687, 'Paradox Interactive': 3656, 'Plug In Digital': 515, 'PlayWay': 10392, 'Strategy First': 4253, 'Sierra On-Line': 11434, 'Atlus': 9065, 'THQ Nordic': 1283, 'Interplay Productions': 11483, 'SNK': 11893, 'Infogrames': 11453, '2K Games': 358, 'Namco': 10901, 'Warner Bros. Interactive': 350, 'Sekai Project': 3169, 'Microids': 1287, 'Taito': 10867, 'Majesco Entertainment': 1034, 'Acclaim Entertainment': 11433, 'D3 Publisher': 10782, 'Deep Silver': 311, 'Bethesda Softworks': 339, 'Devolver Digital': 1307, 'Koei Tecmo Games': 14676, '505 Games': 243, 'NIS America': 10695, '1C Company': 3370, 'Codemasters': 1294, 'Activision Value Publishing': 11620, 'Slitherine': 14672, 'Gameloft': 35, 'Team17 Digital': 402, 'BANDAI NAMCO Entertainment US': 31896, 'Kiss': 9835, 'Focus Home Interactive': 713}
    lista_de_tags = {
        'Singleplayer': 31, '2D': 45, 'Pixel Graphics': 122, '3D': 571, 'Short': 111, 'Horror': 16, 'Steam Achievements': 40847, 'Space': 25, 'Retro': 74, 'Multiplayer': 7, 'Cute': 88, 'Atmospheric': 13, 'First-Person': 8, 'Fantasy': 64, 'fun': 2590, 'Top-Down': 61, 'Funny': 4, 'Exploration': 6, 'Colorful': 165, 'Music': 136, 'Story Rich': 118, 'RPG': 24, 'Steam Cloud': 40849, 'Full controller support': 40836, 'Family Sharing': 91686, 'Sci-fi': 32, 'Physics': 114, 'Relaxing': 138, 'Action-Adventure': 69, 'Early Access': 14, 'Dark': 41, 'Minimalist': 112, 'Anime': 134, 'Mystery': 117, 'friends': 744, 'combat': 1465, 'Point & Click': 141, 'Female Protagonist': 189, 'FPS': 30, 'Roguelike': 639, 'Comedy': 123, 'Controller': 115, 'Difficult': 49, 'Third Person': 149, 'Local Multiplayer': 72, 'Co-op': 18, 'Partial Controller Support': 40845, 'VR': 33, 'challenge': 1863, "Shoot 'Em Up": 56}
    lista_de_lojas = get_rawg_data("stores")
    
    if request.method == "POST":
        nome_genero = request.form.get("genre")
        nome_plataforma = request.form.get("platform")
        nome_publisher = request.form.get("publisher")
        nome_tag = request.form.get("tag")
        nome_store = request.form.get("store")
        
        id_genero = lista_de_generos.get(nome_genero)
        id_plataforma = lista_de_plataformas.get(nome_plataforma)
        id_publisher = lista_de_publisher.get(nome_publisher)
        id_tag = lista_de_tags.get(nome_tag)
        id_store = lista_de_lojas.get(nome_store)
        
        escolhas = {"genres": id_genero, "platforms": id_plataforma,"publishers": id_publisher, "tags": id_tag, "stores": id_store}
        
        raw_game_data = get_game_list(escolhas)
        game_recommendation = None    
        if raw_game_data:
            game_recommendation = random.choice(raw_game_data)        
    
        return render_template("recomendar_jogo.html", generos=sorted(lista_de_generos),
                                            plataformas=sorted(lista_de_plataformas),
                                            publishers=sorted(lista_de_publisher),
                                            tags=sorted(lista_de_tags),
                                            lojas=sorted(lista_de_lojas),
                                            game = game_recommendation)
    else: 
            return render_template("recomendar_jogo.html", generos=sorted(lista_de_generos),
                                        plataformas=sorted(lista_de_plataformas),
                                        publishers=sorted(lista_de_publisher),
                                        tags=sorted(lista_de_tags),
                                        lojas=sorted(lista_de_lojas),
                                        game = game_recommendation)