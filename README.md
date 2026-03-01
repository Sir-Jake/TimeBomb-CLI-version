# 💣 TimeBomb CLI

A productivity timer with a twist — complete your tasks before the bomb explodes, or lose health!

## How It Works

1. **Login** or create an account
2. **Add a task** and set a timer
3. **Complete the task** before time runs out — press `Ctrl+C` to defuse the bomb
4. **Fail** and you take damage. Run out of health? **Game Over.**

## Features

- ⏱️ Countdown timer with audio cues
- 🔊 Background music and tense ticking sounds
- 💾 Task and user data saved to JSON
- ❤️ Health system — take damage on failure
- 🔁 Extend time if you need more

## Setup

```bash
# Clone the repo
git clone https://github.com/Sir-Jake/TimeBomb-CLI-version.git
cd TimeBomb-CLI-version

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python3 main.py
```

## Requirements

- Python 3.10+
- pygame
- colorama

## Project Structure

```
TimeBomb-CLI-version/
├── main.py              # Entry point & game loop
├── requirements.txt
├── assets/              # Audio files
├── data/                # User & task data (JSON)
└── src/
    ├── audio.py         # Sound effects & music
    ├── auth.py          # Login & account creation
    ├── models.py        # Player & Task classes
    └── storage.py       # JSON read/write
```

## Developers

- **Jake**
- **Mary**
- **Asumpta**
- **Noah**
