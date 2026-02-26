import os
import sys
import time
from src import auth, storage
from src.models import Player

# ===== MAIN GAME =====
class Game:
    def __init__(self):
        self.player = None
    
    def clear(self): os.system('clear')

    def game_over(self):
        if self.player.health <= 0:
            print("GAME OVER")
            sys.exit()

    def timer(self):
        self.clear()
        print("="*40)
        print("TIMER ")
        print("="*40)
        
        task = input("Task: ")
        mins = input("Minutes: ")
        mins = 25 if mins == "" else int(mins)
        
        print(f"\n{task} - {mins}min. Ctrl+C to quit")
        
        try:
            for i in range(mins * 60, 0, -1):
                m, s = i//60, i%60
                print(f" {m:02d}:{s:02d} ", end="\r")
                time.sleep(1)
            
            print("DONE!")
            self.player.take_damage(0)

            input("press enter to continue...")
            
        except KeyboardInterrupt:
            print(" ABORTED!")
            self.player.take_damage(20)
            self.game_over()
            input("Enter to continue...")

    def run(self):
        while True:
            self.clear()
            if not self.player:
                print("1. Login\n2. Exit")
                choice = input("Choice: ")
                
                if choice == "1": 
                    self.player = auth.authenticate()
                elif choice == "2": 
                    sys.exit()
            else:
                print(f"{self.player.username} |  {self.player.health}")
                print("1. Start Timer\n2. Logout")
                choice = input("Choice: ")
                
                if choice == "1": 
                    self.timer()
                elif choice == "2": 
                    self.player = None

                    
if __name__ == "__main__":
    Game().run()
    
