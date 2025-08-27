from flask import request, render_template, Blueprint, session
from app.utils import buscar_jogo, lista_de_generos_jogos, lista_de_lojas_jogos, lista_de_plataformas_jogos, lista_de_tags_jogos, lista_de_paises_series, lista_de_generos_series, lista_de_idiomas_series, buscar_serie
import random

bp = Blueprint('main', __name__)

@bp.route("/")
def homepage():
    return render_template("index.html")

@bp.route("/login")
def fazerLogin():
    return render_template("paginaLogin.html")

@bp.route("/jogos", methods=["GET", "POST"])
def recomendar_jogo():
    
    if request.method == 'POST':
        plataforma = request.form.get('platform')
        genero = request.form.get('genre')
        loja = request.form.get('store')
        year = request.form.get('year')
        tag = request.form.get('tag')
        
        funcao_busca = buscar_jogo(plataforma=plataforma, genero=genero, loja=loja, ano_lancamento=year, tag=tag)
        
        qtd_filtrados = len(funcao_busca)
        recomendacao = random.choice(funcao_busca)
        
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
            
            return render_template("recomendar_jogo.html",
                                dados_jogo=dados,
                                plataformas=sorted(lista_de_plataformas_jogos),
                                tags=sorted(lista_de_tags_jogos),
                                lojas=sorted(lista_de_lojas_jogos),
                                generos=sorted(lista_de_generos_jogos),
                                erro=None,
                                buscou=True,
                                qtd_filtrados=qtd_filtrados)
        else:
            return render_template("recomendar_jogo.html",
                                dados_jogo=None,
                                plataformas=sorted(lista_de_plataformas_jogos),
                                tags=sorted(lista_de_tags_jogos),
                                lojas=sorted(lista_de_lojas_jogos),
                                generos=sorted(lista_de_generos_jogos),
                                erro="Nenhum jogo encontrado com os critérios selecionados",
                                buscou=True,)

    return render_template("recomendar_jogo.html",
                        dados_jogo=None,
                        plataformas=sorted(lista_de_plataformas_jogos),
                        tags=sorted(lista_de_tags_jogos),
                        lojas=sorted(lista_de_lojas_jogos),
                        generos=sorted(lista_de_generos_jogos),
                        erro=None,
                        buscou=False)

@bp.route("/filmes", methods=["POST", "GET"])
def recomendar_filme():
    
    return render_template("recomendar_filme.html")

@bp.route("/series", methods=["POST", "GET"])
def recomendar_serie():
    
    if request.method == "POST":
        genero = request.form.get("genre")
        ano = request.form.get("year")
        pais = request.form.get("country")
        idioma = request.form.get("language")
    
        funcao_busca = buscar_serie(genero=genero, ano=ano, pais=pais, idioma=idioma)
        qtd_filtrados = len(funcao_busca)
        recomendacao = random.choice(funcao_busca)
        
        if recomendacao:
            dados = {
                "id": recomendacao.id,
                "name":recomendacao.name,
                "genres": recomendacao.genres,
                "first_air_date": recomendacao.first_air_date,
                "poster_path": recomendacao.poster_path,
                "origin_country": recomendacao.origin_country,
                "original_language": recomendacao.original_language,
                "original_name": recomendacao.original_name,
                "overview": recomendacao.overview
                }
        
            return render_template("recomendar_serie.html", generos=sorted(lista_de_generos_series),
                                                        pais_origem=sorted(lista_de_paises_series),
                                                        idiomas=sorted(lista_de_idiomas_series),
                                                        qtd_filtrados=qtd_filtrados,
                                                        dados_serie=dados,
                                                        erro=None,
                                                        buscou=True)
        else:
            return render_template("recomendar_serie.html", generos=sorted(lista_de_generos_series),
                                                        pais_origem=sorted(lista_de_paises_series),
                                                        idiomas=sorted(lista_de_idiomas_series),
                                                        qtd_filtrados=qtd_filtrados,
                                                        dados_serie=dados,
                                                        erro="Nenhuma Serie encontrada com esse filtro",
                                                        buscou=True)
    
    return render_template("recomendar_serie.html", generos=sorted(lista_de_generos_series),
                                                    pais_origem=sorted(lista_de_paises_series),
                                                    idiomas=sorted(lista_de_idiomas_series))

@bp.route("/livros")
def recomendar_livro(): 
    return render_template("recomendar_livro.html")
