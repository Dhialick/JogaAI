from flask import Flask, render_template, request
import requests, os, random

app = Flask(__name__)

rawg_api_key = os.getenv("RAWG_API_KEY")

def get_rawg_data(endpoint_path):
    endpoint_url = f"https://api.rawg.io/api/{endpoint_path}?key={rawg_api_key}"
    complete_data_map = {}

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
        
        return complete_data_map
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição {e}")

def get_big_rawg_data(endpoint_path):
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
lista_de_publisher = get_big_rawg_data("publishers")
lista_de_tags = get_big_rawg_data("tags")
lista_de_lojas = get_rawg_data("stores")

@app.route("/", methods=["GET"])
def homepage():        
        return render_template("index.html", generos=sorted(lista_de_generos),
                                            plataformas=sorted(lista_de_plataformas),
                                            publishers=sorted(lista_de_publisher),
                                            tags=sorted(lista_de_tags),
                                            lojas=sorted(lista_de_lojas))

@app.route("/resultado")
def resultado():
    return render_template("resultado.html")

if __name__ == "__main__":
    app.run(debug=True)