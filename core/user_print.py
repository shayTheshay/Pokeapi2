from typing import Any

def farewell_greeting_to_user() -> None:
    print("Thank you for choosing to look at some pokemon with us! have a pleasant day")

def ask_user_draw_pokemon() -> None:
    print("Would you like to draw a pokemon card?")


def present_pokemon_data(pokemon: dict[str, Any]) -> None:
    print(f"Pokémon ID: {pokemon['id']}")
    print(f"Name: {pokemon['name'].capitalize()}")

    print("Types:")
    for type_info in pokemon['types']:
        print(f" - {type_info['type']['name'].capitalize()}")

    print("Abilities:")
    for ability_info in pokemon['abilities']:
        ability = ability_info['ability']['name']
        hidden = " (Hidden)" if ability_info.get('is_hidden') else ""
        print(f" - {ability.capitalize()}{hidden}")