import requests

def handle_response(url):
    """Handle different HTTP status codes with basic error handling."""
    try:
        response = requests.get(url)

        ## Check status code category
        if 200 <= response.status_code < 300:
            return response
        elif 300 <= response.status_code < 400:
            print(f"Redirection! Status code: {response.status_code}")
            ## For redirection, you might want to follow the redirect
        elif 400 <= response.status_code < 500:
            print(f"Client error! Status code: {response.status_code}")
            ## Handle client errors
        elif 500 <= response.status_code < 600:
            print(f"Server error! Status code: {response.status_code}")
            ## Handle server errors
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def json_data(response):
    data = response.json()
    return data

def pokemon_value_None_False(pokemon_data):
    if pokemon_data is None:
        print("There was a problem with the calling")
    elif pokemon_data is False:
        print("You can try again with the next pokemon calling")
    else:
        print("Value is not None or False, Check pokemon value from api")
    return pokemon_data