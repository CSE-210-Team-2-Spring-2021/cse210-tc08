import random
from game.point import Point

class StartGameAction:
    """The class that runs when a game is lost. Plays the game when a key is pressed
    
    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors, in this case I use ball
        """
        ball = cast["ball"][0] # there's only one in the cast
        while True:
            space_pressed = self._input_service.space_pressed()
            if space_pressed:
                x = random.randint(-1,1)
                y = -1
                direction = Point(x,y)
                ball.set_velocity(direction)
                break  