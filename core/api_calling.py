from requests_handle import handle_response, json_data
from file_handling import insert_pokemon_to_json
from convert_file import convert_to_api
from constants import min_id, base_url, pokemon_list_url
from typing import Union, Dict, Any
import requests

def get_pokemon_api_data(pokemon_id:int) -> Union[bool, Dict[str, Any]]: #Wrong, should return dict not bool because insert pokemon to json returns dict, also recheck logic for running
    site_available = check_poke_site_available()
    if site_available == False:
        print("There was a problem reaching the site")
        return False
    max_id = get_max_pokemon_id(site_available)
    
    pokemon_id_available = call_pokemon_value_avilable(pokemon_id)

    if pokemon_id_available == False:
        return pokemon_id_unavailable(pokemon_id, max_id)
    else:
        return json_data(pokemon_id_available)
         

def check_poke_site_available() -> Union[requests.Response, bool]:
    return call_url_check(base_url + pokemon_list_url)


def pokemon_id_unavailable(pokemon_id:int, max_id:int) -> bool:
    response = check_id_in_range(pokemon_id, max_id)
    if response == False:
        print("Something went wrong in the calling")
    return response


def check_id_in_range(pokemon_id:str, max_id:str) -> bool:
    if min_id > pokemon_id or max_id < pokemon_id:
        print(f"The number id for the pokemon should be between {min_id} to {max_id}")
        return False
    return True

def get_max_pokemon_id(data:requests.Response) -> int:
    data =  json_data(data)
    return int(data['count'])


def call_pokemon_value_avilable(pokemon_id:int) -> Union[requests.Response, bool]: 
    pokemon_id = convert_to_api(pokemon_id)
    return call_url_check(base_url + pokemon_list_url + "/" + str(pokemon_id))


def call_url_check(call_url: str) -> Union[requests.Response, bool]:
    response = handle_response(call_url)
    if response is None:
        print("Network request failed.")
        return False

    if 200 <= response.status_code < 300:
        return response
    else:
        print(f"Unexpected status code: {response.status_code}, {response}")
        return False
    


    

