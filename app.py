from flask import Flask, render_template,request 
import pokemon_functions as pf


app=Flask(__name__)

@app.route("/")
def hello():
    selected_type=request.args.get("type")
    if selected_type:
        pokemons=pf.get_pokemon_by_type(selected_type)
    else:
        pokemons=pf.all_pokemons()
    types=pf.all_types()
    return render_template("index.html",pokemons=pokemons,types=types,selected_type=selected_type)

@app.route("/pokemon/<identifier>")
def details(identifier):
    pokemon=pf.get_pokemon_info(identifier)
    if pokemon is None:
        return "pokemon not found", 404
    primary_type=pokemon['types'][0] if pokemon['types'] else 'normal'
    return render_template("detail.html",pokemon=pokemon, primary_type=primary_type)
    
    

if __name__== "__main__":
    app.run()

