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
        
        assert ball.get_velocity() != (0, 0), "Velocity should not be zero!"
        
        for i, brick in enumerate(bricks):
            if ball.get_position().equals(brick.get_position()):
                bricks.pop(i)
                x = random.randint(-3, 3)
                y = random.randint(-3, 3)
                velocity = Point(x, y)
                ball.set_velocity(velocity)

        for unit in wall:
            x_ball = 0
            y_ball = 0
            (x_ball, y_ball) = ball.get_velocity()
            if ball.get_position().equals(unit.get_position()):
                if x_ball > 0:
                    if y_ball > 0:
                        x = random.randint(-2, -1)
                        y = random.randint(1, 2)
                    
                    else:
                        x = random.randint(-2, -1)
                        y = random.randint(-2, -1)
                
                else:
                    if y_ball > 0:
                        x = random.randint(1, 2)
                        y = random.randint(1, 2)
                    
                    else:
                        x = random.randint(1, 2)
                        y = random.randint(-2, -1)
                velocity = Point(x, y)
                ball.set_velocity(velocity)

        for unit in floor:
            if ball.get_position().equals(unit.get_position()):
                return True

        for unit in ceiling:
            if ball.get_position().equals(unit.get_position()):
                x = random.randint(-3, 3)
                y = random.randint(-3, 1)
                velocity = Point(x, y)
                ball.set_velocity(velocity)

        if ball.get_position().equals(paddle.get_position()):
            x = random.randint(-3, 3)
            y = random.randint(1, 3)
            velocity = Point(x, y)
            ball.set_velocity(velocity)