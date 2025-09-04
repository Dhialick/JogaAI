from flask import request, render_template, Blueprint, session
from app.utils import buscar_jogo, lista_de_generos_jogos, lista_de_lojas_jogos, lista_de_plataformas_jogos, lista_de_tags_jogos, lista_de_paises_series, lista_de_generos_series, lista_de_idiomas_series, buscar_serie, buscar_filme, lista_de_generos_filmes, lista_de_idiomas_filmes
import random

bp = Blueprint('main', __name__)

@bp.route("/")
def homepage():
    return render_template("index.html")

@bp.route("/login")
def fazerLogin():
    return render_template("paginaLogin.html")


@bp.route("/sobre")
def sobre_nos():
    return render_template("sobre.html")

## Rotas de Recomendações

@bp.route("/jogos", methods=["GET", "POST"])
def recomendar_jogo():
    
    plataforma = genero = loja = tag = year = None
    
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
                                qtd_filtrados=qtd_filtrados,
                                plataforma=plataforma,
                                genero=genero,
                                loja=loja,
                                year=year,
                                tag=tag)
        else:
            return render_template("recomendar_jogo.html",
                                dados_jogo=None,
                                plataformas=sorted(lista_de_plataformas_jogos),
                                tags=sorted(lista_de_tags_jogos),
                                lojas=sorted(lista_de_lojas_jogos),
                                generos=sorted(lista_de_generos_jogos),
                                erro="Nenhum jogo encontrado com os critérios selecionados",
                                buscou=True,
                                plataforma=plataforma,
                                genero=genero,
                                loja=loja,
                                year=year,
                                tag=tag)

    return render_template("recomendar_jogo.html",
                        dados_jogo=None,
                        plataformas=sorted(lista_de_plataformas_jogos),
                        tags=sorted(lista_de_tags_jogos),
                        lojas=sorted(lista_de_lojas_jogos),
                        generos=sorted(lista_de_generos_jogos),
                        erro=None,
                        buscou=False,
                        plataforma=plataforma,
                        genero=genero,
                        loja=loja,
                        year=year,
                        tag=tag)

@bp.route("/filmes", methods=["POST", "GET"])
def recomendar_filme():
    
    genre = year = language = None
    
    if request.method == "POST":
        genero = request.form.get("genre")
        ano = request.form.get("year")
        idioma = request.form.get("language")
    
        funcao_busca = buscar_filme(genero=genero, ano=ano, idioma=idioma)
        qtd_filtrados = len(funcao_busca)
        recomendacao = random.choice(funcao_busca)
        
        if recomendacao:
            dados = {"id": recomendacao.id,
                     "title": recomendacao.title,
                     "synopsis": recomendacao.synopsis,
                     "original_language": recomendacao.original_language,
                     "release_date": recomendacao.release_date,
                     "genres": recomendacao.genres,
                     "poster_url": recomendacao.poster_url
                     }
            
            return render_template("recomendar_filme.html",
                       genres=sorted(list(lista_de_generos_filmes.values())),
                       languages=sorted(list(lista_de_idiomas_filmes.keys())),
                       year=ano,
                       qtd_filtrados=qtd_filtrados,
                       erro=None,
                       buscou=True,
                       dados_filme=dados)

            
        else:
            return render_template("recomendar_filme.html", generos=sorted(lista_de_generos_filmes),
                                                            idioma=sorted(lista_de_idiomas_filmes),
                                                            ano=ano,
                                                            qtd_filtrados=qtd_filtrados,
                                                            buscou=True,
                                                            mensagem="Nenhum Filme encontrada com esse filtro",
                                                            dados_filme=dados,
                                                            genre=genre,
                                                            year=year,
                                                            language=language
                                                            )
    
    
    return render_template("recomendar_filme.html")

@bp.route("/series", methods=["POST", "GET"])
def recomendar_serie():
    
    genre = year = country = language = None
    
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
        
            return render_template("recomendar_serie.html", generos=sorted(lista_de_generos_series.keys()),
                                                        pais_origem=sorted(lista_de_paises_series),
                                                        idiomas=sorted(lista_de_idiomas_series),
                                                        qtd_filtrados=qtd_filtrados,
                                                        dados_serie=dados,
                                                        erro=None,
                                                        buscou=True,
                                                        genre=genre,
                                                        year=year,
                                                        country=country,
                                                        language=language)
        else:
            return render_template("recomendar_serie.html", generos=sorted(lista_de_generos_series),
                                                        pais_origem=sorted(lista_de_paises_series),
                                                        idiomas=sorted(lista_de_idiomas_series),
                                                        qtd_filtrados=qtd_filtrados,
                                                        dados_serie=dados,
                                                        erro="Nenhuma Serie encontrada com esse filtro",
                                                        buscou=True,
                                                        genre=genre,
                                                        year=year,
                                                        country=country,
                                                        language=language)
    
    return render_template("recomendar_serie.html", generos=sorted(lista_de_generos_series),
                                                    pais_origem=sorted(lista_de_paises_series),
                                                    idiomas=sorted(lista_de_idiomas_series),
                                                    genre=genre,
                                                    year=year,
                                                    country=country,
                                                    language=language)

@bp.route("/livros")
def recomendar_livro(): 
    return render_template("recomendar_livro.html")
