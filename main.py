import os
import sys
import time

def login():
    name = input("Username: ")
    return Player(name)


class Player:
    def __init__(self, name): self.name = name; self.health = 100
    def take_damage(self, amt): self.health -= amt; print(f"Health: {self.health}")

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
        
        task = input("Task: ")
        mins = input("Minutes (25): ")
        mins = 25 if mins == "" else int(mins)
        
        print(f"\n{task} - {mins}min. Ctrl+C to quit")
        
        try:
            for i in range(mins * 60, 0, -1):
                m, s = i//60, i%60
                print(f" {m:02d}:{s:02d} ", end="\r")
                time.sleep(1)
            
            print("DONE!")
            self.player.take_damage(10)

            input("press enter to continue...")
            
        except KeyboardInterrupt:
            print(" ABORTED!")
            self.player.take_damage(20)
            input("Enter to continue...")

    def run(self):
        while True:
            self.clear()
            if not self.player:
                print("1. Login\n2. Exit")
                c = input("Choice: ")
                
                if c == "1": 
                    self.player = login()
                elif c == "2": 
                    sys.exit()
            else:
                print(f"{self.player.name} |  {self.player.health}")
                print("1. Start Timer\n2. Logout")
                c = input("Choice: ")
                
                if c == "1": 
                    self.timer()
                elif c == "2": 
                    self.player = None

                    

Game().run()
    
