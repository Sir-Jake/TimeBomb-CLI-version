
#blueprint that defines the structure  and behavior of an object
class Player:
    #constructor method that initializes the attributes of the Player class
    def __init__(self, username, health=100):
        self.username = username
        self._health = health  #magic method that allows us to access the health attribute using player.
                                    #health instead of player._health
        self.completed_tasks = 0