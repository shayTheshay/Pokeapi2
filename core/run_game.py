from file_handling import extract_poke_data_json
from api_calling import get_pokemon_api_data
from user_print import present_pokemon_data, ask_user_draw_pokemon, farewell_greeting_to_user
from user_input import user_answer
from pokemon_random import choose_random_num
from requests_handle import pokemon_value_None_False

def run_game():

    ask_user_draw_pokemon()
    answer = str(user_answer())

    while answer == "yes":
        random_pokemon_id = choose_random_num() 
        pokemon = extract_poke_data_json(random_pokemon_id)
        if pokemon:
            present_pokemon_data(pokemon)
        else:
            pokemon_data = get_pokemon_api_data(random_pokemon_id)
            if pokemon_data :
                present_pokemon_data(pokemon_data)
            else:
                pokemon_value_None_False(pokemon_data)
        ask_user_draw_pokemon()
        answer = user_answer()

    farewell_greeting_to_user()

if __name__ == "__main__":
    run_game()