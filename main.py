import os
import sys
import time

def login():
    name = input("Username: ")
    return {"name": name, "health": 100}


class Game:
    def run(self):
        print("Game starting...")

# ===== MAIN GAME =====
class Game:
    def __init__(self):
        self.player = None
    
    def clear(self): os.system('clear')

    def timer(self):
        self.clear()
        print("="*40)
        print("TIMER ")
        print("="*40)
        
        task = input("\nTask: ")
        mins = input("Minutes (25): ")
        mins = 25 if mins == "" else int(mins)
        
        print(f"\n{task} - {mins}min. Ctrl+C to quit")
        
        try:
            for i in range(mins * 60, 0, -1):
                m, s = i//60, i%60
                print(f" {m:02d}:{s:02d} ", end="", flush=True)
                time.sleep(1)
            
            print("DONE!")
            self.player.take_damage(10)
            input("Enter to continue...")
            
        except KeyboardInterrupt:
            print(" ABORTED!")
            self.player.take_damage(20)
            input("Enter to continue...")


if __name__ == "__main__":
    Game().run()
