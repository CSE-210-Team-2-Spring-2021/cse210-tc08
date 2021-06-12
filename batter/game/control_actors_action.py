from game import constants
from game.action import Action
from game.point import Point

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
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
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        paddle = cast["paddle"] 
        paddle_position = paddle[0].get_position().get_x()
        if paddle_position <= 2:
            x = direction.get_x()
            if x < 0:
                direction = Point(0, 0)
        paddle_position = paddle[len(paddle) - 1].get_position().get_x()
        if paddle_position >= (constants.MAX_X - 2):
            x = direction.get_x()
            if x > 0:
                direction = Point(0, 0)

        for pad in paddle:
            pad.set_velocity(direction)        
