import requests
base_url="https://pokeapi.co/api/v2"

def all_pokemons():
    url=f"{base_url}/pokemon?limit=1025"
    response=requests.get(url)
    if response.status_code==200:
        results= response.json()
        pokemons=[]
        for i in results["results"]:
            id_=i["url"].split("/")[-2]
            pokemons.append({"name":i["name"],"id":id_})        
    return pokemons
        

def get_pokemon_info(name):

    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    if response.status_code==200:
        pokemon_info=response.json()
        pokemon_data={
            "name":pokemon_info["name"],
            "id":pokemon_info["id"],
            "height":pokemon_info["height"],
            "weight":pokemon_info["weight"],
            "types":[t["type"]["name"] for t in pokemon_info["types"]],
            "abilities":[a["ability"]["name"] for a in pokemon_info["abilities"]],
            "stats":{s["stat"]["name"]:s["base_stat"] for s in pokemon_info["stats"]},
            "sprite":pokemon_info["sprites"]["other"]["official-artwork"]["front_default"]
        }
        return pokemon_data
    else:
        print(f"failed to retrive data {response.status_code}")
        return None

def get_pokemon_by_type(types):
    url=f"{base_url}/type/{types}"
    response=requests.get(url)
    if(response.status_code==200):
        pokemon_info=response.json()
        pokemons=[]
        for i in pokemon_info["pokemon"]:
            id_=i["pokemon"]["url"].split("/")[-2]
            pokemons.append({"name":i["pokemon"]["name"],"id":id_})
    return pokemons


def all_types():
    url=f"{base_url}/type"
    response=requests.get(url)
    if(response.status_code==200):
        type_info=response.json()
        types=[]
        for i in type_info["results"]:
            types.append((i["name"]))
    return types





