import boto3
from convert_file import convert_to_local


############################### After implementing parameter store you can remove these lines accordingly
from constants import region, dynamodb_name
###############################

dynamo_resource = boto3.resource('dynamodb', region_name = region)

def check_dynamo_table_exist() -> bool:
    try:
        dynamo_resource.Table(dynamodb_name)
        return True
    except Exception as e:
        print("Problem occured please check:", e)
        return False
    
def extract_poke_data_dynamodb(pokemon_id: int) -> dict: #check concern of separation
    file_exist = check_dynamo_table_exist()    
    if file_exist:
        table = dynamo_resource.Table(dynamodb_name)
        try:
            key = {
                'id': pokemon_id # The "id" is hard coded, please make sure to separate into constants or even make it available in parameter store, this is just an educational project thus not needed here
            }
            response = table.get_item(Key=key)
            item = response.get('Item')
        
            return item
        
        except Exception as e:
            print("There was a problem: ", e)

    else:
        print("There was a problem, for some reason the table was not created as needed")
        return None


def insert_pokemon_to_dynamodb(pokemon_data:dict)-> None:
    try:

        pokemon_id = (convert_to_local(pokemon_data['id']))
        name = pokemon_data['name']
        types = pokemon_data['types']
        abilities = pokemon_data['abilities']

        new_pokemon = {
        "id" : pokemon_id,
        "name" : name,
        "types" : types, 
        "abilities" : abilities,
        }

        table = dynamo_resource.Table(dynamodb_name)
        table.put_item(Item= new_pokemon)
    except Exception as e:
        print("There was an error in the code:", e)