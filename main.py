import os
import sys
import time
from src.audio import init_audio, play_sound, play_music, stop_music
from src import auth
from src.models import Player
from src.storage import add_task   # ✅ ADDED


# ===== MAIN GAME =====
class Game:
    def __init__(self):
        self.player = None
    
    def clear(self): 
        os.system('clear')

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
        
        # ✅ SAVE TASK IMMEDIATELY WHEN CREATED
        new_task = {
            "task": task,
            "minutes": mins,
            "status": "completed"
        }

        add_task(self.player.acc_id, new_task)

        init_audio()

        try:
            for seconds_left in range(mins * 60, 0, -1):
                m, s = seconds_left // 60, seconds_left % 60
                print(f" {m:02d}:{s:02d} ", end="\r")

                if seconds_left == 120:
                    play_music("assets/tick.wav", loop=True)
                if seconds_left == 30:
                    play_sound("assets/tick.wav")
                if seconds_left == 10:
                    play_sound("assets/tick.wav")
                if seconds_left == 600:
                    play_music("assets/tick.wav", loop=True)
                if seconds_left == 5:
                    play_music("assets/explosion.mp3", loop=True)

                time.sleep(1)

            stop_music()
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
                print("1. Add Task\n2. Logout")
                choice = input("Choice: ")
                
                if choice == "1": 
                    self.timer()
                elif choice == "2": 
                    self.player = None

                    
if __name__ == "__main__":
    Game().run()