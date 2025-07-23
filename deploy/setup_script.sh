#!/bin/bash

echo "=== Starting EC2 setup script ==="

# 1. Update system packages
sudo dnf update -y

# 2. Install core tools: Python 3, pip, Git, unzip
sudo dnf install -y python3 python3-pip git unzip

# 3. Go to home directory
cd /home/ec2-user

# 4. Clone the project (replace with your real repo if needed)
echo "Cloning repo..."
git clone https://github.com/shayTheshay/pokeapi2
cd pokeapi2

# 5. Fix ownership for EC2 user
sudo chown -R ec2-user:ec2-user /home/ec2-user/pokeapi2

# 6. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 7. Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt || echo "requirements.txt not found, continuing..."
pip install requests
pip install python-dotenv
pip install boto3
# 8. Run the Pokémon app on boot (non-interactive background mode)
nohup python3 core/run_game.py > game_output.log 2>&1 &

# 9. Automatically start game when SSH connects (interactive session)
echo 'if [[ $- == *i* ]]; then cd /home/ec2-user/pokeapi2 && source venv/bin/activate && python3 core/run_game.py; fi' >> /home/ec2-user/.bash_profile

echo "EC2 setup complete. Pokémon game will run now and on each SSH login."
