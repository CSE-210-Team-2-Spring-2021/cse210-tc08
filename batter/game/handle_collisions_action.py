import random
from game import constants
from game.action import Action
from game.point import Point


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

        wall = cast["wall"]
        floor = cast["floor"]
        ceiling = cast["ceiling"]
        paddle = cast["paddle"][0]
        ball = cast["ball"][0]
        bricks = cast["brick"]
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                bricks.pop(brick)
                x = random.randint(1, 5)
                y = random.randint(1, 5)
                velocity = Point(x, y)
                ball.set_velocity(velocity)

        for unit in wall:
            if ball.get_position().equals(unit.get_position()):
                x = random.randint(1, 5)
                y = random.randint(1, 5)
                velocity = Point(x, y)
                ball.set_velocity(velocity)

        for unit in floor:
            if ball.get_position().equals(unit.get_position()):
                x = random.randint(1, 5)
                y = random.randint(1, 5)
                velocity = Point(x, y)
                ball.set_velocity(velocity)

        for unit in ceiling:
            if ball.get_position().equals(unit.get_position()):
                x = random.randint(1, 5)
                y = random.randint(1, 5)
                velocity = Point(x, y)
                ball.set_velocity(velocity)

        if ball.get_position().equals(paddle.get_position()):
            x = random.randint(1, 5)
            y = random.randint(1, 5)
            velocity = Point(x, y)
            ball.set_velocity(velocity)