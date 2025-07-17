from requests_handle import handle_response, json_data
from file_handling import insert_pokemon_to_json
from convert_file import convert_to_api
from constants import min_id, base_url, pokemon_list_url


def get_pokemon_api_data(pokemon_id): 
    site_available = check_poke_site_available()
    if site_available == False:
        print("There was a problem reaching the site")
        return False
    max_id = get_max_pokemon_id(site_available)
    
    pokemon_id_available = call_pokemon_value_avilable(pokemon_id)

    if pokemon_id_available == False:
        return pokemon_id_unavailable(pokemon_id, max_id)
    else:
        return insert_pokemon_to_json(json_data(pokemon_id_available))
         

def check_poke_site_available():
    return call_url_check(base_url + pokemon_list_url)


def pokemon_id_unavailable(pokemon_id, max_id):
    response = check_id_in_range(pokemon_id, max_id)
    if response == None:
        print("Something went wrong in the calling")
    return response


def check_id_in_range(pokemon_id, max_id):
    if min_id > pokemon_id or max_id < pokemon_id:
        print(f"The number id for the pokemon should be between {min_id} to {max_id}")
        return False

def get_max_pokemon_id(data):
    data =  json_data(data)
    return int(data['count'])


def call_pokemon_value_avilable(pokemon_id): 
    pokemon_id = convert_to_api(pokemon_id)
    return call_url_check(base_url + pokemon_list_url + "/" + str(pokemon_id))


def call_url_check(call_url):
    response = handle_response(call_url)
    if response is None:
        print("Network request failed.")
        return False

    if 200 <= response.status_code < 300:
        return response
    else:
        print(f"Unexpected status code: {response.status_code}, {response}")
        return False
    


    

