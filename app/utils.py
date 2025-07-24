import requests, time
from app.config import HEADERS, rawg_api_key

def get_rawg_data(endpoint_path):
    complete_data_map = {}
    page = 1
    has_next = True
    
    while has_next:
        endpoint_url = (f"https://api.rawg.io/api/{endpoint_path}?key={rawg_api_key}&page={page}&page_size=100")
        
        try:
            response = requests.get(endpoint_url, headers=HEADERS)
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
            time.sleep(1)
            
        except requests.exceptions.RequestException as e:
            print(f"erro na requisição: {e}")
            break
        
    return complete_data_map


def get_game_list(escolhas):
    page = 1
    base_url = f"https://api.rawg.io/api/games?key={rawg_api_key}&page={page}&page_size=1000"
            
    for chave, item in escolhas.items():
        if item is not None:
            base_url += f"&{chave}={item}"
      
    try:
        response = requests.get(base_url, headers=HEADERS)
        response.raise_for_status()
        raw_game_list = response.json()
        raw_game_list = raw_game_list.get("results", [])
        return raw_game_list

    except requests.exceptions.RequestException as e:
        print(f"erro ao buscar lista de jogos: {e}")
        return []


