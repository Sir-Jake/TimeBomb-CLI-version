# 💣 TimeBomb CLI

A terminal-based game where players race against the clock to complete tasks before they **explode!**

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone <repo-url>
cd TimeBomb-CLI-version
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the game

```bash
python -m timebomb_cli.main
```

## 🎮 How to Play

1. **Register** a new account or **Login** with existing credentials.
2. **Create a Task** — give it a description and a time limit (in seconds).
3. **Start Countdown** — pick a task and race to finish before the timer hits zero!
4. Press **Enter** when you're done to defuse the bomb. ✅
5. If time runs out … 💥 **BOOM!**

## 📁 Project Structure

```
timebomb_cli/
├── main.py              # The Game Engine
├── requirements.txt     # Dependencies
├── README.md            # You are here
├── .gitignore
├── data/
│   ├── users.json       # Player accounts & stats
│   └── tasks.json       # Active tasks
├── assets/
│   ├── tick.wav          # Countdown sound
│   └── explosion.wav    # Explosion sound
└── src/
    ├── __init__.py
    ├── models.py         # Player & Task classes
    ├── storage.py        # JSON I/O
    ├── auth.py           # Login & registration
    └── audio.py          # Sound effects
```

## 🛠️ Tech Stack

- **Python 3.10+**
- **pygame** — audio playback
- **colorama** — coloured terminal output
