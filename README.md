
# 🧬 Pokémon Card Drawer

## 🎴 Description

A command-line Python application that lets you draw random Pokémon cards using real-time data from the [PokeAPI](https://pokeapi.co/).  
The game runs locally **or** on a fully automated **AWS EC2 instance**.


- 🟢 Local mode: run `run_game.py` from the `core/` directory.
- ☁️ Cloud mode: run `main.py` to launch an EC2 instance that installs and runs the game for you.

> Make sure you follow the requirements below — both for local and cloud usage.



## 📦 Features

- ✅ Randomly draw Pokémon by ID
- ✅ Cache Pokémon data locally in JSON for offline use
- ✅ Skip broken ID ranges in the PokeAPI (e.g., jumps from 1025 to 10001)
- ✅ Display Pokémon: `ID`, `name`, `type(s)`, `abilities`
- ✅ Auto-handling of network/API failures
- ✅ Continuous, interactive draw loop
- ✅ When connecting via SSH to EC2, the game auto-starts


---

## 🚀 How It Works

1. 🧠 The user is asked: “Would you like to draw a Pokémon card?”
2. 🎲 A random valid Pokémon ID is selected.
3. 📂 The program checks if the data is cached in `pokemon_data.json`.
4. 🌐 If not, the data is fetched from the [PokeAPI](https://pokeapi.co/).
5. 🎴 Pokémon details are displayed.
6. 🔁 The user can draw again or exit.

---

## 🔧 Requirements

- Git installed on your computer
- git clone the repository to your computer
- Python 3 or higher installed
- `requests` library and `python dotnet` library
  Install with:
  ```bash
  pip install requests
  pip install python-dotenv

-  create a `.env` file which should contain the following for your aws machine.
  ```bash
  REGION-NAME = [You region name]
  IMAGE_ID = [An image ID you would like to use]
  INSTANCE_TYPE = [An instance type like "t3.micro"]
  KEY_PAIR_NAME = [You can use the default "vockey" or anything else you created]
  SECURITY_GROUP_NAME = [You should name it ]
  POKEMON_EC2_NAME = [ 'pokeapi-server' or any unique name]
  ```
  

  After creating the .env file you are ready to run! 
  run the game using the main or if you are running locally just use the run_game method