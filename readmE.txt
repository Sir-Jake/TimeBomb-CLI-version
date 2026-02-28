Setup Instructions
bash
# 1. Clone the repo
git clone https://github.com/Sir-Jake/TimeBomb-CLI-version.git
cd TimeBomb-CLI-version
# 2. Create a virtual environment
python3 -m venv venv
# 3. Activate it
source venv/bin/activate
# 4. Install dependencies
pip install -r requirements.txt
# 5. Run the game
python3 main.py
Your 
requirements.txt
 already lists pygame and colorama, so step 4 handles both automatically.

If someone wants to install them individually instead:

bash
pip install pygame
pip install colorama
[!NOTE] On Linux, if pygame audio doesn't work, you may also need:

bash
sudo apt install libsdl2-mixer-2.0-0 libsdl2-2.0-0