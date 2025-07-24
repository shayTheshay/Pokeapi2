from file_handling import extract_poke_data_json, insert_pokemon_to_json
from api_calling import get_pokemon_api_data
from user_print import present_pokemon_data, ask_user_draw_pokemon, farewell_greeting_to_user
from pokemon_random import choose_random_num
from requests_handle import pokemon_value_None_False
from file_handling_dynamoDB import extract_poke_data_dynamodb, insert_pokemon_to_dynamodb

def run_game() -> None:

    ask_user_draw_pokemon()
    answer = str(input())

    while answer == "yes":
        random_pokemon_id = choose_random_num() 
        pokemon = extract_poke_data_json(random_pokemon_id) # extract_poke_data_dynamodb(random_pokemon_id) # checking if pokemon exist in json_file
        if pokemon:
            present_pokemon_data(pokemon)
        else:
            pokemon_data = get_pokemon_api_data(random_pokemon_id)
            if pokemon_data:
                insert_pokemon_to_dynamodb(pokemon_data)
                present_pokemon_data(pokemon_data)
            else:
                pokemon_value_None_False(pokemon_data)
        ask_user_draw_pokemon()
        answer = input()

    farewell_greeting_to_user()

if __name__ == "__main__":
    run_game()