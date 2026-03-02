import os, sys, time
from src.audio import init_audio, play_sound, play_music, stop_music, stop_all
from src import auth, storage
from src.storage import add_task

# ===== MAIN GAME =====
class Game:
    def __init__(self):
        self.player = None
    
    def clear(self): os.system('clear')

    def save_health(self):
        account = storage.load_account(str(self.player.acc_id))
        account["health"] = self.player.health
        storage.save_account(self.player.acc_id, account)
      
    def timer(self):
        self.clear()
        print("="*40)
        print("TIMER ")
        print("="*40)
        
        task = input("Task: ")
        mins = input("Minutes: ")
        mins = 25 if mins == "" else int(mins)
        
        new_task = {
            "task": task,
            "minutes": mins,
            "status": "completed"
        }
        add_task(self.player.acc_id, new_task)
        #print(f"\n{task} - Ctrl+C to quit")
        
        init_audio()

        # loop allows extension of time
        while True:
            print(f"\n{task} - {mins}min. Ctrl+C to defuse")

            try:
                # Start background music if timer is 3+ minutes
                if mins >= 3:
                    play_music("assets/smoothmusic.mp3", loop=True)

                for seconds_left in range(mins * 60, 0, -1):
                    m, s = seconds_left//60, seconds_left%60
                    print(f" {m:02d}:{s:02d} ", end="\r")
                    #if seconds_left == 30:
                        #play_music("assets/tick.wav")
                    #if seconds_left == 10:
                        #play_music("assets/tick.wav")
                    if seconds_left == 68:
                        stop_music()  # stop smooth music before tense phase
                    if seconds_left <= 67:
                        play_music("assets/tensetick.mp3", loop=True)  # start tense loop
                    if seconds_left == 5:
                        play_sound("assets/explosion.mp3")
                    time.sleep(1)

                # Timer ran out
                stop_all()
                print("Failed!")
                self.player.take_damage(20)
                self.save_health()
                choice = input("Extend Time? (Y/N): ")
                if choice.lower() == "y":
                    mins = int(input("Extra minutes: "))
                    continue  # restart the while loop with new mins
                else:
                    break  # exit to menu       

            except KeyboardInterrupt:
                stop_all()
                print(" DEFUSED!")
                self.player.heal(10)
                self.save_health()
                break  # exit to menu

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
    
