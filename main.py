import os
import sys
import time

def login():
    name = input("Username: ")
    return {"name": name, "health": 100}


class Game:
    def run(self):
        print("Game starting...")


if __name__ == "__main__":
    Game().run()
