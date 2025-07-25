#### Basic url values

base_url = "https://pokeapi.co/api/v2/"

pokemon_list_url = "pokemon"

limit_url = "?limit=100000"

file_json_name = "pokemon_data.json"

#### values that might change but only increase, representing the pokemon number from 1 to 1302

min_id = 1

maximum_id = 1302

#### For some unkown reason the id_pokemon number in the api jumps from 1025 to 10001, these are constant values that help "jump" over the gap and keep counting to the remainer of 1302 id's

id_change_convertion = 1025

id_change_convertion_range = 10000


#### This is not suppossed to be here, but as this is an educational only, it is okay
#### Please use parameter store instead of using this. implement it to access the dynamodb in the ec2 created

region= "us-west-2"

dynamodb_name = "pokemon-database"





