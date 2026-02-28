
#blueprint that defines the structure  and behavior of an object
class Player:
    #constructor method that initializes the attributes of the Player class
    def __init__(self, username, acc_id=None, health=100):
        self.username = username
        self.acc_id = acc_id
        self._health = health  #magic method that allows us to access the health attribute using player.
                                    #health instead of player._health
        self.completed_tasks = 0

    @property
    def health(self):
        return self._health

    def take_damage(self, amount):
        if amount <= 0:
            return
        self._health -= amount
        if self._health < 0:
            self._health = 0

    def heal(self, amount):
        if amount <= 0:
            return
        self._health += amount
        if self._health > 100:
            self._health = 100

    def complete_task(self):
        self.completed_tasks += 1

    def is_alive(self):
        return self._health > 0

    def __str__(self):
        return f"{self.username} | Health: {self._health} | Tasks Completed: {self.completed_tasks}"


class Task:
    def __init__(self, title, difficulty=10):
        self.title = title
        self.difficulty = difficulty
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def apply_splash_damage(self, player):
        splash_damage = int(self.difficulty * 0.10)
        player.take_damage(splash_damage)

    def __str__(self):
        status = "Completed" if self.completed else "Active"
        return f"Task: {self.title} | Difficulty: {self.difficulty} | Status: {status}"
