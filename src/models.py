#blueprint that defines the structure  and behavior of an object
class Player:
    #constructor method that initializes the attributes of the Player class
    def __init__(self,acc_id, username, health=100):
        self.acc_id = acc_id
        self.username = username
        self._health = health  #magic method that allows us to access the health attribute using player.
                                    #health instead of player._health

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
