from flask import Flask, render_template, request
import requests, os, random

app = Flask(__name__)

rawg_api_key = os.getenv("RAWG_API_KEY")

def get_rawg_data(endpoint_path):
    complete_data_map = {}
    page = 1
    has_next = True
    
    while has_next:
        endpoint_url = (f"https://api.rawg.io/api/{endpoint_path}?key={rawg_api_key}&page={page}&page_size=100")
        
        try:
            response = requests.get(endpoint_url)
            response.raise_for_status()
            raw_data_map = response.json()
            
            for item in raw_data_map.get("results", []):
                name = item.get("name")
                
                if endpoint_path == "genres":
                    value = item.get("slug")
                else:
                    value = item.get("id")
                
                if name and value:
                    complete_data_map[name] = str(value)
                    
            has_next = bool(raw_data_map.get("next"))
            page += 1
            
        except requests.exceptions.RequestException as e:
            print(f"erro na requisição: {e}")
            break
        
    return complete_data_map

lista_de_generos = get_rawg_data("genres")
lista_de_plataformas = get_rawg_data("platforms")
lista_de_publisher = get_rawg_data("publishers")
lista_de_tags = get_rawg_data("tags")
lista_de_lojas = get_rawg_data("stores")

def get_game_list(escolhas):
    page = 1
    base_url = f"https://api.rawg.io/api/games?key={rawg_api_key}&page={page}&page_size=1000"
            
    for chave, item in escolhas.items():
        if item is not None:
            base_url += f"&{chave}={item}"
      
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        raw_game_list = response.json()
        raw_game_list = raw_game_list.get("results", [])
        return raw_game_list

    except requests.exceptions.RequestException as e:
        print(f"erro ao buscar lista de jogos: {e}")
        return []

@app.route("/", methods=["GET", "POST"])
def homepage():
    game_recommendation = None
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
    
    return render_template("index.html", generos=sorted(lista_de_generos),
                                        plataformas=sorted(lista_de_plataformas),
                                        publishers=sorted(lista_de_publisher),
                                        tags=sorted(lista_de_tags),
                                        lojas=sorted(lista_de_lojas),
                                        game = game_recommendation)


if __name__ == "__main__":
    app.run(debug=True)