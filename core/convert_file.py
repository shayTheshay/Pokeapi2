from constants import id_change_convertion, id_change_convertion_range


#### id_change_convertion is 1025, id_change_convertion_range is 10000
#### reason is the url changes abruptly from id 1025 to 10001 without any reason in the pokeapi website.

def convert_to_api(pokemon_id): 
    if pokemon_id > id_change_convertion:
        pokemon_id = pokemon_id - id_change_convertion + id_change_convertion_range
    return pokemon_id

def convert_to_local(pokemon_id):
    if pokemon_id > id_change_convertion:
        pokemon_id = pokemon_id - id_change_convertion_range + id_change_convertion
    return pokemon_id