from flask import request, render_template, Blueprint
from app.utils import buscar_jogo, lista_de_generos, lista_de_lojas, lista_de_plataformas, lista_de_tags

bp = Blueprint('main', __name__)

@bp.route("/")
def homepage():
    return render_template("index.html")

@bp.route("/jogos", methods=["GET", "POST"])
def recomendar_jogo():
    
    if request.method == 'POST':
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
            
            return render_template("recomendar_jogo.html",dados_jogo = dados,
                                plataformas=sorted(lista_de_plataformas),
                                tags=sorted(lista_de_tags),
                                lojas=sorted(lista_de_lojas),
                                generos=sorted(lista_de_generos))
    else:
        return render_template("recomendar_jogo.html",
                               dados_jogo=None,
                               plataformas=sorted(lista_de_plataformas),
                               tags=sorted(lista_de_tags),
                               lojas=sorted(lista_de_lojas),
                               generos=sorted(lista_de_generos))
            
@bp.route("/filmes")
def recomendar_filme():
    return render_template("recomendar_filme.html")

@bp.route("/series")
def recomendar_serie():
    return render_template("recomendar_serie.html")

@bp.route("/livros")
def recomendar_livro(): 
    return render_template("recomendar_livro.html")

@bp.route("/teste")
def teste():
    return render_template("recomendar_jogo.html")