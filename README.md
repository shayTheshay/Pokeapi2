# 🧬 Pokémon Card Drawer

## 🎴 Description

A command-line Python application that lets you draw random Pokémon cards using real-time data from the [PokeAPI](https://pokeapi.co/).

The game runs locally **or** on a fully automated **AWS EC2 instance** with **DynamoDB** for cloud-based data storage.

**Please remember this is a project for educational purposes.**

- 🟢 **Local mode**: run `run_game.py` from the `core/` directory.
- ☁️ **Cloud mode**: run `main.py` to launch an EC2 instance that installs and runs the game for you.

> Make sure you follow the requirements below — both for local and cloud usage.

---

## 📦 Features

- ✅ Randomly draw Pokémon by ID
- ✅ Cache Pokémon data in **AWS DynamoDB** for scalable cloud storage
- ✅ Skip broken ID ranges in the PokeAPI (e.g., jumps from 1025 to 10001)
- ✅ Display Pokémon: `ID`, `name`, `type(s)`, `abilities`
- ✅ Auto-handling of network/API failures
- ✅ Continuous, interactive draw loop
- ✅ When connecting via SSH to EC2, the game auto-starts
- ✅ Automated AWS infrastructure deployment (EC2 + DynamoDB)

---

## 🚀 How It Works

1. 🧠 The user is asked: "Would you like to draw a Pokémon card?"
2. 🎲 A random valid Pokémon ID is selected.
3. 📊 The program checks if the data exists in **DynamoDB**.
4. 🌐 If not cached, the data is fetched from the [PokeAPI](https://pokeapi.co/).
5. 💾 New Pokémon data is automatically stored in DynamoDB for future use.
6. 🎴 Pokémon details are displayed.
7. 🔁 The user can draw again or exit.

---

## 🔧 Requirements

### Prerequisites

- **Git** installed on your computer
- **Python 3** or higher installed
- **AWS CLI** configured with appropriate permissions
- **AWS Account** with EC2 and DynamoDB access

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shayTheshay/pokeapi2
   cd pokeapi2
   ```

2. **Install Python dependencies:**
   ```bash
   pip install requests
   pip install python-dotenv
   pip install boto3
   ```

3. **Create environment file:**
   
   Create a `.env` file in the root directory with the following variables:
   ```bash
   REGION_NAME=us-east-1
   IMAGE_ID=ami-0abcdef1234567890
   INSTANCE_TYPE=t3.micro
   KEY_PAIR_NAME=vockey
   SECURITY_GROUP_NAME=pokemon-sg
   POKEMON_EC2_NAME=pokeapi-server
   DYNAMODB_NAME=pokemon-data
   ```

### AWS Configuration

Ensure your AWS credentials are configured either through:

- **AWS CLI**: `aws configure`
- **Environment variables**
- **IAM roles** (if running on EC2)

**Required AWS permissions:**

- **EC2**: Create, describe, and manage instances
- **DynamoDB**: Create tables, read/write items
- **Security Groups**: Create and manage security groups

---

## 🎮 Usage

### Cloud Deployment (Recommended)

```bash
python main.py
```

This will:
- Create a new EC2 instance
- Set up DynamoDB table
- Install all dependencies
- Start the Pokémon game automatically

**Note**: Should take a few minutes because it takes time for the EC2 to start.

### Local Development

```bash
python run_game.py
```

Start the python main as `run_game.py`. The game will start automatically upon connection!

---

## 🏗️ Architecture

### Cloud Infrastructure

- **EC2 Instance**: Hosts the Python application
- **DynamoDB**: Stores cached Pokémon data
- **Security Group**: Controls network access
- **Auto-scaling**: Built for scalable data storage

### Data Flow

1. User requests Pokémon card
2. Check DynamoDB for existing data
3. If not found, fetch from PokeAPI
4. Store in DynamoDB for future requests
5. Display Pokémon information

---

## 📁 Project Structure

```
pokeapi2/
├── core/
│   ├── run_game.py              # Main game logic
│   ├── file_handling_dynamoDB.py # DynamoDB operations
│   ├── api_calling.py           # PokeAPI integration
│   ├── constants.py             # Configuration constants
│   └── ...
├── deploy/
│   ├── ec2_setup.py            # EC2 deployment
│   ├── dynamoDB_setup.py       # DynamoDB table creation
│   └── setup_script.sh         # EC2 initialization script
├── main.py                     # Cloud deployment entry point
├── .env                        # Environment variables
└── README.md
```

---

## 🔍 Key Improvements

- **Migrated from JSON to DynamoDB**: Scalable, cloud-native data storage
- **Automated Infrastructure**: One-command deployment of entire stack
- **Enhanced Error Handling**: Robust AWS service integration
- **Production Ready**: Suitable for multi-user scenarios

---

## 🐛 Troubleshooting

### Common Issues

- **AWS Credentials**: Ensure AWS CLI is configured correctly
- **Permissions**: Verify IAM permissions for EC2 and DynamoDB
  
  *I used the student default role thus it is in constants but you can add a `iam.py` and configure yourself the setup for role → policy → attach → instance-profile*

- **Region**: Make sure all services are in the same AWS region → that is how I used it, I know it works. Otherwise I cannot guarantee it fully works
- **Table Exists**: The script handles existing DynamoDB tables gracefully

---

## 📝 License

This project is for educational purposes and uses the free [PokeAPI](https://pokeapi.co/) service.

---

**For any question or fix you are more than welcome to contact me!**

**Happy Pokémon hunting! 🎉**