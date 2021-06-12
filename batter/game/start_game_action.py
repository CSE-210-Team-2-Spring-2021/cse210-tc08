import random, math
from game.action import Action
from game.point import Point
from game.bricks import Bricks


class StartGameAction(Action):
    """The class that runs when a game is lost. Plays the game when a key is pressed

    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """
    
    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors, in this case I use ball
        """
        ball = cast["ball"][0]  # there's only one in the cast
        index = math.floor(len(cast['paddle'])/2)
        paddle_position = cast['paddle'][index].get_position()
        x = paddle_position.get_x()
        y = paddle_position.get_y()
        ball_position  = Point(x, (y - 1))
        ball.set_position(ball_position)
        ball.reset_floor()
        brick =  Bricks()
        brick.generate_bricks(cast)

        while True:
            space_pressed = self._input_service.space_pressed()
            if space_pressed:
                x = random.randint(-1, 1)
                y = -1
                direction = Point(x, y)
                ball.set_velocity(direction)
                break
