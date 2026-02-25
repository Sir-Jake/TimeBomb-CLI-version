import sys
import os

# Add the parent directory to the path so we can import src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models import Player, Task


def main():
    # Create a player
    player = Player("Noah")

    print("Player created:")
    print(player)

    # Player takes damage
    player.take_damage(20)
    print("\nAfter taking damage:")
    print(player)

    # Player heals
    player.heal(10)
    print("\nAfter healing:")
    print(player)

    # Complete a task
    player.complete_task()
    print("\nAfter completing a task:")
    print(player)

    # Create a task
    task = Task("Defuse Bomb", difficulty=15)
    print("\nTask created:")
    print(task)


if __name__ == "__main__":
    main()