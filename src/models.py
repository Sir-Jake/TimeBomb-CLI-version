
#blueprint that defines the structure  and behavior of an object
class Player:
    #constructor method that initializes the attributes of the Player class
    def __init__(self, username, health=100):
        self.username = username
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
