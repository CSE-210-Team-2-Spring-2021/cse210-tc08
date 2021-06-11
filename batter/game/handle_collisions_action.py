import random
from game import constants
from game.action import Action


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        wall = cast["wall"][2]
        floor = cast["floor"][0]
        bat = cast["bat"][0]
        ball = cast["ball"][0]
        bricks = cast["brick"]
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                description = brick.get_description()
                wall.set_text(description)
